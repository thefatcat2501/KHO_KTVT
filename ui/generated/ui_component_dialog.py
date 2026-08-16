# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'component_dialog.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QDialog, QFormLayout,
    QFrame, QHBoxLayout, QLabel, QLineEdit,
    QListWidget, QListWidgetItem, QPlainTextEdit, QPushButton,
    QScrollArea, QSizePolicy, QSpacerItem, QSpinBox,
    QVBoxLayout, QWidget)

from utils.barcode_input import BarcodeLineEdit

class Ui_ComponentDialog(object):
    def setupUi(self, ComponentDialog):
        if not ComponentDialog.objectName():
            ComponentDialog.setObjectName(u"ComponentDialog")
        ComponentDialog.resize(640, 640)
        ComponentDialog.setModal(True)
        self.mainLayout = QVBoxLayout(ComponentDialog)
        self.mainLayout.setSpacing(10)
        self.mainLayout.setObjectName(u"mainLayout")
        self.mainLayout.setContentsMargins(24, 20, 24, 20)
        self.lblDialogTitle = QLabel(ComponentDialog)
        self.lblDialogTitle.setObjectName(u"lblDialogTitle")
        self.lblDialogTitle.setProperty(u"objectName", u"dialogTitle")

        self.mainLayout.addWidget(self.lblDialogTitle)

        self.scrollArea = QScrollArea(ComponentDialog)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setFrameShape(QFrame.NoFrame)
        self.scrollAreaContents = QWidget()
        self.scrollAreaContents.setObjectName(u"scrollAreaContents")
        self.scrollAreaContents.setGeometry(QRect(0, 0, 580, 560))
        self.formLayout = QFormLayout(self.scrollAreaContents)
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setHorizontalSpacing(14)
        self.formLayout.setVerticalSpacing(10)
        self.formLayout.setLabelAlignment(Qt.AlignRight|Qt.AlignVCenter)
        self.lblCode = QLabel(self.scrollAreaContents)
        self.lblCode.setObjectName(u"lblCode")

        self.formLayout.setWidget(0, QFormLayout.ItemRole.LabelRole, self.lblCode)

        self.codeRowLayout = QHBoxLayout()
        self.codeRowLayout.setObjectName(u"codeRowLayout")
        self.txtCode = QLineEdit(self.scrollAreaContents)
        self.txtCode.setObjectName(u"txtCode")

        self.codeRowLayout.addWidget(self.txtCode)


        self.formLayout.setLayout(0, QFormLayout.ItemRole.FieldRole, self.codeRowLayout)

        self.lblBarcode = QLabel(self.scrollAreaContents)
        self.lblBarcode.setObjectName(u"lblBarcode")

        self.formLayout.setWidget(1, QFormLayout.ItemRole.LabelRole, self.lblBarcode)

        self.txtBarcode = BarcodeLineEdit(self.scrollAreaContents)
        self.txtBarcode.setObjectName(u"txtBarcode")

        self.formLayout.setWidget(1, QFormLayout.ItemRole.FieldRole, self.txtBarcode)

        self.lblName = QLabel(self.scrollAreaContents)
        self.lblName.setObjectName(u"lblName")

        self.formLayout.setWidget(2, QFormLayout.ItemRole.LabelRole, self.lblName)

        self.txtName = QLineEdit(self.scrollAreaContents)
        self.txtName.setObjectName(u"txtName")

        self.formLayout.setWidget(2, QFormLayout.ItemRole.FieldRole, self.txtName)

        self.lblCategory = QLabel(self.scrollAreaContents)
        self.lblCategory.setObjectName(u"lblCategory")

        self.formLayout.setWidget(3, QFormLayout.ItemRole.LabelRole, self.lblCategory)

        self.categoryRowLayout = QHBoxLayout()
        self.categoryRowLayout.setObjectName(u"categoryRowLayout")
        self.cboCategory = QComboBox(self.scrollAreaContents)
        self.cboCategory.setObjectName(u"cboCategory")
        self.cboCategory.setEditable(True)

        self.categoryRowLayout.addWidget(self.cboCategory)


        self.formLayout.setLayout(3, QFormLayout.ItemRole.FieldRole, self.categoryRowLayout)

        self.lblManufacturer = QLabel(self.scrollAreaContents)
        self.lblManufacturer.setObjectName(u"lblManufacturer")

        self.formLayout.setWidget(4, QFormLayout.ItemRole.LabelRole, self.lblManufacturer)

        self.cboManufacturer = QComboBox(self.scrollAreaContents)
        self.cboManufacturer.setObjectName(u"cboManufacturer")
        self.cboManufacturer.setEditable(True)

        self.formLayout.setWidget(4, QFormLayout.ItemRole.FieldRole, self.cboManufacturer)

        self.lblUnit = QLabel(self.scrollAreaContents)
        self.lblUnit.setObjectName(u"lblUnit")

        self.formLayout.setWidget(5, QFormLayout.ItemRole.LabelRole, self.lblUnit)

        self.cboUnit = QComboBox(self.scrollAreaContents)
        self.cboUnit.setObjectName(u"cboUnit")
        self.cboUnit.setEditable(True)

        self.formLayout.setWidget(5, QFormLayout.ItemRole.FieldRole, self.cboUnit)

        self.lblQuantity = QLabel(self.scrollAreaContents)
        self.lblQuantity.setObjectName(u"lblQuantity")

        self.formLayout.setWidget(6, QFormLayout.ItemRole.LabelRole, self.lblQuantity)

        self.spnQuantity = QSpinBox(self.scrollAreaContents)
        self.spnQuantity.setObjectName(u"spnQuantity")
        self.spnQuantity.setMinimum(0)
        self.spnQuantity.setMaximum(1000000)

        self.formLayout.setWidget(6, QFormLayout.ItemRole.FieldRole, self.spnQuantity)

        self.lblMinQuantity = QLabel(self.scrollAreaContents)
        self.lblMinQuantity.setObjectName(u"lblMinQuantity")

        self.formLayout.setWidget(7, QFormLayout.ItemRole.LabelRole, self.lblMinQuantity)

        self.spnMinQuantity = QSpinBox(self.scrollAreaContents)
        self.spnMinQuantity.setObjectName(u"spnMinQuantity")
        self.spnMinQuantity.setMinimum(0)
        self.spnMinQuantity.setMaximum(1000000)

        self.formLayout.setWidget(7, QFormLayout.ItemRole.FieldRole, self.spnMinQuantity)

        self.lblYear = QLabel(self.scrollAreaContents)
        self.lblYear.setObjectName(u"lblYear")

        self.formLayout.setWidget(8, QFormLayout.ItemRole.LabelRole, self.lblYear)

        self.spnYear = QSpinBox(self.scrollAreaContents)
        self.spnYear.setObjectName(u"spnYear")
        self.spnYear.setMinimum(2000)
        self.spnYear.setMaximum(2100)

        self.formLayout.setWidget(8, QFormLayout.ItemRole.FieldRole, self.spnYear)

        self.lblLocation = QLabel(self.scrollAreaContents)
        self.lblLocation.setObjectName(u"lblLocation")

        self.formLayout.setWidget(9, QFormLayout.ItemRole.LabelRole, self.lblLocation)

        self.txtLocation = QLineEdit(self.scrollAreaContents)
        self.txtLocation.setObjectName(u"txtLocation")

        self.formLayout.setWidget(9, QFormLayout.ItemRole.FieldRole, self.txtLocation)

        self.lblProducts = QLabel(self.scrollAreaContents)
        self.lblProducts.setObjectName(u"lblProducts")

        self.formLayout.setWidget(10, QFormLayout.ItemRole.LabelRole, self.lblProducts)

        self.productsColLayout = QVBoxLayout()
        self.productsColLayout.setSpacing(4)
        self.productsColLayout.setObjectName(u"productsColLayout")
        self.txtProductSearch = QLineEdit(self.scrollAreaContents)
        self.txtProductSearch.setObjectName(u"txtProductSearch")

        self.productsColLayout.addWidget(self.txtProductSearch)

        self.lstProducts = QListWidget(self.scrollAreaContents)
        self.lstProducts.setObjectName(u"lstProducts")
        self.lstProducts.setMinimumSize(QSize(0, 90))
        self.lstProducts.setMaximumSize(QSize(16777215, 110))

        self.productsColLayout.addWidget(self.lstProducts)


        self.formLayout.setLayout(10, QFormLayout.ItemRole.FieldRole, self.productsColLayout)

        self.lblDescription = QLabel(self.scrollAreaContents)
        self.lblDescription.setObjectName(u"lblDescription")

        self.formLayout.setWidget(11, QFormLayout.ItemRole.LabelRole, self.lblDescription)

        self.pteDescription = QPlainTextEdit(self.scrollAreaContents)
        self.pteDescription.setObjectName(u"pteDescription")
        self.pteDescription.setMaximumSize(QSize(16777215, 80))

        self.formLayout.setWidget(11, QFormLayout.ItemRole.FieldRole, self.pteDescription)

        self.scrollArea.setWidget(self.scrollAreaContents)

        self.mainLayout.addWidget(self.scrollArea)

        self.lblFormError = QLabel(ComponentDialog)
        self.lblFormError.setObjectName(u"lblFormError")
        self.lblFormError.setProperty(u"objectName", u"errorLabel")

        self.mainLayout.addWidget(self.lblFormError)

        self.buttonRowLayout = QHBoxLayout()
        self.buttonRowLayout.setObjectName(u"buttonRowLayout")
        self.btnSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.buttonRowLayout.addItem(self.btnSpacer)

        self.btnCancel = QPushButton(ComponentDialog)
        self.btnCancel.setObjectName(u"btnCancel")
        self.btnCancel.setMinimumSize(QSize(110, 38))
        self.btnCancel.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.buttonRowLayout.addWidget(self.btnCancel)

        self.btnSave = QPushButton(ComponentDialog)
        self.btnSave.setObjectName(u"btnSave")
        self.btnSave.setMinimumSize(QSize(140, 38))
        self.btnSave.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btnSave.setProperty(u"objectName", u"accentButton")

        self.buttonRowLayout.addWidget(self.btnSave)


        self.mainLayout.addLayout(self.buttonRowLayout)


        self.retranslateUi(ComponentDialog)

        self.btnSave.setDefault(True)


        QMetaObject.connectSlotsByName(ComponentDialog)
    # setupUi

    def retranslateUi(self, ComponentDialog):
        ComponentDialog.setWindowTitle(QCoreApplication.translate("ComponentDialog", u"Th\u00f4ng tin linh ki\u1ec7n", None))
        self.lblDialogTitle.setText(QCoreApplication.translate("ComponentDialog", u"Th\u00eam linh ki\u1ec7n m\u1edbi", None))
        self.lblCode.setText(QCoreApplication.translate("ComponentDialog", u"M\u00e3 linh ki\u1ec7n *", None))
        self.txtCode.setPlaceholderText(QCoreApplication.translate("ComponentDialog", u"VD: LK0001 (\u0111\u1ec3 tr\u1ed1ng s\u1ebd t\u1ef1 sinh m\u00e3)", None))
        self.lblBarcode.setText(QCoreApplication.translate("ComponentDialog", u"M\u00e3 v\u1ea1ch", None))
        self.txtBarcode.setPlaceholderText(QCoreApplication.translate("ComponentDialog", u"Qu\u00e9t ho\u1eb7c nh\u1eadp m\u00e3 v\u1ea1ch (kh\u00f4ng b\u1eaft bu\u1ed9c)", None))
        self.lblName.setText(QCoreApplication.translate("ComponentDialog", u"T\u00ean linh ki\u1ec7n *", None))
        self.txtName.setPlaceholderText(QCoreApplication.translate("ComponentDialog", u"VD: \u0110i\u1ec7n tr\u1edf 10K 1/4W", None))
        self.lblCategory.setText(QCoreApplication.translate("ComponentDialog", u"Lo\u1ea1i linh ki\u1ec7n", None))
        self.lblManufacturer.setText(QCoreApplication.translate("ComponentDialog", u"Nh\u00e0 s\u1ea3n xu\u1ea5t", None))
        self.lblUnit.setText(QCoreApplication.translate("ComponentDialog", u"\u0110\u01a1n v\u1ecb t\u00ednh", None))
        self.lblQuantity.setText(QCoreApplication.translate("ComponentDialog", u"T\u1ed3n kho ban \u0111\u1ea7u", None))
        self.lblMinQuantity.setText(QCoreApplication.translate("ComponentDialog", u"Ng\u01b0\u1ee1ng c\u1ea3nh b\u00e1o t\u1ed1i thi\u1ec3u", None))
        self.lblYear.setText(QCoreApplication.translate("ComponentDialog", u"N\u0103m nh\u1eadp kho", None))
        self.lblLocation.setText(QCoreApplication.translate("ComponentDialog", u"V\u1ecb tr\u00ed l\u01b0u kho", None))
        self.txtLocation.setPlaceholderText(QCoreApplication.translate("ComponentDialog", u"VD: K\u1ec7 A - Ng\u0103n 3", None))
        self.lblProducts.setText(QCoreApplication.translate("ComponentDialog", u"S\u1ea3n ph\u1ea9m s\u1eed d\u1ee5ng", None))
        self.txtProductSearch.setPlaceholderText(QCoreApplication.translate("ComponentDialog", u"G\u00f5 \u0111\u1ec3 l\u1ecdc nhanh s\u1ea3n ph\u1ea9m (VD: \"bo m\u1ea1ch\")...", None))
        self.lblDescription.setText(QCoreApplication.translate("ComponentDialog", u"M\u00f4 t\u1ea3 / Ghi ch\u00fa", None))
        self.lblFormError.setText("")
        self.btnCancel.setText(QCoreApplication.translate("ComponentDialog", u"H\u1ee7y", None))
        self.btnSave.setText(QCoreApplication.translate("ComponentDialog", u"\U0001f4be  L\U000001b0u l\U00001ea1i", None))
    # retranslateUi

