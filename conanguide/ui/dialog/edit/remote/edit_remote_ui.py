# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'edit_remote.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

from conanguide.ui.res import resources_rc

class Ui_DialogEditRemote(object):
    def setupUi(self, DialogEditRemote):
        if not DialogEditRemote.objectName():
            DialogEditRemote.setObjectName(u"DialogEditRemote")
        DialogEditRemote.resize(550, 129)
        DialogEditRemote.setMinimumSize(QSize(550, 129))
        DialogEditRemote.setMaximumSize(QSize(550, 129))
        icon = QIcon()
        icon.addFile(u":/general/icon/conan_guide_icon.png", QSize(), QIcon.Normal, QIcon.Off)
        DialogEditRemote.setWindowIcon(icon)
        self.verticalLayout = QVBoxLayout(DialogEditRemote)
        self.verticalLayout.setSpacing(2)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(5, 5, 5, 5)
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label = QLabel(DialogEditRemote)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(40, 0))

        self.horizontalLayout.addWidget(self.label)

        self.lineEditName = QLineEdit(DialogEditRemote)
        self.lineEditName.setObjectName(u"lineEditName")

        self.horizontalLayout.addWidget(self.lineEditName)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_2 = QLabel(DialogEditRemote)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMinimumSize(QSize(40, 0))

        self.horizontalLayout_2.addWidget(self.label_2)

        self.lineEditURL = QLineEdit(DialogEditRemote)
        self.lineEditURL.setObjectName(u"lineEditURL")

        self.horizontalLayout_2.addWidget(self.lineEditURL)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.checkBoxVerifySSL = QCheckBox(DialogEditRemote)
        self.checkBoxVerifySSL.setObjectName(u"checkBoxVerifySSL")
        self.checkBoxVerifySSL.setLayoutDirection(Qt.LeftToRight)

        self.horizontalLayout_4.addWidget(self.checkBoxVerifySSL)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer)


        self.verticalLayout.addLayout(self.horizontalLayout_4)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.labelInfo = QLabel(DialogEditRemote)
        self.labelInfo.setObjectName(u"labelInfo")
        self.labelInfo.setMinimumSize(QSize(0, 22))
        self.labelInfo.setMaximumSize(QSize(16777215, 22))

        self.horizontalLayout_3.addWidget(self.labelInfo)

        self.btnOK = QPushButton(DialogEditRemote)
        self.btnOK.setObjectName(u"btnOK")
        self.btnOK.setMinimumSize(QSize(0, 25))
        self.btnOK.setMaximumSize(QSize(75, 16777215))

        self.horizontalLayout_3.addWidget(self.btnOK)

        self.btnCancel = QPushButton(DialogEditRemote)
        self.btnCancel.setObjectName(u"btnCancel")
        self.btnCancel.setMinimumSize(QSize(0, 25))
        self.btnCancel.setMaximumSize(QSize(75, 16777215))

        self.horizontalLayout_3.addWidget(self.btnCancel)


        self.verticalLayout.addLayout(self.horizontalLayout_3)


        self.retranslateUi(DialogEditRemote)

        QMetaObject.connectSlotsByName(DialogEditRemote)
    # setupUi

    def retranslateUi(self, DialogEditRemote):
        DialogEditRemote.setWindowTitle(QCoreApplication.translate("DialogEditRemote", u"Dialog", None))
        self.label.setText(QCoreApplication.translate("DialogEditRemote", u"Name", None))
        self.label_2.setText(QCoreApplication.translate("DialogEditRemote", u"URL", None))
        self.checkBoxVerifySSL.setText(QCoreApplication.translate("DialogEditRemote", u"Verify SSL", None))
        self.labelInfo.setText("")
        self.btnOK.setText(QCoreApplication.translate("DialogEditRemote", u"OK", None))
        self.btnCancel.setText(QCoreApplication.translate("DialogEditRemote", u"Cancel", None))
    # re# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'edit_remote.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

from conanguide.ui.res import resources_rc

class Ui_DialogEditRemote(object):
    def setupUi(self, DialogEditRemote):
        if not DialogEditRemote.objectName():
            DialogEditRemote.setObjectName(u"DialogEditRemote")
        DialogEditRemote.resize(550, 129)
        DialogEditRemote.setMinimumSize(QSize(550, 129))
        DialogEditRemote.setMaximumSize(QSize(550, 129))
        icon = QIcon()
        icon.addFile(u":/general/icon/conan_guide_icon.png", QSize(), QIcon.Normal, QIcon.Off)
        DialogEditRemote.setWindowIcon(icon)
        self.verticalLayout = QVBoxLayout(DialogEditRemote)
        self.verticalLayout.setSpacing(2)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(5, 5, 5, 5)
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label = QLabel(DialogEditRemote)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(40, 0))

        self.horizontalLayout.addWidget(self.label)

        self.lineEditName = QLineEdit(DialogEditRemote)
        self.lineEditName.setObjectName(u"lineEditName")

        self.horizontalLayout.addWidget(self.lineEditName)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_2 = QLabel(DialogEditRemote)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMinimumSize(QSize(40, 0))

        self.horizontalLayout_2.addWidget(self.label_2)

        self.lineEditURL = QLineEdit(DialogEditRemote)
        self.lineEditURL.setObjectName(u"lineEditURL")

        self.horizontalLayout_2.addWidget(self.lineEditURL)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.checkBoxVerifySSL = QCheckBox(DialogEditRemote)
        self.checkBoxVerifySSL.setObjectName(u"checkBoxVerifySSL")
        self.checkBoxVerifySSL.setLayoutDirection(Qt.LeftToRight)

        self.horizontalLayout_4.addWidget(self.checkBoxVerifySSL)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer)


        self.verticalLayout.addLayout(self.horizontalLayout_4)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.labelInfo = QLabel(DialogEditRemote)
        self.labelInfo.setObjectName(u"labelInfo")
        self.labelInfo.setMinimumSize(QSize(0, 22))
        self.labelInfo.setMaximumSize(QSize(16777215, 22))

        self.horizontalLayout_3.addWidget(self.labelInfo)

        self.btnOK = QPushButton(DialogEditRemote)
        self.btnOK.setObjectName(u"btnOK")
        self.btnOK.setMinimumSize(QSize(0, 25))
        self.btnOK.setMaximumSize(QSize(75, 16777215))

        self.horizontalLayout_3.addWidget(self.btnOK)

        self.btnCancel = QPushButton(DialogEditRemote)
        self.btnCancel.setObjectName(u"btnCancel")
        self.btnCancel.setMinimumSize(QSize(0, 25))
        self.btnCancel.setMaximumSize(QSize(75, 16777215))

        self.horizontalLayout_3.addWidget(self.btnCancel)


        self.verticalLayout.addLayout(self.horizontalLayout_3)


        self.retranslateUi(DialogEditRemote)

        QMetaObject.connectSlotsByName(DialogEditRemote)
    # setupUi

    def retranslateUi(self, DialogEditRemote):
        DialogEditRemote.setWindowTitle(QCoreApplication.translate("DialogEditRemote", u"Dialog", None))
        self.label.setText(QCoreApplication.translate("DialogEditRemote", u"Name", None))
        self.label_2.setText(QCoreApplication.translate("DialogEditRemote", u"URL", None))
        self.checkBoxVerifySSL.setText(QCoreApplication.translate("DialogEditRemote", u"Verify SSL", None))
        self.labelInfo.setText("")
        self.btnOK.setText(QCoreApplication.translate("DialogEditRemote", u"OK", None))
        self.btnCancel.setText(QCoreApplication.translate("DialogEditRemote", u"Cancel", None))
    # retranslateUi

