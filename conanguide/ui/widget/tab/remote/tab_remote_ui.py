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
        TabRemote.resize(971, 652)
        self.verticalLayout_2 = QVBoxLayout(TabRemote)
        self.verticalLayout_2.setSpacing(2)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frame_7 = QFrame(TabRemote)
        self.frame_7.setObjectName(u"frame_7")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_7.sizePolicy().hasHeightForWidth())
        self.frame_7.setSizePolicy(sizePolicy)
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_16 = QHBoxLayout(self.frame_7)
        self.horizontalLayout_16.setSpacing(0)
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.horizontalLayout_16.setContentsMargins(0, 0, 0, 0)
        self.toolButtonRefresh = QToolButton(self.frame_7)
        self.toolButtonRefresh.setObjectName(u"toolButtonRefresh")
        self.toolButtonRefresh.setMinimumSize(QSize(25, 25))
        icon = QIcon()
        icon.addFile(u":/icon/light/refresh.png", QSize(), QIcon.Normal, QIcon.Off)
        self.toolButtonRefresh.setIcon(icon)
        self.toolButtonRefresh.setCheckable(False)
        self.toolButtonRefresh.setChecked(False)
        self.toolButtonRefresh.setAutoRaise(False)

        self.horizontalLayout_16.addWidget(self.toolButtonRefresh)

        self.horizontalSpacer_5 = QSpacerItem(10, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_16.addItem(self.horizontalSpacer_5)

        self.toolButtonAdd = QToolButton(self.frame_7)
        self.toolButtonAdd.setObjectName(u"toolButtonAdd")
        self.toolButtonAdd.setMinimumSize(QSize(25, 25))
        self.toolButtonAdd.setMaximumSize(QSize(20, 16777215))
        icon1 = QIcon()
        icon1.addFile(u":/icon/light/add.png", QSize(), QIcon.Normal, QIcon.Off)
        self.toolButtonAdd.setIcon(icon1)

        self.horizontalLayout_16.addWidget(self.toolButtonAdd)

        self.toolButtonRemove = QToolButton(self.frame_7)
        self.toolButtonRemove.setObjectName(u"toolButtonRemove")
        sizePolicy1 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.toolButtonRemove.sizePolicy().hasHeightForWidth())
        self.toolButtonRemove.setSizePolicy(sizePolicy1)
        self.toolButtonRemove.setMinimumSize(QSize(25, 25))
        icon2 = QIcon()
        icon2.addFile(u":/icon/light/remove.png", QSize(), QIcon.Normal, QIcon.Off)
        self.toolButtonRemove.setIcon(icon2)

        self.horizontalLayout_16.addWidget(self.toolButtonRemove)

        self.toolButtonEdit = QToolButton(self.frame_7)
        self.toolButtonEdit.setObjectName(u"toolButtonEdit")
        sizePolicy1.setHeightForWidth(self.toolButtonEdit.sizePolicy().hasHeightForWidth())
        self.toolButtonEdit.setSizePolicy(sizePolicy1)
        self.toolButtonEdit.setMinimumSize(QSize(25, 25))
        icon3 = QIcon()
        icon3.addFile(u":/icon/light/edit.png", QSize(), QIcon.Normal, QIcon.Off)
        self.toolButtonEdit.setIcon(icon3)

        self.horizontalLayout_16.addWidget(self.toolButtonEdit)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_16.addItem(self.horizontalSpacer_2)


        self.verticalLayout_2.addWidget(self.frame_7)

        self.splitter = QSplitter(TabRemote)
        self.splitter.setObjectName(u"splitter")
        self.splitter.setOrientation(Qt.Horizontal)
        self.groupBox = QGroupBox(self.splitter)
        self.groupBox.setObjectName(u"groupBox")
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy2.setHorizontalStretch(1)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy2)
        self.horizontalLayout = QHBoxLayout(self.groupBox)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(2, 2, 2, 2)
        self.tableViewRemoteList = QTableView(self.groupBox)
        self.tableViewRemoteList.setObjectName(u"tableViewRemoteList")
        self.tableViewRemoteList.setSelectionMode(QAbstractItemView.SingleSelection)
        self.tableViewRemoteList.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.tableViewRemoteList.setHorizontalScrollMode(QAbstractItemView.ScrollPerPixel)

        self.horizontalLayout.addWidget(self.tableViewRemoteList)

        self.splitter.addWidget(self.groupBox)
        self.groupBox_2 = QGroupBox(self.splitter)
        self.groupBox_2.setObjectName(u"groupBox_2")
        sizePolicy3 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.groupBox_2.sizePolicy().hasHeightForWidth())
        self.groupBox_2.setSizePolicy(sizePolicy3)
        self.verticalLayout = QVBoxLayout(self.groupBox_2)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(2, 2, 2, 2)
        self.listViewRemoteRecipeReference = QListView(self.groupBox_2)
        self.listViewRemoteRecipeReference.setObjectName(u"listViewRemoteRecipeReference")

        self.verticalLayout.addWidget(self.listViewRemoteRecipeReference)

        self.splitter.addWidget(self.groupBox_2)

        self.verticalLayout_2.addWidget(self.splitter)


        self.retranslateUi(TabRemote)

        QMetaObject.connectSlotsByName(TabRemote)
    # setupUi

    def retranslateUi(self, TabRemote):
        TabRemote.setWindowTitle(QCoreApplication.translate("TabRemote", u"Form", None))
#if QT_CONFIG(tooltip)
        self.toolButtonRefresh.setToolTip(QCoreApplication.translate("TabRemote", u"Refresh", None))
#endif // QT_CONFIG(tooltip)
        self.toolButtonRefresh.setText("")
#if QT_CONFIG(tooltip)
        self.toolButtonAdd.setToolTip(QCoreApplication.translate("TabRemote", u"Add Remote", None))
#endif // QT_CONFIG(tooltip)
        self.toolButtonAdd.setText("")
#if QT_CONFIG(tooltip)
        self.toolButtonRemove.setToolTip(QCoreApplication.translate("TabRemote", u"Remove Remote", None))
#endif // QT_CONFIG(tooltip)
        self.toolButtonRemove.setText("")
#if QT_CONFIG(tooltip)
        self.toolButtonEdit.setToolTip(QCoreApplication.translate("TabRemote", u"Edit Remote", None))
#endif // QT_CONFIG(tooltip)
        self.toolButtonEdit.setText("")
        self.groupBox.setTitle(QCoreApplication.translate("TabRemote", u"Remote List", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("TabRemote", u"Recipe Reference", None))
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
        TabRemote.resize(971, 652)
        self.verticalLayout_2 = QVBoxLayout(TabRemote)
        self.verticalLayout_2.setSpacing(2)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frame_7 = QFrame(TabRemote)
        self.frame_7.setObjectName(u"frame_7")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_7.sizePolicy().hasHeightForWidth())
        self.frame_7.setSizePolicy(sizePolicy)
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_16 = QHBoxLayout(self.frame_7)
        self.horizontalLayout_16.setSpacing(0)
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.horizontalLayout_16.setContentsMargins(0, 0, 0, 0)
        self.toolButtonRefresh = QToolButton(self.frame_7)
        self.toolButtonRefresh.setObjectName(u"toolButtonRefresh")
        self.toolButtonRefresh.setMinimumSize(QSize(25, 25))
        icon = QIcon()
        icon.addFile(u":/icon/light/refresh.png", QSize(), QIcon.Normal, QIcon.Off)
        self.toolButtonRefresh.setIcon(icon)
        self.toolButtonRefresh.setCheckable(False)
        self.toolButtonRefresh.setChecked(False)
        self.toolButtonRefresh.setAutoRaise(False)

        self.horizontalLayout_16.addWidget(self.toolButtonRefresh)

        self.horizontalSpacer_5 = QSpacerItem(10, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_16.addItem(self.horizontalSpacer_5)

        self.toolButtonAdd = QToolButton(self.frame_7)
        self.toolButtonAdd.setObjectName(u"toolButtonAdd")
        self.toolButtonAdd.setMinimumSize(QSize(25, 25))
        self.toolButtonAdd.setMaximumSize(QSize(20, 16777215))
        icon1 = QIcon()
        icon1.addFile(u":/icon/light/add.png", QSize(), QIcon.Normal, QIcon.Off)
        self.toolButtonAdd.setIcon(icon1)

        self.horizontalLayout_16.addWidget(self.toolButtonAdd)

        self.toolButtonRemove = QToolButton(self.frame_7)
        self.toolButtonRemove.setObjectName(u"toolButtonRemove")
        sizePolicy1 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.toolButtonRemove.sizePolicy().hasHeightForWidth())
        self.toolButtonRemove.setSizePolicy(sizePolicy1)
        self.toolButtonRemove.setMinimumSize(QSize(25, 25))
        icon2 = QIcon()
        icon2.addFile(u":/icon/light/remove.png", QSize(), QIcon.Normal, QIcon.Off)
        self.toolButtonRemove.setIcon(icon2)

        self.horizontalLayout_16.addWidget(self.toolButtonRemove)

        self.toolButtonEdit = QToolButton(self.frame_7)
        self.toolButtonEdit.setObjectName(u"toolButtonEdit")
        sizePolicy1.setHeightForWidth(self.toolButtonEdit.sizePolicy().hasHeightForWidth())
        self.toolButtonEdit.setSizePolicy(sizePolicy1)
        self.toolButtonEdit.setMinimumSize(QSize(25, 25))
        icon3 = QIcon()
        icon3.addFile(u":/icon/light/edit.png", QSize(), QIcon.Normal, QIcon.Off)
        self.toolButtonEdit.setIcon(icon3)

        self.horizontalLayout_16.addWidget(self.toolButtonEdit)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_16.addItem(self.horizontalSpacer_2)


        self.verticalLayout_2.addWidget(self.frame_7)

        self.splitter = QSplitter(TabRemote)
        self.splitter.setObjectName(u"splitter")
        self.splitter.setOrientation(Qt.Horizontal)
        self.groupBox = QGroupBox(self.splitter)
        self.groupBox.setObjectName(u"groupBox")
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy2.setHorizontalStretch(1)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy2)
        self.horizontalLayout = QHBoxLayout(self.groupBox)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(2, 2, 2, 2)
        self.tableViewRemoteList = QTableView(self.groupBox)
        self.tableViewRemoteList.setObjectName(u"tableViewRemoteList")
        self.tableViewRemoteList.setSelectionMode(QAbstractItemView.SingleSelection)
        self.tableViewRemoteList.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.tableViewRemoteList.setHorizontalScrollMode(QAbstractItemView.ScrollPerPixel)

        self.horizontalLayout.addWidget(self.tableViewRemoteList)

        self.splitter.addWidget(self.groupBox)
        self.groupBox_2 = QGroupBox(self.splitter)
        self.groupBox_2.setObjectName(u"groupBox_2")
        sizePolicy3 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.groupBox_2.sizePolicy().hasHeightForWidth())
        self.groupBox_2.setSizePolicy(sizePolicy3)
        self.verticalLayout = QVBoxLayout(self.groupBox_2)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(2, 2, 2, 2)
        self.listViewRemoteRecipeReference = QListView(self.groupBox_2)
        self.listViewRemoteRecipeReference.setObjectName(u"listViewRemoteRecipeReference")

        self.verticalLayout.addWidget(self.listViewRemoteRecipeReference)

        self.splitter.addWidget(self.groupBox_2)

        self.verticalLayout_2.addWidget(self.splitter)


        self.retranslateUi(TabRemote)

        QMetaObject.connectSlotsByName(TabRemote)
    # setupUi

    def retranslateUi(self, TabRemote):
        TabRemote.setWindowTitle(QCoreApplication.translate("TabRemote", u"Form", None))
#if QT_CONFIG(tooltip)
        self.toolButtonRefresh.setToolTip(QCoreApplication.translate("TabRemote", u"Refresh", None))
#endif // QT_CONFIG(tooltip)
        self.toolButtonRefresh.setText("")
#if QT_CONFIG(tooltip)
        self.toolButtonAdd.setToolTip(QCoreApplication.translate("TabRemote", u"Add Remote", None))
#endif // QT_CONFIG(tooltip)
        self.toolButtonAdd.setText("")
#if QT_CONFIG(tooltip)
        self.toolButtonRemove.setToolTip(QCoreApplication.translate("TabRemote", u"Remove Remote", None))
#endif // QT_CONFIG(tooltip)
        self.toolButtonRemove.setText("")
#if QT_CONFIG(tooltip)
        self.toolButtonEdit.setToolTip(QCoreApplication.translate("TabRemote", u"Edit Remote", None))
#endif // QT_CONFIG(tooltip)
        self.toolButtonEdit.setText("")
        self.groupBox.setTitle(QCoreApplication.translate("TabRemote", u"Remote List", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("TabRemote", u"Recipe Reference", None))
    # retranslateUi

