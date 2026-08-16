"""
services/stock_service.py
--------------------------
Lớp nghiệp vụ xử lý phiếu NHẬP KHO và XUẤT KHO.

Đây là nơi DUY NHẤT được phép tạo phiếu nhập/xuất, vì mỗi thao tác phải
thực hiện ĐỒNG THỜI và ATOMIC (trong 1 transaction) các bước:
    1) Ghi phiếu (import_receipts / export_receipts)
    2) Ghi chi tiết từng dòng linh kiện (receipt_details)
    3) Cập nhật số lượng tồn kho của từng linh kiện (components.quantity)
    4) Ghi log biến động tồn kho (stock_transactions) để truy vết

Nếu có lỗi ở bất kỳ bước nào, toàn bộ giao dịch sẽ được rollback để đảm
bảo tồn kho luôn khớp chính xác với lịch sử phiếu nhập/xuất.
"""
from database.db_manager import db_manager
from dao.import_receipt_dao import ImportReceiptDAO
from dao.export_receipt_dao import ExportReceiptDAO
from utils.exceptions import EmptyReceiptError, InsufficientStockError, ValidationError

import_receipt_dao = ImportReceiptDAO()
export_receipt_dao = ExportReceiptDAO()


class StockService:
    # ------------------------------------------------------------ IMPORT
    def create_import_receipt(
        self, items: list[dict], supplier: str = "", note: str = "", created_by: str = ""
    ) -> str:
        """
        items: [{'component_id': int, 'quantity': int, 'unit_price': float}, ...]
        Trả về receipt_code vừa tạo.
        """
        items = self._clean_items(items)
        with db_manager.transaction() as conn:
            code = import_receipt_dao.next_receipt_code()
            cur = conn.execute(
                "INSERT INTO import_receipts (receipt_code, supplier, note, created_by) "
                "VALUES (?, ?, ?, ?)",
                (code, supplier.strip() or None, note.strip() or None, created_by or None),
            )
            receipt_id = cur.lastrowid

            for it in items:
                conn.execute(
                    "INSERT INTO import_receipt_details "
                    "(receipt_id, component_id, quantity, unit_price) VALUES (?, ?, ?, ?)",
                    (receipt_id, it["component_id"], it["quantity"], it["unit_price"]),
                )
                conn.execute(
                    "UPDATE components SET quantity = quantity + ?, "
                    "updated_at = datetime('now','localtime') WHERE id = ?",
                    (it["quantity"], it["component_id"]),
                )
                new_qty = conn.execute(
                    "SELECT quantity FROM components WHERE id = ?", (it["component_id"],)
                ).fetchone()["quantity"]
                conn.execute(
                    "INSERT INTO stock_transactions "
                    "(component_id, transaction_type, quantity, balance_after, "
                    " reference_type, reference_id, note) "
                    "VALUES (?, 'IN', ?, ?, 'IMPORT', ?, ?)",
                    (it["component_id"], it["quantity"], new_qty, receipt_id, note or None),
                )
            return code

    # ------------------------------------------------------------ EXPORT
    def create_export_receipt(
        self, items: list[dict], recipient: str = "", note: str = "", created_by: str = ""
    ) -> str:
        items = self._clean_items(items)
        with db_manager.transaction() as conn:
            # Kiểm tra đủ tồn kho cho TẤT CẢ các dòng trước khi trừ bất kỳ dòng nào
            for it in items:
                row = conn.execute(
                    "SELECT name, quantity FROM components WHERE id = ?",
                    (it["component_id"],),
                ).fetchone()
                if row is None:
                    raise ValidationError("Linh kiện không tồn tại trong hệ thống.")
                if row["quantity"] < it["quantity"]:
                    raise InsufficientStockError(
                        f'"{row["name"]}" chỉ còn {row["quantity"]} trong kho, '
                        f'không đủ để xuất {it["quantity"]}.'
                    )

            code = export_receipt_dao.next_receipt_code()
            cur = conn.execute(
                "INSERT INTO export_receipts (receipt_code, recipient, note, created_by) "
                "VALUES (?, ?, ?, ?)",
                (code, recipient.strip() or None, note.strip() or None, created_by or None),
            )
            receipt_id = cur.lastrowid

            for it in items:
                conn.execute(
                    "INSERT INTO export_receipt_details "
                    "(receipt_id, component_id, quantity, unit_price) VALUES (?, ?, ?, ?)",
                    (receipt_id, it["component_id"], it["quantity"], it["unit_price"]),
                )
                conn.execute(
                    "UPDATE components SET quantity = quantity - ?, "
                    "updated_at = datetime('now','localtime') WHERE id = ?",
                    (it["quantity"], it["component_id"]),
                )
                new_qty = conn.execute(
                    "SELECT quantity FROM components WHERE id = ?", (it["component_id"],)
                ).fetchone()["quantity"]
                conn.execute(
                    "INSERT INTO stock_transactions "
                    "(component_id, transaction_type, quantity, balance_after, "
                    " reference_type, reference_id, note) "
                    "VALUES (?, 'OUT', ?, ?, 'EXPORT', ?, ?)",
                    (it["component_id"], -it["quantity"], new_qty, receipt_id, note or None),
                )
            return code

    # ------------------------------------------------------------ VOID (hủy phiếu)
    def void_import_receipt(self, receipt_id: int) -> None:
        """Hủy phiếu nhập: trừ lại số lượng đã cộng vào kho, sau đó xóa phiếu."""
        with db_manager.transaction() as conn:
            details = conn.execute(
                "SELECT component_id, quantity FROM import_receipt_details WHERE receipt_id=?",
                (receipt_id,),
            ).fetchall()
            for d in details:
                conn.execute(
                    "UPDATE components SET quantity = quantity - ?, "
                    "updated_at = datetime('now','localtime') WHERE id = ?",
                    (d["quantity"], d["component_id"]),
                )
                new_qty = conn.execute(
                    "SELECT quantity FROM components WHERE id = ?", (d["component_id"],)
                ).fetchone()["quantity"]
                conn.execute(
                    "INSERT INTO stock_transactions "
                    "(component_id, transaction_type, quantity, balance_after, "
                    " reference_type, reference_id, note) "
                    "VALUES (?, 'ADJUST', ?, ?, 'IMPORT', ?, 'Hủy phiếu nhập')",
                    (d["component_id"], -d["quantity"], new_qty, receipt_id),
                )
            conn.execute("DELETE FROM import_receipts WHERE id = ?", (receipt_id,))

    def void_export_receipt(self, receipt_id: int) -> None:
        """Hủy phiếu xuất: cộng lại số lượng đã trừ khỏi kho, sau đó xóa phiếu."""
        with db_manager.transaction() as conn:
            details = conn.execute(
                "SELECT component_id, quantity FROM export_receipt_details WHERE receipt_id=?",
                (receipt_id,),
            ).fetchall()
            for d in details:
                conn.execute(
                    "UPDATE components SET quantity = quantity + ?, "
                    "updated_at = datetime('now','localtime') WHERE id = ?",
                    (d["quantity"], d["component_id"]),
                )
                new_qty = conn.execute(
                    "SELECT quantity FROM components WHERE id = ?", (d["component_id"],)
                ).fetchone()["quantity"]
                conn.execute(
                    "INSERT INTO stock_transactions "
                    "(component_id, transaction_type, quantity, balance_after, "
                    " reference_type, reference_id, note) "
                    "VALUES (?, 'ADJUST', ?, ?, 'EXPORT', ?, 'Hủy phiếu xuất')",
                    (d["component_id"], d["quantity"], new_qty, receipt_id),
                )
            conn.execute("DELETE FROM export_receipts WHERE id = ?", (receipt_id,))

    # ------------------------------------------------------------ helpers
    @staticmethod
    def _clean_items(items: list[dict]) -> list[dict]:
        if not items:
            raise EmptyReceiptError("Phiếu chưa có linh kiện nào, vui lòng quét hoặc thêm ít nhất 1 dòng.")
        cleaned = []
        for it in items:
            qty = int(it.get("quantity") or 0)
            if qty <= 0:
                raise ValidationError("Số lượng của mỗi dòng linh kiện phải lớn hơn 0.")
            cleaned.append(
                {
                    "component_id": it["component_id"],
                    "quantity": qty,
                    "unit_price": float(it.get("unit_price") or 0),
                }
            )
        return cleaned


stock_service = StockService()
