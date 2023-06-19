# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_gui.ui'
##
## Created by: Qt User Interface Compiler version 6.2.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QAbstractScrollArea, QApplication, QCheckBox, QFrame,
    QGridLayout, QHBoxLayout, QHeaderView, QLabel,
    QLayout, QMainWindow, QMenu, QMenuBar,
    QPlainTextEdit, QProgressBar, QPushButton, QScrollArea,
    QSizePolicy, QSpacerItem, QTabWidget, QTableWidget,
    QTableWidgetItem, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.setWindowModality(Qt.NonModal)
        MainWindow.resize(777, 720)
        sizePolicy = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QSize(746, 720))
        MainWindow.setAcceptDrops(False)
        MainWindow.setAutoFillBackground(False)
        self.actionRead_partition_s = QAction(MainWindow)
        self.actionRead_partition_s.setObjectName(u"actionRead_partition_s")
        self.actionRead_full_flash = QAction(MainWindow)
        self.actionRead_full_flash.setObjectName(u"actionRead_full_flash")
        self.actionRead_offset = QAction(MainWindow)
        self.actionRead_offset.setObjectName(u"actionRead_offset")
        self.actionWrite_partition_s = QAction(MainWindow)
        self.actionWrite_partition_s.setObjectName(u"actionWrite_partition_s")
        self.actionWrite_full_flash = QAction(MainWindow)
        self.actionWrite_full_flash.setObjectName(u"actionWrite_full_flash")
        self.actionWrite_at_offset = QAction(MainWindow)
        self.actionWrite_at_offset.setObjectName(u"actionWrite_at_offset")
        self.actionErase_partitions_s = QAction(MainWindow)
        self.actionErase_partitions_s.setObjectName(u"actionErase_partitions_s")
        self.actionErase_at_offset = QAction(MainWindow)
        self.actionErase_at_offset.setObjectName(u"actionErase_at_offset")
        self.actionRead_RPMB = QAction(MainWindow)
        self.actionRead_RPMB.setObjectName(u"actionRead_RPMB")
        self.actionWrite_RPMB = QAction(MainWindow)
        self.actionWrite_RPMB.setObjectName(u"actionWrite_RPMB")
        self.actionRead_preloader = QAction(MainWindow)
        self.actionRead_preloader.setObjectName(u"actionRead_preloader")
        self.actionGenerate_RPMB_keys = QAction(MainWindow)
        self.actionGenerate_RPMB_keys.setObjectName(u"actionGenerate_RPMB_keys")
        self.actionRead_boot2 = QAction(MainWindow)
        self.actionRead_boot2.setObjectName(u"actionRead_boot2")
        self.actionWrite_preloader = QAction(MainWindow)
        self.actionWrite_preloader.setObjectName(u"actionWrite_preloader")
        self.actionWrite_boot2 = QAction(MainWindow)
        self.actionWrite_boot2.setObjectName(u"actionWrite_boot2")
        self.actionUnlock_device = QAction(MainWindow)
        self.actionUnlock_device.setObjectName(u"actionUnlock_device")
        self.actionLock_device = QAction(MainWindow)
        self.actionLock_device.setObjectName(u"actionLock_device")
        self.action_Quit = QAction(MainWindow)
        self.action_Quit.setObjectName(u"action_Quit")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout_8 = QGridLayout(self.centralwidget)
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.connectInfo = QWidget(self.centralwidget)
        self.connectInfo.setObjectName(u"connectInfo")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.connectInfo.sizePolicy().hasHeightForWidth())
        self.connectInfo.setSizePolicy(sizePolicy1)
        self.connectInfo.setMinimumSize(QSize(0, 0))
        self.connectInfo.setMaximumSize(QSize(16777215, 0))
        self.verticalLayout_6 = QVBoxLayout(self.connectInfo)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalSpacer_2 = QSpacerItem(5, 20, QSizePolicy.Minimum, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_2)

        self.horizontalSpacer_7 = QSpacerItem(9, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_7)

        self.initStepsImage = QLabel(self.connectInfo)
        self.initStepsImage.setObjectName(u"initStepsImage")
        self.initStepsImage.setMinimumSize(QSize(685, 330))
        self.initStepsImage.setMaximumSize(QSize(685, 330))
        self.initStepsImage.setFrameShape(QFrame.NoFrame)
        self.initStepsImage.setPixmap(QPixmap(u"images/initsteps.png"))
        self.initStepsImage.setScaledContents(True)
        self.initStepsImage.setAlignment(Qt.AlignHCenter|Qt.AlignTop)
        self.initStepsImage.setWordWrap(False)
        self.initStepsImage.setMargin(0)

        self.horizontalLayout_4.addWidget(self.initStepsImage)

        self.horizontalSpacer = QSpacerItem(5, 18, QSizePolicy.Minimum, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer)


        self.verticalLayout_6.addLayout(self.horizontalLayout_4)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalSpacer_6 = QSpacerItem(10, 0, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_6)

        self.label_2 = QLabel(self.connectInfo)
        self.label_2.setObjectName(u"label_2")
        sizePolicy2 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy2)
        self.label_2.setMinimumSize(QSize(195, 0))
        self.label_2.setMaximumSize(QSize(195, 16777215))
        self.label_2.setAlignment(Qt.AlignHCenter|Qt.AlignTop)
        self.label_2.setWordWrap(True)
        self.label_2.setMargin(5)

        self.horizontalLayout_3.addWidget(self.label_2)

        self.horizontalSpacer_3 = QSpacerItem(50, 0, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_3)

        self.label_3 = QLabel(self.connectInfo)
        self.label_3.setObjectName(u"label_3")
        sizePolicy2.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy2)
        self.label_3.setMinimumSize(QSize(195, 10))
        self.label_3.setMaximumSize(QSize(195, 16777215))
        self.label_3.setAlignment(Qt.AlignHCenter|Qt.AlignTop)
        self.label_3.setWordWrap(True)
        self.label_3.setMargin(5)

        self.horizontalLayout_3.addWidget(self.label_3)

        self.horizontalSpacer_4 = QSpacerItem(50, 0, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_4)

        self.label_4 = QLabel(self.connectInfo)
        self.label_4.setObjectName(u"label_4")
        sizePolicy2.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy2)
        self.label_4.setMinimumSize(QSize(195, 0))
        self.label_4.setMaximumSize(QSize(195, 16777215))
        self.label_4.setScaledContents(False)
        self.label_4.setAlignment(Qt.AlignHCenter|Qt.AlignTop)
        self.label_4.setWordWrap(True)
        self.label_4.setMargin(5)

        self.horizontalLayout_3.addWidget(self.label_4)

        self.horizontalSpacer_5 = QSpacerItem(10, 0, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_5)


        self.verticalLayout_6.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalSpacer_showdebug = QSpacerItem(50, 0, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_showdebug)

        self.showdebugbtn = QPushButton(self.connectInfo)
        self.showdebugbtn.setObjectName(u"showdebugbtn")

        self.horizontalLayout_5.addWidget(self.showdebugbtn)


        self.verticalLayout_6.addLayout(self.horizontalLayout_5)


        self.gridLayout_8.addWidget(self.connectInfo, 2, 0, 1, 1)

        self.line_2 = QFrame(self.centralwidget)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFrameShape(QFrame.HLine)
        self.line_2.setFrameShadow(QFrame.Sunken)

        self.gridLayout_8.addWidget(self.line_2, 1, 0, 1, 1)

        self.topInfo = QHBoxLayout()
        self.topInfo.setObjectName(u"topInfo")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.title = QLabel(self.centralwidget)
        self.title.setObjectName(u"title")
        self.title.setEnabled(True)
        sizePolicy3 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.title.sizePolicy().hasHeightForWidth())
        self.title.setSizePolicy(sizePolicy3)
        self.title.setMinimumSize(QSize(0, 24))
        self.title.setMaximumSize(QSize(16777215, 20))
        font = QFont()
        font.setFamilies([u"Arial"])
        font.setPointSize(18)
        self.title.setFont(font)
        self.title.setLineWidth(0)
        self.title.setTextFormat(Qt.AutoText)
        self.title.setScaledContents(False)
        self.title.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.title.setWordWrap(False)
        self.title.setIndent(0)

        self.verticalLayout.addWidget(self.title)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.logoPic = QLabel(self.centralwidget)
        self.logoPic.setObjectName(u"logoPic")
        sizePolicy3.setHeightForWidth(self.logoPic.sizePolicy().hasHeightForWidth())
        self.logoPic.setSizePolicy(sizePolicy3)
        self.logoPic.setMinimumSize(QSize(128, 128))
        self.logoPic.setMaximumSize(QSize(128, 128))
        self.logoPic.setPixmap(QPixmap(u"images/logo_256.png"))
        self.logoPic.setScaledContents(True)
        self.logoPic.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)

        self.horizontalLayout.addWidget(self.logoPic)

        self.copyrightInfo = QLabel(self.centralwidget)
        self.copyrightInfo.setObjectName(u"copyrightInfo")
        sizePolicy4 = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.Minimum)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.copyrightInfo.sizePolicy().hasHeightForWidth())
        self.copyrightInfo.setSizePolicy(sizePolicy4)

        self.horizontalLayout.addWidget(self.copyrightInfo)


        self.verticalLayout.addLayout(self.horizontalLayout)


        self.topInfo.addLayout(self.verticalLayout)

        self.verticalLayout_7 = QVBoxLayout()
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.phoneInfoTextbox = QLabel(self.centralwidget)
        self.phoneInfoTextbox.setObjectName(u"phoneInfoTextbox")
        sizePolicy5 = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.Expanding)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.phoneInfoTextbox.sizePolicy().hasHeightForWidth())
        self.phoneInfoTextbox.setSizePolicy(sizePolicy5)
        self.phoneInfoTextbox.setAlignment(Qt.AlignRight|Qt.AlignTop|Qt.AlignTrailing)
        self.phoneInfoTextbox.setWordWrap(True)

        self.verticalLayout_7.addWidget(self.phoneInfoTextbox)

        self.phoneDebugInfoTextbox = QLabel(self.centralwidget)
        self.phoneDebugInfoTextbox.setObjectName(u"phoneDebugInfoTextbox")
        self.phoneDebugInfoTextbox.setStyleSheet(u"color:#888;")
        self.phoneDebugInfoTextbox.setTextFormat(Qt.PlainText)
        self.phoneDebugInfoTextbox.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.verticalLayout_7.addWidget(self.phoneDebugInfoTextbox)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalSpacer_8 = QSpacerItem(40, 1, QSizePolicy.MinimumExpanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_8)

        self.consettingsbtn = QPushButton(self.centralwidget)
        self.consettingsbtn.setObjectName(u"consettingsbtn")
        self.consettingsbtn.setMaximumSize(QSize(200, 16777215))

        self.horizontalLayout_2.addWidget(self.consettingsbtn)


        self.verticalLayout_7.addLayout(self.horizontalLayout_2)

        self.verticalSpacer_5 = QSpacerItem(20, 2, QSizePolicy.Minimum, QSizePolicy.Maximum)

        self.verticalLayout_7.addItem(self.verticalSpacer_5)

        self.verticalSpacer_6 = QSpacerItem(20, 30, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout_7.addItem(self.verticalSpacer_6)


        self.topInfo.addLayout(self.verticalLayout_7)

        self.widget_3 = QWidget(self.centralwidget)
        self.widget_3.setObjectName(u"widget_3")
        sizePolicy3.setHeightForWidth(self.widget_3.sizePolicy().hasHeightForWidth())
        self.widget_3.setSizePolicy(sizePolicy3)
        self.widget_3.setMinimumSize(QSize(87, 166))
        self.pic = QLabel(self.widget_3)
        self.pic.setObjectName(u"pic")
        self.pic.setGeometry(QRect(0, 0, 87, 128))
        sizePolicy6 = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.Fixed)
        sizePolicy6.setHorizontalStretch(0)
        sizePolicy6.setVerticalStretch(0)
        sizePolicy6.setHeightForWidth(self.pic.sizePolicy().hasHeightForWidth())
        self.pic.setSizePolicy(sizePolicy6)
        self.pic.setMinimumSize(QSize(50, 128))
        self.pic.setMaximumSize(QSize(87, 128))
        self.pic.setPixmap(QPixmap(u"images/phone_notfound.png"))
        self.pic.setScaledContents(True)
        self.pic.setAlignment(Qt.AlignCenter)
        self.pic.setWordWrap(False)
        self.spinner_pic = QLabel(self.widget_3)
        self.spinner_pic.setObjectName(u"spinner_pic")
        self.spinner_pic.setGeometry(QRect(18, 40, 51, 51))
        sizePolicy3.setHeightForWidth(self.spinner_pic.sizePolicy().hasHeightForWidth())
        self.spinner_pic.setSizePolicy(sizePolicy3)
        self.spinner_pic.setPixmap(QPixmap(u"images/phone_loading.png"))
        self.spinner_pic.setScaledContents(True)
        self.spinner_pic.setAlignment(Qt.AlignCenter)

        self.topInfo.addWidget(self.widget_3)


        self.gridLayout_8.addLayout(self.topInfo, 0, 0, 1, 1)

        self.Main = QVBoxLayout()
        self.Main.setSpacing(0)
        self.Main.setObjectName(u"Main")
        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setEnabled(True)
        sizePolicy.setHeightForWidth(self.tabWidget.sizePolicy().hasHeightForWidth())
        self.tabWidget.setSizePolicy(sizePolicy)
        self.tabWidget.setMinimumSize(QSize(650, 340))
        self.tabWidget.setMouseTracking(False)
        self.tabWidget.setAutoFillBackground(False)
        self.readtab = QWidget()
        self.readtab.setObjectName(u"readtab")
        self.gridLayout_7 = QGridLayout(self.readtab)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.readDumpGPTCheckbox = QCheckBox(self.readtab)
        self.readDumpGPTCheckbox.setObjectName(u"readDumpGPTCheckbox")

        self.gridLayout_7.addWidget(self.readDumpGPTCheckbox, 4, 1, 1, 1)

        self.readtitle = QLabel(self.readtab)
        self.readtitle.setObjectName(u"readtitle")
        sizePolicy1.setHeightForWidth(self.readtitle.sizePolicy().hasHeightForWidth())
        self.readtitle.setSizePolicy(sizePolicy1)
        self.readtitle.setMinimumSize(QSize(0, 20))
        self.readtitle.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)

        self.gridLayout_7.addWidget(self.readtitle, 0, 0, 1, 1)

        self.readpartitionList = QScrollArea(self.readtab)
        self.readpartitionList.setObjectName(u"readpartitionList")
        sizePolicy7 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.MinimumExpanding)
        sizePolicy7.setHorizontalStretch(0)
        sizePolicy7.setVerticalStretch(0)
        sizePolicy7.setHeightForWidth(self.readpartitionList.sizePolicy().hasHeightForWidth())
        self.readpartitionList.setSizePolicy(sizePolicy7)
        self.readpartitionList.setMinimumSize(QSize(0, 280))
        self.readpartitionList.setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.readpartitionList.setHorizontalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.readpartitionList.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContentsOnFirstShow)
        self.readpartitionList.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 573, 278))
        self.readpartitionList.setWidget(self.scrollAreaWidgetContents)

        self.gridLayout_7.addWidget(self.readpartitionList, 2, 0, 1, 1)

        self.readpartitionsbtn = QPushButton(self.readtab)
        self.readpartitionsbtn.setObjectName(u"readpartitionsbtn")

        self.gridLayout_7.addWidget(self.readpartitionsbtn, 0, 1, 1, 1)

        self.readselectallcheckbox = QCheckBox(self.readtab)
        self.readselectallcheckbox.setObjectName(u"readselectallcheckbox")

        self.gridLayout_7.addWidget(self.readselectallcheckbox, 1, 0, 1, 1)

        self.tabWidget.addTab(self.readtab, "")
        self.writetab = QWidget()
        self.writetab.setObjectName(u"writetab")
        self.gridLayout_6 = QGridLayout(self.writetab)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.writetitle = QLabel(self.writetab)
        self.writetitle.setObjectName(u"writetitle")
        sizePolicy1.setHeightForWidth(self.writetitle.sizePolicy().hasHeightForWidth())
        self.writetitle.setSizePolicy(sizePolicy1)
        self.writetitle.setMinimumSize(QSize(0, 20))
        self.writetitle.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)

        self.gridLayout_6.addWidget(self.writetitle, 0, 0, 1, 1)

        self.writepartitionList = QScrollArea(self.writetab)
        self.writepartitionList.setObjectName(u"writepartitionList")
        sizePolicy5.setHeightForWidth(self.writepartitionList.sizePolicy().hasHeightForWidth())
        self.writepartitionList.setSizePolicy(sizePolicy5)
        self.writepartitionList.setMinimumSize(QSize(0, 280))
        self.writepartitionList.setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.writepartitionList.setHorizontalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.writepartitionList.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContentsOnFirstShow)
        self.writepartitionList.setWidgetResizable(True)
        self.scrollAreaWidgetContents_2 = QWidget()
        self.scrollAreaWidgetContents_2.setObjectName(u"scrollAreaWidgetContents_2")
        self.scrollAreaWidgetContents_2.setGeometry(QRect(0, 0, 98, 278))
        self.writepartitionList.setWidget(self.scrollAreaWidgetContents_2)

        self.gridLayout_6.addWidget(self.writepartitionList, 1, 0, 2, 1)

        self.writepartbtn = QPushButton(self.writetab)
        self.writepartbtn.setObjectName(u"writepartbtn")

        self.gridLayout_6.addWidget(self.writepartbtn, 0, 1, 1, 1)

        self.writeselectfromdir = QPushButton(self.writetab)
        self.writeselectfromdir.setObjectName(u"writeselectfromdir")

        self.gridLayout_6.addWidget(self.writeselectfromdir, 2, 1, 1, 1)

        self.tabWidget.addTab(self.writetab, "")
        self.erasetab = QWidget()
        self.erasetab.setObjectName(u"erasetab")
        self.gridLayout_5 = QGridLayout(self.erasetab)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.erasepartitionList = QScrollArea(self.erasetab)
        self.erasepartitionList.setObjectName(u"erasepartitionList")
        sizePolicy5.setHeightForWidth(self.erasepartitionList.sizePolicy().hasHeightForWidth())
        self.erasepartitionList.setSizePolicy(sizePolicy5)
        self.erasepartitionList.setMinimumSize(QSize(0, 280))
        self.erasepartitionList.setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.erasepartitionList.setHorizontalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.erasepartitionList.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContentsOnFirstShow)
        self.erasepartitionList.setWidgetResizable(True)
        self.scrollAreaWidgetContents_3 = QWidget()
        self.scrollAreaWidgetContents_3.setObjectName(u"scrollAreaWidgetContents_3")
        self.scrollAreaWidgetContents_3.setGeometry(QRect(0, 0, 98, 278))
        self.erasepartitionList.setWidget(self.scrollAreaWidgetContents_3)

        self.gridLayout_5.addWidget(self.erasepartitionList, 2, 0, 2, 1)

        self.erasetitle = QLabel(self.erasetab)
        self.erasetitle.setObjectName(u"erasetitle")
        sizePolicy1.setHeightForWidth(self.erasetitle.sizePolicy().hasHeightForWidth())
        self.erasetitle.setSizePolicy(sizePolicy1)
        self.erasetitle.setMinimumSize(QSize(0, 20))
        self.erasetitle.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)

        self.gridLayout_5.addWidget(self.erasetitle, 0, 0, 1, 1)

        self.erasepartitionsbtn = QPushButton(self.erasetab)
        self.erasepartitionsbtn.setObjectName(u"erasepartitionsbtn")

        self.gridLayout_5.addWidget(self.erasepartitionsbtn, 0, 1, 1, 1)

        self.eraseselectallpartitionscheckbox = QCheckBox(self.erasetab)
        self.eraseselectallpartitionscheckbox.setObjectName(u"eraseselectallpartitionscheckbox")

        self.gridLayout_5.addWidget(self.eraseselectallpartitionscheckbox, 1, 0, 1, 1)

        self.tabWidget.addTab(self.erasetab, "")
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.gridLayout_4 = QGridLayout(self.tab)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.readflashbtn = QPushButton(self.tab)
        self.readflashbtn.setObjectName(u"readflashbtn")

        self.verticalLayout_2.addWidget(self.readflashbtn)

        self.readpreloaderbtn = QPushButton(self.tab)
        self.readpreloaderbtn.setObjectName(u"readpreloaderbtn")

        self.verticalLayout_2.addWidget(self.readpreloaderbtn)

        self.readboot2btn = QPushButton(self.tab)
        self.readboot2btn.setObjectName(u"readboot2btn")

        self.verticalLayout_2.addWidget(self.readboot2btn)

        self.readrpmbbtn = QPushButton(self.tab)
        self.readrpmbbtn.setObjectName(u"readrpmbbtn")

        self.verticalLayout_2.addWidget(self.readrpmbbtn)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer)


        self.gridLayout_4.addLayout(self.verticalLayout_2, 0, 0, 2, 1)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.writeflashbtn = QPushButton(self.tab)
        self.writeflashbtn.setObjectName(u"writeflashbtn")

        self.verticalLayout_3.addWidget(self.writeflashbtn)

        self.writepreloaderbtn = QPushButton(self.tab)
        self.writepreloaderbtn.setObjectName(u"writepreloaderbtn")

        self.verticalLayout_3.addWidget(self.writepreloaderbtn)

        self.writeboot2btn = QPushButton(self.tab)
        self.writeboot2btn.setObjectName(u"writeboot2btn")

        self.verticalLayout_3.addWidget(self.writeboot2btn)

        self.writerpmbbtn = QPushButton(self.tab)
        self.writerpmbbtn.setObjectName(u"writerpmbbtn")

        self.verticalLayout_3.addWidget(self.writerpmbbtn)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer_2)


        self.gridLayout_4.addLayout(self.verticalLayout_3, 0, 1, 2, 1)

        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.erasepreloaderbtn = QPushButton(self.tab)
        self.erasepreloaderbtn.setObjectName(u"erasepreloaderbtn")

        self.verticalLayout_4.addWidget(self.erasepreloaderbtn)

        self.eraseboot2btn = QPushButton(self.tab)
        self.eraseboot2btn.setObjectName(u"eraseboot2btn")

        self.verticalLayout_4.addWidget(self.eraseboot2btn)

        self.eraserpmbbtn = QPushButton(self.tab)
        self.eraserpmbbtn.setObjectName(u"eraserpmbbtn")

        self.verticalLayout_4.addWidget(self.eraserpmbbtn)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_4.addItem(self.verticalSpacer_3)


        self.gridLayout_4.addLayout(self.verticalLayout_4, 0, 2, 1, 1)

        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.lockbutton = QPushButton(self.tab)
        self.lockbutton.setObjectName(u"lockbutton")

        self.verticalLayout_5.addWidget(self.lockbutton)

        self.unlockbutton = QPushButton(self.tab)
        self.unlockbutton.setObjectName(u"unlockbutton")

        self.verticalLayout_5.addWidget(self.unlockbutton)


        self.gridLayout_4.addLayout(self.verticalLayout_5, 1, 2, 1, 1)

        self.tabWidget.addTab(self.tab, "")
        self.keytab = QWidget()
        self.keytab.setObjectName(u"keytab")
        self.gridLayout_2 = QGridLayout(self.keytab)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.keytable = QTableWidget(self.keytab)
        if (self.keytable.columnCount() < 2):
            self.keytable.setColumnCount(2)
        __qtablewidgetitem = QTableWidgetItem()
        self.keytable.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.keytable.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        if (self.keytable.rowCount() < 7):
            self.keytable.setRowCount(7)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.keytable.setVerticalHeaderItem(0, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.keytable.setVerticalHeaderItem(1, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.keytable.setVerticalHeaderItem(2, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.keytable.setVerticalHeaderItem(3, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.keytable.setVerticalHeaderItem(4, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.keytable.setVerticalHeaderItem(5, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.keytable.setVerticalHeaderItem(6, __qtablewidgetitem8)
        self.keytable.setObjectName(u"keytable")
        self.keytable.setEnabled(True)
        self.keytable.setSortingEnabled(True)
        self.keytable.setWordWrap(False)
        self.keytable.horizontalHeader().setProperty("showSortIndicator", True)
        self.keytable.horizontalHeader().setStretchLastSection(True)
        self.keytable.verticalHeader().setVisible(False)
        self.keytable.verticalHeader().setCascadingSectionResizes(False)
        self.keytable.verticalHeader().setStretchLastSection(False)

        self.gridLayout_2.addWidget(self.keytable, 1, 0, 1, 1)

        self.keystatuslabel = QLabel(self.keytab)
        self.keystatuslabel.setObjectName(u"keystatuslabel")

        self.gridLayout_2.addWidget(self.keystatuslabel, 2, 0, 1, 1)

        self.generatekeybtn = QPushButton(self.keytab)
        self.generatekeybtn.setObjectName(u"generatekeybtn")

        self.gridLayout_2.addWidget(self.generatekeybtn, 3, 0, 1, 1)

        self.tabWidget.addTab(self.keytab, "")
        self.debugtab = QWidget()
        self.debugtab.setObjectName(u"debugtab")
        self.gridLayout_3 = QGridLayout(self.debugtab)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.widget_2 = QWidget(self.debugtab)
        self.widget_2.setObjectName(u"widget_2")

        self.gridLayout.addWidget(self.widget_2, 1, 0, 1, 1)

        self.logBox = QPlainTextEdit(self.debugtab)
        self.logBox.setObjectName(u"logBox")
        sizePolicy8 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy8.setHorizontalStretch(0)
        sizePolicy8.setVerticalStretch(0)
        sizePolicy8.setHeightForWidth(self.logBox.sizePolicy().hasHeightForWidth())
        self.logBox.setSizePolicy(sizePolicy8)
        self.logBox.setMinimumSize(QSize(722, 0))
        self.logBox.setStyleSheet(u"")
        self.logBox.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.logBox.setReadOnly(True)
        self.logBox.setProperty("hidden", False)

        self.gridLayout.addWidget(self.logBox, 0, 0, 1, 2)


        self.gridLayout_3.addLayout(self.gridLayout, 0, 0, 1, 1)

        self.tabWidget.addTab(self.debugtab, "")

        self.Main.addWidget(self.tabWidget)

        self.verticalSpacer_4 = QSpacerItem(20, 15, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.Main.addItem(self.verticalSpacer_4)

        self.partProgressText = QLabel(self.centralwidget)
        self.partProgressText.setObjectName(u"partProgressText")

        self.Main.addWidget(self.partProgressText)

        self.partProgress = QProgressBar(self.centralwidget)
        self.partProgress.setObjectName(u"partProgress")
        self.partProgress.setValue(0)

        self.Main.addWidget(self.partProgress)

        self.fullProgressText = QLabel(self.centralwidget)
        self.fullProgressText.setObjectName(u"fullProgressText")

        self.Main.addWidget(self.fullProgressText)

        self.fullProgress = QProgressBar(self.centralwidget)
        self.fullProgress.setObjectName(u"fullProgress")
        self.fullProgress.setValue(0)

        self.Main.addWidget(self.fullProgress)


        self.gridLayout_8.addLayout(self.Main, 3, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.line_2.raise_()
        self.connectInfo.raise_()
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 777, 24))
        self.menuFile = QMenu(self.menubar)
        self.menuFile.setObjectName(u"menuFile")
        MainWindow.setMenuBar(self.menubar)

        self.menubar.addAction(self.menuFile.menuAction())
        self.menuFile.addAction(self.action_Quit)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"App v2.0", None))
        self.actionRead_partition_s.setText(QCoreApplication.translate("MainWindow", u"Quit", None))
        self.actionRead_full_flash.setText(QCoreApplication.translate("MainWindow", u"Read full flash", None))
        self.actionRead_offset.setText(QCoreApplication.translate("MainWindow", u"Read at offset", None))
        self.actionWrite_partition_s.setText(QCoreApplication.translate("MainWindow", u"Write partition(s)", None))
        self.actionWrite_full_flash.setText(QCoreApplication.translate("MainWindow", u"Write full flash", None))
        self.actionWrite_at_offset.setText(QCoreApplication.translate("MainWindow", u"Write at offset", None))
        self.actionErase_partitions_s.setText(QCoreApplication.translate("MainWindow", u"Erase partitions(s)", None))
        self.actionErase_at_offset.setText(QCoreApplication.translate("MainWindow", u"Erase at offset", None))
        self.actionRead_RPMB.setText(QCoreApplication.translate("MainWindow", u"Read RPMB", None))
        self.actionWrite_RPMB.setText(QCoreApplication.translate("MainWindow", u"Write RPMB", None))
        self.actionRead_preloader.setText(QCoreApplication.translate("MainWindow", u"Read preloader", None))
        self.actionGenerate_RPMB_keys.setText(QCoreApplication.translate("MainWindow", u"Generate RPMB keys", None))
        self.actionRead_boot2.setText(QCoreApplication.translate("MainWindow", u"Read boot2", None))
        self.actionWrite_preloader.setText(QCoreApplication.translate("MainWindow", u"Write preloader", None))
        self.actionWrite_boot2.setText(QCoreApplication.translate("MainWindow", u"Write boot2", None))
        self.actionUnlock_device.setText(QCoreApplication.translate("MainWindow", u"Unlock / Lock", None))
        self.actionLock_device.setText(QCoreApplication.translate("MainWindow", u"Lock device", None))
        self.action_Quit.setText(QCoreApplication.translate("MainWindow", u"&Quit", None))
        self.initStepsImage.setText("")
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-weight:600;\">Step 1:</span></p><p>Power off the phone</p></body></html>", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-weight:600;\">Step 2:</span></p><p>Connect the USB cable, hold both volume buttons if needed</p></body></html>", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>No connection? Try shorting the test point to ground</p></body></html>", None))
        self.showdebugbtn.setText(QCoreApplication.translate("MainWindow", u"Show Debug Log", None))
        self.title.setText(QCoreApplication.translate("MainWindow", u"App v2.0", None))
        self.logoPic.setText("")
        self.copyrightInfo.setText(QCoreApplication.translate("MainWindow", u"<b>Made by:</b> Bjoern Kerler<br/><b>Gui by:</b> Geert-Jan Kreileman<br/><br/><b>Credits:</b><br/>kamakiri [xyzz]<br/>linecode exploit [chimera]<br/>Chaosmaster<br/>and all contributers</p>", None))
        self.phoneInfoTextbox.setText(QCoreApplication.translate("MainWindow", u"No phone detected.", None))
        self.phoneDebugInfoTextbox.setText("")
        self.consettingsbtn.setText(QCoreApplication.translate("MainWindow", u"Connection settings", None))
        self.pic.setText("")
        self.spinner_pic.setText("")
        self.readDumpGPTCheckbox.setText(QCoreApplication.translate("MainWindow", u"Dump GPT", None))
        self.readtitle.setText(QCoreApplication.translate("MainWindow", u"Select partitions to read", None))
        self.readpartitionsbtn.setText(QCoreApplication.translate("MainWindow", u"Read partition(s)", None))
        self.readselectallcheckbox.setText(QCoreApplication.translate("MainWindow", u"Select all partitions", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.readtab), QCoreApplication.translate("MainWindow", u"Read partition(s)", None))
        self.writetitle.setText(QCoreApplication.translate("MainWindow", u"Select partitions to write", None))
        self.writepartbtn.setText(QCoreApplication.translate("MainWindow", u"Write partition(s)", None))
        self.writeselectfromdir.setText(QCoreApplication.translate("MainWindow", u"Select from directory", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.writetab), QCoreApplication.translate("MainWindow", u"Write partition(s)", None))
        self.erasetitle.setText(QCoreApplication.translate("MainWindow", u"Select partitions to erase", None))
        self.erasepartitionsbtn.setText(QCoreApplication.translate("MainWindow", u"Erase partition(s)", None))
        self.eraseselectallpartitionscheckbox.setText(QCoreApplication.translate("MainWindow", u"Select all partitions", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.erasetab), QCoreApplication.translate("MainWindow", u"Erase partition(s)", None))
        self.readflashbtn.setText(QCoreApplication.translate("MainWindow", u"Read flash", None))
        self.readpreloaderbtn.setText(QCoreApplication.translate("MainWindow", u"Read preloader", None))
        self.readboot2btn.setText(QCoreApplication.translate("MainWindow", u"Read boot2", None))
        self.readrpmbbtn.setText(QCoreApplication.translate("MainWindow", u"Read RPMB", None))
        self.writeflashbtn.setText(QCoreApplication.translate("MainWindow", u"Write flash", None))
        self.writepreloaderbtn.setText(QCoreApplication.translate("MainWindow", u"Write preloader", None))
        self.writeboot2btn.setText(QCoreApplication.translate("MainWindow", u"Write boot2", None))
        self.writerpmbbtn.setText(QCoreApplication.translate("MainWindow", u"Write RPMB", None))
        self.erasepreloaderbtn.setText(QCoreApplication.translate("MainWindow", u"Erase preloader", None))
        self.eraseboot2btn.setText(QCoreApplication.translate("MainWindow", u"Erase boot2", None))
        self.eraserpmbbtn.setText(QCoreApplication.translate("MainWindow", u"Erase RPMB", None))
        self.lockbutton.setText(QCoreApplication.translate("MainWindow", u"Lock bootloader", None))
        self.unlockbutton.setText(QCoreApplication.translate("MainWindow", u"Unlock bootloader", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("MainWindow", u"Flash Tools", None))
        ___qtablewidgetitem = self.keytable.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"Type", None));
        ___qtablewidgetitem1 = self.keytable.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"Value", None));
        ___qtablewidgetitem2 = self.keytable.verticalHeaderItem(0)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"Neue Zeile", None));
        ___qtablewidgetitem3 = self.keytable.verticalHeaderItem(1)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"Neue Zeile", None));
        ___qtablewidgetitem4 = self.keytable.verticalHeaderItem(2)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"Neue Zeile", None));
        ___qtablewidgetitem5 = self.keytable.verticalHeaderItem(3)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"Neue Zeile", None));
        ___qtablewidgetitem6 = self.keytable.verticalHeaderItem(4)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"Neue Zeile", None));
        ___qtablewidgetitem7 = self.keytable.verticalHeaderItem(5)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("MainWindow", u"Neue Zeile", None));
        ___qtablewidgetitem8 = self.keytable.verticalHeaderItem(6)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("MainWindow", u"Neue Zeile", None));
        self.keystatuslabel.setText(QCoreApplication.translate("MainWindow", u"Ready.", None))
        self.generatekeybtn.setText(QCoreApplication.translate("MainWindow", u"Generate Keys", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.keytab), QCoreApplication.translate("MainWindow", u"Keys", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.debugtab), QCoreApplication.translate("MainWindow", u"Debug Log", None))
        self.partProgressText.setText("")
        self.fullProgressText.setText("")
        self.menuFile.setTitle(QCoreApplication.translate("MainWindow", u"&File", None))
    # retranslateUi

