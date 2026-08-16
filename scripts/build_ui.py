"""
scripts/build_ui.py
--------------------
Biên dịch toàn bộ file thiết kế giao diện (.ui) trong thư mục ui/designs
sang mã Python (.py) trong ui/generated, sử dụng công cụ pyside6-uic.

CÁCH DÙNG:
    Sau khi chỉnh sửa giao diện bằng Qt Designer (file .ui), chạy lại
    script này để cập nhật code Python tương ứng:

        python scripts/build_ui.py

LƯU Ý QUAN TRỌNG:
    - KHÔNG sửa tay các file trong ui/generated/ (ui_*.py) vì sẽ bị ghi
      đè mỗi khi chạy lại script này. Toàn bộ logic nghiệp vụ (xử lý
      sự kiện, kết nối CSDL...) phải được viết trong ui/widgets/, KHÔNG
      viết trong ui/generated/.
    - Nếu máy chưa cài PySide6 / thiếu lệnh pyside6-uic, cài đặt bằng:
        pip install PySide6
"""
import subprocess
import sys
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
DESIGNS_DIR = BASE_DIR / "ui" / "designs"
GENERATED_DIR = BASE_DIR / "ui" / "generated"


def find_uic_command() -> list[str]:
    """Tìm lệnh biên dịch .ui phù hợp (ưu tiên pyside6-uic)."""
    import shutil

    for cmd in ("pyside6-uic", "pyside2-uic"):
        if shutil.which(cmd):
            return [cmd]
    # Fallback: gọi qua module Python nếu lệnh CLI không có trong PATH
    return [sys.executable, "-m", "PySide6.scripts.pyside_tool", "uic"]


def main() -> int:
    GENERATED_DIR.mkdir(parents=True, exist_ok=True)
    init_file = GENERATED_DIR / "__init__.py"
    if not init_file.exists():
        init_file.touch()

    ui_files = sorted(DESIGNS_DIR.glob("*.ui"))
    if not ui_files:
        print(f"Không tìm thấy file .ui nào trong {DESIGNS_DIR}")
        return 1

    uic_cmd = find_uic_command()
    ok, failed = 0, []

    for ui_file in ui_files:
        out_file = GENERATED_DIR / f"ui_{ui_file.stem}.py"
        cmd = uic_cmd + [str(ui_file), "-o", str(out_file)]
        result = subprocess.run(cmd, capture_output=True, text=True)
        if result.returncode == 0:
            print(f"  [OK]   {ui_file.name:<36} -> {out_file.name}")
            ok += 1
        else:
            print(f"  [LỖI]  {ui_file.name}: {result.stderr.strip()}")
            failed.append(ui_file.name)

    print(f"\nHoàn tất: {ok}/{len(ui_files)} file biên dịch thành công.")
    if failed:
        print("Các file lỗi:", ", ".join(failed))
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
