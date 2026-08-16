"""
smoke_test.py - KHÔNG phải một phần của ứng dụng, chỉ dùng để kiểm thử
toàn bộ luồng nghiệp vụ chính trước khi bàn giao:
    - Tạo danh mục (loại / NSX / sản phẩm)
    - Tạo linh kiện mới kèm mã vạch
    - Quét mã vạch (mã đã tồn tại + mã CHƯA tồn tại -> tạo mới tại chỗ)
    - Tạo phiếu nhập kho -> kiểm tra tồn kho tăng đúng
    - Tạo phiếu xuất kho -> kiểm tra tồn kho giảm đúng
    - Xuất kho vượt tồn -> phải báo lỗi, KHÔNG được trừ kho
    - Hủy phiếu -> kiểm tra tồn kho được hoàn tác đúng
    - Dashboard phản ánh đúng số liệu
    - Sao lưu + khôi phục dữ liệu
    - Duyệt qua toàn bộ các trang của MainWindow không lỗi
"""
import os
import shutil
import sys
from pathlib import Path

os.environ.setdefault("QT_QPA_PLATFORM", "offscreen")

# Dùng một thư mục dữ liệu TÁCH BIỆT cho việc test để không đụng vào dữ liệu thật
TEST_HOME = Path("/tmp/inventory_smoke_test_home")
if TEST_HOME.exists():
    shutil.rmtree(TEST_HOME)
TEST_HOME.mkdir(parents=True)
os.environ["HOME"] = str(TEST_HOME)
os.environ["XDG_DATA_HOME"] = str(TEST_HOME / ".local" / "share")

sys.path.insert(0, str(Path(__file__).resolve().parent))

from PySide6.QtWidgets import QApplication, QDialog  # noqa: E402

app = QApplication(sys.argv)

from dao.base_lookup_dao import CategoryDAO, ProductDAO  # noqa: E402
from dao.component_dao import ComponentDAO  # noqa: E402
from dao.manufacturer_dao import ManufacturerDAO  # noqa: E402
from services.backup_service import backup_service  # noqa: E402
from services.component_service import component_service  # noqa: E402
from services.stock_service import stock_service  # noqa: E402
from ui.widgets.main_window import MainWindow  # noqa: E402
from utils.exceptions import InsufficientStockError  # noqa: E402

category_dao = CategoryDAO()
manufacturer_dao = ManufacturerDAO()
product_dao = ProductDAO()
component_dao = ComponentDAO()

passed, failed = 0, 0


def check(label: str, condition: bool) -> None:
    global passed, failed
    if condition:
        print(f"  [OK]   {label}")
        passed += 1
    else:
        print(f"  [FAIL] {label}")
        failed += 1


print("== 1) Danh mục ==")
cat_id = category_dao.create("Điện trở", "Linh kiện thụ động")
man_id = manufacturer_dao.create("Yageo", "0123456789", "Đài Loan")
prod_id = product_dao.create("Bo mạch nguồn X1", "")
check("Tạo loại/NSX/sản phẩm thành công", all([cat_id, man_id, prod_id]))

print("== 2) Tạo linh kiện mới kèm mã vạch ==")
component_id = component_service.create_component(
    {
        "code": "",
        "barcode": "8938501234567",
        "name": "Điện trở 10K 1/4W",
        "category_id": cat_id,
        "manufacturer_id": man_id,
        "unit": "Cái",
        "quantity": 100,
        "min_quantity": 20,
        "price": 500,
        "year_imported": 2025,
        "location": "Kệ A1",
        "description": "",
    },
    product_ids=[prod_id],
)
c = component_dao.get_by_id(component_id)
check("Linh kiện được tạo với mã tự sinh dạng LKxxxx", c["code"].startswith("LK"))
check("Tồn kho ban đầu = 100", c["quantity"] == 100)
check("Gán đúng sản phẩm sử dụng", prod_id in c["product_ids"])

print("== 3) Tra cứu theo mã vạch (giả lập quét) ==")
found = component_dao.get_by_barcode("8938501234567")
check("Tìm thấy linh kiện theo mã vạch vừa quét", found is not None and found["id"] == component_id)
not_found = component_dao.get_by_barcode("0000000000000")
check("Mã vạch chưa tồn tại -> trả về None (kích hoạt luồng tạo mới)", not_found is None)

print("== 4) Phiếu NHẬP kho ==")
receipt_code_in = stock_service.create_import_receipt(
    items=[{"component_id": component_id, "quantity": 50, "unit_price": 500}],
    supplier="Công ty ABC",
    note="Nhập bổ sung",
)
c = component_dao.get_by_id(component_id)
check(f"Mã phiếu nhập tự sinh hợp lệ ({receipt_code_in})", receipt_code_in.startswith("PN"))
check("Tồn kho tăng đúng 100 -> 150 sau khi nhập 50", c["quantity"] == 150)

print("== 5) Phiếu XUẤT kho ==")
receipt_code_out = stock_service.create_export_receipt(
    items=[{"component_id": component_id, "quantity": 30, "unit_price": 500}],
    recipient="Xưởng lắp ráp 1",
    note="Xuất sản xuất",
)
c = component_dao.get_by_id(component_id)
check(f"Mã phiếu xuất tự sinh hợp lệ ({receipt_code_out})", receipt_code_out.startswith("PX"))
check("Tồn kho giảm đúng 150 -> 120 sau khi xuất 30", c["quantity"] == 120)

print("== 6) Xuất kho vượt tồn kho hiện có (phải bị chặn) ==")
blocked = False
try:
    stock_service.create_export_receipt(
        items=[{"component_id": component_id, "quantity": 999999, "unit_price": 500}],
        recipient="X",
    )
except InsufficientStockError:
    blocked = True
c = component_dao.get_by_id(component_id)
check("Xuất vượt tồn kho bị chặn đúng bằng InsufficientStockError", blocked)
check("Tồn kho KHÔNG bị trừ khi giao dịch bị chặn (vẫn = 120)", c["quantity"] == 120)

print("== 7) Hủy phiếu (void) hoàn tác đúng tồn kho ==")
import_receipts = component_dao  # placeholder just to keep flake happy
from dao.import_receipt_dao import ImportReceiptDAO  # noqa: E402

import_dao = ImportReceiptDAO()
last_import = import_dao.list_all()[0]
stock_service.void_import_receipt(last_import["id"])
c = component_dao.get_by_id(component_id)
check("Hủy phiếu nhập hoàn tác đúng tồn kho (120 -> 70)", c["quantity"] == 70)

print("== 8) Dashboard / thống kê ==")
check("count_all() >= 1", component_dao.count_all() >= 1)
check("count_low_stock() hợp lý (>=0)", component_dao.count_low_stock() >= 0)
check("total_stock_value() > 0", component_dao.total_stock_value() > 0)
check("total_stock_quantity() khớp đúng tồn kho hiện tại (= 70)", component_dao.total_stock_quantity() == 70)

print("== 9) Sao lưu & khôi phục ==")
backup_path = backup_service.create_backup()
check("File backup được tạo", backup_path.exists())
# Xuất thêm 1 phiếu để CSDL hiện tại khác với bản backup vừa tạo
stock_service.create_export_receipt(items=[{"component_id": component_id, "quantity": 10, "unit_price": 500}], recipient="Test")
c_before_restore = component_dao.get_by_id(component_id)
check("Tồn kho đã đổi trước khi khôi phục (70 -> 60)", c_before_restore["quantity"] == 60)
backup_service.restore_backup(backup_path)
c_after_restore = component_dao.get_by_id(component_id)
check("Khôi phục thành công đưa tồn kho về đúng thời điểm backup (60 -> 70)", c_after_restore["quantity"] == 70)
check("list_backups() thấy được bản vừa tạo", len(backup_service.list_backups()) >= 1)

print("== 10) Duyệt toàn bộ giao diện MainWindow không lỗi ==")
window = MainWindow()
for key in ["dashboard", "components", "stock_in", "stock_out", "receipts", "categories", "backup"]:
    window._navigate(key)
check("Điều hướng qua tất cả các trang không phát sinh lỗi", True)

# Giả lập luồng quét mã vạch trực tiếp trên trang Nhập kho
window.stock_in_page._on_barcode_scanned("8938501234567")
check("Quét mã vạch đã biết -> thêm đúng 1 dòng vào phiếu đang tạo", len(window.stock_in_page.items) == 1)
window.stock_in_page._on_barcode_scanned("8938501234567")
check("Quét lại cùng mã vạch -> cộng dồn số lượng (không tạo dòng trùng)", 
      len(window.stock_in_page.items) == 1 and window.stock_in_page.items[0]["quantity"] == 2)

print("== 11) Dữ liệu gợi ý tự động (autocomplete) ==")
component_service.create_component(
    {"code": "RES10K", "name": "Điện trở 10K", "quantity": 0, "location": "Kệ A - Ngăn 1"}
)
component_service.create_component(
    {"code": "RES1M", "name": "Điện trở 1M", "quantity": 0, "location": "Kệ A - Ngăn 2"}
)
component_service.create_component(
    {"code": "CAP100N", "name": "Tụ 100nF", "quantity": 0, "location": "Kệ B - Ngăn 1"}
)
all_codes = component_dao.list_all_codes()
res_codes = [c for c in all_codes if c.upper().startswith("RES")]
check("list_all_codes() gợi ý đúng các mã bắt đầu bằng 'RES'", set(res_codes) == {"RES10K", "RES1M"})
check("list_all_codes() KHÔNG gợi ý nhầm mã không cùng tiền tố", "CAP100N" not in res_codes)
locations = component_dao.list_distinct_locations()
check(
    "list_distinct_locations() trả về đủ và không trùng lặp vị trí đã dùng",
    set(locations) >= {"Kệ A - Ngăn 1", "Kệ A - Ngăn 2", "Kệ B - Ngăn 1"} and len(locations) == len(set(locations)),
)

print(f"\n===== KẾT QUẢ: {passed} PASS / {failed} FAIL =====")
sys.exit(1 if failed else 0)
