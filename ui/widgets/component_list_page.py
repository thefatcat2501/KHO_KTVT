"""
ui/widgets/component_list_page.py
------------------------------------
Trang "Linh kiện / Vật tư": tìm kiếm, lọc theo loại / nhà sản xuất / năm
nhập / sản phẩm sử dụng, thêm - sửa - xóa linh kiện.
"""
from PySide6.QtCore import Qt
from PySide6.QtGui import QColor
from PySide6.QtWidgets import QDialog, QTableWidgetItem

from dao.base_lookup_dao import CategoryDAO, ProductDAO
from dao.component_dao import ComponentDAO
from dao.manufacturer_dao import ManufacturerDAO
from ui.generated.ui_component_list_page import Ui_ComponentListPage
from ui.widgets.base_page import BasePage
from ui.widgets.component_dialog import ComponentDialog
from utils.formatters import format_int
from utils.ui_helpers import confirm, show_warning

category_dao = CategoryDAO()
manufacturer_dao = ManufacturerDAO()
product_dao = ProductDAO()
component_dao = ComponentDAO()

LOW_STOCK_COLOR = QColor("#DC2626")


class ComponentListPage(BasePage):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_ComponentListPage()
        self.ui.setupUi(self)

        self._results: list[dict] = []

        self.ui.txtSearch.textChanged.connect(self._on_filter_changed)
        self.ui.cboFilterCategory.currentIndexChanged.connect(self._on_filter_changed)
        self.ui.cboFilterManufacturer.currentIndexChanged.connect(self._on_filter_changed)
        self.ui.cboFilterProduct.currentIndexChanged.connect(self._on_filter_changed)
        self.ui.cboFilterYear.currentIndexChanged.connect(self._on_filter_changed)
        self.ui.chkLowStockOnly.toggled.connect(self._on_filter_changed)
        self.ui.btnClearFilter.clicked.connect(self._on_clear_filter)

        self.ui.btnAddComponent.clicked.connect(self._on_add)
        self.ui.btnEditComponent.clicked.connect(self._on_edit)
        self.ui.btnViewDetail.clicked.connect(self._on_edit)
        self.ui.btnDeleteComponent.clicked.connect(self._on_delete)
        self.ui.tblComponents.itemDoubleClicked.connect(lambda _: self._on_edit())

        self.refresh()

    # ------------------------------------------------------------ BasePage
    def refresh(self) -> None:
        self._load_filter_options()
        self._on_filter_changed()

    # ------------------------------------------------------------ filters
    def _load_filter_options(self) -> None:
        self._reload_combo(self.ui.cboFilterCategory, category_dao.list_all(), "Tất cả loại")
        self._reload_combo(self.ui.cboFilterManufacturer, manufacturer_dao.list_all(), "Tất cả NSX")
        self._reload_combo(self.ui.cboFilterProduct, product_dao.list_all(), "Tất cả sản phẩm")

        self.ui.cboFilterYear.blockSignals(True)
        current_year = self.ui.cboFilterYear.currentData()
        self.ui.cboFilterYear.clear()
        self.ui.cboFilterYear.addItem("Tất cả năm", None)
        for y in component_dao.list_years():
            self.ui.cboFilterYear.addItem(str(y), y)
        idx = self.ui.cboFilterYear.findData(current_year)
        self.ui.cboFilterYear.setCurrentIndex(idx if idx >= 0 else 0)
        self.ui.cboFilterYear.blockSignals(False)

    @staticmethod
    def _reload_combo(combo, rows: list[dict], all_label: str) -> None:
        combo.blockSignals(True)
        current_data = combo.currentData()
        combo.clear()
        combo.addItem(all_label, None)
        for r in rows:
            combo.addItem(r["name"], r["id"])
        idx = combo.findData(current_data)
        combo.setCurrentIndex(idx if idx >= 0 else 0)
        combo.blockSignals(False)

    def _on_clear_filter(self) -> None:
        self.ui.txtSearch.blockSignals(True)
        self.ui.txtSearch.clear()
        self.ui.txtSearch.blockSignals(False)
        for combo in (
            self.ui.cboFilterCategory,
            self.ui.cboFilterManufacturer,
            self.ui.cboFilterProduct,
            self.ui.cboFilterYear,
        ):
            combo.blockSignals(True)
            combo.setCurrentIndex(0)
            combo.blockSignals(False)
        self.ui.chkLowStockOnly.blockSignals(True)
        self.ui.chkLowStockOnly.setChecked(False)
        self.ui.chkLowStockOnly.blockSignals(False)
        self._on_filter_changed()

    def _on_filter_changed(self, *_args) -> None:
        self._results = component_dao.search(
            keyword=self.ui.txtSearch.text().strip(),
            category_id=self.ui.cboFilterCategory.currentData(),
            manufacturer_id=self.ui.cboFilterManufacturer.currentData(),
            product_id=self.ui.cboFilterProduct.currentData(),
            year=self.ui.cboFilterYear.currentData(),
            low_stock_only=self.ui.chkLowStockOnly.isChecked(),
        )
        self._populate_table()

    # ------------------------------------------------------------ table
    def _populate_table(self) -> None:
        table = self.ui.tblComponents
        table.setSortingEnabled(False)
        table.setRowCount(0)
        for row, c in enumerate(self._results):
            table.insertRow(row)
            code_item = QTableWidgetItem(c["code"])
            code_item.setData(Qt.ItemDataRole.UserRole, c["id"])
            table.setItem(row, 0, code_item)
            table.setItem(row, 1, QTableWidgetItem(c.get("barcode") or ""))
            table.setItem(row, 2, QTableWidgetItem(c["name"]))
            table.setItem(row, 3, QTableWidgetItem(c.get("category_name") or ""))
            table.setItem(row, 4, QTableWidgetItem(c.get("manufacturer_name") or ""))
            table.setItem(row, 5, QTableWidgetItem(c.get("unit") or ""))

            qty_item = QTableWidgetItem(format_int(c.get("quantity")))
            if (c.get("quantity") or 0) <= (c.get("min_quantity") or 0):
                qty_item.setForeground(LOW_STOCK_COLOR)
            table.setItem(row, 6, qty_item)

            table.setItem(row, 7, QTableWidgetItem(str(c.get("year_imported") or "")))
            table.setItem(row, 8, QTableWidgetItem(c.get("location") or ""))
        table.setSortingEnabled(True)
        self.ui.lblResultCount.setText(f"{len(self._results)} linh kiện")

    def _selected_component_id(self) -> int | None:
        row = self.ui.tblComponents.currentRow()
        if row < 0:
            return None
        item = self.ui.tblComponents.item(row, 0)
        return item.data(Qt.ItemDataRole.UserRole) if item else None

    # ------------------------------------------------------------ CRUD actions
    def _on_add(self) -> None:
        dlg = ComponentDialog(self)
        if dlg.exec() == QDialog.DialogCode.Accepted:
            self.refresh()

    def _on_edit(self) -> None:
        component_id = self._selected_component_id()
        if component_id is None:
            show_warning(self, "Vui lòng chọn một linh kiện trong danh sách.")
            return
        dlg = ComponentDialog(self, component_id=component_id)
        if dlg.exec() == QDialog.DialogCode.Accepted:
            self.refresh()

    def _on_delete(self) -> None:
        component_id = self._selected_component_id()
        if component_id is None:
            show_warning(self, "Vui lòng chọn một linh kiện trong danh sách.")
            return
        if confirm(
            self,
            "Bạn có chắc muốn xóa linh kiện này?\n"
            "(Lịch sử phiếu nhập/xuất liên quan vẫn được giữ nguyên)",
        ):
            component_dao.delete(component_id, soft=True)
            self.refresh()
