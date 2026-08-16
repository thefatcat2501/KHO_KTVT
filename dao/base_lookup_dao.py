"""
dao/base_lookup_dao.py
-----------------------
DAO cơ sở dùng chung cho các bảng "danh mục đơn giản" dạng
(id, name, description) như categories, products - giúp tránh lặp code.
"""
from database.db_manager import db_manager


class BaseLookupDAO:
    table_name: str = ""

    def list_all(self, keyword: str = "") -> list[dict]:
        if keyword:
            sql = f"SELECT * FROM {self.table_name} WHERE name LIKE ? ORDER BY name"
            return db_manager.query_all(sql, (f"%{keyword}%",))
        return db_manager.query_all(f"SELECT * FROM {self.table_name} ORDER BY name")

    def get_by_id(self, item_id: int) -> dict | None:
        return db_manager.query_one(
            f"SELECT * FROM {self.table_name} WHERE id = ?", (item_id,)
        )

    def get_by_name(self, name: str) -> dict | None:
        return db_manager.query_one(
            f"SELECT * FROM {self.table_name} WHERE name = ?", (name,)
        )

    def create(self, name: str, description: str = "") -> int:
        cur = db_manager.execute(
            f"INSERT INTO {self.table_name} (name, description) VALUES (?, ?)",
            (name.strip(), description.strip() if description else None),
        )
        db_manager.connection.commit()
        return cur.lastrowid

    def update(self, item_id: int, name: str, description: str = "") -> None:
        db_manager.execute(
            f"UPDATE {self.table_name} SET name = ?, description = ? WHERE id = ?",
            (name.strip(), description.strip() if description else None, item_id),
        )
        db_manager.connection.commit()

    def delete(self, item_id: int) -> None:
        db_manager.execute(f"DELETE FROM {self.table_name} WHERE id = ?", (item_id,))
        db_manager.connection.commit()

    def get_or_create(self, name: str) -> int:
        name = name.strip()
        existing = self.get_by_name(name)
        if existing:
            return existing["id"]
        return self.create(name)


class CategoryDAO(BaseLookupDAO):
    table_name = "categories"


class ProductDAO(BaseLookupDAO):
    table_name = "products"
