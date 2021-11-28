# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'tab_remote.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

from conanguide.ui.res import resources_rc

class Ui_TabRemote(object):
    def setupUi(self, TabRemote):
        if not TabRemote.objectName():
            TabRemote.setObjectName(u"TabRemote")
        TabRemote.resize(772, 652)
        self.verticalLayout = QVBoxLayout(TabRemote)
        self.verticalLayout.setSpacing(5)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame_7 = QFrame(TabRemote)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_16 = QHBoxLayout(self.frame_7)
        self.horizontalLayout_16.setSpacing(0)
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.horizontalLayout_16.setContentsMargins(0, 0, 0, 0)
        self.toolButton = QToolButton(self.frame_7)
        self.toolButton.setObjectName(u"toolButton")
        self.toolButton.setMinimumSize(QSize(25, 25))
        self.toolButton.setMaximumSize(QSize(20, 16777215))
        icon = QIcon()
        icon.addFile(u":/icon/light/add.png", QSize(), QIcon.Normal, QIcon.Off)
        self.toolButton.setIcon(icon)

        self.horizontalLayout_16.addWidget(self.toolButton)

        self.toolButton_2 = QToolButton(self.frame_7)
        self.toolButton_2.setObjectName(u"toolButton_2")
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.toolButton_2.sizePolicy().hasHeightForWidth())
        self.toolButton_2.setSizePolicy(sizePolicy)
        self.toolButton_2.setMinimumSize(QSize(25, 25))
        icon1 = QIcon()
        icon1.addFile(u":/icon/light/remove.png", QSize(), QIcon.Normal, QIcon.Off)
        self.toolButton_2.setIcon(icon1)

        self.horizontalLayout_16.addWidget(self.toolButton_2)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_16.addItem(self.horizontalSpacer_2)


        self.verticalLayout.addWidget(self.frame_7)

        self.tableViewRemoteList = QTableView(TabRemote)
        self.tableViewRemoteList.setObjectName(u"tableViewRemoteList")
        self.tableViewRemoteList.setHorizontalScrollMode(QAbstractItemView.ScrollPerPixel)

        self.verticalLayout.addWidget(self.tableViewRemoteList)


        self.retranslateUi(TabRemote)

        QMetaObject.connectSlotsByName(TabRemote)
    # setupUi

    def retranslateUi(self, TabRemote):
        TabRemote.setWindowTitle(QCoreApplication.translate("TabRemote", u"Form", None))
        self.toolButton.setText("")
        self.toolButton_2.setText("")
    # re# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'tab_remote.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

from conanguide.ui.res import resources_rc

class Ui_TabRemote(object):
    def setupUi(self, TabRemote):
        if not TabRemote.objectName():
            TabRemote.setObjectName(u"TabRemote")
        TabRemote.resize(772, 652)
        self.verticalLayout = QVBoxLayout(TabRemote)
        self.verticalLayout.setSpacing(5)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame_7 = QFrame(TabRemote)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_16 = QHBoxLayout(self.frame_7)
        self.horizontalLayout_16.setSpacing(0)
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.horizontalLayout_16.setContentsMargins(0, 0, 0, 0)
        self.toolButton = QToolButton(self.frame_7)
        self.toolButton.setObjectName(u"toolButton")
        self.toolButton.setMinimumSize(QSize(25, 25))
        self.toolButton.setMaximumSize(QSize(20, 16777215))
        icon = QIcon()
        icon.addFile(u":/icon/light/add.png", QSize(), QIcon.Normal, QIcon.Off)
        self.toolButton.setIcon(icon)

        self.horizontalLayout_16.addWidget(self.toolButton)

        self.toolButton_2 = QToolButton(self.frame_7)
        self.toolButton_2.setObjectName(u"toolButton_2")
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.toolButton_2.sizePolicy().hasHeightForWidth())
        self.toolButton_2.setSizePolicy(sizePolicy)
        self.toolButton_2.setMinimumSize(QSize(25, 25))
        icon1 = QIcon()
        icon1.addFile(u":/icon/light/remove.png", QSize(), QIcon.Normal, QIcon.Off)
        self.toolButton_2.setIcon(icon1)

        self.horizontalLayout_16.addWidget(self.toolButton_2)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_16.addItem(self.horizontalSpacer_2)


        self.verticalLayout.addWidget(self.frame_7)

        self.tableViewRemoteList = QTableView(TabRemote)
        self.tableViewRemoteList.setObjectName(u"tableViewRemoteList")
        self.tableViewRemoteList.setHorizontalScrollMode(QAbstractItemView.ScrollPerPixel)

        self.verticalLayout.addWidget(self.tableViewRemoteList)


        self.retranslateUi(TabRemote)

        QMetaObject.connectSlotsByName(TabRemote)
    # setupUi

    def retranslateUi(self, TabRemote):
        TabRemote.setWindowTitle(QCoreApplication.translate("TabRemote", u"Form", None))
        self.toolButton.setText("")
        self.toolButton_2.setText("")
    # retranslateUi

