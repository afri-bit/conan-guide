# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'tab_profile.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

from conanguide.ui.res import resources_rc

class Ui_TabProfile(object):
    def setupUi(self, TabProfile):
        if not TabProfile.objectName():
            TabProfile.setObjectName(u"TabProfile")
        TabProfile.resize(1121, 875)
        self.horizontalLayout = QHBoxLayout(TabProfile)
        self.horizontalLayout.setSpacing(5)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.splitter_7 = QSplitter(TabProfile)
        self.splitter_7.setObjectName(u"splitter_7")
        self.splitter_7.setOrientation(Qt.Horizontal)
        self.frame_22 = QFrame(self.splitter_7)
        self.frame_22.setObjectName(u"frame_22")
        self.frame_22.setMinimumSize(QSize(300, 0))
        self.frame_22.setFrameShape(QFrame.StyledPanel)
        self.frame_22.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_22)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frame_18 = QFrame(self.frame_22)
        self.frame_18.setObjectName(u"frame_18")
        self.frame_18.setFrameShape(QFrame.StyledPanel)
        self.frame_18.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_19 = QHBoxLayout(self.frame_18)
        self.horizontalLayout_19.setSpacing(0)
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.horizontalLayout_19.setContentsMargins(2, 2, 2, 2)
        self.toolButtonProfileAdd = QToolButton(self.frame_18)
        self.toolButtonProfileAdd.setObjectName(u"toolButtonProfileAdd")
        self.toolButtonProfileAdd.setMinimumSize(QSize(25, 25))
        icon = QIcon()
        icon.addFile(u":/icon/light/add.png", QSize(), QIcon.Normal, QIcon.Off)
        self.toolButtonProfileAdd.setIcon(icon)

        self.horizontalLayout_19.addWidget(self.toolButtonProfileAdd)

        self.toolButtonProfileRemove = QToolButton(self.frame_18)
        self.toolButtonProfileRemove.setObjectName(u"toolButtonProfileRemove")
        self.toolButtonProfileRemove.setMinimumSize(QSize(25, 25))
        icon1 = QIcon()
        icon1.addFile(u":/icon/light/remove.png", QSize(), QIcon.Normal, QIcon.Off)
        self.toolButtonProfileRemove.setIcon(icon1)

        self.horizontalLayout_19.addWidget(self.toolButtonProfileRemove)

        self.toolButtonSaveChange = QToolButton(self.frame_18)
        self.toolButtonSaveChange.setObjectName(u"toolButtonSaveChange")
        self.toolButtonSaveChange.setMinimumSize(QSize(25, 25))
        self.toolButtonSaveChange.setIcon(icon1)

        self.horizontalLayout_19.addWidget(self.toolButtonSaveChange)

        self.toolButtonRevertChange = QToolButton(self.frame_18)
        self.toolButtonRevertChange.setObjectName(u"toolButtonRevertChange")
        self.toolButtonRevertChange.setMinimumSize(QSize(25, 25))
        self.toolButtonRevertChange.setIcon(icon1)

        self.horizontalLayout_19.addWidget(self.toolButtonRevertChange)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_19.addItem(self.horizontalSpacer_3)


        self.verticalLayout_2.addWidget(self.frame_18)

        self.splitter = QSplitter(self.frame_22)
        self.splitter.setObjectName(u"splitter")
        self.splitter.setOrientation(Qt.Vertical)
        self.listViewProfile = QListView(self.splitter)
        self.listViewProfile.setObjectName(u"listViewProfile")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.listViewProfile.sizePolicy().hasHeightForWidth())
        self.listViewProfile.setSizePolicy(sizePolicy)
        self.splitter.addWidget(self.listViewProfile)

        self.verticalLayout_2.addWidget(self.splitter)

        self.splitter_7.addWidget(self.frame_22)
        self.frameConanProfileAttribute = QFrame(self.splitter_7)
        self.frameConanProfileAttribute.setObjectName(u"frameConanProfileAttribute")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(1)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.frameConanProfileAttribute.sizePolicy().hasHeightForWidth())
        self.frameConanProfileAttribute.setSizePolicy(sizePolicy1)
        self.frameConanProfileAttribute.setContextMenuPolicy(Qt.DefaultContextMenu)
        self.frameConanProfileAttribute.setFrameShape(QFrame.StyledPanel)
        self.frameConanProfileAttribute.setFrameShadow(QFrame.Raised)
        self.verticalLayoutConanProfileAttribute = QVBoxLayout(self.frameConanProfileAttribute)
        self.verticalLayoutConanProfileAttribute.setSpacing(5)
        self.verticalLayoutConanProfileAttribute.setObjectName(u"verticalLayoutConanProfileAttribute")
        self.verticalLayoutConanProfileAttribute.setContentsMargins(2, 2, 2, 2)
        self.splitter_7.addWidget(self.frameConanProfileAttribute)

        self.horizontalLayout.addWidget(self.splitter_7)


        self.retranslateUi(TabProfile)

        QMetaObject.connectSlotsByName(TabProfile)
    # setupUi

    def retranslateUi(self, TabProfile):
        TabProfile.setWindowTitle(QCoreApplication.translate("TabProfile", u"Form", None))
        self.toolButtonProfileAdd.setText("")
        self.toolButtonProfileRemove.setText("")
        self.toolButtonSaveChange.setText("")
        self.toolButtonRevertChange.setText("")
    # re# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'tab_profile.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

from conanguide.ui.res import resources_rc

class Ui_TabProfile(object):
    def setupUi(self, TabProfile):
        if not TabProfile.objectName():
            TabProfile.setObjectName(u"TabProfile")
        TabProfile.resize(1121, 875)
        self.horizontalLayout = QHBoxLayout(TabProfile)
        self.horizontalLayout.setSpacing(5)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.splitter_7 = QSplitter(TabProfile)
        self.splitter_7.setObjectName(u"splitter_7")
        self.splitter_7.setOrientation(Qt.Horizontal)
        self.frame_22 = QFrame(self.splitter_7)
        self.frame_22.setObjectName(u"frame_22")
        self.frame_22.setMinimumSize(QSize(300, 0))
        self.frame_22.setFrameShape(QFrame.StyledPanel)
        self.frame_22.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_22)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frame_18 = QFrame(self.frame_22)
        self.frame_18.setObjectName(u"frame_18")
        self.frame_18.setFrameShape(QFrame.StyledPanel)
        self.frame_18.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_19 = QHBoxLayout(self.frame_18)
        self.horizontalLayout_19.setSpacing(0)
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.horizontalLayout_19.setContentsMargins(2, 2, 2, 2)
        self.toolButtonProfileAdd = QToolButton(self.frame_18)
        self.toolButtonProfileAdd.setObjectName(u"toolButtonProfileAdd")
        self.toolButtonProfileAdd.setMinimumSize(QSize(25, 25))
        icon = QIcon()
        icon.addFile(u":/icon/light/add.png", QSize(), QIcon.Normal, QIcon.Off)
        self.toolButtonProfileAdd.setIcon(icon)

        self.horizontalLayout_19.addWidget(self.toolButtonProfileAdd)

        self.toolButtonProfileRemove = QToolButton(self.frame_18)
        self.toolButtonProfileRemove.setObjectName(u"toolButtonProfileRemove")
        self.toolButtonProfileRemove.setMinimumSize(QSize(25, 25))
        icon1 = QIcon()
        icon1.addFile(u":/icon/light/remove.png", QSize(), QIcon.Normal, QIcon.Off)
        self.toolButtonProfileRemove.setIcon(icon1)

        self.horizontalLayout_19.addWidget(self.toolButtonProfileRemove)

        self.toolButtonSaveChange = QToolButton(self.frame_18)
        self.toolButtonSaveChange.setObjectName(u"toolButtonSaveChange")
        self.toolButtonSaveChange.setMinimumSize(QSize(25, 25))
        self.toolButtonSaveChange.setIcon(icon1)

        self.horizontalLayout_19.addWidget(self.toolButtonSaveChange)

        self.toolButtonRevertChange = QToolButton(self.frame_18)
        self.toolButtonRevertChange.setObjectName(u"toolButtonRevertChange")
        self.toolButtonRevertChange.setMinimumSize(QSize(25, 25))
        self.toolButtonRevertChange.setIcon(icon1)

        self.horizontalLayout_19.addWidget(self.toolButtonRevertChange)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_19.addItem(self.horizontalSpacer_3)


        self.verticalLayout_2.addWidget(self.frame_18)

        self.splitter = QSplitter(self.frame_22)
        self.splitter.setObjectName(u"splitter")
        self.splitter.setOrientation(Qt.Vertical)
        self.listViewProfile = QListView(self.splitter)
        self.listViewProfile.setObjectName(u"listViewProfile")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.listViewProfile.sizePolicy().hasHeightForWidth())
        self.listViewProfile.setSizePolicy(sizePolicy)
        self.splitter.addWidget(self.listViewProfile)

        self.verticalLayout_2.addWidget(self.splitter)

        self.splitter_7.addWidget(self.frame_22)
        self.frameConanProfileAttribute = QFrame(self.splitter_7)
        self.frameConanProfileAttribute.setObjectName(u"frameConanProfileAttribute")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(1)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.frameConanProfileAttribute.sizePolicy().hasHeightForWidth())
        self.frameConanProfileAttribute.setSizePolicy(sizePolicy1)
        self.frameConanProfileAttribute.setContextMenuPolicy(Qt.DefaultContextMenu)
        self.frameConanProfileAttribute.setFrameShape(QFrame.StyledPanel)
        self.frameConanProfileAttribute.setFrameShadow(QFrame.Raised)
        self.verticalLayoutConanProfileAttribute = QVBoxLayout(self.frameConanProfileAttribute)
        self.verticalLayoutConanProfileAttribute.setSpacing(5)
        self.verticalLayoutConanProfileAttribute.setObjectName(u"verticalLayoutConanProfileAttribute")
        self.verticalLayoutConanProfileAttribute.setContentsMargins(2, 2, 2, 2)
        self.splitter_7.addWidget(self.frameConanProfileAttribute)

        self.horizontalLayout.addWidget(self.splitter_7)


        self.retranslateUi(TabProfile)

        QMetaObject.connectSlotsByName(TabProfile)
    # setupUi

    def retranslateUi(self, TabProfile):
        TabProfile.setWindowTitle(QCoreApplication.translate("TabProfile", u"Form", None))
        self.toolButtonProfileAdd.setText("")
        self.toolButtonProfileRemove.setText("")
        self.toolButtonSaveChange.setText("")
        self.toolButtonRevertChange.setText("")
    # retranslateUi

