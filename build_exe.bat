@echo off
chcp 65001 >nul
echo ================================================================
echo   Dong goi Phan mem Quan ly Kho Linh kien thanh file .exe
echo ================================================================

where python >nul 2>nul
if errorlevel 1 (
    echo [LOI] Khong tim thay Python trong PATH. Vui long cai Python 3.10+ truoc.
    pause
    exit /b 1
)

echo.
echo [1/3] Cai dat thu vien can thiet...
pip install -r requirements.txt
pip install pyinstaller

echo.
echo [2/3] Don dep ban build cu (neu co)...
rmdir /s /q build 2>nul
rmdir /s /q dist 2>nul

echo.
echo [3/3] Dong goi bang PyInstaller...
pyinstaller --noconfirm QuanLyKhoLinhKien.spec

echo.
if exist "dist\QuanLyKhoLinhKien\QuanLyKhoLinhKien.exe" (
    echo ================================================================
    echo   HOAN TAT! File .exe nam tai:
    echo   dist\QuanLyKhoLinhKien\QuanLyKhoLinhKien.exe
    echo ================================================================
) else (
    echo [LOI] Khong tim thay file .exe sau khi build. Xem log loi o tren.
)

pause
