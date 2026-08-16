"""utils/exceptions.py - Các lớp exception nghiệp vụ dùng chung."""


class AppError(Exception):
    """Lỗi nghiệp vụ chung, thông điệp có thể hiển thị trực tiếp cho người dùng."""


class InsufficientStockError(AppError):
    """Số lượng tồn kho không đủ để xuất kho."""


class DuplicateBarcodeError(AppError):
    """Mã vạch đã tồn tại trên một linh kiện khác."""


class DuplicateCodeError(AppError):
    """Mã linh kiện đã tồn tại."""


class EmptyReceiptError(AppError):
    """Phiếu nhập/xuất không có dòng linh kiện nào."""


class ValidationError(AppError):
    """Dữ liệu nhập vào không hợp lệ."""
