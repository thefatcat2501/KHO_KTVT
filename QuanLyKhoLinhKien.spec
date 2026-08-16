# -*- mode: python ; coding: utf-8 -*-
"""
QuanLyKhoLinhKien.spec
------------------------
File cấu hình PyInstaller để đóng gói phần mềm Python này thành một
chương trình .exe chạy độc lập trên Windows (người dùng cuối KHÔNG cần
cài Python).

QUAN TRỌNG: PyInstaller không hỗ trợ biên dịch chéo hệ điều hành - phải
chạy lệnh này TRÊN MÁY WINDOWS thì mới ra được file .exe cho Windows.

CÁCH DÙNG (trên Windows, trong thư mục gốc dự án):

    pip install -r requirements.txt
    pip install pyinstaller
    pyinstaller --noconfirm QuanLyKhoLinhKien.spec

    (hoặc chạy sẵn: build_exe.bat)

Kết quả nằm trong thư mục:  dist\\QuanLyKhoLinhKien\\QuanLyKhoLinhKien.exe

Dùng chế độ "onedir" (1 thư mục chứa .exe + các file phụ trợ) thay vì
"onefile" (nén thành 1 file .exe duy nhất) vì onedir khởi động nhanh
hơn đáng kể với ứng dụng Qt/PySide6 (onefile phải tự giải nén ra thư
mục tạm mỗi lần mở phần mềm). Muốn phân phối cho người dùng, chỉ cần
nén cả thư mục dist\\QuanLyKhoLinhKien\\ lại rồi gửi đi.
"""
from pathlib import Path

PROJECT_ROOT = Path(SPECPATH)  # SPECPATH do PyInstaller tự cấp khi chạy file .spec

a = Analysis(
    ["main.py"],
    pathex=[str(PROJECT_ROOT)],
    binaries=[],
    datas=[
        # Giữ nguyên cấu trúc thư mục con để config.py (dựa trên đường dẫn
        # tương đối) vẫn tìm đúng file khi chạy từ bản .exe đã đóng gói.
        (str(PROJECT_ROOT / "resources"), "resources"),
        (str(PROJECT_ROOT / "database" / "schema.sql"), "database"),
    ],
    hiddenimports=[
        "PySide6.QtSvg",  # dùng để vẽ logo dạng .svg ở sidebar
    ],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
)

pyz = PYZ(a.pure, a.zipped_data)

exe = EXE(
    pyz,
    a.scripts,
    [],
    exclude_binaries=True,
    name="QuanLyKhoLinhKien",
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    console=False,  # ẩn cửa sổ Command Prompt đen, chỉ hiện giao diện Qt
    icon=None,      # thay bằng đường dẫn tới file .ico riêng nếu muốn icon tùy chỉnh
)

coll = COLLECT(
    exe,
    a.binaries,
    a.zipfiles,
    a.datas,
    strip=False,
    upx=True,
    upx_exclude=[],
    name="QuanLyKhoLinhKien",
)
