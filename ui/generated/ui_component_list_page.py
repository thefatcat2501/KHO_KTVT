# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'component_list_page.ui'
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
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QCheckBox, QComboBox,
    QFrame, QHBoxLayout, QHeaderView, QLabel,
    QLineEdit, QPushButton, QSizePolicy, QSpacerItem,
    QTableWidget, QTableWidgetItem, QVBoxLayout, QWidget)

class Ui_ComponentListPage(object):
    def setupUi(self, ComponentListPage):
        if not ComponentListPage.objectName():
            ComponentListPage.setObjectName(u"ComponentListPage")
        ComponentListPage.resize(1000, 700)
        self.mainLayout = QVBoxLayout(ComponentListPage)
        self.mainLayout.setSpacing(12)
        self.mainLayout.setObjectName(u"mainLayout")
        self.mainLayout.setContentsMargins(28, 18, 28, 18)
        self.filterFrame = QFrame(ComponentListPage)
        self.filterFrame.setObjectName(u"filterFrame")
        self.filterOuterLayout = QVBoxLayout(self.filterFrame)
        self.filterOuterLayout.setSpacing(10)
        self.filterOuterLayout.setObjectName(u"filterOuterLayout")
        self.filterOuterLayout.setContentsMargins(16, 12, 16, 12)
        self.searchRowLayout = QHBoxLayout()
        self.searchRowLayout.setObjectName(u"searchRowLayout")
        self.txtSearch = QLineEdit(self.filterFrame)
        self.txtSearch.setObjectName(u"txtSearch")
        self.txtSearch.setMinimumSize(QSize(0, 38))

        self.searchRowLayout.addWidget(self.txtSearch)

        self.btnAddComponent = QPushButton(self.filterFrame)
        self.btnAddComponent.setObjectName(u"btnAddComponent")
        self.btnAddComponent.setMinimumSize(QSize(150, 38))
        self.btnAddComponent.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btnAddComponent.setProperty(u"objectName", u"accentButton")

        self.searchRowLayout.addWidget(self.btnAddComponent)


        self.filterOuterLayout.addLayout(self.searchRowLayout)

        self.filterRowLayout = QHBoxLayout()
        self.filterRowLayout.setSpacing(10)
        self.filterRowLayout.setObjectName(u"filterRowLayout")
        self.lblFilterCategory = QLabel(self.filterFrame)
        self.lblFilterCategory.setObjectName(u"lblFilterCategory")

        self.filterRowLayout.addWidget(self.lblFilterCategory)

        self.cboFilterCategory = QComboBox(self.filterFrame)
        self.cboFilterCategory.setObjectName(u"cboFilterCategory")
        self.cboFilterCategory.setMinimumSize(QSize(140, 34))

        self.filterRowLayout.addWidget(self.cboFilterCategory)

        self.lblFilterManufacturer = QLabel(self.filterFrame)
        self.lblFilterManufacturer.setObjectName(u"lblFilterManufacturer")

        self.filterRowLayout.addWidget(self.lblFilterManufacturer)

        self.cboFilterManufacturer = QComboBox(self.filterFrame)
        self.cboFilterManufacturer.setObjectName(u"cboFilterManufacturer")
        self.cboFilterManufacturer.setMinimumSize(QSize(150, 34))

        self.filterRowLayout.addWidget(self.cboFilterManufacturer)

        self.lblFilterProduct = QLabel(self.filterFrame)
        self.lblFilterProduct.setObjectName(u"lblFilterProduct")

        self.filterRowLayout.addWidget(self.lblFilterProduct)

        self.cboFilterProduct = QComboBox(self.filterFrame)
        self.cboFilterProduct.setObjectName(u"cboFilterProduct")
        self.cboFilterProduct.setMinimumSize(QSize(150, 34))

        self.filterRowLayout.addWidget(self.cboFilterProduct)

        self.lblFilterYear = QLabel(self.filterFrame)
        self.lblFilterYear.setObjectName(u"lblFilterYear")

        self.filterRowLayout.addWidget(self.lblFilterYear)

        self.cboFilterYear = QComboBox(self.filterFrame)
        self.cboFilterYear.setObjectName(u"cboFilterYear")
        self.cboFilterYear.setMinimumSize(QSize(100, 34))

        self.filterRowLayout.addWidget(self.cboFilterYear)

        self.chkLowStockOnly = QCheckBox(self.filterFrame)
        self.chkLowStockOnly.setObjectName(u"chkLowStockOnly")

        self.filterRowLayout.addWidget(self.chkLowStockOnly)

        self.filterSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.filterRowLayout.addItem(self.filterSpacer)

        self.btnClearFilter = QPushButton(self.filterFrame)
        self.btnClearFilter.setObjectName(u"btnClearFilter")
        self.btnClearFilter.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.filterRowLayout.addWidget(self.btnClearFilter)


        self.filterOuterLayout.addLayout(self.filterRowLayout)


        self.mainLayout.addWidget(self.filterFrame)

        self.tblComponents = QTableWidget(ComponentListPage)
        if (self.tblComponents.columnCount() < 9):
            self.tblComponents.setColumnCount(9)
        __qtablewidgetitem = QTableWidgetItem()
        self.tblComponents.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tblComponents.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tblComponents.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tblComponents.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tblComponents.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tblComponents.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.tblComponents.setHorizontalHeaderItem(6, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.tblComponents.setHorizontalHeaderItem(7, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.tblComponents.setHorizontalHeaderItem(8, __qtablewidgetitem8)
        self.tblComponents.setObjectName(u"tblComponents")
        self.tblComponents.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tblComponents.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.tblComponents.setSelectionMode(QAbstractItemView.SingleSelection)
        self.tblComponents.setAlternatingRowColors(True)
        self.tblComponents.setSortingEnabled(True)
        self.tblComponents.horizontalHeader().setStretchLastSection(False)

        self.mainLayout.addWidget(self.tblComponents)

        self.footerLayout = QHBoxLayout()
        self.footerLayout.setObjectName(u"footerLayout")
        self.lblResultCount = QLabel(ComponentListPage)
        self.lblResultCount.setObjectName(u"lblResultCount")

        self.footerLayout.addWidget(self.lblResultCount)

        self.footerSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.footerLayout.addItem(self.footerSpacer)

        self.btnViewDetail = QPushButton(ComponentListPage)
        self.btnViewDetail.setObjectName(u"btnViewDetail")
        self.btnViewDetail.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.footerLayout.addWidget(self.btnViewDetail)

        self.btnEditComponent = QPushButton(ComponentListPage)
        self.btnEditComponent.setObjectName(u"btnEditComponent")
        self.btnEditComponent.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.footerLayout.addWidget(self.btnEditComponent)

        self.btnDeleteComponent = QPushButton(ComponentListPage)
        self.btnDeleteComponent.setObjectName(u"btnDeleteComponent")
        self.btnDeleteComponent.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btnDeleteComponent.setProperty(u"objectName", u"dangerButton")

        self.footerLayout.addWidget(self.btnDeleteComponent)


        self.mainLayout.addLayout(self.footerLayout)


        self.retranslateUi(ComponentListPage)

        QMetaObject.connectSlotsByName(ComponentListPage)
    # setupUi

    def retranslateUi(self, ComponentListPage):
        self.txtSearch.setPlaceholderText(QCoreApplication.translate("ComponentListPage", u"\U0001f50d  T\U000000ecm theo m\U000000e3, t\U000000ean linh ki\U00001ec7n, m\U000000e3 v\U00001ea1ch...", None))
        self.btnAddComponent.setText(QCoreApplication.translate("ComponentListPage", u"\u2795  Th\u00eam linh ki\u1ec7n", None))
        self.lblFilterCategory.setText(QCoreApplication.translate("ComponentListPage", u"Lo\u1ea1i:", None))
        self.lblFilterManufacturer.setText(QCoreApplication.translate("ComponentListPage", u"Nh\u00e0 s\u1ea3n xu\u1ea5t:", None))
        self.lblFilterProduct.setText(QCoreApplication.translate("ComponentListPage", u"S\u1ea3n ph\u1ea9m s\u1eed d\u1ee5ng:", None))
        self.lblFilterYear.setText(QCoreApplication.translate("ComponentListPage", u"N\u0103m nh\u1eadp:", None))
        self.chkLowStockOnly.setText(QCoreApplication.translate("ComponentListPage", u"Ch\u1ec9 hi\u1ec7n s\u1eafp h\u1ebft h\u00e0ng", None))
        self.btnClearFilter.setText(QCoreApplication.translate("ComponentListPage", u"X\u00f3a l\u1ecdc", None))
        ___qtablewidgetitem = self.tblComponents.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("ComponentListPage", u"M\u00e3 LK", None))
        ___qtablewidgetitem1 = self.tblComponents.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("ComponentListPage", u"M\u00e3 v\u1ea1ch", None))
        ___qtablewidgetitem2 = self.tblComponents.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("ComponentListPage", u"T\u00ean linh ki\u1ec7n", None))
        ___qtablewidgetitem3 = self.tblComponents.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("ComponentListPage", u"Lo\u1ea1i", None))
        ___qtablewidgetitem4 = self.tblComponents.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("ComponentListPage", u"Nh\u00e0 s\u1ea3n xu\u1ea5t", None))
        ___qtablewidgetitem5 = self.tblComponents.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("ComponentListPage", u"\u0110\u01a1n v\u1ecb", None))
        ___qtablewidgetitem6 = self.tblComponents.horizontalHeaderItem(6)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("ComponentListPage", u"T\u1ed3n kho", None))
        ___qtablewidgetitem7 = self.tblComponents.horizontalHeaderItem(7)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("ComponentListPage", u"N\u0103m nh\u1eadp", None))
        ___qtablewidgetitem8 = self.tblComponents.horizontalHeaderItem(8)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("ComponentListPage", u"V\u1ecb tr\u00ed", None))
        self.lblResultCount.setText(QCoreApplication.translate("ComponentListPage", u"0 linh ki\u1ec7n", None))
        self.btnViewDetail.setText(QCoreApplication.translate("ComponentListPage", u"\U0001f441  Xem chi ti\U00001ebft", None))
        self.btnEditComponent.setText(QCoreApplication.translate("ComponentListPage", u"\u270f\ufe0f  S\u1eeda", None))
        self.btnDeleteComponent.setText(QCoreApplication.translate("ComponentListPage", u"\U0001f5d1  X\U000000f3a", None))
        pass
    # retranslateUi

