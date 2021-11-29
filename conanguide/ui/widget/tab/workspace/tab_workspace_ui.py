# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'tab_workspace.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

from conanguide.ui.res import resources_rc

class Ui_TabWorkspace(object):
    def setupUi(self, TabWorkspace):
        if not TabWorkspace.objectName():
            TabWorkspace.setObjectName(u"TabWorkspace")
        TabWorkspace.resize(913, 576)
        self.verticalLayout = QVBoxLayout(TabWorkspace)
        self.verticalLayout.setSpacing(2)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame_7 = QFrame(TabWorkspace)
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
        self.toolButtonRefresh.setMinimumSize(QSize(35, 35))
        icon = QIcon()
        icon.addFile(u":/icon/light/refresh.png", QSize(), QIcon.Normal, QIcon.Off)
        self.toolButtonRefresh.setIcon(icon)
        self.toolButtonRefresh.setCheckable(False)
        self.toolButtonRefresh.setChecked(False)
        self.toolButtonRefresh.setAutoRaise(False)

        self.horizontalLayout_16.addWidget(self.toolButtonRefresh)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_16.addItem(self.horizontalSpacer_2)


        self.verticalLayout.addWidget(self.frame_7)

        self.splitter = QSplitter(TabWorkspace)
        self.splitter.setObjectName(u"splitter")
        self.splitter.setOrientation(Qt.Vertical)
        self.frame_24 = QFrame(self.splitter)
        self.frame_24.setObjectName(u"frame_24")
        self.frame_24.setMaximumSize(QSize(16777215, 228))
        self.frame_24.setFrameShape(QFrame.StyledPanel)
        self.frame_24.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_24)
        self.verticalLayout_3.setSpacing(2)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(2, 2, 2, 2)
        self.frame_4 = QFrame(self.frame_24)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.frame_4)
        self.horizontalLayout_5.setSpacing(5)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(2, 2, 2, 2)
        self.label_4 = QLabel(self.frame_4)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setMinimumSize(QSize(75, 0))

        self.horizontalLayout_5.addWidget(self.label_4)

        self.lineEditUser = QLineEdit(self.frame_4)
        self.lineEditUser.setObjectName(u"lineEditUser")

        self.horizontalLayout_5.addWidget(self.lineEditUser)

        self.label_14 = QLabel(self.frame_4)
        self.label_14.setObjectName(u"label_14")

        self.horizontalLayout_5.addWidget(self.label_14)

        self.label_13 = QLabel(self.frame_4)
        self.label_13.setObjectName(u"label_13")

        self.horizontalLayout_5.addWidget(self.label_13)

        self.lineEditChannel = QLineEdit(self.frame_4)
        self.lineEditChannel.setObjectName(u"lineEditChannel")

        self.horizontalLayout_5.addWidget(self.lineEditChannel)


        self.verticalLayout_3.addWidget(self.frame_4)

        self.frame_8 = QFrame(self.frame_24)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.frame_8)
        self.horizontalLayout_6.setSpacing(5)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(2, 2, 2, 2)
        self.label_5 = QLabel(self.frame_8)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setMinimumSize(QSize(75, 0))

        self.horizontalLayout_6.addWidget(self.label_5)

        self.lineEditRecipePath = QLineEdit(self.frame_8)
        self.lineEditRecipePath.setObjectName(u"lineEditRecipePath")
        self.lineEditRecipePath.setMinimumSize(QSize(0, 0))
        self.lineEditRecipePath.setReadOnly(False)

        self.horizontalLayout_6.addWidget(self.lineEditRecipePath)

        self.toolBtnExplorerRecipePath = QToolButton(self.frame_8)
        self.toolBtnExplorerRecipePath.setObjectName(u"toolBtnExplorerRecipePath")
        sizePolicy1 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.toolBtnExplorerRecipePath.sizePolicy().hasHeightForWidth())
        self.toolBtnExplorerRecipePath.setSizePolicy(sizePolicy1)
        self.toolBtnExplorerRecipePath.setMinimumSize(QSize(0, 0))

        self.horizontalLayout_6.addWidget(self.toolBtnExplorerRecipePath)


        self.verticalLayout_3.addWidget(self.frame_8)

        self.frame_9 = QFrame(self.frame_24)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setFrameShape(QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.frame_9)
        self.horizontalLayout_7.setSpacing(5)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(2, 2, 2, 2)
        self.label_6 = QLabel(self.frame_9)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setMinimumSize(QSize(75, 0))

        self.horizontalLayout_7.addWidget(self.label_6)

        self.lineEditInstallPath = QLineEdit(self.frame_9)
        self.lineEditInstallPath.setObjectName(u"lineEditInstallPath")

        self.horizontalLayout_7.addWidget(self.lineEditInstallPath)

        self.toolBtnExplorerInstallPath = QToolButton(self.frame_9)
        self.toolBtnExplorerInstallPath.setObjectName(u"toolBtnExplorerInstallPath")

        self.horizontalLayout_7.addWidget(self.toolBtnExplorerInstallPath)


        self.verticalLayout_3.addWidget(self.frame_9)

        self.frame_10 = QFrame(self.frame_24)
        self.frame_10.setObjectName(u"frame_10")
        self.frame_10.setFrameShape(QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.frame_10)
        self.horizontalLayout_8.setSpacing(5)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(2, 2, 2, 2)
        self.label_7 = QLabel(self.frame_10)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setMinimumSize(QSize(75, 0))

        self.horizontalLayout_8.addWidget(self.label_7)

        self.lineEditBuildPath = QLineEdit(self.frame_10)
        self.lineEditBuildPath.setObjectName(u"lineEditBuildPath")

        self.horizontalLayout_8.addWidget(self.lineEditBuildPath)

        self.toolBtnExplorerBuildPath = QToolButton(self.frame_10)
        self.toolBtnExplorerBuildPath.setObjectName(u"toolBtnExplorerBuildPath")

        self.horizontalLayout_8.addWidget(self.toolBtnExplorerBuildPath)


        self.verticalLayout_3.addWidget(self.frame_10)

        self.frame_11 = QFrame(self.frame_24)
        self.frame_11.setObjectName(u"frame_11")
        self.frame_11.setFrameShape(QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_9 = QHBoxLayout(self.frame_11)
        self.horizontalLayout_9.setSpacing(5)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setContentsMargins(2, 2, 2, 2)
        self.label_8 = QLabel(self.frame_11)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setMinimumSize(QSize(75, 0))

        self.horizontalLayout_9.addWidget(self.label_8)

        self.lineEditSourcePath = QLineEdit(self.frame_11)
        self.lineEditSourcePath.setObjectName(u"lineEditSourcePath")

        self.horizontalLayout_9.addWidget(self.lineEditSourcePath)

        self.toolBtnExplorerSourcePath = QToolButton(self.frame_11)
        self.toolBtnExplorerSourcePath.setObjectName(u"toolBtnExplorerSourcePath")

        self.horizontalLayout_9.addWidget(self.toolBtnExplorerSourcePath)


        self.verticalLayout_3.addWidget(self.frame_11)

        self.frame_13 = QFrame(self.frame_24)
        self.frame_13.setObjectName(u"frame_13")
        self.frame_13.setFrameShape(QFrame.StyledPanel)
        self.frame_13.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_12 = QHBoxLayout(self.frame_13)
        self.horizontalLayout_12.setSpacing(5)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.horizontalLayout_12.setContentsMargins(2, 2, 2, 2)
        self.label_11 = QLabel(self.frame_13)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setMinimumSize(QSize(75, 0))

        self.horizontalLayout_12.addWidget(self.label_11)

        self.lineEditPackageExpPath = QLineEdit(self.frame_13)
        self.lineEditPackageExpPath.setObjectName(u"lineEditPackageExpPath")

        self.horizontalLayout_12.addWidget(self.lineEditPackageExpPath)

        self.toolBtnExplorerPackagePath = QToolButton(self.frame_13)
        self.toolBtnExplorerPackagePath.setObjectName(u"toolBtnExplorerPackagePath")

        self.horizontalLayout_12.addWidget(self.toolBtnExplorerPackagePath)


        self.verticalLayout_3.addWidget(self.frame_13)

        self.frame_12 = QFrame(self.frame_24)
        self.frame_12.setObjectName(u"frame_12")
        self.frame_12.setFrameShape(QFrame.StyledPanel)
        self.frame_12.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_10 = QHBoxLayout(self.frame_12)
        self.horizontalLayout_10.setSpacing(5)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalLayout_10.setContentsMargins(2, 2, 2, 2)
        self.label_9 = QLabel(self.frame_12)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setMinimumSize(QSize(75, 0))

        self.horizontalLayout_10.addWidget(self.label_9)

        self.lineEditAdditionalParams = QLineEdit(self.frame_12)
        self.lineEditAdditionalParams.setObjectName(u"lineEditAdditionalParams")

        self.horizontalLayout_10.addWidget(self.lineEditAdditionalParams)


        self.verticalLayout_3.addWidget(self.frame_12)

        self.frame_14 = QFrame(self.frame_24)
        self.frame_14.setObjectName(u"frame_14")
        self.frame_14.setFrameShape(QFrame.StyledPanel)
        self.frame_14.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_13 = QHBoxLayout(self.frame_14)
        self.horizontalLayout_13.setSpacing(5)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.horizontalLayout_13.setContentsMargins(2, 2, 2, 2)
        self.label_12 = QLabel(self.frame_14)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setMinimumSize(QSize(75, 0))
        self.label_12.setMaximumSize(QSize(50, 16777215))

        self.horizontalLayout_13.addWidget(self.label_12)

        self.comboBoxProfile = QComboBox(self.frame_14)
        self.comboBoxProfile.setObjectName(u"comboBoxProfile")

        self.horizontalLayout_13.addWidget(self.comboBoxProfile)


        self.verticalLayout_3.addWidget(self.frame_14)

        self.splitter.addWidget(self.frame_24)
        self.groupBox_4 = QGroupBox(self.splitter)
        self.groupBox_4.setObjectName(u"groupBox_4")
        self.horizontalLayout = QHBoxLayout(self.groupBox_4)
        self.horizontalLayout.setSpacing(2)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(2, 2, 2, 2)
        self.frame_5 = QFrame(self.groupBox_4)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.frame_5)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.toolButtonClearConsole = QToolButton(self.frame_5)
        self.toolButtonClearConsole.setObjectName(u"toolButtonClearConsole")
        self.toolButtonClearConsole.setMinimumSize(QSize(25, 25))
        icon1 = QIcon()
        icon1.addFile(u":/icon/light/garbage_can.png", QSize(), QIcon.Normal, QIcon.Off)
        self.toolButtonClearConsole.setIcon(icon1)
        self.toolButtonClearConsole.setCheckable(False)

        self.verticalLayout_5.addWidget(self.toolButtonClearConsole)

        self.toolButtonConsoleScrollToEnd = QToolButton(self.frame_5)
        self.toolButtonConsoleScrollToEnd.setObjectName(u"toolButtonConsoleScrollToEnd")
        self.toolButtonConsoleScrollToEnd.setMinimumSize(QSize(25, 25))
        icon2 = QIcon()
        icon2.addFile(u":/icon/light/scroll_to_end.png", QSize(), QIcon.Normal, QIcon.Off)
        self.toolButtonConsoleScrollToEnd.setIcon(icon2)
        self.toolButtonConsoleScrollToEnd.setCheckable(True)
        self.toolButtonConsoleScrollToEnd.setChecked(True)

        self.verticalLayout_5.addWidget(self.toolButtonConsoleScrollToEnd)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_5.addItem(self.verticalSpacer_2)


        self.horizontalLayout.addWidget(self.frame_5)

        self.console = QPlainTextEdit(self.groupBox_4)
        self.console.setObjectName(u"console")
        font = QFont()
        font.setFamily(u"Consolas")
        font.setPointSize(8)
        self.console.setFont(font)
        self.console.setReadOnly(True)
        self.console.setTextInteractionFlags(Qt.TextSelectableByMouse)
        self.console.setCenterOnScroll(False)

        self.horizontalLayout.addWidget(self.console)

        self.splitter.addWidget(self.groupBox_4)

        self.verticalLayout.addWidget(self.splitter)


        self.retranslateUi(TabWorkspace)

        QMetaObject.connectSlotsByName(TabWorkspace)
    # setupUi

    def retranslateUi(self, TabWorkspace):
        TabWorkspace.setWindowTitle(QCoreApplication.translate("TabWorkspace", u"Form", None))
#if QT_CONFIG(tooltip)
        self.toolButtonRefresh.setToolTip(QCoreApplication.translate("TabWorkspace", u"Refresh", None))
#endif // QT_CONFIG(tooltip)
        self.toolButtonRefresh.setText("")
        self.label_4.setText(QCoreApplication.translate("TabWorkspace", u"User", None))
        self.label_14.setText(QCoreApplication.translate("TabWorkspace", u"/", None))
        self.label_13.setText(QCoreApplication.translate("TabWorkspace", u"Channel", None))
        self.label_5.setText(QCoreApplication.translate("TabWorkspace", u"Recipe Path", None))
        self.toolBtnExplorerRecipePath.setText(QCoreApplication.translate("TabWorkspace", u"...", None))
        self.label_6.setText(QCoreApplication.translate("TabWorkspace", u"Install Path", None))
        self.toolBtnExplorerInstallPath.setText(QCoreApplication.translate("TabWorkspace", u"...", None))
        self.label_7.setText(QCoreApplication.translate("TabWorkspace", u"Build Path", None))
        self.toolBtnExplorerBuildPath.setText(QCoreApplication.translate("TabWorkspace", u"...", None))
        self.label_8.setText(QCoreApplication.translate("TabWorkspace", u"Source Path", None))
        self.toolBtnExplorerSourcePath.setText(QCoreApplication.translate("TabWorkspace", u"...", None))
        self.label_11.setText(QCoreApplication.translate("TabWorkspace", u"Package Path", None))
        self.toolBtnExplorerPackagePath.setText(QCoreApplication.translate("TabWorkspace", u"...", None))
        self.label_9.setText(QCoreApplication.translate("TabWorkspace", u"Parameter", None))
        self.label_12.setText(QCoreApplication.translate("TabWorkspace", u"Profile", None))
        self.groupBox_4.setTitle(QCoreApplication.translate("TabWorkspace", u"Console", None))
        self.toolButtonClearConsole.setText("")
        self.toolButtonConsoleScrollToEnd.setText("")
        self.console.setPlainText("")
    # retranslateUi

