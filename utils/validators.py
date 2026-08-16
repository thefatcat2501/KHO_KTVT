"""utils/validators.py - Hàm kiểm tra dữ liệu nhập vào từ các form."""
from utils.exceptions import ValidationError


def require_text(value: str, field_label: str) -> str:
    value = (value or "").strip()
    if not value:
        raise ValidationError(f"{field_label} không được để trống.")
    return value


def require_positive_int(value, field_label: str) -> int:
    try:
        n = int(value)
    except (TypeError, ValueError):
        raise ValidationError(f"{field_label} phải là số nguyên.")
    if n <= 0:
        raise ValidationError(f"{field_label} phải lớn hơn 0.")
    return n
