"""
services/component_service.py
-------------------------------
Lớp nghiệp vụ cho linh kiện: sinh mã tự động, kiểm tra trùng mã/mã vạch
trước khi ghi CSDL (thông báo lỗi rõ ràng cho người dùng thay vì để lỗi
IntegrityError của SQLite rơi thẳng ra giao diện).
"""
from database.db_manager import db_manager
from dao.component_dao import ComponentDAO
from utils.exceptions import DuplicateBarcodeError, DuplicateCodeError, ValidationError

component_dao = ComponentDAO()


class ComponentService:
    def generate_next_code(self) -> str:
        row = db_manager.query_one("SELECT COUNT(*) c FROM components")
        seq = (row["c"] or 0) + 1
        candidate = f"LK{seq:04d}"
        # Đảm bảo không trùng nếu có linh kiện đã bị xóa/đổi mã trước đó
        while component_dao.code_exists(candidate):
            seq += 1
            candidate = f"LK{seq:04d}"
        return candidate

    def create_component(self, data: dict, product_ids: list[int] = None) -> int:
        self._validate(data)
        if not data.get("code"):
            data["code"] = self.generate_next_code()
        if component_dao.code_exists(data["code"]):
            raise DuplicateCodeError(f'Mã linh kiện "{data["code"]}" đã tồn tại.')
        if data.get("barcode") and component_dao.barcode_exists(data["barcode"]):
            raise DuplicateBarcodeError(f'Mã vạch "{data["barcode"]}" đã được gán cho linh kiện khác.')
        return component_dao.create(data, product_ids)

    def update_component(self, component_id: int, data: dict, product_ids: list[int] = None) -> None:
        self._validate(data)
        if component_dao.code_exists(data["code"], exclude_id=component_id):
            raise DuplicateCodeError(f'Mã linh kiện "{data["code"]}" đã tồn tại.')
        if data.get("barcode") and component_dao.barcode_exists(data["barcode"], exclude_id=component_id):
            raise DuplicateBarcodeError(f'Mã vạch "{data["barcode"]}" đã được gán cho linh kiện khác.')
        component_dao.update(component_id, data, product_ids)

    def assign_barcode(self, component_id: int, barcode: str) -> None:
        barcode = (barcode or "").strip()
        if not barcode:
            raise ValidationError("Mã vạch không được để trống.")
        if component_dao.barcode_exists(barcode, exclude_id=component_id):
            raise DuplicateBarcodeError(f'Mã vạch "{barcode}" đã được gán cho linh kiện khác.')
        component_dao.assign_barcode(component_id, barcode)

    @staticmethod
    def _validate(data: dict) -> None:
        if not (data.get("name") or "").strip():
            raise ValidationError("Tên linh kiện không được để trống.")


component_service = ComponentService()
