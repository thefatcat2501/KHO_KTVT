# Phần mềm Quản lý Kho Linh kiện

Ứng dụng desktop **local-first** (không cần internet, không cần đăng
nhập) để quản lý kho linh kiện/vật tư điện tử, chạy trên **Windows
10/11**. Xây dựng bằng **Python + PySide6 (Qt for Python)**, giao diện
thiết kế bằng **Qt Designer**, dữ liệu lưu trong **SQLite** ngay trên
máy cài đặt.

## 1. Tính năng chính

- **Danh sách linh kiện**: tìm kiếm, thêm, sửa, xóa; lọc theo loại,
  nhà sản xuất, năm nhập kho, sản phẩm sử dụng.
- **Nhập kho / Xuất kho**: quét mã vạch liên tục kiểu máy tính tiền
  siêu thị (quét → tự tìm & thêm vào phiếu → tự xóa ô nhập → sẵn sàng
  quét tiếp), có thể sửa số lượng/đơn giá từng dòng, xem lại và xác
  nhận trước khi lưu phiếu.
- **Mã vạch chưa tồn tại**: cho phép tạo linh kiện mới ngay tại chỗ và
  gán mã vạch, không phải thoát ra màn hình khác.
- **Tồn kho tự động cập nhật** chính xác sau mỗi lần nhập/xuất, có nhật
  ký biến động (audit log) và cho phép hủy phiếu nếu nhập sai.
- **Lịch sử phiếu nhập/xuất**: xem chi tiết từng phiếu, lọc theo ngày.
- **Danh mục**: quản lý Loại linh kiện, Nhà sản xuất, Sản phẩm sử dụng.
- **Sao lưu & khôi phục dữ liệu**: sao lưu CSDL bất kỳ lúc nào, xem
  lịch sử các bản sao lưu, khôi phục lại khi cần (tự tạo thêm 1 bản
  sao lưu an toàn của dữ liệu hiện tại trước khi ghi đè).
- Giao diện hiện đại, tối giản, tối ưu thao tác bằng bàn phím + máy
  quét mã vạch (giống phần mềm bán hàng/POS).

## 2. Yêu cầu hệ thống

- Windows 10 hoặc 11 (64-bit)
- Python 3.10 trở lên ( khuyến nghị 3.11/3.12 )
- Máy quét mã vạch USB kiểu **HID keyboard-wedge** (loại phổ biến
  nhất, cắm USB là dùng được ngay, không cần driver riêng) - *không
  bắt buộc*, phần mềm vẫn dùng được đầy đủ bằng cách gõ tay mã vạch
  hoặc tìm theo tên.

## 3. Cài đặt

```bat
:: 1. Tải/giải nén mã nguồn, mở Command Prompt tại thư mục dự án
:: 2. (khuyến nghị) Tạo môi trường ảo
python -m venv venv
venv\Scripts\activate

:: 3. Cài thư viện
pip install -r requirements.txt

:: 4. Chạy phần mềm
python main.py
```

Lần chạy đầu tiên, phần mềm sẽ tự tạo CSDL SQLite trống (kèm đầy đủ
bảng) - không cần thao tác gì thêm.

## 4. Cấu trúc thư mục

```
inventory_management/
├── main.py                      # Điểm khởi chạy ứng dụng
├── config.py                    # Đường dẫn dữ liệu, hằng số dùng chung
├── requirements.txt
├── smoke_test.py                # Script kiểm thử luồng nghiệp vụ chính (không thuộc ứng dụng)
│
├── ui/
│   ├── designs/                 # File thiết kế giao diện Qt Designer (.ui) — SỬA Ở ĐÂY
│   ├── generated/                # Code Python biên dịch tự động từ .ui — KHÔNG SỬA TAY
│   └── widgets/                  # Logic nghiệp vụ + kết nối sự kiện cho từng màn hình
│
├── database/
│   ├── schema.sql                # Toàn bộ cấu trúc bảng CSDL
│   └── db_manager.py             # Quản lý kết nối SQLite (singleton, transaction)
│
├── dao/                          # Data Access Object — các câu lệnh SQL thuần
├── services/                     # Nghiệp vụ (transaction atomic nhập/xuất, backup, sinh mã...)
├── utils/                        # Widget mã vạch, định dạng số liệu, validate, hộp thoại dùng chung
├── resources/
│   ├── styles/modern.qss         # Bảng màu / giao diện hiện đại dùng toàn ứng dụng
│   └── icons/
└── scripts/
    └── build_ui.py                # Biên dịch lại toàn bộ .ui -> .py sau khi sửa bằng Qt Designer
```

## 5. Quy trình phát triển: UI → Python → Database

Đúng theo yêu cầu, dự án được xây dựng theo thứ tự:

1. **Thiết kế giao diện** bằng Qt Designer, lưu thành file `.ui` trong
   `ui/designs/`.
2. **Biên dịch `.ui` → `.py`** bằng `pyside6-uic` (đã đóng gói sẵn qua
   script `scripts/build_ui.py`), sinh ra các lớp `Ui_<TênMànHình>`
   trong `ui/generated/`.
3. **Viết logic liên kết** trong `ui/widgets/`: mỗi màn hình là một
   class kế thừa `QWidget`/`QDialog`, gọi `self.ui = Ui_XXX();
   self.ui.setupUi(self)`, sau đó kết nối sự kiện (click, quét mã
   vạch...) và gọi xuống tầng `services/`/`dao/`.
4. **Tầng CSDL** (`database/`, `dao/`) cung cấp dữ liệu cho tầng trên.

**Nếu cần chỉnh sửa giao diện:** mở file `.ui` tương ứng bằng Qt
Designer (`Tools → External Tools` hoặc chạy trực tiếp `designer`),
sửa xong chạy lại:

```bat
python scripts\build_ui.py
```

Toàn bộ code trong `ui/generated/` sẽ được sinh lại tự động — **không
bao giờ sửa tay các file trong thư mục này** vì sẽ bị ghi đè.

## 6. Máy quét mã vạch hoạt động như thế nào?

Hầu hết máy quét mã vạch USB hoạt động ở chế độ bàn phím ảo (HID
keyboard-wedge) — cắm vào là máy tính nhận diện như một bàn phím,
quét xong máy tự "gõ" toàn bộ mã rồi gửi thêm phím Enter. Vì vậy phần
mềm **không cần driver hay thư viện gì thêm**: chỉ cần ô nhập liệu ở
trang Nhập/Xuất kho luôn giữ focus, mỗi lần Enter được gửi tới sẽ tự
tra cứu, thêm vào phiếu, rồi tự xóa nội dung để sẵn sàng quét mã tiếp
theo — đúng mô hình các phần mềm bán hàng/siêu thị đang dùng. Logic
này nằm ở `utils/barcode_input.py` (lớp `BarcodeLineEdit`).

Nếu về sau cần hỗ trợ máy quét kết nối qua cổng COM/Serial (một số
dòng máy công nghiệp), chỉ cần viết thêm 1 adapter đọc dữ liệu serial
và phát cùng tín hiệu `scanned(str)`, phần còn lại của ứng dụng không
cần sửa gì.

## 7. Dữ liệu được lưu ở đâu?

Theo đúng thông lệ ứng dụng Windows (tránh lỗi quyền ghi khi cài trong
`Program Files`), CSDL và các bản sao lưu được lưu tại thư mục dữ liệu
người dùng, **tách biệt khỏi thư mục cài đặt/mã nguồn**:

```
%APPDATA%\QuanLyKhoLinhKien\data\inventory.db      <- CSDL chính
%APPDATA%\QuanLyKhoLinhKien\backups\                <- Các bản sao lưu
```

(thường là `C:\Users\<tên người dùng>\AppData\Roaming\QuanLyKhoLinhKien\`).
Đường dẫn chính xác cũng được hiển thị ngay trong trang **Sao lưu &
Khôi phục** của phần mềm.

## 8. Đóng gói thành file `.exe`

Có thể đóng gói toàn bộ phần mềm Python này thành 1 chương trình `.exe`
chạy độc lập trên Windows — **người dùng cuối không cần cài Python**.
Dự án đã có sẵn file cấu hình `QuanLyKhoLinhKien.spec` cho
[PyInstaller](https://pyinstaller.org/), cách dùng đơn giản nhất là
chạy file có sẵn:

```bat
build_exe.bat
```

Hoặc chạy tay từng bước:

```bat
pip install -r requirements.txt
pip install pyinstaller
pyinstaller --noconfirm QuanLyKhoLinhKien.spec
```

Kết quả nằm trong `dist\QuanLyKhoLinhKien\QuanLyKhoLinhKien.exe`
(dùng chế độ *onedir* — cả thư mục `dist\QuanLyKhoLinhKien\` cần được
giữ nguyên cùng nhau/gửi đi cùng nhau, không tách riêng file `.exe`).

> ⚠️ **Lưu ý:** PyInstaller không hỗ trợ biên dịch chéo hệ điều hành —
> lệnh này phải chạy **trên máy Windows** thì mới ra được `.exe` cho
> Windows (chạy trên Linux/macOS sẽ ra file thực thi cho chính hệ điều
> hành đó). File `.spec` đã được kiểm chứng chạy thành công (bundle đủ
> `resources/` và `database/schema.sql`, CSDL khởi tạo đúng) trong quá
> trình phát triển.

## 9. Kiểm thử

`smoke_test.py` là script kiểm thử nhanh (không thuộc giao diện người
dùng) chạy qua toàn bộ luồng nghiệp vụ chính — tạo danh mục, tạo linh
kiện, quét mã vạch, nhập/xuất kho, chặn xuất vượt tồn, hủy phiếu,
sao lưu/khôi phục, và duyệt qua mọi màn hình — sử dụng một thư mục dữ
liệu tạm riêng biệt (không đụng vào dữ liệu thật):

```bat
python smoke_test.py
```

## 10. Giới hạn hiện tại & hướng mở rộng

- Chưa hỗ trợ nhiều người dùng đồng thời qua mạng (đúng theo yêu cầu
  "local-first", 1 máy 1 CSDL). Nếu cần dùng chung nhiều máy, có thể
  đặt file CSDL vào thư mục mạng dùng chung — SQLite hỗ trợ được với
  số lượng người dùng đồng thời ít.
- Xuất phiếu ra PDF/in trực tiếp chưa có — có thể bổ sung ở
  `services/` (ví dụ dùng `reportlab`) mà không ảnh hưởng cấu trúc
  hiện tại.
- Ảnh linh kiện: CSDL đã có sẵn cột `image_path`, có thể bổ sung thao
  tác chọn/hiển thị ảnh trong `ComponentDialog` khi cần.
