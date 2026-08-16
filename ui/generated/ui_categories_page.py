# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'categories_page.ui'
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
    QHeaderView, QLabel, QLineEdit, QPlainTextEdit,
    QPushButton, QSizePolicy, QSpacerItem, QTabWidget,
    QTableWidget, QTableWidgetItem, QVBoxLayout, QWidget)

class Ui_CategoriesPage(object):
    def setupUi(self, CategoriesPage):
        if not CategoriesPage.objectName():
            CategoriesPage.setObjectName(u"CategoriesPage")
        CategoriesPage.resize(1000, 700)
        self.mainLayout = QVBoxLayout(CategoriesPage)
        self.mainLayout.setObjectName(u"mainLayout")
        self.mainLayout.setContentsMargins(28, 18, 28, 18)
        self.tabWidget = QTabWidget(CategoriesPage)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabCategory = QWidget()
        self.tabCategory.setObjectName(u"tabCategory")
        self.tabCategoryLayout = QHBoxLayout(self.tabCategory)
        self.tabCategoryLayout.setObjectName(u"tabCategoryLayout")
        self.tblCategory = QTableWidget(self.tabCategory)
        if (self.tblCategory.columnCount() < 2):
            self.tblCategory.setColumnCount(2)
        __qtablewidgetitem = QTableWidgetItem()
        self.tblCategory.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tblCategory.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        self.tblCategory.setObjectName(u"tblCategory")
        self.tblCategory.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tblCategory.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.tblCategory.setAlternatingRowColors(True)
        self.tblCategory.horizontalHeader().setStretchLastSection(True)

        self.tabCategoryLayout.addWidget(self.tblCategory)

        self.formCategoryFrame = QFrame(self.tabCategory)
        self.formCategoryFrame.setObjectName(u"formCategoryFrame")
        self.formCategoryFrame.setMinimumSize(QSize(300, 0))
        self.formCategoryFrame.setMaximumSize(QSize(320, 16777215))
        self.formCategoryLayout = QVBoxLayout(self.formCategoryFrame)
        self.formCategoryLayout.setSpacing(10)
        self.formCategoryLayout.setObjectName(u"formCategoryLayout")
        self.formCategoryLayout.setContentsMargins(16, 14, 16, -1)
        self.lblCategoryFormTitle = QLabel(self.formCategoryFrame)
        self.lblCategoryFormTitle.setObjectName(u"lblCategoryFormTitle")
        self.lblCategoryFormTitle.setProperty(u"objectName", u"sectionTitle")

        self.formCategoryLayout.addWidget(self.lblCategoryFormTitle)

        self.txtCategoryName = QLineEdit(self.formCategoryFrame)
        self.txtCategoryName.setObjectName(u"txtCategoryName")

        self.formCategoryLayout.addWidget(self.txtCategoryName)

        self.pteCategoryDesc = QPlainTextEdit(self.formCategoryFrame)
        self.pteCategoryDesc.setObjectName(u"pteCategoryDesc")
        self.pteCategoryDesc.setMaximumSize(QSize(16777215, 90))

        self.formCategoryLayout.addWidget(self.pteCategoryDesc)

        self.categoryBtnLayout = QHBoxLayout()
        self.categoryBtnLayout.setObjectName(u"categoryBtnLayout")
        self.btnCategorySave = QPushButton(self.formCategoryFrame)
        self.btnCategorySave.setObjectName(u"btnCategorySave")
        self.btnCategorySave.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btnCategorySave.setProperty(u"objectName", u"accentButton")

        self.categoryBtnLayout.addWidget(self.btnCategorySave)

        self.btnCategoryNew = QPushButton(self.formCategoryFrame)
        self.btnCategoryNew.setObjectName(u"btnCategoryNew")
        self.btnCategoryNew.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.categoryBtnLayout.addWidget(self.btnCategoryNew)

        self.btnCategoryDelete = QPushButton(self.formCategoryFrame)
        self.btnCategoryDelete.setObjectName(u"btnCategoryDelete")
        self.btnCategoryDelete.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btnCategoryDelete.setProperty(u"objectName", u"dangerButton")

        self.categoryBtnLayout.addWidget(self.btnCategoryDelete)


        self.formCategoryLayout.addLayout(self.categoryBtnLayout)

        self.categorySpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.formCategoryLayout.addItem(self.categorySpacer)


        self.tabCategoryLayout.addWidget(self.formCategoryFrame)

        self.tabWidget.addTab(self.tabCategory, "")
        self.tabManufacturer = QWidget()
        self.tabManufacturer.setObjectName(u"tabManufacturer")
        self.tabManufacturerLayout = QHBoxLayout(self.tabManufacturer)
        self.tabManufacturerLayout.setObjectName(u"tabManufacturerLayout")
        self.tblManufacturer = QTableWidget(self.tabManufacturer)
        if (self.tblManufacturer.columnCount() < 3):
            self.tblManufacturer.setColumnCount(3)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tblManufacturer.setHorizontalHeaderItem(0, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tblManufacturer.setHorizontalHeaderItem(1, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tblManufacturer.setHorizontalHeaderItem(2, __qtablewidgetitem4)
        self.tblManufacturer.setObjectName(u"tblManufacturer")
        self.tblManufacturer.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tblManufacturer.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.tblManufacturer.setAlternatingRowColors(True)
        self.tblManufacturer.horizontalHeader().setStretchLastSection(True)

        self.tabManufacturerLayout.addWidget(self.tblManufacturer)

        self.formManufacturerFrame = QFrame(self.tabManufacturer)
        self.formManufacturerFrame.setObjectName(u"formManufacturerFrame")
        self.formManufacturerFrame.setMinimumSize(QSize(300, 0))
        self.formManufacturerFrame.setMaximumSize(QSize(320, 16777215))
        self.formManufacturerLayout = QVBoxLayout(self.formManufacturerFrame)
        self.formManufacturerLayout.setSpacing(10)
        self.formManufacturerLayout.setObjectName(u"formManufacturerLayout")
        self.formManufacturerLayout.setContentsMargins(16, 14, 16, -1)
        self.lblManufacturerFormTitle = QLabel(self.formManufacturerFrame)
        self.lblManufacturerFormTitle.setObjectName(u"lblManufacturerFormTitle")
        self.lblManufacturerFormTitle.setProperty(u"objectName", u"sectionTitle")

        self.formManufacturerLayout.addWidget(self.lblManufacturerFormTitle)

        self.txtManufacturerName = QLineEdit(self.formManufacturerFrame)
        self.txtManufacturerName.setObjectName(u"txtManufacturerName")

        self.formManufacturerLayout.addWidget(self.txtManufacturerName)

        self.txtManufacturerContact = QLineEdit(self.formManufacturerFrame)
        self.txtManufacturerContact.setObjectName(u"txtManufacturerContact")

        self.formManufacturerLayout.addWidget(self.txtManufacturerContact)

        self.txtManufacturerAddress = QLineEdit(self.formManufacturerFrame)
        self.txtManufacturerAddress.setObjectName(u"txtManufacturerAddress")

        self.formManufacturerLayout.addWidget(self.txtManufacturerAddress)

        self.manufacturerBtnLayout = QHBoxLayout()
        self.manufacturerBtnLayout.setObjectName(u"manufacturerBtnLayout")
        self.btnManufacturerSave = QPushButton(self.formManufacturerFrame)
        self.btnManufacturerSave.setObjectName(u"btnManufacturerSave")
        self.btnManufacturerSave.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btnManufacturerSave.setProperty(u"objectName", u"accentButton")

        self.manufacturerBtnLayout.addWidget(self.btnManufacturerSave)

        self.btnManufacturerNew = QPushButton(self.formManufacturerFrame)
        self.btnManufacturerNew.setObjectName(u"btnManufacturerNew")
        self.btnManufacturerNew.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.manufacturerBtnLayout.addWidget(self.btnManufacturerNew)

        self.btnManufacturerDelete = QPushButton(self.formManufacturerFrame)
        self.btnManufacturerDelete.setObjectName(u"btnManufacturerDelete")
        self.btnManufacturerDelete.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btnManufacturerDelete.setProperty(u"objectName", u"dangerButton")

        self.manufacturerBtnLayout.addWidget(self.btnManufacturerDelete)


        self.formManufacturerLayout.addLayout(self.manufacturerBtnLayout)

        self.manufacturerSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.formManufacturerLayout.addItem(self.manufacturerSpacer)


        self.tabManufacturerLayout.addWidget(self.formManufacturerFrame)

        self.tabWidget.addTab(self.tabManufacturer, "")
        self.tabProduct = QWidget()
        self.tabProduct.setObjectName(u"tabProduct")
        self.tabProductLayout = QHBoxLayout(self.tabProduct)
        self.tabProductLayout.setObjectName(u"tabProductLayout")
        self.tblProduct = QTableWidget(self.tabProduct)
        if (self.tblProduct.columnCount() < 2):
            self.tblProduct.setColumnCount(2)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tblProduct.setHorizontalHeaderItem(0, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.tblProduct.setHorizontalHeaderItem(1, __qtablewidgetitem6)
        self.tblProduct.setObjectName(u"tblProduct")
        self.tblProduct.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tblProduct.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.tblProduct.setAlternatingRowColors(True)
        self.tblProduct.horizontalHeader().setStretchLastSection(True)

        self.tabProductLayout.addWidget(self.tblProduct)

        self.formProductFrame = QFrame(self.tabProduct)
        self.formProductFrame.setObjectName(u"formProductFrame")
        self.formProductFrame.setMinimumSize(QSize(300, 0))
        self.formProductFrame.setMaximumSize(QSize(320, 16777215))
        self.formProductLayout = QVBoxLayout(self.formProductFrame)
        self.formProductLayout.setSpacing(10)
        self.formProductLayout.setObjectName(u"formProductLayout")
        self.formProductLayout.setContentsMargins(16, 14, 16, -1)
        self.lblProductFormTitle = QLabel(self.formProductFrame)
        self.lblProductFormTitle.setObjectName(u"lblProductFormTitle")
        self.lblProductFormTitle.setProperty(u"objectName", u"sectionTitle")

        self.formProductLayout.addWidget(self.lblProductFormTitle)

        self.txtProductName = QLineEdit(self.formProductFrame)
        self.txtProductName.setObjectName(u"txtProductName")

        self.formProductLayout.addWidget(self.txtProductName)

        self.pteProductDesc = QPlainTextEdit(self.formProductFrame)
        self.pteProductDesc.setObjectName(u"pteProductDesc")
        self.pteProductDesc.setMaximumSize(QSize(16777215, 90))

        self.formProductLayout.addWidget(self.pteProductDesc)

        self.productBtnLayout = QHBoxLayout()
        self.productBtnLayout.setObjectName(u"productBtnLayout")
        self.btnProductSave = QPushButton(self.formProductFrame)
        self.btnProductSave.setObjectName(u"btnProductSave")
        self.btnProductSave.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btnProductSave.setProperty(u"objectName", u"accentButton")

        self.productBtnLayout.addWidget(self.btnProductSave)

        self.btnProductNew = QPushButton(self.formProductFrame)
        self.btnProductNew.setObjectName(u"btnProductNew")
        self.btnProductNew.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.productBtnLayout.addWidget(self.btnProductNew)

        self.btnProductDelete = QPushButton(self.formProductFrame)
        self.btnProductDelete.setObjectName(u"btnProductDelete")
        self.btnProductDelete.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btnProductDelete.setProperty(u"objectName", u"dangerButton")

        self.productBtnLayout.addWidget(self.btnProductDelete)


        self.formProductLayout.addLayout(self.productBtnLayout)

        self.productSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.formProductLayout.addItem(self.productSpacer)


        self.tabProductLayout.addWidget(self.formProductFrame)

        self.tabWidget.addTab(self.tabProduct, "")

        self.mainLayout.addWidget(self.tabWidget)


        self.retranslateUi(CategoriesPage)

        QMetaObject.connectSlotsByName(CategoriesPage)
    # setupUi

    def retranslateUi(self, CategoriesPage):
        ___qtablewidgetitem = self.tblCategory.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("CategoriesPage", u"T\u00ean lo\u1ea1i", None))
        ___qtablewidgetitem1 = self.tblCategory.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("CategoriesPage", u"M\u00f4 t\u1ea3", None))
        self.lblCategoryFormTitle.setText(QCoreApplication.translate("CategoriesPage", u"Th\u00eam / S\u1eeda lo\u1ea1i linh ki\u1ec7n", None))
        self.txtCategoryName.setPlaceholderText(QCoreApplication.translate("CategoriesPage", u"T\u00ean lo\u1ea1i linh ki\u1ec7n *", None))
        self.btnCategorySave.setText(QCoreApplication.translate("CategoriesPage", u"\U0001f4be  L\U000001b0u", None))
        self.btnCategoryNew.setText(QCoreApplication.translate("CategoriesPage", u"\u2795  M\u1edbi", None))
        self.btnCategoryDelete.setText(QCoreApplication.translate("CategoriesPage", u"\U0001f5d1  X\U000000f3a", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabCategory), QCoreApplication.translate("CategoriesPage", u"\U0001f3f7\U0000fe0f  Lo\U00001ea1i linh ki\U00001ec7n", None))
        ___qtablewidgetitem2 = self.tblManufacturer.horizontalHeaderItem(0)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("CategoriesPage", u"T\u00ean nh\u00e0 s\u1ea3n xu\u1ea5t", None))
        ___qtablewidgetitem3 = self.tblManufacturer.horizontalHeaderItem(1)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("CategoriesPage", u"Th\u00f4ng tin li\u00ean h\u1ec7", None))
        ___qtablewidgetitem4 = self.tblManufacturer.horizontalHeaderItem(2)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("CategoriesPage", u"\u0110\u1ecba ch\u1ec9", None))
        self.lblManufacturerFormTitle.setText(QCoreApplication.translate("CategoriesPage", u"Th\u00eam / S\u1eeda nh\u00e0 s\u1ea3n xu\u1ea5t", None))
        self.txtManufacturerName.setPlaceholderText(QCoreApplication.translate("CategoriesPage", u"T\u00ean nh\u00e0 s\u1ea3n xu\u1ea5t *", None))
        self.txtManufacturerContact.setPlaceholderText(QCoreApplication.translate("CategoriesPage", u"S\u0110T / Email li\u00ean h\u1ec7", None))
        self.txtManufacturerAddress.setPlaceholderText(QCoreApplication.translate("CategoriesPage", u"\u0110\u1ecba ch\u1ec9", None))
        self.btnManufacturerSave.setText(QCoreApplication.translate("CategoriesPage", u"\U0001f4be  L\U000001b0u", None))
        self.btnManufacturerNew.setText(QCoreApplication.translate("CategoriesPage", u"\u2795  M\u1edbi", None))
        self.btnManufacturerDelete.setText(QCoreApplication.translate("CategoriesPage", u"\U0001f5d1  X\U000000f3a", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabManufacturer), QCoreApplication.translate("CategoriesPage", u"\U0001f3ed  Nh\U000000e0 s\U00001ea3n xu\U00001ea5t", None))
        ___qtablewidgetitem5 = self.tblProduct.horizontalHeaderItem(0)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("CategoriesPage", u"T\u00ean s\u1ea3n ph\u1ea9m", None))
        ___qtablewidgetitem6 = self.tblProduct.horizontalHeaderItem(1)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("CategoriesPage", u"M\u00f4 t\u1ea3", None))
        self.lblProductFormTitle.setText(QCoreApplication.translate("CategoriesPage", u"Th\u00eam / S\u1eeda s\u1ea3n ph\u1ea9m s\u1eed d\u1ee5ng", None))
        self.txtProductName.setPlaceholderText(QCoreApplication.translate("CategoriesPage", u"T\u00ean s\u1ea3n ph\u1ea9m *", None))
        self.btnProductSave.setText(QCoreApplication.translate("CategoriesPage", u"\U0001f4be  L\U000001b0u", None))
        self.btnProductNew.setText(QCoreApplication.translate("CategoriesPage", u"\u2795  M\u1edbi", None))
        self.btnProductDelete.setText(QCoreApplication.translate("CategoriesPage", u"\U0001f5d1  X\U000000f3a", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabProduct), QCoreApplication.translate("CategoriesPage", u"\U0001f4e6  S\U00001ea3n ph\U00001ea9m s\U00001eed d\U00001ee5ng", None))
        pass
    # retranslateUi

