# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'edit_name.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

from conanguide.ui.res import resources_rc

class Ui_DialogEditName(object):
    def setupUi(self, DialogEditName):
        if not DialogEditName.objectName():
            DialogEditName.setObjectName(u"DialogEditName")
        DialogEditName.setWindowModality(Qt.NonModal)
        DialogEditName.resize(400, 63)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(DialogEditName.sizePolicy().hasHeightForWidth())
        DialogEditName.setSizePolicy(sizePolicy)
        DialogEditName.setMinimumSize(QSize(400, 63))
        DialogEditName.setMaximumSize(QSize(400, 64))
        DialogEditName.setBaseSize(QSize(350, 63))
        icon = QIcon()
        icon.addFile(u":/general/icon/conan_guide_icon.png", QSize(), QIcon.Normal, QIcon.Off)
        DialogEditName.setWindowIcon(icon)
        DialogEditName.setSizeGripEnabled(False)
        DialogEditName.setModal(False)
        self.verticalLayout = QVBoxLayout(DialogEditName)
        self.verticalLayout.setSpacing(2)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(5, 5, 5, 5)
        self.lineEdit = QLineEdit(DialogEditName)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setMinimumSize(QSize(0, 25))

        self.verticalLayout.addWidget(self.lineEdit)

        self.frame = QFrame(DialogEditName)
        self.frame.setObjectName(u"frame")
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.labelInfo = QLabel(self.frame)
        self.labelInfo.setObjectName(u"labelInfo")
        self.labelInfo.setMinimumSize(QSize(0, 22))
        self.labelInfo.setMaximumSize(QSize(16777215, 22))

        self.horizontalLayout.addWidget(self.labelInfo)

        self.btnOK = QPushButton(self.frame)
        self.btnOK.setObjectName(u"btnOK")
        self.btnOK.setMinimumSize(QSize(0, 25))
        self.btnOK.setMaximumSize(QSize(75, 16777215))

        self.horizontalLayout.addWidget(self.btnOK)

        self.btnCancel = QPushButton(self.frame)
        self.btnCancel.setObjectName(u"btnCancel")
        self.btnCancel.setMinimumSize(QSize(0, 25))
        self.btnCancel.setMaximumSize(QSize(75, 16777215))

        self.horizontalLayout.addWidget(self.btnCancel)


        self.verticalLayout.addWidget(self.frame)


        self.retranslateUi(DialogEditName)

        QMetaObject.connectSlotsByName(DialogEditName)
    # setupUi

    def retranslateUi(self, DialogEditName):
        DialogEditName.setWindowTitle(QCoreApplication.translate("DialogEditName", u"Dialog", None))
        self.labelInfo.setText("")
        self.btnOK.setText(QCoreApplication.translate("DialogEditName", u"OK", None))
        self.btnCancel.setText(QCoreApplication.translate("DialogEditName", u"Cancel", None))
    # re# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'edit_name.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

from conanguide.ui.res import resources_rc

class Ui_DialogEditName(object):
    def setupUi(self, DialogEditName):
        if not DialogEditName.objectName():
            DialogEditName.setObjectName(u"DialogEditName")
        DialogEditName.setWindowModality(Qt.NonModal)
        DialogEditName.resize(400, 63)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(DialogEditName.sizePolicy().hasHeightForWidth())
        DialogEditName.setSizePolicy(sizePolicy)
        DialogEditName.setMinimumSize(QSize(400, 63))
        DialogEditName.setMaximumSize(QSize(400, 64))
        DialogEditName.setBaseSize(QSize(350, 63))
        icon = QIcon()
        icon.addFile(u":/general/icon/conan_guide_icon.png", QSize(), QIcon.Normal, QIcon.Off)
        DialogEditName.setWindowIcon(icon)
        DialogEditName.setSizeGripEnabled(False)
        DialogEditName.setModal(False)
        self.verticalLayout = QVBoxLayout(DialogEditName)
        self.verticalLayout.setSpacing(2)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(5, 5, 5, 5)
        self.lineEdit = QLineEdit(DialogEditName)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setMinimumSize(QSize(0, 25))

        self.verticalLayout.addWidget(self.lineEdit)

        self.frame = QFrame(DialogEditName)
        self.frame.setObjectName(u"frame")
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.labelInfo = QLabel(self.frame)
        self.labelInfo.setObjectName(u"labelInfo")
        self.labelInfo.setMinimumSize(QSize(0, 22))
        self.labelInfo.setMaximumSize(QSize(16777215, 22))

        self.horizontalLayout.addWidget(self.labelInfo)

        self.btnOK = QPushButton(self.frame)
        self.btnOK.setObjectName(u"btnOK")
        self.btnOK.setMinimumSize(QSize(0, 25))
        self.btnOK.setMaximumSize(QSize(75, 16777215))

        self.horizontalLayout.addWidget(self.btnOK)

        self.btnCancel = QPushButton(self.frame)
        self.btnCancel.setObjectName(u"btnCancel")
        self.btnCancel.setMinimumSize(QSize(0, 25))
        self.btnCancel.setMaximumSize(QSize(75, 16777215))

        self.horizontalLayout.addWidget(self.btnCancel)


        self.verticalLayout.addWidget(self.frame)


        self.retranslateUi(DialogEditName)

        QMetaObject.connectSlotsByName(DialogEditName)
    # setupUi

    def retranslateUi(self, DialogEditName):
        DialogEditName.setWindowTitle(QCoreApplication.translate("DialogEditName", u"Dialog", None))
        self.labelInfo.setText("")
        self.btnOK.setText(QCoreApplication.translate("DialogEditName", u"OK", None))
        self.btnCancel.setText(QCoreApplication.translate("DialogEditName", u"Cancel", None))
    # retranslateUi

