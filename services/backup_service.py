"""
services/backup_service.py
----------------------------
Sao lưu (backup) và khôi phục (restore) dữ liệu CSDL SQLite.

Dùng SQLite Online Backup API (Connection.backup) thay vì copy file trực
tiếp, vì cách này an toàn ngay cả khi CSDL đang được sử dụng/ghi dữ liệu
(tránh trường hợp copy file .db bị lỗi giữa chừng, hỏng dữ liệu).
"""
import shutil
import sqlite3
from datetime import datetime
from pathlib import Path

from config import BACKUP_DIR, DB_PATH
from database.db_manager import db_manager
from utils.exceptions import AppError

BACKUP_PREFIX = "backup_"
BACKUP_SUFFIX = ".db"


class BackupService:
    def create_backup(self) -> Path:
        """Tạo 1 bản sao lưu mới, trả về đường dẫn file backup."""
        BACKUP_DIR.mkdir(parents=True, exist_ok=True)
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        backup_path = BACKUP_DIR / f"{BACKUP_PREFIX}{timestamp}{BACKUP_SUFFIX}"

        src_conn = db_manager.connection
        dst_conn = sqlite3.connect(str(backup_path))
        try:
            src_conn.backup(dst_conn)
        finally:
            dst_conn.close()
        return backup_path

    def list_backups(self) -> list[dict]:
        BACKUP_DIR.mkdir(parents=True, exist_ok=True)
        results = []
        for f in sorted(BACKUP_DIR.glob(f"{BACKUP_PREFIX}*{BACKUP_SUFFIX}"), reverse=True):
            stat = f.stat()
            results.append(
                {
                    "path": f,
                    "name": f.name,
                    "created_at": datetime.fromtimestamp(stat.st_mtime),
                    "size_bytes": stat.st_size,
                }
            )
        return results

    def restore_backup(self, backup_path: Path) -> None:
        """
        Khôi phục CSDL từ 1 file backup. Trước khi ghi đè, tự động tạo
        thêm 1 bản sao lưu "an toàn" của CSDL hiện tại để có thể hoàn tác
        nếu file backup được chọn bị lỗi hoặc không đúng định dạng.
        """
        backup_path = Path(backup_path)
        if not backup_path.exists():
            raise AppError("Không tìm thấy file sao lưu đã chọn.")

        # Kiểm tra sơ bộ file backup có phải CSDL SQLite hợp lệ không
        try:
            test_conn = sqlite3.connect(str(backup_path))
            test_conn.execute("SELECT name FROM sqlite_master WHERE type='table' LIMIT 1")
            test_conn.close()
        except sqlite3.DatabaseError:
            raise AppError("File sao lưu không hợp lệ hoặc đã bị hỏng.")

        # Sao lưu an toàn CSDL hiện tại trước khi ghi đè
        safety_dir = BACKUP_DIR / "truoc_khi_khoi_phuc"
        safety_dir.mkdir(parents=True, exist_ok=True)
        safety_name = f"{BACKUP_PREFIX}truockhiphuchoi_{datetime.now().strftime('%Y%m%d_%H%M%S')}{BACKUP_SUFFIX}"
        db_manager.connection.commit()
        shutil.copy2(DB_PATH, safety_dir / safety_name)

        db_manager.close()
        shutil.copy2(backup_path, DB_PATH)
        db_manager.reconnect()

    def delete_backup(self, backup_path: Path) -> None:
        backup_path = Path(backup_path)
        if backup_path.exists() and backup_path.parent == BACKUP_DIR:
            backup_path.unlink()


backup_service = BackupService()
