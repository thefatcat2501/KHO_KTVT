"""
config.py
---------
Cấu hình chung cho toàn bộ ứng dụng: đường dẫn dữ liệu, thư mục backup,
hằng số dùng chung. Cơ sở dữ liệu được lưu trực tiếp trên máy cài đặt
(local), KHÔNG phụ thuộc mạng/internet.
"""
import os
import sys
from pathlib import Path

APP_NAME = "QuanLyKhoLinhKien"
APP_DISPLAY_NAME = "Phần mềm Quản lý Kho Linh kiện"
APP_VERSION = "1.0.0"


def _get_app_data_dir() -> Path:
    """
    Trả về thư mục lưu dữ liệu ứng dụng theo hệ điều hành.
    - Windows : %APPDATA%\\QuanLyKhoLinhKien
    - macOS   : ~/Library/Application Support/QuanLyKhoLinhKien
    - Linux   : ~/.local/share/QuanLyKhoLinhKien
    Khi chạy dưới dạng file .exe đóng gói (PyInstaller), logic này vẫn
    hoạt động đúng vì chỉ dựa trên biến môi trường / thư mục home.
    """
    if sys.platform.startswith("win"):
        base = os.environ.get("APPDATA") or str(Path.home())
        return Path(base) / APP_NAME
    elif sys.platform == "darwin":
        return Path.home() / "Library" / "Application Support" / APP_NAME
    else:
        base = os.environ.get("XDG_DATA_HOME") or str(Path.home() / ".local" / "share")
        return Path(base) / APP_NAME


# Thư mục gốc chứa mã nguồn (dùng để tìm resources, ui khi chạy từ source)
BASE_DIR = Path(__file__).resolve().parent

# Thư mục dữ liệu người dùng (DB + backup) - tách biệt khỏi mã nguồn để
# không bị mất dữ liệu khi cập nhật phần mềm.
APP_DATA_DIR = _get_app_data_dir()
DB_DIR = APP_DATA_DIR / "data"
BACKUP_DIR = APP_DATA_DIR / "backups"

DB_DIR.mkdir(parents=True, exist_ok=True)
BACKUP_DIR.mkdir(parents=True, exist_ok=True)

DB_PATH = DB_DIR / "inventory.db"
SCHEMA_PATH = BASE_DIR / "database" / "schema.sql"

# Resources
STYLE_QSS_PATH = BASE_DIR / "resources" / "styles" / "modern.qss"
ICONS_DIR = BASE_DIR / "resources" / "icons"

# Đơn vị tính mặc định gợi ý
DEFAULT_UNITS = ["Cái", "Chiếc", "Hộp", "Cuộn", "Bộ", "Mét", "Kg", "Gói"]

# Ngưỡng thời gian (ms) giữa 2 ký tự để phân biệt máy quét mã vạch với
# người gõ tay (máy quét thường gõ rất nhanh, < 30ms/ký tự).
BARCODE_SCAN_INTERVAL_MS = 40
BARCODE_MIN_LENGTH = 4
