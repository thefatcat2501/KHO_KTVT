"""
main.py
--------
Điểm khởi chạy chính của Phần mềm Quản lý Kho Linh kiện.

Chạy bằng:
    python main.py

CSDL SQLite được tạo tự động (nếu chưa có) tại thư mục dữ liệu người
dùng của hệ điều hành (xem config.py) - không cần cấu hình gì thêm,
không cần internet, không cần đăng nhập.
"""
import sys

from PySide6.QtWidgets import QApplication

from config import APP_DISPLAY_NAME, STYLE_QSS_PATH
from ui.widgets.main_window import MainWindow


def load_stylesheet() -> str:
    try:
        with open(STYLE_QSS_PATH, "r", encoding="utf-8") as f:
            return f.read()
    except FileNotFoundError:
        return ""


def main() -> int:
    app = QApplication(sys.argv)
    app.setApplicationName(APP_DISPLAY_NAME)
    app.setStyleSheet(load_stylesheet())

    window = MainWindow()
    window.showMaximized()

    return app.exec()


if __name__ == "__main__":
    sys.exit(main())
