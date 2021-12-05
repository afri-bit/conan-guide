# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'about.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

from conanguide.ui.res import resources_rc

class Ui_DialogAbout(object):
    def setupUi(self, DialogAbout):
        if not DialogAbout.objectName():
            DialogAbout.setObjectName(u"DialogAbout")
        DialogAbout.setWindowModality(Qt.NonModal)
        DialogAbout.resize(550, 280)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(DialogAbout.sizePolicy().hasHeightForWidth())
        DialogAbout.setSizePolicy(sizePolicy)
        DialogAbout.setMinimumSize(QSize(550, 280))
        DialogAbout.setMaximumSize(QSize(550, 280))
        DialogAbout.setBaseSize(QSize(550, 280))
        DialogAbout.setContextMenuPolicy(Qt.NoContextMenu)
        self.horizontalLayout_5 = QHBoxLayout(DialogAbout)
        self.horizontalLayout_5.setSpacing(10)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(2, 2, 2, 2)
        self.labelConanGuideIcon = QLabel(DialogAbout)
        self.labelConanGuideIcon.setObjectName(u"labelConanGuideIcon")
        sizePolicy.setHeightForWidth(self.labelConanGuideIcon.sizePolicy().hasHeightForWidth())
        self.labelConanGuideIcon.setSizePolicy(sizePolicy)
        self.labelConanGuideIcon.setMaximumSize(QSize(180, 180))
        self.labelConanGuideIcon.setPixmap(QPixmap(u":/general/icon/conan_guide_icon.png"))
        self.labelConanGuideIcon.setScaledContents(True)

        self.horizontalLayout_5.addWidget(self.labelConanGuideIcon)

        self.frame_2 = QFrame(DialogAbout)
        self.frame_2.setObjectName(u"frame_2")
        sizePolicy.setHeightForWidth(self.frame_2.sizePolicy().hasHeightForWidth())
        self.frame_2.setSizePolicy(sizePolicy)
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.frame_2)
        self.verticalLayout.setSpacing(3)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.labelTitle = QLabel(self.frame_2)
        self.labelTitle.setObjectName(u"labelTitle")
        font = QFont()
        font.setFamily(u"Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.labelTitle.setFont(font)
        self.labelTitle.setFrameShape(QFrame.NoFrame)
        self.labelTitle.setScaledContents(False)

        self.verticalLayout.addWidget(self.labelTitle)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label = QLabel(self.frame_2)
        self.label.setObjectName(u"label")

        self.horizontalLayout.addWidget(self.label)

        self.labelConanGuideVersion = QLabel(self.frame_2)
        self.labelConanGuideVersion.setObjectName(u"labelConanGuideVersion")

        self.horizontalLayout.addWidget(self.labelConanGuideVersion)

        self.horizontalSpacer_2 = QSpacerItem(40, 10, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.labelURL = QLabel(self.frame_2)
        self.labelURL.setObjectName(u"labelURL")
        self.labelURL.setWordWrap(True)
        self.labelURL.setOpenExternalLinks(True)

        self.verticalLayout.addWidget(self.labelURL)

        self.labelDescription = QLabel(self.frame_2)
        self.labelDescription.setObjectName(u"labelDescription")
        self.labelDescription.setWordWrap(True)

        self.verticalLayout.addWidget(self.labelDescription)

        self.verticalSpacer_5 = QSpacerItem(20, 10, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout.addItem(self.verticalSpacer_5)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setSpacing(2)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalSpacer_5 = QSpacerItem(10, 10, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_5)

        self.label_2 = QLabel(self.frame_2)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout_2.addWidget(self.label_2)

        self.labelPythonVersion = QLabel(self.frame_2)
        self.labelPythonVersion.setObjectName(u"labelPythonVersion")

        self.horizontalLayout_2.addWidget(self.labelPythonVersion)

        self.horizontalSpacer_3 = QSpacerItem(40, 10, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_3)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setSpacing(2)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalSpacer_6 = QSpacerItem(10, 10, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_6)

        self.label_3 = QLabel(self.frame_2)
        self.label_3.setObjectName(u"label_3")

        self.horizontalLayout_3.addWidget(self.label_3)

        self.labelConanVersion = QLabel(self.frame_2)
        self.labelConanVersion.setObjectName(u"labelConanVersion")

        self.horizontalLayout_3.addWidget(self.labelConanVersion)

        self.horizontalSpacer_4 = QSpacerItem(40, 10, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_4)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.verticalSpacer = QSpacerItem(20, 10, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.labelLicense = QLabel(self.frame_2)
        self.labelLicense.setObjectName(u"labelLicense")
        self.labelLicense.setWordWrap(True)

        self.verticalLayout.addWidget(self.labelLicense)

        self.verticalSpacer_2 = QSpacerItem(20, 5, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout.addItem(self.verticalSpacer_2)

        self.label_4 = QLabel(self.frame_2)
        self.label_4.setObjectName(u"label_4")

        self.verticalLayout.addWidget(self.label_4)

        self.frame = QFrame(self.frame_2)
        self.frame.setObjectName(u"frame")
        self.frame.setMinimumSize(QSize(42, 42))
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame)
        self.horizontalLayout_4.setSpacing(2)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.toolButtonPython = QToolButton(self.frame)
        self.toolButtonPython.setObjectName(u"toolButtonPython")
        self.toolButtonPython.setMinimumSize(QSize(40, 40))
        self.toolButtonPython.setMaximumSize(QSize(40, 40))
        icon = QIcon()
        icon.addFile(u":/general/icon/python_icon.png", QSize(), QIcon.Normal, QIcon.Off)
        self.toolButtonPython.setIcon(icon)
        self.toolButtonPython.setIconSize(QSize(30, 30))

        self.horizontalLayout_4.addWidget(self.toolButtonPython)

        self.toolButtonConan = QToolButton(self.frame)
        self.toolButtonConan.setObjectName(u"toolButtonConan")
        self.toolButtonConan.setMinimumSize(QSize(40, 40))
        self.toolButtonConan.setMaximumSize(QSize(40, 40))
        icon1 = QIcon()
        icon1.addFile(u":/general/icon/conan_io_icon.png", QSize(), QIcon.Normal, QIcon.Off)
        self.toolButtonConan.setIcon(icon1)
        self.toolButtonConan.setIconSize(QSize(30, 30))

        self.horizontalLayout_4.addWidget(self.toolButtonConan)

        self.toolButtonQt = QToolButton(self.frame)
        self.toolButtonQt.setObjectName(u"toolButtonQt")
        self.toolButtonQt.setMinimumSize(QSize(40, 40))
        self.toolButtonQt.setMaximumSize(QSize(40, 40))
        icon2 = QIcon()
        icon2.addFile(u":/general/icon/qt_icon.png", QSize(), QIcon.Normal, QIcon.Off)
        self.toolButtonQt.setIcon(icon2)
        self.toolButtonQt.setIconSize(QSize(30, 30))

        self.horizontalLayout_4.addWidget(self.toolButtonQt)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer)


        self.verticalLayout.addWidget(self.frame)

        self.frame_3 = QFrame(self.frame_2)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.frame_3)
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.pushButtonOK = QPushButton(self.frame_3)
        self.pushButtonOK.setObjectName(u"pushButtonOK")
        self.pushButtonOK.setMinimumSize(QSize(0, 25))

        self.horizontalLayout_6.addWidget(self.pushButtonOK)


        self.verticalLayout.addWidget(self.frame_3)


        self.horizontalLayout_5.addWidget(self.frame_2)


        self.retranslateUi(DialogAbout)

        QMetaObject.connectSlotsByName(DialogAbout)
    # setupUi

    def retranslateUi(self, DialogAbout):
        DialogAbout.setWindowTitle(QCoreApplication.translate("DialogAbout", u"Dialog", None))
        self.labelConanGuideIcon.setText("")
        self.labelTitle.setText(QCoreApplication.translate("DialogAbout", u"Conan GUIde", None))
        self.label.setText(QCoreApplication.translate("DialogAbout", u"Version", None))
        self.labelConanGuideVersion.setText(QCoreApplication.translate("DialogAbout", u"0.0.0", None))
        self.labelURL.setText(QCoreApplication.translate("DialogAbout", u"<html><head/><body><p><a href=\"https://github.com/afri-bit/conan-guide\"><span style=\" text-decoration: underline; color:#0000ff;\">https://github.com/afri-bit/conan-guide</span></a></p></body></html>", None))
        self.labelDescription.setText(QCoreApplication.translate("DialogAbout", u"Conan GUIde is Qt based Graphical User Interface (GUI) to interact with conan local cache.", None))
        self.label_2.setText(QCoreApplication.translate("DialogAbout", u"Python Version:", None))
        self.labelPythonVersion.setText(QCoreApplication.translate("DialogAbout", u"0.0.0", None))
        self.label_3.setText(QCoreApplication.translate("DialogAbout", u"Conan Version:", None))
        self.labelConanVersion.setText(QCoreApplication.translate("DialogAbout", u"0.0.0", None))
        self.labelLicense.setText(QCoreApplication.translate("DialogAbout", u"Conan GUIde is licensed under the MIT license.\n"
"Copyright (C) 2021, Afrizal Herlambang", None))
        self.label_4.setText(QCoreApplication.translate("DialogAbout", u"Powered by:", None))
        self.toolButtonPython.setText("")
        self.toolButtonConan.setText("")
        self.toolButtonQt.setText("")
        self.pushButtonOK.setText(QCoreApplication.translate("DialogAbout", u"OK", None))
    # retranslateUi

