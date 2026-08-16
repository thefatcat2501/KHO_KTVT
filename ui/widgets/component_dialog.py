"""
ui/widgets/component_dialog.py
--------------------------------
Hộp thoại thêm mới / sửa thông tin linh kiện. Được dùng ở 2 nơi:
    1) Trang "Linh kiện / Vật tư" (nút Thêm / Sửa)
    2) Trang Nhập kho / Xuất kho khi quét phải mã vạch CHƯA có trong CSDL
       (mở dialog này ở chế độ thêm mới, tự điền sẵn mã vạch vừa quét)

Lưu ý thiết kế: sau khi linh kiện đã tồn tại, ô "Tồn kho ban đầu" và
"Mã linh kiện" sẽ bị khóa khi sửa - tồn kho từ lúc này chỉ được phép
thay đổi thông qua phiếu Nhập/Xuất kho để đảm bảo số liệu luôn khớp với
lịch sử giao dịch (không cho sửa tay gây sai lệch tồn kho).
"""
from datetime import datetime

from PySide6.QtCore import Qt
from PySide6.QtWidgets import QCompleter, QDialog, QListWidgetItem

from config import DEFAULT_UNITS
from dao.base_lookup_dao import CategoryDAO, ProductDAO
from dao.component_dao import ComponentDAO
from dao.manufacturer_dao import ManufacturerDAO
from services.component_service import component_service
from ui.generated.ui_component_dialog import Ui_ComponentDialog
from utils.exceptions import AppError

category_dao = CategoryDAO()
product_dao = ProductDAO()
manufacturer_dao = ManufacturerDAO()
component_dao = ComponentDAO()


class ComponentDialog(QDialog):
    def __init__(self, parent=None, component_id: int | None = None, prefill_barcode: str = ""):
        super().__init__(parent)
        self.ui = Ui_ComponentDialog()
        self.ui.setupUi(self)

        self.component_id = component_id
        self.saved_component_id: int | None = None  # nơi caller đọc kết quả sau khi accept()

        self._load_lookups()
        self._setup_autocomplete()
        self.ui.cboUnit.addItems(DEFAULT_UNITS)
        self.ui.spnYear.setValue(datetime.now().year)

        if component_id:
            self.ui.lblDialogTitle.setText("Sửa thông tin linh kiện")
            self._load_component(component_id)
        else:
            self.ui.lblDialogTitle.setText("Thêm linh kiện mới")
            if prefill_barcode:
                self.ui.txtBarcode.setText(prefill_barcode)
                self.ui.txtName.setFocus()

        self.ui.btnSave.clicked.connect(self._on_save)
        self.ui.btnCancel.clicked.connect(self.reject)
        self.ui.txtProductSearch.textChanged.connect(self._on_product_search_changed)

    # ------------------------------------------------------------ gợi ý tự động (autocomplete)
    def _setup_autocomplete(self) -> None:
        """Gợi ý dạng dropdown khi gõ, khớp theo TIỀN TỐ (bắt đầu bằng ký tự
        đã gõ) - VD: gõ "RES" gợi ý RES10K, RES1M... Áp dụng cho "Mã linh
        kiện" (chỉ hữu ích khi thêm mới - ô này bị khóa khi sửa) và "Vị trí
        lưu kho" (giúp tái sử dụng đúng tên vị trí đã có, tránh gõ lệch chữ
        VD "Kệ A" và "Ke A" thành 2 vị trí khác nhau)."""
        code_completer = QCompleter(component_dao.list_all_codes(), self)
        code_completer.setCaseSensitivity(Qt.CaseSensitivity.CaseInsensitive)
        code_completer.setFilterMode(Qt.MatchFlag.MatchStartsWith)
        code_completer.setCompletionMode(QCompleter.CompletionMode.PopupCompletion)
        self.ui.txtCode.setCompleter(code_completer)

        location_completer = QCompleter(component_dao.list_distinct_locations(), self)
        location_completer.setCaseSensitivity(Qt.CaseSensitivity.CaseInsensitive)
        location_completer.setFilterMode(Qt.MatchFlag.MatchStartsWith)
        location_completer.setCompletionMode(QCompleter.CompletionMode.PopupCompletion)
        self.ui.txtLocation.setCompleter(location_completer)

    def _on_product_search_changed(self, text: str) -> None:
        """Lọc nhanh danh sách "Sản phẩm sử dụng" theo tiền tố đang gõ,
        không đổi trạng thái tick đã chọn - chỉ ẩn/hiện dòng không khớp."""
        keyword = text.strip().lower()
        for i in range(self.ui.lstProducts.count()):
            item = self.ui.lstProducts.item(i)
            item.setHidden(bool(keyword) and not item.text().lower().startswith(keyword))

    # ------------------------------------------------------------ load data
    def _load_lookups(self) -> None:
        self.ui.cboCategory.clear()
        self.ui.cboCategory.addItem("", None)
        for c in category_dao.list_all():
            self.ui.cboCategory.addItem(c["name"], c["id"])

        self.ui.cboManufacturer.clear()
        self.ui.cboManufacturer.addItem("", None)
        for m in manufacturer_dao.list_all():
            self.ui.cboManufacturer.addItem(m["name"], m["id"])

        self.ui.lstProducts.clear()
        for p in product_dao.list_all():
            item = QListWidgetItem(p["name"])
            item.setData(Qt.ItemDataRole.UserRole, p["id"])
            item.setFlags(item.flags() | Qt.ItemFlag.ItemIsUserCheckable)
            item.setCheckState(Qt.CheckState.Unchecked)
            self.ui.lstProducts.addItem(item)

    def _load_component(self, component_id: int) -> None:
        c = component_dao.get_by_id(component_id)
        if not c:
            return
        self.ui.txtCode.setText(c["code"])
        self.ui.txtCode.setEnabled(False)
        self.ui.txtBarcode.setText(c.get("barcode") or "")
        self.ui.txtName.setText(c["name"])
        self._select_combo_by_data(self.ui.cboCategory, c.get("category_id"))
        self._select_combo_by_data(self.ui.cboManufacturer, c.get("manufacturer_id"))
        unit_idx = self.ui.cboUnit.findText(c.get("unit") or "")
        if unit_idx >= 0:
            self.ui.cboUnit.setCurrentIndex(unit_idx)
        else:
            self.ui.cboUnit.setCurrentText(c.get("unit") or "")
        self.ui.spnQuantity.setValue(c.get("quantity") or 0)
        self.ui.spnQuantity.setEnabled(False)
        self.ui.spnQuantity.setToolTip("Tồn kho chỉ có thể thay đổi qua phiếu Nhập/Xuất kho.")
        self.ui.spnMinQuantity.setValue(c.get("min_quantity") or 0)
        self.ui.spnYear.setValue(c.get("year_imported") or datetime.now().year)
        self.ui.txtLocation.setText(c.get("location") or "")
        self.ui.pteDescription.setPlainText(c.get("description") or "")

        product_ids = set(c.get("product_ids") or [])
        for i in range(self.ui.lstProducts.count()):
            item = self.ui.lstProducts.item(i)
            if item.data(Qt.ItemDataRole.UserRole) in product_ids:
                item.setCheckState(Qt.CheckState.Checked)

    @staticmethod
    def _select_combo_by_data(combo, data_value) -> None:
        for i in range(combo.count()):
            if combo.itemData(i) == data_value:
                combo.setCurrentIndex(i)
                return
        combo.setCurrentIndex(0)

    # ------------------------------------------------------------ save
    def _on_save(self) -> None:
        self.ui.lblFormError.setText("")
        name = self.ui.txtName.text().strip()
        if not name:
            self.ui.lblFormError.setText("Vui lòng nhập tên linh kiện.")
            return

        category_id = self._get_or_create_lookup(self.ui.cboCategory, category_dao)
        manufacturer_id = self._get_or_create_lookup(self.ui.cboManufacturer, manufacturer_dao)

        data = {
            "code": self.ui.txtCode.text().strip(),
            "barcode": self.ui.txtBarcode.text().strip(),
            "name": name,
            "category_id": category_id,
            "manufacturer_id": manufacturer_id,
            "unit": self.ui.cboUnit.currentText().strip() or "Cái",
            "quantity": self.ui.spnQuantity.value(),
            "min_quantity": self.ui.spnMinQuantity.value(),
            "year_imported": self.ui.spnYear.value(),
            "location": self.ui.txtLocation.text().strip(),
            "description": self.ui.pteDescription.toPlainText().strip(),
        }
        product_ids = [
            self.ui.lstProducts.item(i).data(Qt.ItemDataRole.UserRole)
            for i in range(self.ui.lstProducts.count())
            if self.ui.lstProducts.item(i).checkState() == Qt.CheckState.Checked
        ]

        try:
            if self.component_id:
                component_service.update_component(self.component_id, data, product_ids)
                self.saved_component_id = self.component_id
            else:
                self.saved_component_id = component_service.create_component(data, product_ids)
            self.accept()
        except AppError as e:
            self.ui.lblFormError.setText(str(e))

    @staticmethod
    def _get_or_create_lookup(combo, dao):
        text = combo.currentText().strip()
        if not text:
            return None
        idx = combo.findText(text)
        if idx >= 0:
            return combo.itemData(idx)
        return dao.get_or_create(text)
