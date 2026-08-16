# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'dashboard_page.ui'
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
    QHeaderView, QLabel, QPushButton, QSizePolicy,
    QSpacerItem, QTableWidget, QTableWidgetItem, QVBoxLayout,
    QWidget)

class Ui_DashboardPage(object):
    def setupUi(self, DashboardPage):
        if not DashboardPage.objectName():
            DashboardPage.setObjectName(u"DashboardPage")
        DashboardPage.resize(1000, 700)
        self.mainLayout = QVBoxLayout(DashboardPage)
        self.mainLayout.setSpacing(18)
        self.mainLayout.setObjectName(u"mainLayout")
        self.mainLayout.setContentsMargins(28, 22, 28, 22)
        self.cardsLayout = QHBoxLayout()
        self.cardsLayout.setSpacing(16)
        self.cardsLayout.setObjectName(u"cardsLayout")
        self.cardTotalComponents = QFrame(DashboardPage)
        self.cardTotalComponents.setObjectName(u"cardTotalComponents")
        self.cardTotalComponents.setMinimumSize(QSize(0, 110))
        self.cardTotalComponents.setStyleSheet(u"QFrame#cardTotalComponents{border-left: 4px solid #2563EB;}")
        self.c1Layout = QVBoxLayout(self.cardTotalComponents)
        self.c1Layout.setObjectName(u"c1Layout")
        self.c1Layout.setContentsMargins(18, 14, -1, -1)
        self.lblCard1Title = QLabel(self.cardTotalComponents)
        self.lblCard1Title.setObjectName(u"lblCard1Title")
        self.lblCard1Title.setProperty(u"objectName", u"cardLabel")

        self.c1Layout.addWidget(self.lblCard1Title)

        self.lblCard1Value = QLabel(self.cardTotalComponents)
        self.lblCard1Value.setObjectName(u"lblCard1Value")
        self.lblCard1Value.setProperty(u"objectName", u"cardValue")

        self.c1Layout.addWidget(self.lblCard1Value)


        self.cardsLayout.addWidget(self.cardTotalComponents)

        self.cardStockValue = QFrame(DashboardPage)
        self.cardStockValue.setObjectName(u"cardStockValue")
        self.cardStockValue.setMinimumSize(QSize(0, 110))
        self.cardStockValue.setStyleSheet(u"QFrame#cardStockValue{border-left: 4px solid #16A34A;}")
        self.c2Layout = QVBoxLayout(self.cardStockValue)
        self.c2Layout.setObjectName(u"c2Layout")
        self.c2Layout.setContentsMargins(18, 14, -1, -1)
        self.lblCard2Title = QLabel(self.cardStockValue)
        self.lblCard2Title.setObjectName(u"lblCard2Title")
        self.lblCard2Title.setProperty(u"objectName", u"cardLabel")

        self.c2Layout.addWidget(self.lblCard2Title)

        self.lblCard2Value = QLabel(self.cardStockValue)
        self.lblCard2Value.setObjectName(u"lblCard2Value")
        self.lblCard2Value.setProperty(u"objectName", u"cardValue")

        self.c2Layout.addWidget(self.lblCard2Value)


        self.cardsLayout.addWidget(self.cardStockValue)

        self.cardLowStock = QFrame(DashboardPage)
        self.cardLowStock.setObjectName(u"cardLowStock")
        self.cardLowStock.setMinimumSize(QSize(0, 110))
        self.cardLowStock.setStyleSheet(u"QFrame#cardLowStock{border-left: 4px solid #DC2626;}")
        self.c3Layout = QVBoxLayout(self.cardLowStock)
        self.c3Layout.setObjectName(u"c3Layout")
        self.c3Layout.setContentsMargins(18, 14, -1, -1)
        self.lblCard3Title = QLabel(self.cardLowStock)
        self.lblCard3Title.setObjectName(u"lblCard3Title")
        self.lblCard3Title.setProperty(u"objectName", u"cardLabel")

        self.c3Layout.addWidget(self.lblCard3Title)

        self.lblCard3Value = QLabel(self.cardLowStock)
        self.lblCard3Value.setObjectName(u"lblCard3Value")
        self.lblCard3Value.setProperty(u"objectName", u"cardValue")

        self.c3Layout.addWidget(self.lblCard3Value)


        self.cardsLayout.addWidget(self.cardLowStock)

        self.cardReceipts = QFrame(DashboardPage)
        self.cardReceipts.setObjectName(u"cardReceipts")
        self.cardReceipts.setMinimumSize(QSize(0, 110))
        self.cardReceipts.setStyleSheet(u"QFrame#cardReceipts{border-left: 4px solid #D97706;}")
        self.c4Layout = QVBoxLayout(self.cardReceipts)
        self.c4Layout.setObjectName(u"c4Layout")
        self.c4Layout.setContentsMargins(18, 14, -1, -1)
        self.lblCard4Title = QLabel(self.cardReceipts)
        self.lblCard4Title.setObjectName(u"lblCard4Title")
        self.lblCard4Title.setProperty(u"objectName", u"cardLabel")

        self.c4Layout.addWidget(self.lblCard4Title)

        self.lblCard4Value = QLabel(self.cardReceipts)
        self.lblCard4Value.setObjectName(u"lblCard4Value")
        self.lblCard4Value.setProperty(u"objectName", u"cardValue")

        self.c4Layout.addWidget(self.lblCard4Value)


        self.cardsLayout.addWidget(self.cardReceipts)


        self.mainLayout.addLayout(self.cardsLayout)

        self.bottomLayout = QHBoxLayout()
        self.bottomLayout.setSpacing(16)
        self.bottomLayout.setObjectName(u"bottomLayout")
        self.lowStockFrame = QFrame(DashboardPage)
        self.lowStockFrame.setObjectName(u"lowStockFrame")
        self.lowStockLayout = QVBoxLayout(self.lowStockFrame)
        self.lowStockLayout.setObjectName(u"lowStockLayout")
        self.lowStockLayout.setContentsMargins(18, 14, 18, 14)
        self.lowStockHeader = QHBoxLayout()
        self.lowStockHeader.setObjectName(u"lowStockHeader")
        self.lblLowStockTitle = QLabel(self.lowStockFrame)
        self.lblLowStockTitle.setObjectName(u"lblLowStockTitle")
        self.lblLowStockTitle.setProperty(u"objectName", u"sectionTitle")

        self.lowStockHeader.addWidget(self.lblLowStockTitle)

        self.lsSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.lowStockHeader.addItem(self.lsSpacer)

        self.btnGoToStockIn = QPushButton(self.lowStockFrame)
        self.btnGoToStockIn.setObjectName(u"btnGoToStockIn")
        self.btnGoToStockIn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btnGoToStockIn.setProperty(u"objectName", u"accentButton")

        self.lowStockHeader.addWidget(self.btnGoToStockIn)


        self.lowStockLayout.addLayout(self.lowStockHeader)

        self.tblLowStock = QTableWidget(self.lowStockFrame)
        if (self.tblLowStock.columnCount() < 5):
            self.tblLowStock.setColumnCount(5)
        __qtablewidgetitem = QTableWidgetItem()
        self.tblLowStock.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tblLowStock.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tblLowStock.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tblLowStock.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tblLowStock.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        self.tblLowStock.setObjectName(u"tblLowStock")
        self.tblLowStock.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tblLowStock.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.tblLowStock.setAlternatingRowColors(True)
        self.tblLowStock.horizontalHeader().setStretchLastSection(True)

        self.lowStockLayout.addWidget(self.tblLowStock)


        self.bottomLayout.addWidget(self.lowStockFrame)

        self.quickActionsFrame = QFrame(DashboardPage)
        self.quickActionsFrame.setObjectName(u"quickActionsFrame")
        self.quickActionsFrame.setMinimumSize(QSize(280, 0))
        self.quickActionsFrame.setMaximumSize(QSize(300, 16777215))
        self.quickActionsLayout = QVBoxLayout(self.quickActionsFrame)
        self.quickActionsLayout.setSpacing(10)
        self.quickActionsLayout.setObjectName(u"quickActionsLayout")
        self.quickActionsLayout.setContentsMargins(18, 14, 18, -1)
        self.lblQuickTitle = QLabel(self.quickActionsFrame)
        self.lblQuickTitle.setObjectName(u"lblQuickTitle")
        self.lblQuickTitle.setProperty(u"objectName", u"sectionTitle")

        self.quickActionsLayout.addWidget(self.lblQuickTitle)

        self.btnQuickAddComponent = QPushButton(self.quickActionsFrame)
        self.btnQuickAddComponent.setObjectName(u"btnQuickAddComponent")
        self.btnQuickAddComponent.setMinimumSize(QSize(0, 42))
        self.btnQuickAddComponent.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.quickActionsLayout.addWidget(self.btnQuickAddComponent)

        self.btnQuickStockIn = QPushButton(self.quickActionsFrame)
        self.btnQuickStockIn.setObjectName(u"btnQuickStockIn")
        self.btnQuickStockIn.setMinimumSize(QSize(0, 42))
        self.btnQuickStockIn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.quickActionsLayout.addWidget(self.btnQuickStockIn)

        self.btnQuickStockOut = QPushButton(self.quickActionsFrame)
        self.btnQuickStockOut.setObjectName(u"btnQuickStockOut")
        self.btnQuickStockOut.setMinimumSize(QSize(0, 42))
        self.btnQuickStockOut.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.quickActionsLayout.addWidget(self.btnQuickStockOut)

        self.btnQuickBackup = QPushButton(self.quickActionsFrame)
        self.btnQuickBackup.setObjectName(u"btnQuickBackup")
        self.btnQuickBackup.setMinimumSize(QSize(0, 42))
        self.btnQuickBackup.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.quickActionsLayout.addWidget(self.btnQuickBackup)

        self.qaSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.quickActionsLayout.addItem(self.qaSpacer)


        self.bottomLayout.addWidget(self.quickActionsFrame)


        self.mainLayout.addLayout(self.bottomLayout)


        self.retranslateUi(DashboardPage)

        QMetaObject.connectSlotsByName(DashboardPage)
    # setupUi

    def retranslateUi(self, DashboardPage):
        self.lblCard1Title.setText(QCoreApplication.translate("DashboardPage", u"T\u1ed4NG S\u1ed0 LINH KI\u1ec6N", None))
        self.lblCard1Value.setText(QCoreApplication.translate("DashboardPage", u"0", None))
        self.lblCard2Title.setText(QCoreApplication.translate("DashboardPage", u"S\u1ed0 L\u01af\u1ee2NG T\u1ed2N KHO", None))
        self.lblCard2Value.setText(QCoreApplication.translate("DashboardPage", u"0", None))
        self.lblCard3Title.setText(QCoreApplication.translate("DashboardPage", u"S\u1eaeP H\u1ebeT H\u00c0NG", None))
        self.lblCard3Value.setText(QCoreApplication.translate("DashboardPage", u"0", None))
        self.lblCard4Title.setText(QCoreApplication.translate("DashboardPage", u"PHI\u1ebeU H\u00d4M NAY", None))
        self.lblCard4Value.setText(QCoreApplication.translate("DashboardPage", u"0", None))
        self.lblLowStockTitle.setText(QCoreApplication.translate("DashboardPage", u"\u26a0\ufe0f  Linh ki\u1ec7n s\u1eafp h\u1ebft h\u00e0ng", None))
        self.btnGoToStockIn.setText(QCoreApplication.translate("DashboardPage", u"+ Nh\u1eadp kho ngay", None))
        ___qtablewidgetitem = self.tblLowStock.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("DashboardPage", u"M\u00e3", None))
        ___qtablewidgetitem1 = self.tblLowStock.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("DashboardPage", u"T\u00ean linh ki\u1ec7n", None))
        ___qtablewidgetitem2 = self.tblLowStock.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("DashboardPage", u"T\u1ed3n kho", None))
        ___qtablewidgetitem3 = self.tblLowStock.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("DashboardPage", u"Ng\u01b0\u1ee1ng t\u1ed1i thi\u1ec3u", None))
        ___qtablewidgetitem4 = self.tblLowStock.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("DashboardPage", u"Nh\u00e0 s\u1ea3n xu\u1ea5t", None))
        self.lblQuickTitle.setText(QCoreApplication.translate("DashboardPage", u"Thao t\u00e1c nhanh", None))
        self.btnQuickAddComponent.setText(QCoreApplication.translate("DashboardPage", u"\u2795  Th\u00eam linh ki\u1ec7n m\u1edbi", None))
        self.btnQuickStockIn.setText(QCoreApplication.translate("DashboardPage", u"\U0001f4e5  T\U00001ea1o phi\U00001ebfu nh\U00001eadp kho", None))
        self.btnQuickStockOut.setText(QCoreApplication.translate("DashboardPage", u"\U0001f4e4  T\U00001ea1o phi\U00001ebfu xu\U00001ea5t kho", None))
        self.btnQuickBackup.setText(QCoreApplication.translate("DashboardPage", u"\U0001f4be  Sao l\U000001b0u d\U00001eef li\U00001ec7u ngay", None))
        pass
    # retranslateUi

