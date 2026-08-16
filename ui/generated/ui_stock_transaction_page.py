# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'stock_transaction_page.ui'
##
## Created by: Qt User Interface Compiler version 6.11.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QFrame, QHBoxLayout,
    QHeaderView, QLabel, QLineEdit, QPushButton,
    QSizePolicy, QSpacerItem, QTableWidget, QTableWidgetItem,
    QVBoxLayout, QWidget)

from utils.barcode_input import BarcodeLineEdit

class Ui_StockTransactionPage(object):
    def setupUi(self, StockTransactionPage):
        if not StockTransactionPage.objectName():
            StockTransactionPage.setObjectName(u"StockTransactionPage")
        StockTransactionPage.resize(1000, 700)
        self.mainLayout = QVBoxLayout(StockTransactionPage)
        self.mainLayout.setSpacing(12)
        self.mainLayout.setObjectName(u"mainLayout")
        self.mainLayout.setContentsMargins(28, 18, 28, 18)
        self.infoFrame = QFrame(StockTransactionPage)
        self.infoFrame.setObjectName(u"infoFrame")
        self.infoLayout = QHBoxLayout(self.infoFrame)
        self.infoLayout.setSpacing(14)
        self.infoLayout.setObjectName(u"infoLayout")
        self.infoLayout.setContentsMargins(16, 12, 16, 12)
        self.lblReceiptCodeCaption = QLabel(self.infoFrame)
        self.lblReceiptCodeCaption.setObjectName(u"lblReceiptCodeCaption")

        self.infoLayout.addWidget(self.lblReceiptCodeCaption)

        self.lblReceiptCode = QLabel(self.infoFrame)
        self.lblReceiptCode.setObjectName(u"lblReceiptCode")
        self.lblReceiptCode.setProperty(u"objectName", u"receiptCodeValue")

        self.infoLayout.addWidget(self.lblReceiptCode)

        self.lblPartnerCaption = QLabel(self.infoFrame)
        self.lblPartnerCaption.setObjectName(u"lblPartnerCaption")

        self.infoLayout.addWidget(self.lblPartnerCaption)

        self.txtPartner = QLineEdit(self.infoFrame)
        self.txtPartner.setObjectName(u"txtPartner")
        self.txtPartner.setMinimumSize(QSize(220, 34))

        self.infoLayout.addWidget(self.txtPartner)

        self.lblNoteCaption = QLabel(self.infoFrame)
        self.lblNoteCaption.setObjectName(u"lblNoteCaption")

        self.infoLayout.addWidget(self.lblNoteCaption)

        self.txtNote = QLineEdit(self.infoFrame)
        self.txtNote.setObjectName(u"txtNote")
        self.txtNote.setMinimumSize(QSize(200, 34))

        self.infoLayout.addWidget(self.txtNote)

        self.infoSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.infoLayout.addItem(self.infoSpacer)


        self.mainLayout.addWidget(self.infoFrame)

        self.scanFrame = QFrame(StockTransactionPage)
        self.scanFrame.setObjectName(u"scanFrame")
        self.scanFrame.setMinimumSize(QSize(0, 72))
        self.scanFrame.setProperty(u"objectName", u"scanFrame")
        self.scanLayout = QHBoxLayout(self.scanFrame)
        self.scanLayout.setSpacing(10)
        self.scanLayout.setObjectName(u"scanLayout")
        self.scanLayout.setContentsMargins(16, -1, 16, -1)
        self.lblScanIcon = QLabel(self.scanFrame)
        self.lblScanIcon.setObjectName(u"lblScanIcon")
        self.lblScanIcon.setProperty(u"objectName", u"scanIcon")

        self.scanLayout.addWidget(self.lblScanIcon)

        self.txtBarcode = BarcodeLineEdit(self.scanFrame)
        self.txtBarcode.setObjectName(u"txtBarcode")
        self.txtBarcode.setMinimumSize(QSize(0, 44))
        self.txtBarcode.setProperty(u"objectName", u"barcodeInput")

        self.scanLayout.addWidget(self.txtBarcode)

        self.btnManualAdd = QPushButton(self.scanFrame)
        self.btnManualAdd.setObjectName(u"btnManualAdd")
        self.btnManualAdd.setMinimumSize(QSize(190, 44))
        self.btnManualAdd.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.scanLayout.addWidget(self.btnManualAdd)


        self.mainLayout.addWidget(self.scanFrame)

        self.tblItems = QTableWidget(StockTransactionPage)
        if (self.tblItems.columnCount() < 8):
            self.tblItems.setColumnCount(8)
        __qtablewidgetitem = QTableWidgetItem()
        self.tblItems.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tblItems.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tblItems.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tblItems.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tblItems.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tblItems.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.tblItems.setHorizontalHeaderItem(6, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.tblItems.setHorizontalHeaderItem(7, __qtablewidgetitem7)
        self.tblItems.setObjectName(u"tblItems")
        self.tblItems.setAlternatingRowColors(True)
        self.tblItems.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.tblItems.horizontalHeader().setStretchLastSection(False)

        self.mainLayout.addWidget(self.tblItems)

        self.footerLayout = QHBoxLayout()
        self.footerLayout.setObjectName(u"footerLayout")
        self.lblItemCount = QLabel(StockTransactionPage)
        self.lblItemCount.setObjectName(u"lblItemCount")

        self.footerLayout.addWidget(self.lblItemCount)

        self.footerSpacer1 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.footerLayout.addItem(self.footerSpacer1)

        self.lblTotalQtyCaption = QLabel(StockTransactionPage)
        self.lblTotalQtyCaption.setObjectName(u"lblTotalQtyCaption")

        self.footerLayout.addWidget(self.lblTotalQtyCaption)

        self.lblTotalQty = QLabel(StockTransactionPage)
        self.lblTotalQty.setObjectName(u"lblTotalQty")
        self.lblTotalQty.setProperty(u"objectName", u"totalValue")

        self.footerLayout.addWidget(self.lblTotalQty)

        self.btnClearAll = QPushButton(StockTransactionPage)
        self.btnClearAll.setObjectName(u"btnClearAll")
        self.btnClearAll.setMinimumSize(QSize(110, 40))
        self.btnClearAll.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.footerLayout.addWidget(self.btnClearAll)

        self.btnSaveReceipt = QPushButton(StockTransactionPage)
        self.btnSaveReceipt.setObjectName(u"btnSaveReceipt")
        self.btnSaveReceipt.setMinimumSize(QSize(190, 40))
        self.btnSaveReceipt.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btnSaveReceipt.setProperty(u"objectName", u"accentButton")

        self.footerLayout.addWidget(self.btnSaveReceipt)


        self.mainLayout.addLayout(self.footerLayout)


        self.retranslateUi(StockTransactionPage)

        QMetaObject.connectSlotsByName(StockTransactionPage)
    # setupUi

    def retranslateUi(self, StockTransactionPage):
        self.lblReceiptCodeCaption.setText(QCoreApplication.translate("StockTransactionPage", u"S\u1ed1 phi\u1ebfu:", None))
        self.lblReceiptCode.setText(QCoreApplication.translate("StockTransactionPage", u"(t\u1ef1 \u0111\u1ed9ng)", None))
        self.lblPartnerCaption.setText(QCoreApplication.translate("StockTransactionPage", u"\u0110\u1ed1i t\u00e1c:", None))
        self.txtPartner.setPlaceholderText(QCoreApplication.translate("StockTransactionPage", u"T\u00ean nh\u00e0 cung c\u1ea5p / ng\u01b0\u1eddi nh\u1eadn", None))
        self.lblNoteCaption.setText(QCoreApplication.translate("StockTransactionPage", u"Ghi ch\u00fa:", None))
        self.txtNote.setPlaceholderText(QCoreApplication.translate("StockTransactionPage", u"Ghi ch\u00fa cho phi\u1ebfu (kh\u00f4ng b\u1eaft bu\u1ed9c)", None))
        self.lblScanIcon.setText(QCoreApplication.translate("StockTransactionPage", u"\U0001f4f7", None))
        self.txtBarcode.setPlaceholderText(QCoreApplication.translate("StockTransactionPage", u"Qu\u00e9t m\u00e3 v\u1ea1ch t\u1ea1i \u0111\u00e2y (ho\u1eb7c g\u00f5 m\u00e3 r\u1ed3i nh\u1ea5n Enter)...", None))
        self.btnManualAdd.setText(QCoreApplication.translate("StockTransactionPage", u"\U0001f50d  T\U000000ecm && th\U000000eam th\U00001ee7 c\U000000f4ng", None))
        ___qtablewidgetitem = self.tblItems.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("StockTransactionPage", u"#", None))
        ___qtablewidgetitem1 = self.tblItems.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("StockTransactionPage", u"M\u00e3 v\u1ea1ch", None))
        ___qtablewidgetitem2 = self.tblItems.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("StockTransactionPage", u"M\u00e3 LK", None))
        ___qtablewidgetitem3 = self.tblItems.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("StockTransactionPage", u"T\u00ean linh ki\u1ec7n", None))
        ___qtablewidgetitem4 = self.tblItems.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("StockTransactionPage", u"\u0110\u01a1n v\u1ecb", None))
        ___qtablewidgetitem5 = self.tblItems.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("StockTransactionPage", u"T\u1ed3n hi\u1ec7n t\u1ea1i", None))
        ___qtablewidgetitem6 = self.tblItems.horizontalHeaderItem(6)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("StockTransactionPage", u"S\u1ed1 l\u01b0\u1ee3ng", None))
        self.lblItemCount.setText(QCoreApplication.translate("StockTransactionPage", u"0 d\u00f2ng", None))
        self.lblTotalQtyCaption.setText(QCoreApplication.translate("StockTransactionPage", u"T\u1ed5ng s\u1ed1 l\u01b0\u1ee3ng:", None))
        self.lblTotalQty.setText(QCoreApplication.translate("StockTransactionPage", u"0", None))
        self.btnClearAll.setText(QCoreApplication.translate("StockTransactionPage", u"H\u1ee7y phi\u1ebfu", None))
        self.btnSaveReceipt.setText(QCoreApplication.translate("StockTransactionPage", u"\u2705  X\u00e1c nh\u1eadn && L\u01b0u phi\u1ebfu", None))
        pass
    # retranslateUi

