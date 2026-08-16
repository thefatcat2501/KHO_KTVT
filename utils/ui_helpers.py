"""utils/ui_helpers.py - Hàm tiện ích hiển thị hộp thoại thông báo dùng chung."""
from PySide6.QtWidgets import QMessageBox


def show_error(parent, message: str, title: str = "Lỗi") -> None:
    QMessageBox.critical(parent, title, message)


def show_warning(parent, message: str, title: str = "Cảnh báo") -> None:
    QMessageBox.warning(parent, title, message)


def show_info(parent, message: str, title: str = "Thông báo") -> None:
    QMessageBox.information(parent, title, message)


def confirm(parent, message: str, title: str = "Xác nhận") -> bool:
    reply = QMessageBox.question(
        parent,
        title,
        message,
        QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No,
        QMessageBox.StandardButton.No,
    )
    return reply == QMessageBox.StandardButton.Yes
