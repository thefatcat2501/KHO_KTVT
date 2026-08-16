"""
dao/component_dao.py
---------------------
DAO cho bảng components: CRUD, tìm kiếm/lọc theo loại, năm nhập, nhà sản
xuất, sản phẩm sử dụng; tra cứu theo mã vạch; quản lý quan hệ N-N với
bảng products (component_products).
"""
from database.db_manager import db_manager

_SELECT_BASE = """
    SELECT
        c.*,
        cat.name AS category_name,
        m.name   AS manufacturer_name
    FROM components c
    LEFT JOIN categories cat     ON cat.id = c.category_id
    LEFT JOIN manufacturers m    ON m.id   = c.manufacturer_id
"""


class ComponentDAO:
    # ------------------------------------------------------------ READ
    def get_by_id(self, component_id: int) -> dict | None:
        row = db_manager.query_one(_SELECT_BASE + " WHERE c.id = ?", (component_id,))
        if row:
            row["product_ids"] = self._get_product_ids(component_id)
            row["product_names"] = self._get_product_names(component_id)
        return row

    def get_by_barcode(self, barcode: str) -> dict | None:
        if not barcode:
            return None
        row = db_manager.query_one(
            _SELECT_BASE + " WHERE c.barcode = ? AND c.is_active = 1", (barcode.strip(),)
        )
        if row:
            row["product_ids"] = self._get_product_ids(row["id"])
            row["product_names"] = self._get_product_names(row["id"])
        return row

    def get_by_code(self, code: str) -> dict | None:
        return db_manager.query_one(_SELECT_BASE + " WHERE c.code = ?", (code.strip(),))

    def barcode_exists(self, barcode: str, exclude_id: int = None) -> bool:
        if not barcode:
            return False
        sql = "SELECT id FROM components WHERE barcode = ?"
        params = [barcode.strip()]
        if exclude_id:
            sql += " AND id != ?"
            params.append(exclude_id)
        return db_manager.query_one(sql, tuple(params)) is not None

    def code_exists(self, code: str, exclude_id: int = None) -> bool:
        sql = "SELECT id FROM components WHERE code = ?"
        params = [code.strip()]
        if exclude_id:
            sql += " AND id != ?"
            params.append(exclude_id)
        return db_manager.query_one(sql, tuple(params)) is not None

    def search(
        self,
        keyword: str = "",
        category_id: int | None = None,
        manufacturer_id: int | None = None,
        product_id: int | None = None,
        year: int | None = None,
        low_stock_only: bool = False,
        include_inactive: bool = False,
    ) -> list[dict]:
        sql = _SELECT_BASE
        conditions = []
        params: list = []

        if product_id:
            sql += " INNER JOIN component_products cp ON cp.component_id = c.id "
            conditions.append("cp.product_id = ?")
            params.append(product_id)

        if not include_inactive:
            conditions.append("c.is_active = 1")

        if keyword:
            conditions.append(
                "(c.name LIKE ? OR c.code LIKE ? OR c.barcode LIKE ? OR c.description LIKE ?)"
            )
            kw = f"%{keyword.strip()}%"
            params.extend([kw, kw, kw, kw])

        if category_id:
            conditions.append("c.category_id = ?")
            params.append(category_id)

        if manufacturer_id:
            conditions.append("c.manufacturer_id = ?")
            params.append(manufacturer_id)

        if year:
            conditions.append("c.year_imported = ?")
            params.append(year)

        if low_stock_only:
            conditions.append("c.quantity <= c.min_quantity")

        if conditions:
            sql += " WHERE " + " AND ".join(conditions)
        sql += " ORDER BY c.updated_at DESC"

        rows = db_manager.query_all(sql, tuple(params))
        return rows

    def list_years(self) -> list[int]:
        rows = db_manager.query_all(
            "SELECT DISTINCT year_imported FROM components "
            "WHERE year_imported IS NOT NULL ORDER BY year_imported DESC"
        )
        return [r["year_imported"] for r in rows]

    def list_all_codes(self) -> list[str]:
        """Toàn bộ mã linh kiện hiện có, dùng để gợi ý tự động (autocomplete)
        khi người dùng gõ ô "Mã linh kiện" - giúp thấy ngay các mã tương tự
        đã tồn tại (VD: gõ "RES" gợi ý RES10K, RES1M...), tránh đặt trùng/lặp."""
        rows = db_manager.query_all("SELECT code FROM components WHERE is_active=1 ORDER BY code")
        return [r["code"] for r in rows]

    def list_distinct_locations(self) -> list[str]:
        """Toàn bộ vị trí lưu kho đã từng nhập, dùng để gợi ý tự động khi gõ
        ô "Vị trí lưu kho" - giúp nhập lại đúng cùng 1 vị trí đã dùng trước đó."""
        rows = db_manager.query_all(
            "SELECT DISTINCT location FROM components "
            "WHERE is_active=1 AND location IS NOT NULL AND TRIM(location) != '' "
            "ORDER BY location"
        )
        return [r["location"] for r in rows]

    def count_all(self) -> int:
        return db_manager.query_one("SELECT COUNT(*) c FROM components WHERE is_active=1")["c"]

    def count_low_stock(self) -> int:
        return db_manager.query_one(
            "SELECT COUNT(*) c FROM components WHERE is_active=1 AND quantity <= min_quantity"
        )["c"]

    def total_stock_value(self) -> float:
        row = db_manager.query_one(
            "SELECT COALESCE(SUM(quantity * price), 0) v FROM components WHERE is_active=1"
        )
        return row["v"]

    def total_stock_quantity(self) -> int:
        """Tổng số lượng (đơn vị) đang tồn kho, cộng dồn tất cả linh kiện.
        Khác với count_all() (đếm số DÒNG/loại linh kiện)."""
        row = db_manager.query_one(
            "SELECT COALESCE(SUM(quantity), 0) v FROM components WHERE is_active=1"
        )
        return row["v"]

    def list_low_stock(self, limit: int = 20) -> list[dict]:
        return db_manager.query_all(
            _SELECT_BASE
            + " WHERE c.is_active = 1 AND c.quantity <= c.min_quantity "
              "ORDER BY (c.quantity - c.min_quantity) ASC LIMIT ?",
            (limit,),
        )

    # ----------------------------------------------------------- WRITE
    def create(self, data: dict, product_ids: list[int] = None) -> int:
        cur = db_manager.execute(
            """
            INSERT INTO components
                (code, name, barcode, category_id, manufacturer_id, unit,
                 quantity, min_quantity, price, year_imported, location,
                 description, image_path)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            """,
            (
                data["code"].strip(),
                data["name"].strip(),
                (data.get("barcode") or "").strip() or None,
                data.get("category_id"),
                data.get("manufacturer_id"),
                data.get("unit") or "Cái",
                int(data.get("quantity") or 0),
                int(data.get("min_quantity") or 0),
                float(data.get("price") or 0),
                data.get("year_imported"),
                data.get("location") or None,
                data.get("description") or None,
                data.get("image_path") or None,
            ),
        )
        component_id = cur.lastrowid
        db_manager.connection.commit()
        if product_ids:
            self.set_products(component_id, product_ids)
        return component_id

    def update(self, component_id: int, data: dict, product_ids: list[int] = None) -> None:
        db_manager.execute(
            """
            UPDATE components SET
                code=?, name=?, barcode=?, category_id=?, manufacturer_id=?,
                unit=?, min_quantity=?, price=?, year_imported=?, location=?,
                description=?, image_path=?, updated_at=datetime('now','localtime')
            WHERE id=?
            """,
            (
                data["code"].strip(),
                data["name"].strip(),
                (data.get("barcode") or "").strip() or None,
                data.get("category_id"),
                data.get("manufacturer_id"),
                data.get("unit") or "Cái",
                int(data.get("min_quantity") or 0),
                float(data.get("price") or 0),
                data.get("year_imported"),
                data.get("location") or None,
                data.get("description") or None,
                data.get("image_path") or None,
                component_id,
            ),
        )
        db_manager.connection.commit()
        if product_ids is not None:
            self.set_products(component_id, product_ids)

    def delete(self, component_id: int, soft: bool = True) -> None:
        """Xóa mềm (is_active=0) để bảo toàn dữ liệu lịch sử phiếu nhập/xuất."""
        if soft:
            db_manager.execute(
                "UPDATE components SET is_active = 0 WHERE id = ?", (component_id,)
            )
        else:
            db_manager.execute("DELETE FROM components WHERE id = ?", (component_id,))
        db_manager.connection.commit()

    def adjust_quantity(self, component_id: int, delta: int) -> int:
        """Cộng/trừ tồn kho, trả về số lượng tồn sau khi cập nhật."""
        db_manager.execute(
            "UPDATE components SET quantity = quantity + ?, "
            "updated_at=datetime('now','localtime') WHERE id = ?",
            (delta, component_id),
        )
        row = db_manager.query_one(
            "SELECT quantity FROM components WHERE id = ?", (component_id,)
        )
        return row["quantity"]

    def assign_barcode(self, component_id: int, barcode: str) -> None:
        db_manager.execute(
            "UPDATE components SET barcode = ?, updated_at=datetime('now','localtime') "
            "WHERE id = ?",
            (barcode.strip(), component_id),
        )
        db_manager.connection.commit()

    # ------------------------------------------------------- PRODUCTS
    def set_products(self, component_id: int, product_ids: list[int]) -> None:
        db_manager.execute(
            "DELETE FROM component_products WHERE component_id = ?", (component_id,)
        )
        for pid in set(product_ids or []):
            db_manager.execute(
                "INSERT OR IGNORE INTO component_products (component_id, product_id) "
                "VALUES (?, ?)",
                (component_id, pid),
            )
        db_manager.connection.commit()

    def _get_product_ids(self, component_id: int) -> list[int]:
        rows = db_manager.query_all(
            "SELECT product_id FROM component_products WHERE component_id = ?",
            (component_id,),
        )
        return [r["product_id"] for r in rows]

    def _get_product_names(self, component_id: int) -> list[str]:
        rows = db_manager.query_all(
            """
            SELECT p.name FROM products p
            INNER JOIN component_products cp ON cp.product_id = p.id
            WHERE cp.component_id = ?
            ORDER BY p.name
            """,
            (component_id,),
        )
        return [r["name"] for r in rows]
