"""
ui/widgets/component_select_dialog.py
----------------------------------------
Hộp thoại tìm & chọn linh kiện để thêm thủ công vào phiếu nhập/xuất kho,
dành cho trường hợp không có máy quét mã vạch hoặc cần tìm theo tên.
Nếu chưa tìm thấy linh kiện phù hợp, cho phép tạo mới ngay tại đây.
"""
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QDialog, QTableWidgetItem

from dao.component_dao import ComponentDAO
from ui.generated.ui_component_select_dialog import Ui_ComponentSelectDialog
from ui.widgets.component_dialog import ComponentDialog
from utils.formatters import format_int
from utils.ui_helpers import show_warning

component_dao = ComponentDAO()


class ComponentSelectDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_ComponentSelectDialog()
        self.ui.setupUi(self)

        self.selected_component: dict | None = None
        self.selected_qty: int = 1
        self._results: list[dict] = []

        self.ui.txtSearch.textChanged.connect(self._on_search)
        self.ui.tblResults.itemDoubleClicked.connect(lambda _: self._on_add())
        self.ui.btnAdd.clicked.connect(self._on_add)
        self.ui.btnCancel.clicked.connect(self.reject)
        self.ui.btnCreateNew.clicked.connect(self._on_create_new)

        self._on_search("")
        self.ui.txtSearch.setFocus()

    def _on_search(self, text: str) -> None:
        self._results = component_dao.search(keyword=text.strip())
        table = self.ui.tblResults
        table.setRowCount(0)
        for row_idx, c in enumerate(self._results):
            table.insertRow(row_idx)
            code_item = QTableWidgetItem(c["code"])
            code_item.setData(Qt.ItemDataRole.UserRole, c["id"])
            table.setItem(row_idx, 0, code_item)
            table.setItem(row_idx, 1, QTableWidgetItem(c["name"]))
            qty_item = QTableWidgetItem(format_int(c["quantity"]))
            qty_item.setTextAlignment(Qt.AlignmentFlag.AlignRight | Qt.AlignmentFlag.AlignVCenter)
            table.setItem(row_idx, 2, qty_item)
            table.setItem(row_idx, 3, QTableWidgetItem(c.get("unit") or ""))
        if self._results:
            table.selectRow(0)

    def _on_add(self) -> None:
        row = self.ui.tblResults.currentRow()
        if row < 0 or row >= len(self._results):
            show_warning(self, "Vui lòng chọn một linh kiện trong danh sách.")
            return
        self.selected_component = self._results[row]
        self.selected_qty = self.ui.spnQty.value()
        self.accept()

    def _on_create_new(self) -> None:
        dlg = ComponentDialog(self)
        prefill_name = self.ui.txtSearch.text().strip()
        if prefill_name:
            dlg.ui.txtName.setText(prefill_name)
        if dlg.exec() == QDialog.DialogCode.Accepted and dlg.saved_component_id:
            self.selected_component = component_dao.get_by_id(dlg.saved_component_id)
            self.selected_qty = self.ui.spnQty.value()
            self.accept()
