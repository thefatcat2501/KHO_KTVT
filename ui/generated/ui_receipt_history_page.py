# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'receipt_history_page.ui'
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
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QDateEdit, QHBoxLayout,
    QHeaderView, QLabel, QLineEdit, QPushButton,
    QSizePolicy, QSpacerItem, QTabWidget, QTableWidget,
    QTableWidgetItem, QVBoxLayout, QWidget)

class Ui_ReceiptHistoryPage(object):
    def setupUi(self, ReceiptHistoryPage):
        if not ReceiptHistoryPage.objectName():
            ReceiptHistoryPage.setObjectName(u"ReceiptHistoryPage")
        ReceiptHistoryPage.resize(1000, 700)
        self.mainLayout = QVBoxLayout(ReceiptHistoryPage)
        self.mainLayout.setSpacing(12)
        self.mainLayout.setObjectName(u"mainLayout")
        self.mainLayout.setContentsMargins(28, 18, 28, 18)
        self.searchRowLayout = QHBoxLayout()
        self.searchRowLayout.setObjectName(u"searchRowLayout")
        self.txtSearch = QLineEdit(ReceiptHistoryPage)
        self.txtSearch.setObjectName(u"txtSearch")
        self.txtSearch.setMinimumSize(QSize(0, 38))

        self.searchRowLayout.addWidget(self.txtSearch)

        self.dteFrom = QDateEdit(ReceiptHistoryPage)
        self.dteFrom.setObjectName(u"dteFrom")
        self.dteFrom.setCalendarPopup(True)

        self.searchRowLayout.addWidget(self.dteFrom)

        self.lblToDash = QLabel(ReceiptHistoryPage)
        self.lblToDash.setObjectName(u"lblToDash")

        self.searchRowLayout.addWidget(self.lblToDash)

        self.dteTo = QDateEdit(ReceiptHistoryPage)
        self.dteTo.setObjectName(u"dteTo")
        self.dteTo.setCalendarPopup(True)

        self.searchRowLayout.addWidget(self.dteTo)

        self.btnFilterReceipts = QPushButton(ReceiptHistoryPage)
        self.btnFilterReceipts.setObjectName(u"btnFilterReceipts")
        self.btnFilterReceipts.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.searchRowLayout.addWidget(self.btnFilterReceipts)


        self.mainLayout.addLayout(self.searchRowLayout)

        self.tabWidget = QTabWidget(ReceiptHistoryPage)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabImport = QWidget()
        self.tabImport.setObjectName(u"tabImport")
        self.tabImportLayout = QVBoxLayout(self.tabImport)
        self.tabImportLayout.setObjectName(u"tabImportLayout")
        self.tblImportReceipts = QTableWidget(self.tabImport)
        if (self.tblImportReceipts.columnCount() < 5):
            self.tblImportReceipts.setColumnCount(5)
        __qtablewidgetitem = QTableWidgetItem()
        self.tblImportReceipts.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tblImportReceipts.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tblImportReceipts.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tblImportReceipts.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tblImportReceipts.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        self.tblImportReceipts.setObjectName(u"tblImportReceipts")
        self.tblImportReceipts.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tblImportReceipts.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.tblImportReceipts.setAlternatingRowColors(True)
        self.tblImportReceipts.horizontalHeader().setStretchLastSection(True)

        self.tabImportLayout.addWidget(self.tblImportReceipts)

        self.importFooterLayout = QHBoxLayout()
        self.importFooterLayout.setObjectName(u"importFooterLayout")
        self.impSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.importFooterLayout.addItem(self.impSpacer)

        self.btnViewImportDetail = QPushButton(self.tabImport)
        self.btnViewImportDetail.setObjectName(u"btnViewImportDetail")
        self.btnViewImportDetail.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.importFooterLayout.addWidget(self.btnViewImportDetail)

        self.btnVoidImport = QPushButton(self.tabImport)
        self.btnVoidImport.setObjectName(u"btnVoidImport")
        self.btnVoidImport.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btnVoidImport.setProperty(u"objectName", u"dangerButton")

        self.importFooterLayout.addWidget(self.btnVoidImport)


        self.tabImportLayout.addLayout(self.importFooterLayout)

        self.tabWidget.addTab(self.tabImport, "")
        self.tabExport = QWidget()
        self.tabExport.setObjectName(u"tabExport")
        self.tabExportLayout = QVBoxLayout(self.tabExport)
        self.tabExportLayout.setObjectName(u"tabExportLayout")
        self.tblExportReceipts = QTableWidget(self.tabExport)
        if (self.tblExportReceipts.columnCount() < 5):
            self.tblExportReceipts.setColumnCount(5)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tblExportReceipts.setHorizontalHeaderItem(0, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.tblExportReceipts.setHorizontalHeaderItem(1, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.tblExportReceipts.setHorizontalHeaderItem(2, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.tblExportReceipts.setHorizontalHeaderItem(3, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.tblExportReceipts.setHorizontalHeaderItem(4, __qtablewidgetitem9)
        self.tblExportReceipts.setObjectName(u"tblExportReceipts")
        self.tblExportReceipts.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tblExportReceipts.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.tblExportReceipts.setAlternatingRowColors(True)
        self.tblExportReceipts.horizontalHeader().setStretchLastSection(True)

        self.tabExportLayout.addWidget(self.tblExportReceipts)

        self.exportFooterLayout = QHBoxLayout()
        self.exportFooterLayout.setObjectName(u"exportFooterLayout")
        self.expSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.exportFooterLayout.addItem(self.expSpacer)

        self.btnViewExportDetail = QPushButton(self.tabExport)
        self.btnViewExportDetail.setObjectName(u"btnViewExportDetail")
        self.btnViewExportDetail.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.exportFooterLayout.addWidget(self.btnViewExportDetail)

        self.btnVoidExport = QPushButton(self.tabExport)
        self.btnVoidExport.setObjectName(u"btnVoidExport")
        self.btnVoidExport.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btnVoidExport.setProperty(u"objectName", u"dangerButton")

        self.exportFooterLayout.addWidget(self.btnVoidExport)


        self.tabExportLayout.addLayout(self.exportFooterLayout)

        self.tabWidget.addTab(self.tabExport, "")

        self.mainLayout.addWidget(self.tabWidget)


        self.retranslateUi(ReceiptHistoryPage)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(ReceiptHistoryPage)
    # setupUi

    def retranslateUi(self, ReceiptHistoryPage):
        self.txtSearch.setPlaceholderText(QCoreApplication.translate("ReceiptHistoryPage", u"\U0001f50d  T\U000000ecm theo s\U00001ed1 phi\U00001ebfu, \U00000111\U00001ed1i t\U000000e1c, ghi ch\U000000fa...", None))
        self.dteFrom.setDisplayFormat(QCoreApplication.translate("ReceiptHistoryPage", u"dd/MM/yyyy", None))
        self.lblToDash.setText(QCoreApplication.translate("ReceiptHistoryPage", u"\u2014", None))
        self.dteTo.setDisplayFormat(QCoreApplication.translate("ReceiptHistoryPage", u"dd/MM/yyyy", None))
        self.btnFilterReceipts.setText(QCoreApplication.translate("ReceiptHistoryPage", u"L\u1ecdc", None))
        ___qtablewidgetitem = self.tblImportReceipts.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("ReceiptHistoryPage", u"S\u1ed1 phi\u1ebfu", None))
        ___qtablewidgetitem1 = self.tblImportReceipts.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("ReceiptHistoryPage", u"Ng\u00e0y t\u1ea1o", None))
        ___qtablewidgetitem2 = self.tblImportReceipts.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("ReceiptHistoryPage", u"Nh\u00e0 cung c\u1ea5p", None))
        ___qtablewidgetitem3 = self.tblImportReceipts.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("ReceiptHistoryPage", u"T\u1ed5ng SL", None))
        ___qtablewidgetitem4 = self.tblImportReceipts.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("ReceiptHistoryPage", u"Ghi ch\u00fa", None))
        self.btnViewImportDetail.setText(QCoreApplication.translate("ReceiptHistoryPage", u"\U0001f441  Xem chi ti\U00001ebft phi\U00001ebfu", None))
        self.btnVoidImport.setText(QCoreApplication.translate("ReceiptHistoryPage", u"\u21a9  H\u1ee7y phi\u1ebfu n\u00e0y", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabImport), QCoreApplication.translate("ReceiptHistoryPage", u"\U0001f4e5  Phi\U00001ebfu nh\U00001eadp kho", None))
        ___qtablewidgetitem5 = self.tblExportReceipts.horizontalHeaderItem(0)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("ReceiptHistoryPage", u"S\u1ed1 phi\u1ebfu", None))
        ___qtablewidgetitem6 = self.tblExportReceipts.horizontalHeaderItem(1)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("ReceiptHistoryPage", u"Ng\u00e0y t\u1ea1o", None))
        ___qtablewidgetitem7 = self.tblExportReceipts.horizontalHeaderItem(2)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("ReceiptHistoryPage", u"Ng\u01b0\u1eddi nh\u1eadn", None))
        ___qtablewidgetitem8 = self.tblExportReceipts.horizontalHeaderItem(3)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("ReceiptHistoryPage", u"T\u1ed5ng SL", None))
        ___qtablewidgetitem9 = self.tblExportReceipts.horizontalHeaderItem(4)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("ReceiptHistoryPage", u"Ghi ch\u00fa", None))
        self.btnViewExportDetail.setText(QCoreApplication.translate("ReceiptHistoryPage", u"\U0001f441  Xem chi ti\U00001ebft phi\U00001ebfu", None))
        self.btnVoidExport.setText(QCoreApplication.translate("ReceiptHistoryPage", u"\u21a9  H\u1ee7y phi\u1ebfu n\u00e0y", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabExport), QCoreApplication.translate("ReceiptHistoryPage", u"\U0001f4e4  Phi\U00001ebfu xu\U00001ea5t kho", None))
        pass
    # retranslateUi

