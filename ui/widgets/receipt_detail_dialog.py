"""ui/widgets/receipt_detail_dialog.py - Hộp thoại xem chi tiết 1 phiếu nhập/xuất kho (chỉ xem)."""
from PySide6.QtWidgets import QDialog, QTableWidgetItem

from ui.generated.ui_receipt_detail_dialog import Ui_ReceiptDetailDialog
from utils.formatters import format_datetime, format_int


class ReceiptDetailDialog(QDialog):
    def __init__(self, parent=None, mode: str = "IN", receipt: dict = None, details: list[dict] = None):
        super().__init__(parent)
        self.ui = Ui_ReceiptDetailDialog()
        self.ui.setupUi(self)

        receipt = receipt or {}
        details = details or []

        title = "Chi tiết phiếu nhập kho" if mode == "IN" else "Chi tiết phiếu xuất kho"
        self.setWindowTitle(title)
        self.ui.lblTitle.setText(title)

        self.ui.lblCodeValue.setText(receipt.get("receipt_code", "-"))
        self.ui.lblDateValue.setText(format_datetime(receipt.get("created_at")))
        self.ui.lblPartnerCaption.setText("Nhà cung cấp:" if mode == "IN" else "Người nhận:")
        partner = receipt.get("supplier") if mode == "IN" else receipt.get("recipient")
        self.ui.lblPartnerValue.setText(partner or "-")
        self.ui.lblNoteValue.setText(receipt.get("note") or "-")

        table = self.ui.tblDetail
        table.setRowCount(0)
        for i, d in enumerate(details):
            table.insertRow(i)
            table.setItem(i, 0, QTableWidgetItem(d.get("code", "")))
            table.setItem(i, 1, QTableWidgetItem(d.get("name", "")))
            table.setItem(i, 2, QTableWidgetItem(d.get("unit") or ""))
            table.setItem(i, 3, QTableWidgetItem(format_int(d.get("quantity"))))

        self.ui.btnClose.clicked.connect(self.accept)
