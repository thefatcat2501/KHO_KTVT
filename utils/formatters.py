"""utils/formatters.py - Hàm định dạng hiển thị dùng chung cho toàn bộ UI."""
from datetime import datetime


def format_money(value: float | int | None) -> str:
    """1234567 -> '1.234.567 đ'"""
    try:
        value = float(value or 0)
    except (TypeError, ValueError):
        value = 0.0
    text = f"{value:,.0f}".replace(",", ".")
    return f"{text} đ"


def format_int(value: int | None) -> str:
    try:
        value = int(value or 0)
    except (TypeError, ValueError):
        value = 0
    return f"{value:,}".replace(",", ".")


def format_datetime(value: str | None, fmt_out: str = "%d/%m/%Y %H:%M") -> str:
    """Chuyển chuỗi datetime kiểu SQLite ('YYYY-MM-DD HH:MM:SS') sang dd/mm/yyyy hh:mm."""
    if not value:
        return "-"
    for fmt_in in ("%Y-%m-%d %H:%M:%S", "%Y-%m-%d"):
        try:
            return datetime.strptime(value, fmt_in).strftime(fmt_out)
        except ValueError:
            continue
    return value


def format_date(value: str | None) -> str:
    return format_datetime(value, "%d/%m/%Y")


def format_file_size(num_bytes: int) -> str:
    size = float(num_bytes)
    for unit in ("B", "KB", "MB", "GB"):
        if size < 1024 or unit == "GB":
            return f"{size:.1f} {unit}" if unit != "B" else f"{int(size)} {unit}"
        size /= 1024
    return f"{size:.1f} GB"
