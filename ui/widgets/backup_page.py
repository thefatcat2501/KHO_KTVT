"""ui/widgets/backup_page.py - Trang Sao lưu & Khôi phục dữ liệu."""
from pathlib import Path

from PySide6.QtCore import QUrl, Signal
from PySide6.QtGui import QDesktopServices
from PySide6.QtWidgets import QFileDialog, QTableWidgetItem

from config import BACKUP_DIR, DB_PATH
from services.backup_service import backup_service
from ui.generated.ui_backup_page import Ui_BackupPage
from ui.widgets.base_page import BasePage
from utils.exceptions import AppError
from utils.formatters import format_file_size
from utils.ui_helpers import confirm, show_error, show_info, show_warning


class BackupPage(BasePage):
    restored = Signal()  # phát ra sau khi khôi phục dữ liệu thành công, để MainWindow làm mới các trang khác

    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_BackupPage()
        self.ui.setupUi(self)

        self._backups: list[dict] = []
        self.ui.lblDbPath.setText(f"Đường dẫn CSDL: {DB_PATH}")

        self.ui.btnBackupNow.clicked.connect(self._on_backup_now)
        self.ui.btnRestoreFromFile.clicked.connect(self._on_restore_from_file)
        self.ui.btnOpenBackupFolder.clicked.connect(self._on_open_backup_folder)
        self.ui.btnRestoreSelected.clicked.connect(self._on_restore_selected)
        self.ui.btnDeleteBackup.clicked.connect(self._on_delete_backup)

        self.refresh()

    # ------------------------------------------------------------ BasePage
    def refresh(self) -> None:
        self._backups = backup_service.list_backups()
        table = self.ui.tblBackups
        table.setRowCount(0)
        for i, b in enumerate(self._backups):
            table.insertRow(i)
            table.setItem(i, 0, QTableWidgetItem(b["name"]))
            table.setItem(i, 1, QTableWidgetItem(b["created_at"].strftime("%d/%m/%Y %H:%M:%S")))
            table.setItem(i, 2, QTableWidgetItem(format_file_size(b["size_bytes"])))

    def _selected_backup(self) -> dict | None:
        row = self.ui.tblBackups.currentRow()
        if not (0 <= row < len(self._backups)):
            return None
        return self._backups[row]

    # ------------------------------------------------------------ actions
    def _on_backup_now(self) -> None:
        try:
            path = backup_service.create_backup()
            self.refresh()
            show_info(self, f"Đã tạo bản sao lưu thành công:\n{path.name}")
        except Exception as e:  # noqa: BLE001
            show_error(self, f"Không thể tạo bản sao lưu: {e}")

    def _on_restore_from_file(self) -> None:
        path_str, _ = QFileDialog.getOpenFileName(
            self, "Chọn file sao lưu để khôi phục", str(BACKUP_DIR), "SQLite Database (*.db)"
        )
        if path_str:
            self._do_restore(Path(path_str))

    def _on_restore_selected(self) -> None:
        backup = self._selected_backup()
        if not backup:
            show_warning(self, "Vui lòng chọn một bản sao lưu trong danh sách.")
            return
        self._do_restore(backup["path"])

    def _do_restore(self, path: Path) -> None:
        if not confirm(
            self,
            f"Khôi phục dữ liệu từ:\n{path.name}\n\n"
            "Toàn bộ dữ liệu hiện tại sẽ được THAY THẾ bằng dữ liệu trong bản sao lưu này\n"
            "(một bản sao lưu an toàn của dữ liệu hiện tại sẽ được tự động tạo trước khi khôi phục).\n\n"
            "Bạn có chắc chắn muốn tiếp tục?",
            title="Xác nhận khôi phục dữ liệu",
        ):
            return
        try:
            backup_service.restore_backup(path)
            self.refresh()
            self.restored.emit()
            show_info(self, "Khôi phục dữ liệu thành công.")
        except AppError as e:
            show_error(self, str(e))
        except Exception as e:  # noqa: BLE001
            show_error(self, f"Lỗi khi khôi phục dữ liệu: {e}")

    def _on_delete_backup(self) -> None:
        backup = self._selected_backup()
        if not backup:
            show_warning(self, "Vui lòng chọn một bản sao lưu để xóa.")
            return
        if confirm(self, f"Xóa vĩnh viễn bản sao lưu:\n{backup['name']}?"):
            backup_service.delete_backup(backup["path"])
            self.refresh()

    def _on_open_backup_folder(self) -> None:
        BACKUP_DIR.mkdir(parents=True, exist_ok=True)
        QDesktopServices.openUrl(QUrl.fromLocalFile(str(BACKUP_DIR)))
