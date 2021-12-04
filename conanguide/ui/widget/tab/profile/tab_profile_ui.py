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
        self.verticalLayout_2.setSpacing(3)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frame_18 = QFrame(self.frame_22)
        self.frame_18.setObjectName(u"frame_18")
        self.frame_18.setSizeIncrement(QSize(0, 0))
        self.frame_18.setBaseSize(QSize(10, 0))
        self.frame_18.setFrameShape(QFrame.StyledPanel)
        self.frame_18.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_19 = QHBoxLayout(self.frame_18)
        self.horizontalLayout_19.setSpacing(0)
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.horizontalLayout_19.setContentsMargins(1, 1, 0, 0)
        self.toolButtonRefresh = QToolButton(self.frame_18)
        self.toolButtonRefresh.setObjectName(u"toolButtonRefresh")
        self.toolButtonRefresh.setMinimumSize(QSize(25, 25))
        icon = QIcon()
        icon.addFile(u":/icon/light/refresh.png", QSize(), QIcon.Normal, QIcon.Off)
        self.toolButtonRefresh.setIcon(icon)
        self.toolButtonRefresh.setCheckable(False)
        self.toolButtonRefresh.setChecked(False)
        self.toolButtonRefresh.setAutoRaise(False)

        self.horizontalLayout_19.addWidget(self.toolButtonRefresh)

        self.horizontalSpacer_5 = QSpacerItem(10, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_19.addItem(self.horizontalSpacer_5)

        self.toolButtonSortAscending = QToolButton(self.frame_18)
        self.toolButtonSortAscending.setObjectName(u"toolButtonSortAscending")
        self.toolButtonSortAscending.setMinimumSize(QSize(25, 25))
        icon1 = QIcon()
        icon1.addFile(u":/icon/light/sort_ascending.png", QSize(), QIcon.Normal, QIcon.Off)
        self.toolButtonSortAscending.setIcon(icon1)
        self.toolButtonSortAscending.setCheckable(True)
        self.toolButtonSortAscending.setChecked(True)
        self.toolButtonSortAscending.setAutoRaise(False)

        self.horizontalLayout_19.addWidget(self.toolButtonSortAscending)

        self.toolButtonSortDescending = QToolButton(self.frame_18)
        self.toolButtonSortDescending.setObjectName(u"toolButtonSortDescending")
        self.toolButtonSortDescending.setMinimumSize(QSize(25, 25))
        icon2 = QIcon()
        icon2.addFile(u":/icon/light/sort_descending.png", QSize(), QIcon.Normal, QIcon.Off)
        self.toolButtonSortDescending.setIcon(icon2)
        self.toolButtonSortDescending.setCheckable(True)

        self.horizontalLayout_19.addWidget(self.toolButtonSortDescending)

        self.horizontalSpacer_4 = QSpacerItem(10, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_19.addItem(self.horizontalSpacer_4)

        self.toolButtonProfileAdd = QToolButton(self.frame_18)
        self.toolButtonProfileAdd.setObjectName(u"toolButtonProfileAdd")
        self.toolButtonProfileAdd.setMinimumSize(QSize(25, 25))
        icon3 = QIcon()
        icon3.addFile(u":/icon/light/add.png", QSize(), QIcon.Normal, QIcon.Off)
        self.toolButtonProfileAdd.setIcon(icon3)

        self.horizontalLayout_19.addWidget(self.toolButtonProfileAdd)

        self.toolButtonProfileRemove = QToolButton(self.frame_18)
        self.toolButtonProfileRemove.setObjectName(u"toolButtonProfileRemove")
        self.toolButtonProfileRemove.setMinimumSize(QSize(25, 25))
        icon4 = QIcon()
        icon4.addFile(u":/icon/light/remove.png", QSize(), QIcon.Normal, QIcon.Off)
        self.toolButtonProfileRemove.setIcon(icon4)

        self.horizontalLayout_19.addWidget(self.toolButtonProfileRemove)

        self.toolButtonProfileRename = QToolButton(self.frame_18)
        self.toolButtonProfileRename.setObjectName(u"toolButtonProfileRename")
        self.toolButtonProfileRename.setMinimumSize(QSize(25, 25))
        icon5 = QIcon()
        icon5.addFile(u":/icon/light/edit.png", QSize(), QIcon.Normal, QIcon.Off)
        self.toolButtonProfileRename.setIcon(icon5)

        self.horizontalLayout_19.addWidget(self.toolButtonProfileRename)

        self.toolButtonSaveChange = QToolButton(self.frame_18)
        self.toolButtonSaveChange.setObjectName(u"toolButtonSaveChange")
        self.toolButtonSaveChange.setMinimumSize(QSize(25, 25))
        icon6 = QIcon()
        icon6.addFile(u":/icon/light/save.png", QSize(), QIcon.Normal, QIcon.Off)
        self.toolButtonSaveChange.setIcon(icon6)

        self.horizontalLayout_19.addWidget(self.toolButtonSaveChange)

        self.toolButtonRevertChange = QToolButton(self.frame_18)
        self.toolButtonRevertChange.setObjectName(u"toolButtonRevertChange")
        self.toolButtonRevertChange.setMinimumSize(QSize(25, 25))
        icon7 = QIcon()
        icon7.addFile(u":/icon/light/revert.png", QSize(), QIcon.Normal, QIcon.Off)
        self.toolButtonRevertChange.setIcon(icon7)

        self.horizontalLayout_19.addWidget(self.toolButtonRevertChange)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_19.addItem(self.horizontalSpacer_3)


        self.verticalLayout_2.addWidget(self.frame_18)

        self.lineEditSearchProfile = QLineEdit(self.frame_22)
        self.lineEditSearchProfile.setObjectName(u"lineEditSearchProfile")
        self.lineEditSearchProfile.setMinimumSize(QSize(0, 25))
        self.lineEditSearchProfile.setFrame(True)
        self.lineEditSearchProfile.setEchoMode(QLineEdit.Normal)
        self.lineEditSearchProfile.setCursorPosition(0)

        self.verticalLayout_2.addWidget(self.lineEditSearchProfile)

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
        self.frame = QFrame(self.frameConanProfileAttribute)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame)
        self.horizontalLayout_2.setSpacing(5)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(2, 2, 2, 2)
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setPointSize(11)
        self.label.setFont(font)

        self.horizontalLayout_2.addWidget(self.label)

        self.labelProfileName = QLabel(self.frame)
        self.labelProfileName.setObjectName(u"labelProfileName")
        font1 = QFont()
        font1.setPointSize(11)
        font1.setBold(True)
        font1.setWeight(75)
        self.labelProfileName.setFont(font1)
        self.labelProfileName.setFrameShape(QFrame.NoFrame)

        self.horizontalLayout_2.addWidget(self.labelProfileName)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)


        self.verticalLayoutConanProfileAttribute.addWidget(self.frame)

        self.splitter_7.addWidget(self.frameConanProfileAttribute)

        self.horizontalLayout.addWidget(self.splitter_7)


        self.retranslateUi(TabProfile)

        QMetaObject.connectSlotsByName(TabProfile)
    # setupUi

    def retranslateUi(self, TabProfile):
        TabProfile.setWindowTitle(QCoreApplication.translate("TabProfile", u"Form", None))
#if QT_CONFIG(tooltip)
        self.toolButtonRefresh.setToolTip(QCoreApplication.translate("TabProfile", u"Refresh", None))
#endif // QT_CONFIG(tooltip)
        self.toolButtonRefresh.setText("")
#if QT_CONFIG(tooltip)
        self.toolButtonSortAscending.setToolTip(QCoreApplication.translate("TabProfile", u"Sort Ascending", None))
#endif // QT_CONFIG(tooltip)
        self.toolButtonSortAscending.setText("")
#if QT_CONFIG(tooltip)
        self.toolButtonSortDescending.setToolTip(QCoreApplication.translate("TabProfile", u"Sort Descending", None))
#endif // QT_CONFIG(tooltip)
        self.toolButtonSortDescending.setText("")
#if QT_CONFIG(tooltip)
        self.toolButtonProfileAdd.setToolTip(QCoreApplication.translate("TabProfile", u"Add Profile", None))
#endif // QT_CONFIG(tooltip)
        self.toolButtonProfileAdd.setText("")
#if QT_CONFIG(tooltip)
        self.toolButtonProfileRemove.setToolTip(QCoreApplication.translate("TabProfile", u"Remove Profile", None))
#endif // QT_CONFIG(tooltip)
        self.toolButtonProfileRemove.setText("")
#if QT_CONFIG(tooltip)
        self.toolButtonProfileRename.setToolTip(QCoreApplication.translate("TabProfile", u"Rename Profile", None))
#endif // QT_CONFIG(tooltip)
        self.toolButtonProfileRename.setText("")
#if QT_CONFIG(tooltip)
        self.toolButtonSaveChange.setToolTip(QCoreApplication.translate("TabProfile", u"Save Changes", None))
#endif // QT_CONFIG(tooltip)
        self.toolButtonSaveChange.setText("")
#if QT_CONFIG(tooltip)
        self.toolButtonRevertChange.setToolTip(QCoreApplication.translate("TabProfile", u"Revert Changes", None))
#endif // QT_CONFIG(tooltip)
        self.toolButtonRevertChange.setText("")
#if QT_CONFIG(whatsthis)
        self.lineEditSearchProfile.setWhatsThis("")
#endif // QT_CONFIG(whatsthis)
        self.lineEditSearchProfile.setPlaceholderText(QCoreApplication.translate("TabProfile", u"Search Profile...", None))
        self.label.setText(QCoreApplication.translate("TabProfile", u"Profile -", None))
        self.labelProfileName.setText("")
    # retranslateUi

