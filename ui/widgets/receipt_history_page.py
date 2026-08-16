"""ui/widgets/receipt_history_page.py - Trang lịch sử phiếu nhập/xuất kho, xem chi tiết, hủy phiếu."""
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QTableWidgetItem

from dao.export_receipt_dao import ExportReceiptDAO
from dao.import_receipt_dao import ImportReceiptDAO
from services.stock_service import stock_service
from ui.generated.ui_receipt_history_page import Ui_ReceiptHistoryPage
from ui.widgets.base_page import BasePage
from ui.widgets.receipt_detail_dialog import ReceiptDetailDialog
from utils.exceptions import AppError
from utils.formatters import format_datetime, format_int
from utils.ui_helpers import confirm, show_error, show_info, show_warning

import_receipt_dao = ImportReceiptDAO()
export_receipt_dao = ExportReceiptDAO()


class ReceiptHistoryPage(BasePage):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_ReceiptHistoryPage()
        self.ui.setupUi(self)

        self._import_results: list[dict] = []
        self._export_results: list[dict] = []

        today = self.ui.dteTo.date()
        self.ui.dteFrom.setDate(today.addMonths(-3))

        self.ui.txtSearch.textChanged.connect(self._on_filter_changed)
        self.ui.btnFilterReceipts.clicked.connect(self._on_filter_changed)
        self.ui.btnViewImportDetail.clicked.connect(self._on_view_import_detail)
        self.ui.btnViewExportDetail.clicked.connect(self._on_view_export_detail)
        self.ui.btnVoidImport.clicked.connect(self._on_void_import)
        self.ui.btnVoidExport.clicked.connect(self._on_void_export)
        self.ui.tblImportReceipts.itemDoubleClicked.connect(lambda _: self._on_view_import_detail())
        self.ui.tblExportReceipts.itemDoubleClicked.connect(lambda _: self._on_view_export_detail())

        self.refresh()

    # ------------------------------------------------------------ BasePage
    def refresh(self) -> None:
        self._on_filter_changed()

    def _on_filter_changed(self, *_args) -> None:
        keyword = self.ui.txtSearch.text().strip()
        date_from = self.ui.dteFrom.date().toString("yyyy-MM-dd")
        date_to = self.ui.dteTo.date().toString("yyyy-MM-dd")

        self._import_results = import_receipt_dao.list_all(keyword=keyword, date_from=date_from, date_to=date_to)
        self._export_results = export_receipt_dao.list_all(keyword=keyword, date_from=date_from, date_to=date_to)
        self._populate(self.ui.tblImportReceipts, self._import_results, "supplier")
        self._populate(self.ui.tblExportReceipts, self._export_results, "recipient")

    @staticmethod
    def _populate(table, rows: list[dict], partner_key: str) -> None:
        table.setRowCount(0)
        for i, r in enumerate(rows):
            table.insertRow(i)
            code_item = QTableWidgetItem(r["receipt_code"])
            code_item.setData(Qt.ItemDataRole.UserRole, r["id"])
            table.setItem(i, 0, code_item)
            table.setItem(i, 1, QTableWidgetItem(format_datetime(r.get("created_at"))))
            table.setItem(i, 2, QTableWidgetItem(r.get(partner_key) or ""))
            table.setItem(i, 3, QTableWidgetItem(format_int(r.get("total_quantity"))))
            table.setItem(i, 4, QTableWidgetItem(r.get("note") or ""))

    @staticmethod
    def _selected_id(table, results: list[dict]) -> int | None:
        row = table.currentRow()
        if row < 0 or row >= len(results):
            return None
        return results[row]["id"]

    # ------------------------------------------------------------ view detail
    def _on_view_import_detail(self) -> None:
        receipt_id = self._selected_id(self.ui.tblImportReceipts, self._import_results)
        if receipt_id is None:
            show_warning(self, "Vui lòng chọn một phiếu nhập kho.")
            return
        receipt = import_receipt_dao.get_by_id(receipt_id)
        details = import_receipt_dao.get_details(receipt_id)
        ReceiptDetailDialog(self, mode="IN", receipt=receipt, details=details).exec()

    def _on_view_export_detail(self) -> None:
        receipt_id = self._selected_id(self.ui.tblExportReceipts, self._export_results)
        if receipt_id is None:
            show_warning(self, "Vui lòng chọn một phiếu xuất kho.")
            return
        receipt = export_receipt_dao.get_by_id(receipt_id)
        details = export_receipt_dao.get_details(receipt_id)
        ReceiptDetailDialog(self, mode="OUT", receipt=receipt, details=details).exec()

    # ------------------------------------------------------------ void
    def _on_void_import(self) -> None:
        receipt_id = self._selected_id(self.ui.tblImportReceipts, self._import_results)
        if receipt_id is None:
            show_warning(self, "Vui lòng chọn một phiếu nhập kho.")
            return
        if confirm(
            self,
            "Hủy phiếu này sẽ TRỪ LẠI số lượng đã cộng vào kho tương ứng với phiếu.\n"
            "Bạn có chắc chắn muốn hủy?",
        ):
            try:
                stock_service.void_import_receipt(receipt_id)
                self.refresh()
                show_info(self, "Đã hủy phiếu nhập kho.")
            except AppError as e:
                show_error(self, str(e))

    def _on_void_export(self) -> None:
        receipt_id = self._selected_id(self.ui.tblExportReceipts, self._export_results)
        if receipt_id is None:
            show_warning(self, "Vui lòng chọn một phiếu xuất kho.")
            return
        if confirm(
            self,
            "Hủy phiếu này sẽ CỘNG LẠI số lượng đã xuất khỏi kho tương ứng với phiếu.\n"
            "Bạn có chắc chắn muốn hủy?",
        ):
            try:
                stock_service.void_export_receipt(receipt_id)
                self.refresh()
                show_info(self, "Đã hủy phiếu xuất kho.")
            except AppError as e:
                show_error(self, str(e))
