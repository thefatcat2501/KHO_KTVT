"""ui/widgets/dashboard_page.py - Trang tổng quan: số liệu thống kê nhanh + cảnh báo sắp hết hàng."""
from PySide6.QtCore import Signal
from PySide6.QtWidgets import QDialog, QHeaderView, QTableWidgetItem

from dao.component_dao import ComponentDAO
from database.db_manager import db_manager
from services.backup_service import backup_service
from ui.generated.ui_dashboard_page import Ui_DashboardPage
from ui.widgets.base_page import BasePage
from ui.widgets.component_dialog import ComponentDialog
from utils.formatters import format_int
from utils.ui_helpers import show_error, show_info

component_dao = ComponentDAO()


class DashboardPage(BasePage):
    navigate_requested = Signal(str)  # "stock_in" | "stock_out" | ...

    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_DashboardPage()
        self.ui.setupUi(self)

        # Các cột tự co giãn vừa đủ nội dung/tiêu đề (trừ cột cuối - đã
        # được kéo giãn lấp đầy phần còn lại nhờ horizontalHeaderStretchLastSection
        # đặt sẵn trong file .ui) -> tiêu đề dài như "Ngưỡng tối thiểu"
        # luôn hiển thị đầy đủ, không bị cắt chữ.
        self.ui.tblLowStock.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.ResizeToContents)

        self.ui.btnGoToStockIn.clicked.connect(lambda: self.navigate_requested.emit("stock_in"))
        self.ui.btnQuickStockIn.clicked.connect(lambda: self.navigate_requested.emit("stock_in"))
        self.ui.btnQuickStockOut.clicked.connect(lambda: self.navigate_requested.emit("stock_out"))
        self.ui.btnQuickAddComponent.clicked.connect(self._on_quick_add_component)
        self.ui.btnQuickBackup.clicked.connect(self._on_quick_backup)

        self.refresh()

    # ------------------------------------------------------------ BasePage
    def refresh(self) -> None:
        self.ui.lblCard1Value.setText(format_int(component_dao.count_all()))
        self.ui.lblCard2Value.setText(format_int(component_dao.total_stock_quantity()))
        self.ui.lblCard3Value.setText(format_int(component_dao.count_low_stock()))
        self.ui.lblCard4Value.setText(format_int(self._count_receipts_today()))

        low_stock = component_dao.list_low_stock(limit=30)
        table = self.ui.tblLowStock
        table.setRowCount(0)
        for i, c in enumerate(low_stock):
            table.insertRow(i)
            table.setItem(i, 0, QTableWidgetItem(c["code"]))
            table.setItem(i, 1, QTableWidgetItem(c["name"]))
            table.setItem(i, 2, QTableWidgetItem(format_int(c["quantity"])))
            table.setItem(i, 3, QTableWidgetItem(format_int(c["min_quantity"])))
            table.setItem(i, 4, QTableWidgetItem(c.get("manufacturer_name") or ""))

    @staticmethod
    def _count_receipts_today() -> int:
        row = db_manager.query_one(
            "SELECT "
            "  (SELECT COUNT(*) FROM import_receipts WHERE date(created_at) = date('now','localtime')) "
            "+ (SELECT COUNT(*) FROM export_receipts WHERE date(created_at) = date('now','localtime')) "
            "AS c"
        )
        return row["c"] if row else 0

    # ------------------------------------------------------------ quick actions
    def _on_quick_add_component(self) -> None:
        dlg = ComponentDialog(self)
        if dlg.exec() == QDialog.DialogCode.Accepted:
            self.refresh()

    def _on_quick_backup(self) -> None:
        try:
            path = backup_service.create_backup()
            show_info(self, f"Đã tạo bản sao lưu dữ liệu thành công:\n{path.name}")
        except Exception as e:  # noqa: BLE001 - hiển thị lỗi hệ thống nếu có, không để crash UI
            show_error(self, f"Không thể tạo bản sao lưu: {e}")
