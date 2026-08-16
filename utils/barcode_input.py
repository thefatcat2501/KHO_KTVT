"""
utils/barcode_input.py
-----------------------
Widget nhận dữ liệu từ máy quét mã vạch (barcode scanner).

Hầu hết máy quét mã vạch USB trên thị trường hoạt động ở chế độ
"HID keyboard-wedge": với hệ điều hành và ứng dụng, chúng hoạt động y
hệt một bàn phím - khi quét, máy sẽ "gõ" rất nhanh toàn bộ ký tự của mã
vạch rồi tự động gửi thêm phím Enter. Đây chính xác là cách các phần
mềm thu ngân/siêu thị vẫn dùng, nên KHÔNG cần driver hay thư viện đặc
biệt: chỉ cần một ô nhập liệu luôn giữ focus và lắng nghe phím Enter.

BarcodeLineEdit kế thừa QLineEdit, phát tín hiệu scanned(str) mỗi khi
một mã được nhập xong (Enter), sau đó tự xóa nội dung và giữ focus để
sẵn sàng nhận lượt quét tiếp theo -> cho phép quét liên tục nhiều mã
vạch mà không cần thao tác chuột/bàn phím nào thêm.

Ghi chú: nếu sau này cần dùng máy quét kết nối qua cổng COM/Serial
(một số dòng máy quét công nghiệp), chỉ cần bổ sung thêm một adapter đọc
dữ liệu serial khác và cùng phát ra tín hiệu scanned(str) này, phần còn
lại của ứng dụng không cần thay đổi.
"""
from PySide6.QtCore import Signal
from PySide6.QtWidgets import QLineEdit

from config import BARCODE_MIN_LENGTH


class BarcodeLineEdit(QLineEdit):
    """Ô nhập liệu chuyên dụng để quét mã vạch liên tục kiểu POS."""

    scanned = Signal(str)

    def __init__(self, parent=None):
        super().__init__(parent)
        self.returnPressed.connect(self._on_return_pressed)

    def _on_return_pressed(self) -> None:
        code = self.text().strip()
        self.clear()
        if len(code) >= BARCODE_MIN_LENGTH:
            self.scanned.emit(code)
        self.setFocus()

    def focus_and_select(self) -> None:
        self.setFocus()
        self.selectAll()
