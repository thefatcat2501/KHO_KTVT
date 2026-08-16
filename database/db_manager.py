"""
database/db_manager.py
-----------------------
Lớp quản lý kết nối SQLite tập trung (singleton). Chịu trách nhiệm:
- Khởi tạo file .db và schema nếu chưa tồn tại
- Cung cấp connection dùng chung, bật foreign_keys, row_factory dạng dict
- Cung cấp context manager transaction() để đảm bảo tính toàn vẹn
  (atomic) cho các nghiệp vụ nhập/xuất kho nhiều bước.
"""
import sqlite3
import threading
from contextlib import contextmanager
from pathlib import Path

from config import DB_PATH, SCHEMA_PATH


def _dict_factory(cursor: sqlite3.Cursor, row: tuple) -> dict:
    fields = [col[0] for col in cursor.description]
    return dict(zip(fields, row))


class DatabaseManager:
    """Singleton quản lý 1 kết nối SQLite dùng xuyên suốt ứng dụng."""

    _instance = None
    _lock = threading.Lock()

    def __new__(cls, db_path: Path = None):
        with cls._lock:
            if cls._instance is None:
                cls._instance = super().__new__(cls)
                cls._instance._initialized = False
        return cls._instance

    def __init__(self, db_path: Path = None):
        if self._initialized:
            return
        self.db_path = Path(db_path) if db_path else DB_PATH
        self._conn: sqlite3.Connection | None = None
        self._connect()
        self._init_schema()
        self._initialized = True

    # ------------------------------------------------------------------
    def _connect(self) -> None:
        self.db_path.parent.mkdir(parents=True, exist_ok=True)
        self._conn = sqlite3.connect(
            str(self.db_path),
            check_same_thread=False,
            detect_types=sqlite3.PARSE_DECLTYPES,
        )
        self._conn.row_factory = _dict_factory
        self._conn.execute("PRAGMA foreign_keys = ON;")

    def _init_schema(self) -> None:
        if not SCHEMA_PATH.exists():
            raise FileNotFoundError(f"Không tìm thấy file schema: {SCHEMA_PATH}")
        with open(SCHEMA_PATH, "r", encoding="utf-8") as f:
            script = f.read()
        self._conn.executescript(script)
        self._conn.commit()

    # ------------------------------------------------------------------
    @property
    def connection(self) -> sqlite3.Connection:
        if self._conn is None:
            self._connect()
        return self._conn

    def execute(self, sql: str, params: tuple | dict = ()) -> sqlite3.Cursor:
        return self.connection.execute(sql, params)

    def query_one(self, sql: str, params: tuple | dict = ()) -> dict | None:
        cur = self.connection.execute(sql, params)
        return cur.fetchone()

    def query_all(self, sql: str, params: tuple | dict = ()) -> list[dict]:
        cur = self.connection.execute(sql, params)
        return cur.fetchall()

    @contextmanager
    def transaction(self):
        """
        Context manager đảm bảo nhiều câu lệnh INSERT/UPDATE thực thi
        atomic (VD: tạo phiếu nhập kho + cập nhật tồn kho + ghi log).
        Tự động commit khi thành công, rollback khi có lỗi.
        """
        conn = self.connection
        try:
            conn.execute("BEGIN")
            yield conn
            conn.commit()
        except Exception:
            conn.rollback()
            raise

    def close(self) -> None:
        if self._conn is not None:
            self._conn.close()
            self._conn = None

    def reconnect(self, db_path: Path = None) -> None:
        """Dùng khi cần phục hồi (restore) dữ liệu từ file backup khác."""
        self.close()
        if db_path:
            self.db_path = Path(db_path)
        self._connect()
        self._init_schema()


# Instance dùng chung toàn ứng dụng
db_manager = DatabaseManager()
