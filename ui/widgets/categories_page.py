"""
ui/widgets/categories_page.py
--------------------------------
Trang "Danh mục": quản lý Loại linh kiện, Nhà sản xuất, Sản phẩm sử dụng
(các bảng danh mục dùng để lọc & phân loại linh kiện). Mỗi tab là một
CRUD đơn giản độc lập.
"""
import sqlite3

from PySide6.QtCore import Qt
from PySide6.QtWidgets import QTableWidgetItem

from dao.base_lookup_dao import CategoryDAO, ProductDAO
from dao.manufacturer_dao import ManufacturerDAO
from ui.generated.ui_categories_page import Ui_CategoriesPage
from ui.widgets.base_page import BasePage
from utils.ui_helpers import confirm, show_warning

category_dao = CategoryDAO()
manufacturer_dao = ManufacturerDAO()
product_dao = ProductDAO()


class CategoriesPage(BasePage):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_CategoriesPage()
        self.ui.setupUi(self)

        self._category_rows: list[dict] = []
        self._manufacturer_rows: list[dict] = []
        self._product_rows: list[dict] = []
        self._editing_category_id: int | None = None
        self._editing_manufacturer_id: int | None = None
        self._editing_product_id: int | None = None

        self.ui.tblCategory.itemSelectionChanged.connect(self._on_category_selected)
        self.ui.btnCategorySave.clicked.connect(self._on_category_save)
        self.ui.btnCategoryNew.clicked.connect(self._on_category_new)
        self.ui.btnCategoryDelete.clicked.connect(self._on_category_delete)

        self.ui.tblManufacturer.itemSelectionChanged.connect(self._on_manufacturer_selected)
        self.ui.btnManufacturerSave.clicked.connect(self._on_manufacturer_save)
        self.ui.btnManufacturerNew.clicked.connect(self._on_manufacturer_new)
        self.ui.btnManufacturerDelete.clicked.connect(self._on_manufacturer_delete)

        self.ui.tblProduct.itemSelectionChanged.connect(self._on_product_selected)
        self.ui.btnProductSave.clicked.connect(self._on_product_save)
        self.ui.btnProductNew.clicked.connect(self._on_product_new)
        self.ui.btnProductDelete.clicked.connect(self._on_product_delete)

        self.refresh()

    # ------------------------------------------------------------ BasePage
    def refresh(self) -> None:
        self._load_category_table()
        self._load_manufacturer_table()
        self._load_product_table()

    # ================================================================ CATEGORY
    def _load_category_table(self) -> None:
        self._category_rows = category_dao.list_all()
        table = self.ui.tblCategory
        table.setRowCount(0)
        for i, r in enumerate(self._category_rows):
            table.insertRow(i)
            item = QTableWidgetItem(r["name"])
            item.setData(Qt.ItemDataRole.UserRole, r["id"])
            table.setItem(i, 0, item)
            table.setItem(i, 1, QTableWidgetItem(r.get("description") or ""))

    def _on_category_selected(self) -> None:
        row = self.ui.tblCategory.currentRow()
        if not (0 <= row < len(self._category_rows)):
            return
        r = self._category_rows[row]
        self._editing_category_id = r["id"]
        self.ui.txtCategoryName.setText(r["name"])
        self.ui.pteCategoryDesc.setPlainText(r.get("description") or "")

    def _on_category_new(self) -> None:
        self._editing_category_id = None
        self.ui.txtCategoryName.clear()
        self.ui.pteCategoryDesc.clear()
        self.ui.tblCategory.clearSelection()
        self.ui.txtCategoryName.setFocus()

    def _on_category_save(self) -> None:
        name = self.ui.txtCategoryName.text().strip()
        if not name:
            show_warning(self, "Vui lòng nhập tên loại linh kiện.")
            return
        desc = self.ui.pteCategoryDesc.toPlainText().strip()
        try:
            if self._editing_category_id:
                category_dao.update(self._editing_category_id, name, desc)
            else:
                category_dao.create(name, desc)
            self._on_category_new()
            self._load_category_table()
        except sqlite3.IntegrityError:
            show_warning(self, f'Tên loại linh kiện "{name}" đã tồn tại.')

    def _on_category_delete(self) -> None:
        if not self._editing_category_id:
            show_warning(self, "Vui lòng chọn một loại linh kiện để xóa.")
            return
        if confirm(
            self,
            "Xóa loại linh kiện này?\n"
            "Các linh kiện đang thuộc loại này sẽ chuyển về trạng thái chưa phân loại.",
        ):
            category_dao.delete(self._editing_category_id)
            self._on_category_new()
            self._load_category_table()

    # ================================================================ MANUFACTURER
    def _load_manufacturer_table(self) -> None:
        self._manufacturer_rows = manufacturer_dao.list_all()
        table = self.ui.tblManufacturer
        table.setRowCount(0)
        for i, r in enumerate(self._manufacturer_rows):
            table.insertRow(i)
            item = QTableWidgetItem(r["name"])
            item.setData(Qt.ItemDataRole.UserRole, r["id"])
            table.setItem(i, 0, item)
            table.setItem(i, 1, QTableWidgetItem(r.get("contact_info") or ""))
            table.setItem(i, 2, QTableWidgetItem(r.get("address") or ""))

    def _on_manufacturer_selected(self) -> None:
        row = self.ui.tblManufacturer.currentRow()
        if not (0 <= row < len(self._manufacturer_rows)):
            return
        r = self._manufacturer_rows[row]
        self._editing_manufacturer_id = r["id"]
        self.ui.txtManufacturerName.setText(r["name"])
        self.ui.txtManufacturerContact.setText(r.get("contact_info") or "")
        self.ui.txtManufacturerAddress.setText(r.get("address") or "")

    def _on_manufacturer_new(self) -> None:
        self._editing_manufacturer_id = None
        self.ui.txtManufacturerName.clear()
        self.ui.txtManufacturerContact.clear()
        self.ui.txtManufacturerAddress.clear()
        self.ui.tblManufacturer.clearSelection()
        self.ui.txtManufacturerName.setFocus()

    def _on_manufacturer_save(self) -> None:
        name = self.ui.txtManufacturerName.text().strip()
        if not name:
            show_warning(self, "Vui lòng nhập tên nhà sản xuất.")
            return
        contact = self.ui.txtManufacturerContact.text().strip()
        address = self.ui.txtManufacturerAddress.text().strip()
        try:
            if self._editing_manufacturer_id:
                manufacturer_dao.update(self._editing_manufacturer_id, name, contact, address)
            else:
                manufacturer_dao.create(name, contact, address)
            self._on_manufacturer_new()
            self._load_manufacturer_table()
        except sqlite3.IntegrityError:
            show_warning(self, f'Tên nhà sản xuất "{name}" đã tồn tại.')

    def _on_manufacturer_delete(self) -> None:
        if not self._editing_manufacturer_id:
            show_warning(self, "Vui lòng chọn một nhà sản xuất để xóa.")
            return
        if confirm(
            self,
            "Xóa nhà sản xuất này?\n"
            "Các linh kiện đang thuộc nhà sản xuất này sẽ chuyển về trạng thái chưa xác định.",
        ):
            manufacturer_dao.delete(self._editing_manufacturer_id)
            self._on_manufacturer_new()
            self._load_manufacturer_table()

    # ================================================================ PRODUCT
    def _load_product_table(self) -> None:
        self._product_rows = product_dao.list_all()
        table = self.ui.tblProduct
        table.setRowCount(0)
        for i, r in enumerate(self._product_rows):
            table.insertRow(i)
            item = QTableWidgetItem(r["name"])
            item.setData(Qt.ItemDataRole.UserRole, r["id"])
            table.setItem(i, 0, item)
            table.setItem(i, 1, QTableWidgetItem(r.get("description") or ""))

    def _on_product_selected(self) -> None:
        row = self.ui.tblProduct.currentRow()
        if not (0 <= row < len(self._product_rows)):
            return
        r = self._product_rows[row]
        self._editing_product_id = r["id"]
        self.ui.txtProductName.setText(r["name"])
        self.ui.pteProductDesc.setPlainText(r.get("description") or "")

    def _on_product_new(self) -> None:
        self._editing_product_id = None
        self.ui.txtProductName.clear()
        self.ui.pteProductDesc.clear()
        self.ui.tblProduct.clearSelection()
        self.ui.txtProductName.setFocus()

    def _on_product_save(self) -> None:
        name = self.ui.txtProductName.text().strip()
        if not name:
            show_warning(self, "Vui lòng nhập tên sản phẩm sử dụng.")
            return
        desc = self.ui.pteProductDesc.toPlainText().strip()
        try:
            if self._editing_product_id:
                product_dao.update(self._editing_product_id, name, desc)
            else:
                product_dao.create(name, desc)
            self._on_product_new()
            self._load_product_table()
        except sqlite3.IntegrityError:
            show_warning(self, f'Tên sản phẩm "{name}" đã tồn tại.')

    def _on_product_delete(self) -> None:
        if not self._editing_product_id:
            show_warning(self, "Vui lòng chọn một sản phẩm để xóa.")
            return
        if confirm(self, "Xóa sản phẩm sử dụng này khỏi danh mục?"):
            product_dao.delete(self._editing_product_id)
            self._on_product_new()
            self._load_product_table()
