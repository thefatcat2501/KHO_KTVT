# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_window.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QLabel,
    QMainWindow, QPushButton, QSizePolicy, QSpacerItem,
    QStackedWidget, QStatusBar, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1320, 820)
        MainWindow.setMinimumSize(QSize(1100, 680))
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.rootLayout = QHBoxLayout(self.centralwidget)
        self.rootLayout.setSpacing(0)
        self.rootLayout.setObjectName(u"rootLayout")
        self.rootLayout.setContentsMargins(0, 0, 0, 0)
        self.sidebarFrame = QFrame(self.centralwidget)
        self.sidebarFrame.setObjectName(u"sidebarFrame")
        self.sidebarFrame.setMinimumSize(QSize(232, 0))
        self.sidebarFrame.setMaximumSize(QSize(232, 16777215))
        self.sidebarLayout = QVBoxLayout(self.sidebarFrame)
        self.sidebarLayout.setSpacing(4)
        self.sidebarLayout.setObjectName(u"sidebarLayout")
        self.sidebarLayout.setContentsMargins(0, 0, 0, 16)
        self.logoFrame = QFrame(self.sidebarFrame)
        self.logoFrame.setObjectName(u"logoFrame")
        self.logoFrame.setMinimumSize(QSize(0, 84))
        self.logoLayout = QHBoxLayout(self.logoFrame)
        self.logoLayout.setSpacing(10)
        self.logoLayout.setObjectName(u"logoLayout")
        self.logoLayout.setContentsMargins(20, 14, 16, 14)
        self.lblLogoIcon = QLabel(self.logoFrame)
        self.lblLogoIcon.setObjectName(u"lblLogoIcon")
        self.lblLogoIcon.setMinimumSize(QSize(40, 40))
        self.lblLogoIcon.setMaximumSize(QSize(40, 40))
        self.lblLogoIcon.setAlignment(Qt.AlignCenter)

        self.logoLayout.addWidget(self.lblLogoIcon, 0, Qt.AlignLeft|Qt.AlignVCenter)

        self.logoTextLayout = QVBoxLayout()
        self.logoTextLayout.setSpacing(2)
        self.logoTextLayout.setObjectName(u"logoTextLayout")
        self.lblAppTitle = QLabel(self.logoFrame)
        self.lblAppTitle.setObjectName(u"lblAppTitle")
        self.lblAppTitle.setAlignment(Qt.AlignLeft|Qt.AlignVCenter)

        self.logoTextLayout.addWidget(self.lblAppTitle, 0, Qt.AlignLeft|Qt.AlignVCenter)

        self.lblAppSubtitle = QLabel(self.logoFrame)
        self.lblAppSubtitle.setObjectName(u"lblAppSubtitle")
        self.lblAppSubtitle.setAlignment(Qt.AlignLeft|Qt.AlignVCenter)

        self.logoTextLayout.addWidget(self.lblAppSubtitle, 0, Qt.AlignLeft|Qt.AlignVCenter)


        self.logoLayout.addLayout(self.logoTextLayout)

        self.logoRightSpacer = QSpacerItem(10, 10, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.logoLayout.addItem(self.logoRightSpacer)


        self.sidebarLayout.addWidget(self.logoFrame)

        self.navSeparator = QFrame(self.sidebarFrame)
        self.navSeparator.setObjectName(u"navSeparator")
        self.navSeparator.setMinimumSize(QSize(0, 1))
        self.navSeparator.setMaximumSize(QSize(16777215, 1))

        self.sidebarLayout.addWidget(self.navSeparator)

        self.topSpacer1 = QSpacerItem(20, 12, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.sidebarLayout.addItem(self.topSpacer1)

        self.btnNavDashboard = QPushButton(self.sidebarFrame)
        self.btnNavDashboard.setObjectName(u"btnNavDashboard")
        self.btnNavDashboard.setMinimumSize(QSize(0, 46))
        self.btnNavDashboard.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btnNavDashboard.setCheckable(True)
        self.btnNavDashboard.setChecked(True)

        self.sidebarLayout.addWidget(self.btnNavDashboard)

        self.btnNavComponents = QPushButton(self.sidebarFrame)
        self.btnNavComponents.setObjectName(u"btnNavComponents")
        self.btnNavComponents.setMinimumSize(QSize(0, 46))
        self.btnNavComponents.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btnNavComponents.setCheckable(True)

        self.sidebarLayout.addWidget(self.btnNavComponents)

        self.btnNavStockIn = QPushButton(self.sidebarFrame)
        self.btnNavStockIn.setObjectName(u"btnNavStockIn")
        self.btnNavStockIn.setMinimumSize(QSize(0, 46))
        self.btnNavStockIn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btnNavStockIn.setCheckable(True)

        self.sidebarLayout.addWidget(self.btnNavStockIn)

        self.btnNavStockOut = QPushButton(self.sidebarFrame)
        self.btnNavStockOut.setObjectName(u"btnNavStockOut")
        self.btnNavStockOut.setMinimumSize(QSize(0, 46))
        self.btnNavStockOut.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btnNavStockOut.setCheckable(True)

        self.sidebarLayout.addWidget(self.btnNavStockOut)

        self.btnNavReceipts = QPushButton(self.sidebarFrame)
        self.btnNavReceipts.setObjectName(u"btnNavReceipts")
        self.btnNavReceipts.setMinimumSize(QSize(0, 46))
        self.btnNavReceipts.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btnNavReceipts.setCheckable(True)

        self.sidebarLayout.addWidget(self.btnNavReceipts)

        self.btnNavCategories = QPushButton(self.sidebarFrame)
        self.btnNavCategories.setObjectName(u"btnNavCategories")
        self.btnNavCategories.setMinimumSize(QSize(0, 46))
        self.btnNavCategories.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btnNavCategories.setCheckable(True)

        self.sidebarLayout.addWidget(self.btnNavCategories)

        self.btnNavBackup = QPushButton(self.sidebarFrame)
        self.btnNavBackup.setObjectName(u"btnNavBackup")
        self.btnNavBackup.setMinimumSize(QSize(0, 46))
        self.btnNavBackup.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btnNavBackup.setCheckable(True)

        self.sidebarLayout.addWidget(self.btnNavBackup)

        self.sidebarSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.sidebarLayout.addItem(self.sidebarSpacer)

        self.lblVersion = QLabel(self.sidebarFrame)
        self.lblVersion.setObjectName(u"lblVersion")
        self.lblVersion.setAlignment(Qt.AlignCenter)

        self.sidebarLayout.addWidget(self.lblVersion)


        self.rootLayout.addWidget(self.sidebarFrame)

        self.contentFrame = QFrame(self.centralwidget)
        self.contentFrame.setObjectName(u"contentFrame")
        self.contentLayout = QVBoxLayout(self.contentFrame)
        self.contentLayout.setSpacing(0)
        self.contentLayout.setObjectName(u"contentLayout")
        self.contentLayout.setContentsMargins(0, 0, 0, 0)
        self.topBarFrame = QFrame(self.contentFrame)
        self.topBarFrame.setObjectName(u"topBarFrame")
        self.topBarFrame.setMinimumSize(QSize(0, 64))
        self.topBarFrame.setMaximumSize(QSize(16777215, 64))
        self.topBarLayout = QHBoxLayout(self.topBarFrame)
        self.topBarLayout.setObjectName(u"topBarLayout")
        self.topBarLayout.setContentsMargins(28, -1, 28, -1)
        self.lblPageTitle = QLabel(self.topBarFrame)
        self.lblPageTitle.setObjectName(u"lblPageTitle")

        self.topBarLayout.addWidget(self.lblPageTitle)

        self.topBarSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.topBarLayout.addItem(self.topBarSpacer)

        self.lblDateTime = QLabel(self.topBarFrame)
        self.lblDateTime.setObjectName(u"lblDateTime")

        self.topBarLayout.addWidget(self.lblDateTime)


        self.contentLayout.addWidget(self.topBarFrame)

        self.topBarSeparator = QFrame(self.contentFrame)
        self.topBarSeparator.setObjectName(u"topBarSeparator")
        self.topBarSeparator.setMinimumSize(QSize(0, 1))
        self.topBarSeparator.setMaximumSize(QSize(16777215, 1))

        self.contentLayout.addWidget(self.topBarSeparator)

        self.stackedWidget = QStackedWidget(self.contentFrame)
        self.stackedWidget.setObjectName(u"stackedWidget")

        self.contentLayout.addWidget(self.stackedWidget)


        self.rootLayout.addWidget(self.contentFrame)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Ph\u1ea7n m\u1ec1m Qu\u1ea3n l\u00fd Kho Linh ki\u1ec7n", None))
        self.lblLogoIcon.setText("")
        self.lblAppTitle.setText(QCoreApplication.translate("MainWindow", u"KHO LINH KI\u1ec6N", None))
        self.lblAppSubtitle.setText(QCoreApplication.translate("MainWindow", u"Qu\u1ea3n l\u00fd v\u1eadt t\u01b0 & linh ki\u1ec7n", None))
        self.btnNavDashboard.setText(QCoreApplication.translate("MainWindow", u"  \U0001f4ca    T\U00001ed5ng quan", None))
        self.btnNavComponents.setText(QCoreApplication.translate("MainWindow", u"  \U0001f9e9    Linh ki\U00001ec7n / V\U00001eadt t\U000001b0", None))
        self.btnNavStockIn.setText(QCoreApplication.translate("MainWindow", u"  \U0001f4e5    Nh\U00001eadp kho", None))
        self.btnNavStockOut.setText(QCoreApplication.translate("MainWindow", u"  \U0001f4e4    Xu\U00001ea5t kho", None))
        self.btnNavReceipts.setText(QCoreApplication.translate("MainWindow", u"  \U0001f9fe    L\U00001ecbch s\U00001eed phi\U00001ebfu", None))
        self.btnNavCategories.setText(QCoreApplication.translate("MainWindow", u"  \U0001f3f7\U0000fe0f    Danh m\U00001ee5c", None))
        self.btnNavBackup.setText(QCoreApplication.translate("MainWindow", u"  \U0001f4be    Sao l\U000001b0u && Kh\U000000f4i ph\U00001ee5c", None))
        self.lblVersion.setText(QCoreApplication.translate("MainWindow", u"Phi\u00ean b\u1ea3n 1.0.0", None))
        self.lblPageTitle.setText(QCoreApplication.translate("MainWindow", u"T\u1ed5ng quan", None))
        self.lblDateTime.setText(QCoreApplication.translate("MainWindow", u"--/--/---- --:--", None))
    # retranslateUi

