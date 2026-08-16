"""
ui/widgets/main_window.py
----------------------------
Cửa sổ chính của ứng dụng: ghép các trang (Dashboard, Linh kiện, Nhập
kho, Xuất kho, Lịch sử phiếu, Danh mục, Sao lưu) vào QStackedWidget và
điều khiển việc chuyển trang khi người dùng bấm vào các nút trên
sidebar - đảm bảo giao diện tương ứng luôn được hiển thị chính xác.
"""
from datetime import datetime
from pathlib import Path

from PySide6.QtCore import QSize, Qt, QTimer
from PySide6.QtGui import QIcon, QPainter, QPixmap
from PySide6.QtSvg import QSvgRenderer
from PySide6.QtWidgets import QButtonGroup, QMainWindow

from ui.generated.ui_main_window import Ui_MainWindow
from ui.widgets.backup_page import BackupPage
from ui.widgets.categories_page import CategoriesPage
from ui.widgets.component_list_page import ComponentListPage
from ui.widgets.dashboard_page import DashboardPage
from ui.widgets.receipt_history_page import ReceiptHistoryPage
from ui.widgets.stock_transaction_page import StockTransactionPage

WEEKDAY_VI = {
    0: "Thứ Hai",
    1: "Thứ Ba",
    2: "Thứ Tư",
    3: "Thứ Năm",
    4: "Thứ Sáu",
    5: "Thứ Bảy",
    6: "Chủ Nhật",
}

# resources/icons/ nằm ở gốc dự án, 3 cấp trên file này (ui/widgets/main_window.py)
LOGO_PATH = Path(__file__).resolve().parent.parent.parent / "resources" / "icons" / "app_logo.svg"


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self._load_logo()

        # ---- Khởi tạo tất cả các trang nội dung ----
        self.dashboard_page = DashboardPage()
        self.component_list_page = ComponentListPage()
        self.stock_in_page = StockTransactionPage(mode="IN")
        self.stock_out_page = StockTransactionPage(mode="OUT")
        self.receipt_history_page = ReceiptHistoryPage()
        self.categories_page = CategoriesPage()
        self.backup_page = BackupPage()

        self._pages = {
            "dashboard": (self.ui.btnNavDashboard, self.dashboard_page, "Tổng quan"),
            "components": (self.ui.btnNavComponents, self.component_list_page, "Linh kiện / Vật tư"),
            "stock_in": (self.ui.btnNavStockIn, self.stock_in_page, "Nhập kho"),
            "stock_out": (self.ui.btnNavStockOut, self.stock_out_page, "Xuất kho"),
            "receipts": (self.ui.btnNavReceipts, self.receipt_history_page, "Lịch sử phiếu"),
            "categories": (self.ui.btnNavCategories, self.categories_page, "Danh mục"),
            "backup": (self.ui.btnNavBackup, self.backup_page, "Sao lưu & Khôi phục"),
        }

        self._nav_group = QButtonGroup(self)
        self._nav_group.setExclusive(True)
        for key, (btn, page, _title) in self._pages.items():
            self.ui.stackedWidget.addWidget(page)
            self._nav_group.addButton(btn)
            btn.clicked.connect(lambda _checked=False, k=key: self._navigate(k))

        # Dashboard có các nút "Nhập kho ngay" / "Tạo phiếu..." -> điều hướng chéo sang trang khác
        self.dashboard_page.navigate_requested.connect(self._navigate)

        # Sau khi khôi phục dữ liệu từ file sao lưu, làm mới TOÀN BỘ các trang ngay lập tức
        self.backup_page.restored.connect(self._refresh_all_pages)

        self._navigate("dashboard")

        self._clock_timer = QTimer(self)
        self._clock_timer.timeout.connect(self._update_clock)
        self._clock_timer.start(1000)
        self._update_clock()

        self.setWindowTitle("Phần mềm Quản lý Kho Linh kiện")

    # ------------------------------------------------------------ logo
    def _load_logo(self) -> None:
        """Nạp logo (SVG): vào góc trên-trái sidebar (lblLogoIcon) VÀ vào
        icon cửa sổ/taskbar (setWindowIcon) - hiện ngay trước chữ
        "Phần mềm Quản lý Kho Linh kiện" trên thanh tiêu đề."""
        if not LOGO_PATH.exists():
            return

        sidebar_pixmap = self._render_svg(size=40)
        self.ui.lblLogoIcon.setPixmap(sidebar_pixmap)
        self.ui.lblLogoIcon.setFixedSize(QSize(40, 40))

        # Icon cửa sổ/taskbar cần độ phân giải cao hơn để Windows tự
        # chọn kích thước phù hợp (title bar, Alt+Tab, taskbar...).
        icon = QIcon()
        for size in (16, 32, 48, 64, 128, 256):
            icon.addPixmap(self._render_svg(size=size))
        self.setWindowIcon(icon)

    @staticmethod
    def _render_svg(size: int) -> QPixmap:
        pixmap = QPixmap(size, size)
        pixmap.fill(Qt.GlobalColor.transparent)
        renderer = QSvgRenderer(str(LOGO_PATH))
        painter = QPainter(pixmap)
        renderer.render(painter)
        painter.end()
        return pixmap

    # ------------------------------------------------------------ navigation
    def _navigate(self, key: str) -> None:
        if key not in self._pages:
            return
        btn, page, title = self._pages[key]
        self.ui.stackedWidget.setCurrentWidget(page)
        self.ui.lblPageTitle.setText(title)
        btn.setChecked(True)
        page.refresh()  # luôn nạp lại dữ liệu mới nhất mỗi khi chuyển sang 1 trang

    def _refresh_all_pages(self) -> None:
        for _btn, page, _title in self._pages.values():
            page.refresh()

    def _update_clock(self) -> None:
        now = datetime.now()
        weekday = WEEKDAY_VI.get(now.weekday(), "")
        self.ui.lblDateTime.setText(f"{weekday}, {now.strftime('%d/%m/%Y  %H:%M:%S')}")
