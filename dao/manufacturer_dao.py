"""dao/manufacturer_dao.py - CRUD nhà sản xuất."""
from database.db_manager import db_manager


class ManufacturerDAO:
    def list_all(self, keyword: str = "") -> list[dict]:
        if keyword:
            return db_manager.query_all(
                "SELECT * FROM manufacturers WHERE name LIKE ? ORDER BY name",
                (f"%{keyword}%",),
            )
        return db_manager.query_all("SELECT * FROM manufacturers ORDER BY name")

    def get_by_id(self, item_id: int) -> dict | None:
        return db_manager.query_one(
            "SELECT * FROM manufacturers WHERE id = ?", (item_id,)
        )

    def get_by_name(self, name: str) -> dict | None:
        return db_manager.query_one(
            "SELECT * FROM manufacturers WHERE name = ?", (name,)
        )

    def create(self, name: str, contact_info: str = "", address: str = "") -> int:
        cur = db_manager.execute(
            "INSERT INTO manufacturers (name, contact_info, address) VALUES (?, ?, ?)",
            (name.strip(), contact_info or None, address or None),
        )
        db_manager.connection.commit()
        return cur.lastrowid

    def update(self, item_id: int, name: str, contact_info: str = "", address: str = "") -> None:
        db_manager.execute(
            "UPDATE manufacturers SET name=?, contact_info=?, address=? WHERE id=?",
            (name.strip(), contact_info or None, address or None, item_id),
        )
        db_manager.connection.commit()

    def delete(self, item_id: int) -> None:
        db_manager.execute("DELETE FROM manufacturers WHERE id = ?", (item_id,))
        db_manager.connection.commit()

    def get_or_create(self, name: str) -> int:
        name = name.strip()
        existing = self.get_by_name(name)
        if existing:
            return existing["id"]
        return self.create(name)
