"""dao/export_receipt_dao.py - CRUD phiếu xuất kho (đọc dữ liệu / lịch sử).
Việc TẠO phiếu (ghi + cập nhật tồn kho) được thực hiện tại services/stock_service.py.
"""
from database.db_manager import db_manager


class ExportReceiptDAO:
    def list_all(self, keyword: str = "", date_from: str = "", date_to: str = "") -> list[dict]:
        sql = """
            SELECT r.*,
                   (SELECT COALESCE(SUM(d.quantity), 0) FROM export_receipt_details d
                        WHERE d.receipt_id = r.id) AS total_quantity,
                   (SELECT COALESCE(SUM(d.quantity * d.unit_price), 0)
                        FROM export_receipt_details d WHERE d.receipt_id = r.id) AS total_value
            FROM export_receipts r
        """
        conditions, params = [], []
        if keyword:
            conditions.append("(r.receipt_code LIKE ? OR r.recipient LIKE ? OR r.note LIKE ?)")
            kw = f"%{keyword}%"
            params.extend([kw, kw, kw])
        if date_from:
            conditions.append("date(r.created_at) >= date(?)")
            params.append(date_from)
        if date_to:
            conditions.append("date(r.created_at) <= date(?)")
            params.append(date_to)
        if conditions:
            sql += " WHERE " + " AND ".join(conditions)
        sql += " ORDER BY r.created_at DESC"
        return db_manager.query_all(sql, tuple(params))

    def get_by_id(self, receipt_id: int) -> dict | None:
        return db_manager.query_one("SELECT * FROM export_receipts WHERE id=?", (receipt_id,))

    def get_details(self, receipt_id: int) -> list[dict]:
        return db_manager.query_all(
            """
            SELECT d.*, c.code, c.name, c.unit, c.barcode
            FROM export_receipt_details d
            INNER JOIN components c ON c.id = d.component_id
            WHERE d.receipt_id = ?
            ORDER BY d.id
            """,
            (receipt_id,),
        )

    def next_receipt_code(self) -> str:
        from datetime import datetime

        prefix = f"PX{datetime.now().strftime('%y%m%d')}"
        row = db_manager.query_one(
            "SELECT COUNT(*) c FROM export_receipts WHERE receipt_code LIKE ?",
            (f"{prefix}%",),
        )
        seq = row["c"] + 1
        return f"{prefix}-{seq:03d}"
