# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'backup_page.ui'
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
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QCheckBox, QFrame,
    QHBoxLayout, QHeaderView, QLabel, QPushButton,
    QSizePolicy, QSpacerItem, QTableWidget, QTableWidgetItem,
    QVBoxLayout, QWidget)

class Ui_BackupPage(object):
    def setupUi(self, BackupPage):
        if not BackupPage.objectName():
            BackupPage.setObjectName(u"BackupPage")
        BackupPage.resize(1000, 700)
        self.mainLayout = QVBoxLayout(BackupPage)
        self.mainLayout.setSpacing(14)
        self.mainLayout.setObjectName(u"mainLayout")
        self.mainLayout.setContentsMargins(28, 18, 28, 18)
        self.actionFrame = QFrame(BackupPage)
        self.actionFrame.setObjectName(u"actionFrame")
        self.actionLayout = QHBoxLayout(self.actionFrame)
        self.actionLayout.setSpacing(14)
        self.actionLayout.setObjectName(u"actionLayout")
        self.actionLayout.setContentsMargins(18, 16, 18, 16)
        self.actionTextLayout = QVBoxLayout()
        self.actionTextLayout.setObjectName(u"actionTextLayout")
        self.lblActionTitle = QLabel(self.actionFrame)
        self.lblActionTitle.setObjectName(u"lblActionTitle")
        self.lblActionTitle.setProperty(u"objectName", u"sectionTitle")

        self.actionTextLayout.addWidget(self.lblActionTitle)

        self.lblActionDesc = QLabel(self.actionFrame)
        self.lblActionDesc.setObjectName(u"lblActionDesc")
        self.lblActionDesc.setWordWrap(True)

        self.actionTextLayout.addWidget(self.lblActionDesc)


        self.actionLayout.addLayout(self.actionTextLayout)

        self.actionSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.actionLayout.addItem(self.actionSpacer)

        self.btnBackupNow = QPushButton(self.actionFrame)
        self.btnBackupNow.setObjectName(u"btnBackupNow")
        self.btnBackupNow.setMinimumSize(QSize(190, 44))
        self.btnBackupNow.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btnBackupNow.setProperty(u"objectName", u"accentButton")

        self.actionLayout.addWidget(self.btnBackupNow)

        self.btnRestoreFromFile = QPushButton(self.actionFrame)
        self.btnRestoreFromFile.setObjectName(u"btnRestoreFromFile")
        self.btnRestoreFromFile.setMinimumSize(QSize(210, 44))
        self.btnRestoreFromFile.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.actionLayout.addWidget(self.btnRestoreFromFile)


        self.mainLayout.addWidget(self.actionFrame)

        self.autoBackupFrame = QFrame(BackupPage)
        self.autoBackupFrame.setObjectName(u"autoBackupFrame")
        self.autoBackupLayout = QHBoxLayout(self.autoBackupFrame)
        self.autoBackupLayout.setObjectName(u"autoBackupLayout")
        self.autoBackupLayout.setContentsMargins(18, 12, 18, 12)
        self.chkAutoBackup = QCheckBox(self.autoBackupFrame)
        self.chkAutoBackup.setObjectName(u"chkAutoBackup")

        self.autoBackupLayout.addWidget(self.chkAutoBackup)

        self.autoBackupSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.autoBackupLayout.addItem(self.autoBackupSpacer)

        self.lblDbPath = QLabel(self.autoBackupFrame)
        self.lblDbPath.setObjectName(u"lblDbPath")

        self.autoBackupLayout.addWidget(self.lblDbPath)


        self.mainLayout.addWidget(self.autoBackupFrame)

        self.lblHistoryTitle = QLabel(BackupPage)
        self.lblHistoryTitle.setObjectName(u"lblHistoryTitle")
        self.lblHistoryTitle.setProperty(u"objectName", u"sectionTitle")

        self.mainLayout.addWidget(self.lblHistoryTitle)

        self.tblBackups = QTableWidget(BackupPage)
        if (self.tblBackups.columnCount() < 3):
            self.tblBackups.setColumnCount(3)
        __qtablewidgetitem = QTableWidgetItem()
        self.tblBackups.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tblBackups.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tblBackups.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        self.tblBackups.setObjectName(u"tblBackups")
        self.tblBackups.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tblBackups.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.tblBackups.setAlternatingRowColors(True)
        self.tblBackups.horizontalHeader().setStretchLastSection(True)

        self.mainLayout.addWidget(self.tblBackups)

        self.historyFooterLayout = QHBoxLayout()
        self.historyFooterLayout.setObjectName(u"historyFooterLayout")
        self.historyFooterSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.historyFooterLayout.addItem(self.historyFooterSpacer)

        self.btnOpenBackupFolder = QPushButton(BackupPage)
        self.btnOpenBackupFolder.setObjectName(u"btnOpenBackupFolder")
        self.btnOpenBackupFolder.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.historyFooterLayout.addWidget(self.btnOpenBackupFolder)

        self.btnRestoreSelected = QPushButton(BackupPage)
        self.btnRestoreSelected.setObjectName(u"btnRestoreSelected")
        self.btnRestoreSelected.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.historyFooterLayout.addWidget(self.btnRestoreSelected)

        self.btnDeleteBackup = QPushButton(BackupPage)
        self.btnDeleteBackup.setObjectName(u"btnDeleteBackup")
        self.btnDeleteBackup.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btnDeleteBackup.setProperty(u"objectName", u"dangerButton")

        self.historyFooterLayout.addWidget(self.btnDeleteBackup)


        self.mainLayout.addLayout(self.historyFooterLayout)


        self.retranslateUi(BackupPage)

        QMetaObject.connectSlotsByName(BackupPage)
    # setupUi

    def retranslateUi(self, BackupPage):
        self.lblActionTitle.setText(QCoreApplication.translate("BackupPage", u"\U0001f4be  Sao l\U000001b0u & Kh\U000000f4i ph\U00001ee5c d\U00001eef li\U00001ec7u", None))
        self.lblActionDesc.setText(QCoreApplication.translate("BackupPage", u"Sao l\u01b0u to\u00e0n b\u1ed9 d\u1eef li\u1ec7u kho sang m\u1ed9t file .db ri\u00eang, ho\u1eb7c kh\u00f4i ph\u1ee5c l\u1ea1i t\u1eeb b\u1ea3n sao l\u01b0u tr\u01b0\u1edbc \u0111\u00f3 khi c\u1ea7n thi\u1ebft.", None))
        self.btnBackupNow.setText(QCoreApplication.translate("BackupPage", u"\U0001f4be  Sao l\U000001b0u ngay", None))
        self.btnRestoreFromFile.setText(QCoreApplication.translate("BackupPage", u"\U0001f4c2  Kh\U000000f4i ph\U00001ee5c t\U00001eeb file...", None))
        self.chkAutoBackup.setText(QCoreApplication.translate("BackupPage", u"T\u1ef1 \u0111\u1ed9ng sao l\u01b0u khi m\u1edf ph\u1ea7n m\u1ec1m (m\u1ed7i ng\u00e0y m\u1ed9t l\u1ea7n)", None))
        self.lblDbPath.setText(QCoreApplication.translate("BackupPage", u"\u0110\u01b0\u1eddng d\u1eabn CSDL: -", None))
        self.lblHistoryTitle.setText(QCoreApplication.translate("BackupPage", u"L\u1ecbch s\u1eed c\u00e1c b\u1ea3n sao l\u01b0u", None))
        ___qtablewidgetitem = self.tblBackups.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("BackupPage", u"T\u00ean file sao l\u01b0u", None))
        ___qtablewidgetitem1 = self.tblBackups.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("BackupPage", u"Th\u1eddi gian t\u1ea1o", None))
        ___qtablewidgetitem2 = self.tblBackups.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("BackupPage", u"K\u00edch th\u01b0\u1edbc", None))
        self.btnOpenBackupFolder.setText(QCoreApplication.translate("BackupPage", u"\U0001f4c1  M\U00001edf th\U000001b0 m\U00001ee5c sao l\U000001b0u", None))
        self.btnRestoreSelected.setText(QCoreApplication.translate("BackupPage", u"\u267b  Kh\u00f4i ph\u1ee5c b\u1ea3n \u0111\u00e3 ch\u1ecdn", None))
        self.btnDeleteBackup.setText(QCoreApplication.translate("BackupPage", u"\U0001f5d1  X\U000000f3a b\U00001ea3n sao l\U000001b0u", None))
        pass
    # retranslateUi

