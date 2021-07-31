# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'profile_attribute.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

from conanguide.ui.res import resources_rc

class Ui_WidgetProfileAttribute(object):
    def setupUi(self, WidgetProfileAttribute):
        if not WidgetProfileAttribute.objectName():
            WidgetProfileAttribute.setObjectName(u"WidgetProfileAttribute")
        WidgetProfileAttribute.resize(551, 205)
        self.verticalLayout = QVBoxLayout(WidgetProfileAttribute)
        self.verticalLayout.setSpacing(2)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(2, 2, 2, 2)
        self.groupBox = QGroupBox(WidgetProfileAttribute)
        self.groupBox.setObjectName(u"groupBox")
        self.horizontalLayout = QHBoxLayout(self.groupBox)
        self.horizontalLayout.setSpacing(2)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(2, 2, 2, 2)
        self.frame_20 = QFrame(self.groupBox)
        self.frame_20.setObjectName(u"frame_20")
        self.frame_20.setFrameShape(QFrame.StyledPanel)
        self.frame_20.setFrameShadow(QFrame.Raised)
        self.verticalLayout_11 = QVBoxLayout(self.frame_20)
        self.verticalLayout_11.setSpacing(0)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.toolButtonAdd = QToolButton(self.frame_20)
        self.toolButtonAdd.setObjectName(u"toolButtonAdd")
        self.toolButtonAdd.setMinimumSize(QSize(25, 25))
        self.toolButtonAdd.setMaximumSize(QSize(25, 25))
        icon = QIcon()
        icon.addFile(u":/icon/light/add.png", QSize(), QIcon.Normal, QIcon.Off)
        self.toolButtonAdd.setIcon(icon)

        self.verticalLayout_11.addWidget(self.toolButtonAdd)

        self.toolButtonRemove = QToolButton(self.frame_20)
        self.toolButtonRemove.setObjectName(u"toolButtonRemove")
        self.toolButtonRemove.setMinimumSize(QSize(25, 25))
        self.toolButtonRemove.setMaximumSize(QSize(25, 25))
        icon1 = QIcon()
        icon1.addFile(u":/icon/light/remove.png", QSize(), QIcon.Normal, QIcon.Off)
        self.toolButtonRemove.setIcon(icon1)

        self.verticalLayout_11.addWidget(self.toolButtonRemove)

        self.toolButtonClear = QToolButton(self.frame_20)
        self.toolButtonClear.setObjectName(u"toolButtonClear")
        self.toolButtonClear.setMinimumSize(QSize(25, 25))
        self.toolButtonClear.setMaximumSize(QSize(25, 25))
        icon2 = QIcon()
        icon2.addFile(u":/icon/light/garbage_can.png", QSize(), QIcon.Normal, QIcon.Off)
        self.toolButtonClear.setIcon(icon2)

        self.verticalLayout_11.addWidget(self.toolButtonClear)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_11.addItem(self.verticalSpacer)


        self.horizontalLayout.addWidget(self.frame_20)

        self.tableViewAttributes = QTableView(self.groupBox)
        self.tableViewAttributes.setObjectName(u"tableViewAttributes")

        self.horizontalLayout.addWidget(self.tableViewAttributes)


        self.verticalLayout.addWidget(self.groupBox)


        self.retranslateUi(WidgetProfileAttribute)

        QMetaObject.connectSlotsByName(WidgetProfileAttribute)
    # setupUi

    def retranslateUi(self, WidgetProfileAttribute):
        WidgetProfileAttribute.setWindowTitle(QCoreApplication.translate("WidgetProfileAttribute", u"Form", None))
        self.groupBox.setTitle(QCoreApplication.translate("WidgetProfileAttribute", u"GroupBox", None))
        self.toolButtonAdd.setText("")
        self.toolButtonRemove.setText(QCoreApplication.translate("WidgetProfileAttribute", u"-", None))
        self.toolButtonClear.setText(QCoreApplication.translate("WidgetProfileAttribute", u"C", None))
    # re# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'profile_attribute.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

from conanguide.ui.res import resources_rc

class Ui_WidgetProfileAttribute(object):
    def setupUi(self, WidgetProfileAttribute):
        if not WidgetProfileAttribute.objectName():
            WidgetProfileAttribute.setObjectName(u"WidgetProfileAttribute")
        WidgetProfileAttribute.resize(551, 205)
        self.verticalLayout = QVBoxLayout(WidgetProfileAttribute)
        self.verticalLayout.setSpacing(2)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(2, 2, 2, 2)
        self.groupBox = QGroupBox(WidgetProfileAttribute)
        self.groupBox.setObjectName(u"groupBox")
        self.horizontalLayout = QHBoxLayout(self.groupBox)
        self.horizontalLayout.setSpacing(2)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(2, 2, 2, 2)
        self.frame_20 = QFrame(self.groupBox)
        self.frame_20.setObjectName(u"frame_20")
        self.frame_20.setFrameShape(QFrame.StyledPanel)
        self.frame_20.setFrameShadow(QFrame.Raised)
        self.verticalLayout_11 = QVBoxLayout(self.frame_20)
        self.verticalLayout_11.setSpacing(0)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.toolButtonAdd = QToolButton(self.frame_20)
        self.toolButtonAdd.setObjectName(u"toolButtonAdd")
        self.toolButtonAdd.setMinimumSize(QSize(25, 25))
        self.toolButtonAdd.setMaximumSize(QSize(25, 25))
        icon = QIcon()
        icon.addFile(u":/icon/light/add.png", QSize(), QIcon.Normal, QIcon.Off)
        self.toolButtonAdd.setIcon(icon)

        self.verticalLayout_11.addWidget(self.toolButtonAdd)

        self.toolButtonRemove = QToolButton(self.frame_20)
        self.toolButtonRemove.setObjectName(u"toolButtonRemove")
        self.toolButtonRemove.setMinimumSize(QSize(25, 25))
        self.toolButtonRemove.setMaximumSize(QSize(25, 25))
        icon1 = QIcon()
        icon1.addFile(u":/icon/light/remove.png", QSize(), QIcon.Normal, QIcon.Off)
        self.toolButtonRemove.setIcon(icon1)

        self.verticalLayout_11.addWidget(self.toolButtonRemove)

        self.toolButtonClear = QToolButton(self.frame_20)
        self.toolButtonClear.setObjectName(u"toolButtonClear")
        self.toolButtonClear.setMinimumSize(QSize(25, 25))
        self.toolButtonClear.setMaximumSize(QSize(25, 25))
        icon2 = QIcon()
        icon2.addFile(u":/icon/light/garbage_can.png", QSize(), QIcon.Normal, QIcon.Off)
        self.toolButtonClear.setIcon(icon2)

        self.verticalLayout_11.addWidget(self.toolButtonClear)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_11.addItem(self.verticalSpacer)


        self.horizontalLayout.addWidget(self.frame_20)

        self.tableViewAttributes = QTableView(self.groupBox)
        self.tableViewAttributes.setObjectName(u"tableViewAttributes")

        self.horizontalLayout.addWidget(self.tableViewAttributes)


        self.verticalLayout.addWidget(self.groupBox)


        self.retranslateUi(WidgetProfileAttribute)

        QMetaObject.connectSlotsByName(WidgetProfileAttribute)
    # setupUi

    def retranslateUi(self, WidgetProfileAttribute):
        WidgetProfileAttribute.setWindowTitle(QCoreApplication.translate("WidgetProfileAttribute", u"Form", None))
        self.groupBox.setTitle(QCoreApplication.translate("WidgetProfileAttribute", u"GroupBox", None))
        self.toolButtonAdd.setText("")
        self.toolButtonRemove.setText(QCoreApplication.translate("WidgetProfileAttribute", u"-", None))
        self.toolButtonClear.setText(QCoreApplication.translate("WidgetProfileAttribute", u"C", None))
    # retranslateUi

