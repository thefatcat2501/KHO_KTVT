"""
ui/widgets/stock_transaction_page.py
--------------------------------------
Trang "Nhập kho" và "Xuất kho" dùng CHUNG một giao diện/luồng xử lý,
chỉ khác nhau ở mode="IN" hoặc mode="OUT" (nhãn hiển thị + service gọi).

Luồng nghiệp vụ (giống mô hình phần mềm thu ngân/siêu thị):
    1. Người dùng quét mã vạch liên tiếp (hoặc bấm "Tìm & thêm thủ công"
       nếu không có máy quét / muốn tìm theo tên).
    2. Mỗi lượt quét: nếu mã vạch đã có trong CSDL -> tự thêm 1 dòng vào
       bảng (hoặc +1 số lượng nếu đã có trong danh sách); nếu CHƯA có ->
       hỏi và cho tạo linh kiện mới ngay tại chỗ, gán mã vạch vừa quét.
    3. Người dùng có thể sửa số lượng từng dòng, xóa dòng.
    4. Bấm "Xác nhận & Lưu phiếu" -> services/stock_service ghi phiếu +
       cập nhật tồn kho một cách atomic (toàn vẹn dữ liệu).

Ghi chú: kho không quản lý giá tiền vật tư/linh kiện, nên trang này chỉ
theo dõi SỐ LƯỢNG, không có cột đơn giá / thành tiền / tổng tiền.
"""
from PySide6.QtCore import Qt, Signal
from PySide6.QtWidgets import QDialog, QPushButton, QSpinBox, QTableWidgetItem

from dao.component_dao import ComponentDAO
from services.stock_service import stock_service
from ui.generated.ui_stock_transaction_page import Ui_StockTransactionPage
from ui.widgets.base_page import BasePage
from ui.widgets.component_dialog import ComponentDialog
from ui.widgets.component_select_dialog import ComponentSelectDialog
from utils.exceptions import AppError
from utils.formatters import format_int
from utils.ui_helpers import confirm, show_error, show_info, show_warning

component_dao = ComponentDAO()

COL_INDEX, COL_BARCODE, COL_CODE, COL_NAME, COL_UNIT, COL_STOCK, COL_QTY, COL_ACTION = range(8)


class StockTransactionPage(BasePage):
    receipt_saved = Signal()

    def __init__(self, parent=None, mode: str = "IN"):
        super().__init__(parent)
        assert mode in ("IN", "OUT")
        self.mode = mode

        self.ui = Ui_StockTransactionPage()
        self.ui.setupUi(self)

        self.items: list[dict] = []

        if mode == "IN":
            self.ui.lblPartnerCaption.setText("Nhà cung cấp:")
            self.ui.txtPartner.setPlaceholderText("Tên nhà cung cấp")
        else:
            self.ui.lblPartnerCaption.setText("Người nhận:")
            self.ui.txtPartner.setPlaceholderText("Tên người nhận / bộ phận nhận")

        self.ui.txtBarcode.scanned.connect(self._on_barcode_scanned)
        self.ui.btnManualAdd.clicked.connect(self._on_manual_add)
        self.ui.btnClearAll.clicked.connect(self._on_clear_all)
        self.ui.btnSaveReceipt.clicked.connect(self._on_save_receipt)

        self._rebuild_table()

    # ------------------------------------------------------------ scanning
    def _on_barcode_scanned(self, code: str) -> None:
        component = component_dao.get_by_barcode(code) or component_dao.get_by_code(code)
        if component is None:
            self._handle_unknown_barcode(code)
        else:
            self._add_or_increment(component)
        self.ui.txtBarcode.setFocus()

    def _handle_unknown_barcode(self, code: str) -> None:
        if not confirm(
            self,
            f'Mã vạch "{code}" chưa có trong hệ thống.\n'
            f"Bạn có muốn tạo linh kiện mới và gán mã vạch này không?",
            title="Mã vạch chưa tồn tại",
        ):
            return
        dlg = ComponentDialog(self, prefill_barcode=code)
        if dlg.exec() == QDialog.DialogCode.Accepted and dlg.saved_component_id:
            component = component_dao.get_by_id(dlg.saved_component_id)
            if component:
                self._add_or_increment(component)

    def _on_manual_add(self) -> None:
        dlg = ComponentSelectDialog(self)
        if dlg.exec() == QDialog.DialogCode.Accepted and dlg.selected_component:
            self._add_or_increment(dlg.selected_component, qty=dlg.selected_qty)
        self.ui.txtBarcode.setFocus()

    def _add_or_increment(self, component: dict, qty: int = 1) -> None:
        for it in self.items:
            if it["component_id"] == component["id"]:
                it["quantity"] += qty
                self._rebuild_table()
                return
        self.items.append(
            {
                "component_id": component["id"],
                "barcode": component.get("barcode") or "",
                "code": component["code"],
                "name": component["name"],
                "unit": component.get("unit") or "",
                "current_stock": component.get("quantity") or 0,
                "quantity": qty,
            }
        )
        self._rebuild_table()

    # ------------------------------------------------------------ table rendering
    def _rebuild_table(self) -> None:
        table = self.ui.tblItems
        table.setRowCount(0)
        for i, it in enumerate(self.items):
            table.insertRow(i)
            table.setItem(i, COL_INDEX, QTableWidgetItem(str(i + 1)))
            table.setItem(i, COL_BARCODE, QTableWidgetItem(it["barcode"]))
            table.setItem(i, COL_CODE, QTableWidgetItem(it["code"]))
            table.setItem(i, COL_NAME, QTableWidgetItem(it["name"]))
            table.setItem(i, COL_UNIT, QTableWidgetItem(it["unit"]))

            stock_label = format_int(it["current_stock"])
            if self.mode == "OUT" and it["quantity"] > it["current_stock"]:
                stock_label += "  ⚠"
            table.setItem(i, COL_STOCK, QTableWidgetItem(stock_label))

            qty_spin = QSpinBox()
            qty_spin.setRange(1, 1_000_000)
            qty_spin.setValue(it["quantity"])
            qty_spin.valueChanged.connect(lambda val, idx=i: self._on_qty_changed(idx, val))
            table.setCellWidget(i, COL_QTY, qty_spin)

            btn_del = QPushButton("🗑")
            btn_del.setCursor(Qt.CursorShape.PointingHandCursor)
            btn_del.clicked.connect(lambda _, idx=i: self._on_delete_row(idx))
            table.setCellWidget(i, COL_ACTION, btn_del)

        self._update_footer()

    def _on_qty_changed(self, idx: int, val: int) -> None:
        if idx >= len(self.items):
            return
        self.items[idx]["quantity"] = val
        self._update_row_visuals(idx)
        self._update_footer()

    def _update_row_visuals(self, idx: int) -> None:
        it = self.items[idx]
        stock_item = self.ui.tblItems.item(idx, COL_STOCK)
        if stock_item:
            label = format_int(it["current_stock"])
            if self.mode == "OUT" and it["quantity"] > it["current_stock"]:
                label += "  ⚠"
            stock_item.setText(label)

    def _on_delete_row(self, idx: int) -> None:
        if 0 <= idx < len(self.items):
            del self.items[idx]
            self._rebuild_table()

    def _update_footer(self) -> None:
        total_qty = sum(it["quantity"] for it in self.items)
        self.ui.lblItemCount.setText(f"{len(self.items)} dòng")
        self.ui.lblTotalQty.setText(format_int(total_qty))

    # ------------------------------------------------------------ actions
    def _on_clear_all(self) -> None:
        if not self.items and not self.ui.txtPartner.text() and not self.ui.txtNote.text():
            return
        if confirm(self, "Bạn có chắc muốn hủy toàn bộ danh sách đang nhập/xuất?"):
            self._reset_form()

    def _on_save_receipt(self) -> None:
        if not self.items:
            show_warning(self, "Chưa có linh kiện nào trong phiếu. Vui lòng quét hoặc thêm ít nhất 1 dòng.")
            return

        payload = [
            {"component_id": it["component_id"], "quantity": it["quantity"]}
            for it in self.items
        ]
        partner = self.ui.txtPartner.text().strip()
        note = self.ui.txtNote.text().strip()

        try:
            if self.mode == "IN":
                code = stock_service.create_import_receipt(payload, supplier=partner, note=note)
                show_info(self, f"Đã lưu phiếu nhập kho thành công!\nSố phiếu: {code}")
            else:
                code = stock_service.create_export_receipt(payload, recipient=partner, note=note)
                show_info(self, f"Đã lưu phiếu xuất kho thành công!\nSố phiếu: {code}")
            self._reset_form()
            self.receipt_saved.emit()
        except AppError as e:
            show_error(self, str(e))

    def _reset_form(self) -> None:
        self.items = []
        self._rebuild_table()
        self.ui.txtPartner.clear()
        self.ui.txtNote.clear()
        self.ui.txtBarcode.setFocus()

    # ------------------------------------------------------------ BasePage
    def refresh(self) -> None:
        # Cập nhật lại tồn kho hiện tại hiển thị (phòng khi đã thay đổi ở nơi khác)
        for it in self.items:
            c = component_dao.get_by_id(it["component_id"])
            if c:
                it["current_stock"] = c["quantity"]
        self._rebuild_table()
        self.ui.txtBarcode.setFocus()
