# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'receipt_detail_dialog.ui'
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
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QDialog, QFormLayout,
    QFrame, QHBoxLayout, QHeaderView, QLabel,
    QPushButton, QSizePolicy, QSpacerItem, QTableWidget,
    QTableWidgetItem, QVBoxLayout, QWidget)

class Ui_ReceiptDetailDialog(object):
    def setupUi(self, ReceiptDetailDialog):
        if not ReceiptDetailDialog.objectName():
            ReceiptDetailDialog.setObjectName(u"ReceiptDetailDialog")
        ReceiptDetailDialog.resize(720, 560)
        ReceiptDetailDialog.setModal(True)
        self.mainLayout = QVBoxLayout(ReceiptDetailDialog)
        self.mainLayout.setSpacing(10)
        self.mainLayout.setObjectName(u"mainLayout")
        self.mainLayout.setContentsMargins(22, 20, 22, 18)
        self.lblTitle = QLabel(ReceiptDetailDialog)
        self.lblTitle.setObjectName(u"lblTitle")
        self.lblTitle.setProperty(u"objectName", u"dialogTitle")

        self.mainLayout.addWidget(self.lblTitle)

        self.infoFrame = QFrame(ReceiptDetailDialog)
        self.infoFrame.setObjectName(u"infoFrame")
        self.infoForm = QFormLayout(self.infoFrame)
        self.infoForm.setObjectName(u"infoForm")
        self.lblCodeCaption = QLabel(self.infoFrame)
        self.lblCodeCaption.setObjectName(u"lblCodeCaption")

        self.infoForm.setWidget(0, QFormLayout.ItemRole.LabelRole, self.lblCodeCaption)

        self.lblCodeValue = QLabel(self.infoFrame)
        self.lblCodeValue.setObjectName(u"lblCodeValue")

        self.infoForm.setWidget(0, QFormLayout.ItemRole.FieldRole, self.lblCodeValue)

        self.lblDateCaption = QLabel(self.infoFrame)
        self.lblDateCaption.setObjectName(u"lblDateCaption")

        self.infoForm.setWidget(1, QFormLayout.ItemRole.LabelRole, self.lblDateCaption)

        self.lblDateValue = QLabel(self.infoFrame)
        self.lblDateValue.setObjectName(u"lblDateValue")

        self.infoForm.setWidget(1, QFormLayout.ItemRole.FieldRole, self.lblDateValue)

        self.lblPartnerCaption = QLabel(self.infoFrame)
        self.lblPartnerCaption.setObjectName(u"lblPartnerCaption")

        self.infoForm.setWidget(2, QFormLayout.ItemRole.LabelRole, self.lblPartnerCaption)

        self.lblPartnerValue = QLabel(self.infoFrame)
        self.lblPartnerValue.setObjectName(u"lblPartnerValue")

        self.infoForm.setWidget(2, QFormLayout.ItemRole.FieldRole, self.lblPartnerValue)

        self.lblNoteCaption = QLabel(self.infoFrame)
        self.lblNoteCaption.setObjectName(u"lblNoteCaption")

        self.infoForm.setWidget(3, QFormLayout.ItemRole.LabelRole, self.lblNoteCaption)

        self.lblNoteValue = QLabel(self.infoFrame)
        self.lblNoteValue.setObjectName(u"lblNoteValue")

        self.infoForm.setWidget(3, QFormLayout.ItemRole.FieldRole, self.lblNoteValue)


        self.mainLayout.addWidget(self.infoFrame)

        self.tblDetail = QTableWidget(ReceiptDetailDialog)
        if (self.tblDetail.columnCount() < 4):
            self.tblDetail.setColumnCount(4)
        __qtablewidgetitem = QTableWidgetItem()
        self.tblDetail.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tblDetail.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tblDetail.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tblDetail.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        self.tblDetail.setObjectName(u"tblDetail")
        self.tblDetail.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tblDetail.setAlternatingRowColors(True)
        self.tblDetail.horizontalHeader().setStretchLastSection(True)

        self.mainLayout.addWidget(self.tblDetail)

        self.buttonLayout = QHBoxLayout()
        self.buttonLayout.setObjectName(u"buttonLayout")
        self.btnSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.buttonLayout.addItem(self.btnSpacer)

        self.btnClose = QPushButton(ReceiptDetailDialog)
        self.btnClose.setObjectName(u"btnClose")
        self.btnClose.setMinimumSize(QSize(110, 38))
        self.btnClose.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.buttonLayout.addWidget(self.btnClose)


        self.mainLayout.addLayout(self.buttonLayout)


        self.retranslateUi(ReceiptDetailDialog)

        QMetaObject.connectSlotsByName(ReceiptDetailDialog)
    # setupUi

    def retranslateUi(self, ReceiptDetailDialog):
        ReceiptDetailDialog.setWindowTitle(QCoreApplication.translate("ReceiptDetailDialog", u"Chi ti\u1ebft phi\u1ebfu", None))
        self.lblTitle.setText(QCoreApplication.translate("ReceiptDetailDialog", u"Chi ti\u1ebft phi\u1ebfu", None))
        self.lblCodeCaption.setText(QCoreApplication.translate("ReceiptDetailDialog", u"S\u1ed1 phi\u1ebfu:", None))
        self.lblCodeValue.setText(QCoreApplication.translate("ReceiptDetailDialog", u"-", None))
        self.lblDateCaption.setText(QCoreApplication.translate("ReceiptDetailDialog", u"Ng\u00e0y t\u1ea1o:", None))
        self.lblDateValue.setText(QCoreApplication.translate("ReceiptDetailDialog", u"-", None))
        self.lblPartnerCaption.setText(QCoreApplication.translate("ReceiptDetailDialog", u"\u0110\u1ed1i t\u00e1c:", None))
        self.lblPartnerValue.setText(QCoreApplication.translate("ReceiptDetailDialog", u"-", None))
        self.lblNoteCaption.setText(QCoreApplication.translate("ReceiptDetailDialog", u"Ghi ch\u00fa:", None))
        self.lblNoteValue.setText(QCoreApplication.translate("ReceiptDetailDialog", u"-", None))
        ___qtablewidgetitem = self.tblDetail.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("ReceiptDetailDialog", u"M\u00e3 LK", None))
        ___qtablewidgetitem1 = self.tblDetail.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("ReceiptDetailDialog", u"T\u00ean linh ki\u1ec7n", None))
        ___qtablewidgetitem2 = self.tblDetail.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("ReceiptDetailDialog", u"\u0110\u01a1n v\u1ecb", None))
        ___qtablewidgetitem3 = self.tblDetail.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("ReceiptDetailDialog", u"S\u1ed1 l\u01b0\u1ee3ng", None))
        self.btnClose.setText(QCoreApplication.translate("ReceiptDetailDialog", u"\u0110\u00f3ng", None))
    # retranslateUi

