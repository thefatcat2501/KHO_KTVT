# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'component_select_dialog.ui'
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
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QDialog, QHBoxLayout,
    QHeaderView, QLabel, QLineEdit, QPushButton,
    QSizePolicy, QSpacerItem, QSpinBox, QTableWidget,
    QTableWidgetItem, QVBoxLayout, QWidget)

class Ui_ComponentSelectDialog(object):
    def setupUi(self, ComponentSelectDialog):
        if not ComponentSelectDialog.objectName():
            ComponentSelectDialog.setObjectName(u"ComponentSelectDialog")
        ComponentSelectDialog.resize(680, 520)
        ComponentSelectDialog.setModal(True)
        self.mainLayout = QVBoxLayout(ComponentSelectDialog)
        self.mainLayout.setSpacing(10)
        self.mainLayout.setObjectName(u"mainLayout")
        self.mainLayout.setContentsMargins(22, 18, 22, 18)
        self.txtSearch = QLineEdit(ComponentSelectDialog)
        self.txtSearch.setObjectName(u"txtSearch")
        self.txtSearch.setMinimumSize(QSize(0, 38))

        self.mainLayout.addWidget(self.txtSearch)

        self.tblResults = QTableWidget(ComponentSelectDialog)
        if (self.tblResults.columnCount() < 4):
            self.tblResults.setColumnCount(4)
        __qtablewidgetitem = QTableWidgetItem()
        self.tblResults.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tblResults.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tblResults.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tblResults.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        self.tblResults.setObjectName(u"tblResults")
        self.tblResults.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tblResults.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.tblResults.setSelectionMode(QAbstractItemView.SingleSelection)
        self.tblResults.setAlternatingRowColors(True)
        self.tblResults.horizontalHeader().setStretchLastSection(True)

        self.mainLayout.addWidget(self.tblResults)

        self.qtyLayout = QHBoxLayout()
        self.qtyLayout.setObjectName(u"qtyLayout")
        self.lblQtyCaption = QLabel(ComponentSelectDialog)
        self.lblQtyCaption.setObjectName(u"lblQtyCaption")

        self.qtyLayout.addWidget(self.lblQtyCaption)

        self.spnQty = QSpinBox(ComponentSelectDialog)
        self.spnQty.setObjectName(u"spnQty")
        self.spnQty.setMinimum(1)
        self.spnQty.setMaximum(1000000)
        self.spnQty.setValue(1)

        self.qtyLayout.addWidget(self.spnQty)

        self.qtySpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.qtyLayout.addItem(self.qtySpacer)

        self.btnCreateNew = QPushButton(ComponentSelectDialog)
        self.btnCreateNew.setObjectName(u"btnCreateNew")
        self.btnCreateNew.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.qtyLayout.addWidget(self.btnCreateNew)


        self.mainLayout.addLayout(self.qtyLayout)

        self.buttonLayout = QHBoxLayout()
        self.buttonLayout.setObjectName(u"buttonLayout")
        self.btnSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.buttonLayout.addItem(self.btnSpacer)

        self.btnCancel = QPushButton(ComponentSelectDialog)
        self.btnCancel.setObjectName(u"btnCancel")
        self.btnCancel.setMinimumSize(QSize(110, 38))
        self.btnCancel.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.buttonLayout.addWidget(self.btnCancel)

        self.btnAdd = QPushButton(ComponentSelectDialog)
        self.btnAdd.setObjectName(u"btnAdd")
        self.btnAdd.setMinimumSize(QSize(150, 38))
        self.btnAdd.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btnAdd.setProperty(u"objectName", u"accentButton")

        self.buttonLayout.addWidget(self.btnAdd)


        self.mainLayout.addLayout(self.buttonLayout)


        self.retranslateUi(ComponentSelectDialog)

        self.btnAdd.setDefault(True)


        QMetaObject.connectSlotsByName(ComponentSelectDialog)
    # setupUi

    def retranslateUi(self, ComponentSelectDialog):
        ComponentSelectDialog.setWindowTitle(QCoreApplication.translate("ComponentSelectDialog", u"T\u00ecm v\u00e0 ch\u1ecdn linh ki\u1ec7n", None))
        self.txtSearch.setPlaceholderText(QCoreApplication.translate("ComponentSelectDialog", u"\U0001f50d  G\U000000f5 t\U000000ean, m\U000000e3 ho\U00001eb7c m\U000000e3 v\U00001ea1ch linh ki\U00001ec7n \U00000111\U00001ec3 t\U000000ecm...", None))
        ___qtablewidgetitem = self.tblResults.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("ComponentSelectDialog", u"M\u00e3 LK", None))
        ___qtablewidgetitem1 = self.tblResults.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("ComponentSelectDialog", u"T\u00ean linh ki\u1ec7n", None))
        ___qtablewidgetitem2 = self.tblResults.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("ComponentSelectDialog", u"T\u1ed3n kho", None))
        ___qtablewidgetitem3 = self.tblResults.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("ComponentSelectDialog", u"\u0110\u01a1n v\u1ecb", None))
        self.lblQtyCaption.setText(QCoreApplication.translate("ComponentSelectDialog", u"S\u1ed1 l\u01b0\u1ee3ng:", None))
        self.btnCreateNew.setText(QCoreApplication.translate("ComponentSelectDialog", u"\u2795  Linh ki\u1ec7n ch\u01b0a c\u00f3, t\u1ea1o m\u1edbi", None))
        self.btnCancel.setText(QCoreApplication.translate("ComponentSelectDialog", u"H\u1ee7y", None))
        self.btnAdd.setText(QCoreApplication.translate("ComponentSelectDialog", u"\u2795  Th\u00eam v\u00e0o phi\u1ebfu", None))
    # retranslateUi

