"""ui/widgets/base_page.py - Lớp cơ sở cho các trang nội dung trong QStackedWidget."""
from PySide6.QtWidgets import QWidget


class BasePage(QWidget):
    """
    Các trang (Dashboard, Danh sách linh kiện, Nhập kho...) đều kế thừa
    lớp này. MainWindow sẽ tự động gọi refresh() mỗi khi người dùng
    chuyển sang trang đó, để đảm bảo dữ liệu hiển thị luôn mới nhất
    (VD: sau khi lưu phiếu nhập kho thì Dashboard phải cập nhật lại
    tồn kho ngay).
    """

    def refresh(self) -> None:
        """Nạp lại dữ liệu mới nhất cho trang. Lớp con override khi cần."""
        pass
