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
        TabWorkspace.resize(999, 710)
        self.verticalLayout = QVBoxLayout(TabWorkspace)
        self.verticalLayout.setSpacing(5)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.frameToolbar = QFrame(TabWorkspace)
        self.frameToolbar.setObjectName(u"frameToolbar")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frameToolbar.sizePolicy().hasHeightForWidth())
        self.frameToolbar.setSizePolicy(sizePolicy)
        self.frameToolbar.setFrameShape(QFrame.StyledPanel)
        self.frameToolbar.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_16 = QHBoxLayout(self.frameToolbar)
        self.horizontalLayout_16.setSpacing(0)
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.horizontalLayout_16.setContentsMargins(2, 2, 0, 0)
        self.toolButtonRefresh = QToolButton(self.frameToolbar)
        self.toolButtonRefresh.setObjectName(u"toolButtonRefresh")
        self.toolButtonRefresh.setMinimumSize(QSize(25, 25))
        icon = QIcon()
        icon.addFile(u":/icon/light/refresh.png", QSize(), QIcon.Normal, QIcon.Off)
        self.toolButtonRefresh.setIcon(icon)
        self.toolButtonRefresh.setCheckable(False)
        self.toolButtonRefresh.setChecked(False)
        self.toolButtonRefresh.setAutoRaise(False)

        self.horizontalLayout_16.addWidget(self.toolButtonRefresh)

        self.horizontalSpacer = QSpacerItem(10, 20, QSizePolicy.Minimum, QSizePolicy.Minimum)

        self.horizontalLayout_16.addItem(self.horizontalSpacer)

        self.toolButtonSaveConfiguration = QToolButton(self.frameToolbar)
        self.toolButtonSaveConfiguration.setObjectName(u"toolButtonSaveConfiguration")
        self.toolButtonSaveConfiguration.setMinimumSize(QSize(25, 25))
        icon1 = QIcon()
        icon1.addFile(u":/icon/light/save.png", QSize(), QIcon.Normal, QIcon.Off)
        self.toolButtonSaveConfiguration.setIcon(icon1)

        self.horizontalLayout_16.addWidget(self.toolButtonSaveConfiguration)

        self.toolButtonLoadConfiguration = QToolButton(self.frameToolbar)
        self.toolButtonLoadConfiguration.setObjectName(u"toolButtonLoadConfiguration")
        self.toolButtonLoadConfiguration.setMinimumSize(QSize(25, 25))
        icon2 = QIcon()
        icon2.addFile(u":/icon/light/open.png", QSize(), QIcon.Normal, QIcon.Off)
        self.toolButtonLoadConfiguration.setIcon(icon2)

        self.horizontalLayout_16.addWidget(self.toolButtonLoadConfiguration)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_16.addItem(self.horizontalSpacer_2)


        self.verticalLayout.addWidget(self.frameToolbar)

        self.splitter = QSplitter(TabWorkspace)
        self.splitter.setObjectName(u"splitter")
        self.splitter.setOrientation(Qt.Vertical)
        self.frameWorkspace = QFrame(self.splitter)
        self.frameWorkspace.setObjectName(u"frameWorkspace")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Minimum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.frameWorkspace.sizePolicy().hasHeightForWidth())
        self.frameWorkspace.setSizePolicy(sizePolicy1)
        self.frameWorkspace.setMaximumSize(QSize(16777215, 268))
        self.frameWorkspace.setFrameShape(QFrame.StyledPanel)
        self.frameWorkspace.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frameWorkspace)
        self.verticalLayout_3.setSpacing(2)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.verticalLayout_3.setContentsMargins(2, 2, 2, 2)
        self.frame_4 = QFrame(self.frameWorkspace)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setMinimumSize(QSize(0, 30))
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
        self.lineEditUser.setMinimumSize(QSize(0, 25))

        self.horizontalLayout_5.addWidget(self.lineEditUser)

        self.label_14 = QLabel(self.frame_4)
        self.label_14.setObjectName(u"label_14")

        self.horizontalLayout_5.addWidget(self.label_14)

        self.label_13 = QLabel(self.frame_4)
        self.label_13.setObjectName(u"label_13")

        self.horizontalLayout_5.addWidget(self.label_13)

        self.lineEditChannel = QLineEdit(self.frame_4)
        self.lineEditChannel.setObjectName(u"lineEditChannel")
        self.lineEditChannel.setMinimumSize(QSize(0, 25))

        self.horizontalLayout_5.addWidget(self.lineEditChannel)


        self.verticalLayout_3.addWidget(self.frame_4)

        self.frame_8 = QFrame(self.frameWorkspace)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setMinimumSize(QSize(0, 30))
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
        self.lineEditRecipePath.setMinimumSize(QSize(0, 25))
        self.lineEditRecipePath.setReadOnly(False)

        self.horizontalLayout_6.addWidget(self.lineEditRecipePath)

        self.toolBtnExplorerRecipePath = QToolButton(self.frame_8)
        self.toolBtnExplorerRecipePath.setObjectName(u"toolBtnExplorerRecipePath")
        sizePolicy2 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.toolBtnExplorerRecipePath.sizePolicy().hasHeightForWidth())
        self.toolBtnExplorerRecipePath.setSizePolicy(sizePolicy2)
        self.toolBtnExplorerRecipePath.setMinimumSize(QSize(0, 25))

        self.horizontalLayout_6.addWidget(self.toolBtnExplorerRecipePath)


        self.verticalLayout_3.addWidget(self.frame_8)

        self.frame_9 = QFrame(self.frameWorkspace)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setMinimumSize(QSize(0, 30))
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
        self.lineEditInstallPath.setMinimumSize(QSize(0, 25))

        self.horizontalLayout_7.addWidget(self.lineEditInstallPath)

        self.toolBtnExplorerInstallPath = QToolButton(self.frame_9)
        self.toolBtnExplorerInstallPath.setObjectName(u"toolBtnExplorerInstallPath")
        self.toolBtnExplorerInstallPath.setMinimumSize(QSize(0, 25))

        self.horizontalLayout_7.addWidget(self.toolBtnExplorerInstallPath)


        self.verticalLayout_3.addWidget(self.frame_9)

        self.frame_10 = QFrame(self.frameWorkspace)
        self.frame_10.setObjectName(u"frame_10")
        sizePolicy3 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.frame_10.sizePolicy().hasHeightForWidth())
        self.frame_10.setSizePolicy(sizePolicy3)
        self.frame_10.setMinimumSize(QSize(0, 30))
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
        self.lineEditBuildPath.setMinimumSize(QSize(0, 25))

        self.horizontalLayout_8.addWidget(self.lineEditBuildPath)

        self.toolBtnExplorerBuildPath = QToolButton(self.frame_10)
        self.toolBtnExplorerBuildPath.setObjectName(u"toolBtnExplorerBuildPath")
        self.toolBtnExplorerBuildPath.setMinimumSize(QSize(0, 25))

        self.horizontalLayout_8.addWidget(self.toolBtnExplorerBuildPath)


        self.verticalLayout_3.addWidget(self.frame_10)

        self.frame_11 = QFrame(self.frameWorkspace)
        self.frame_11.setObjectName(u"frame_11")
        self.frame_11.setMinimumSize(QSize(0, 30))
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
        self.lineEditSourcePath.setMinimumSize(QSize(0, 25))

        self.horizontalLayout_9.addWidget(self.lineEditSourcePath)

        self.toolBtnExplorerSourcePath = QToolButton(self.frame_11)
        self.toolBtnExplorerSourcePath.setObjectName(u"toolBtnExplorerSourcePath")
        self.toolBtnExplorerSourcePath.setMinimumSize(QSize(0, 25))

        self.horizontalLayout_9.addWidget(self.toolBtnExplorerSourcePath)


        self.verticalLayout_3.addWidget(self.frame_11)

        self.frame_13 = QFrame(self.frameWorkspace)
        self.frame_13.setObjectName(u"frame_13")
        self.frame_13.setMinimumSize(QSize(0, 30))
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

        self.lineEditPackagePath = QLineEdit(self.frame_13)
        self.lineEditPackagePath.setObjectName(u"lineEditPackagePath")
        self.lineEditPackagePath.setMinimumSize(QSize(0, 25))

        self.horizontalLayout_12.addWidget(self.lineEditPackagePath)

        self.toolBtnExplorerPackagePath = QToolButton(self.frame_13)
        self.toolBtnExplorerPackagePath.setObjectName(u"toolBtnExplorerPackagePath")
        self.toolBtnExplorerPackagePath.setMinimumSize(QSize(0, 25))

        self.horizontalLayout_12.addWidget(self.toolBtnExplorerPackagePath)


        self.verticalLayout_3.addWidget(self.frame_13)

        self.frame_12 = QFrame(self.frameWorkspace)
        self.frame_12.setObjectName(u"frame_12")
        self.frame_12.setMinimumSize(QSize(0, 30))
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
        self.lineEditAdditionalParams.setMinimumSize(QSize(0, 25))

        self.horizontalLayout_10.addWidget(self.lineEditAdditionalParams)


        self.verticalLayout_3.addWidget(self.frame_12)

        self.frame_14 = QFrame(self.frameWorkspace)
        self.frame_14.setObjectName(u"frame_14")
        self.frame_14.setMinimumSize(QSize(0, 30))
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
        self.comboBoxProfile.setMinimumSize(QSize(0, 25))

        self.horizontalLayout_13.addWidget(self.comboBoxProfile)


        self.verticalLayout_3.addWidget(self.frame_14)

        self.splitter.addWidget(self.frameWorkspace)
        self.groupBox_4 = QGroupBox(self.splitter)
        self.groupBox_4.setObjectName(u"groupBox_4")
        sizePolicy3.setHeightForWidth(self.groupBox_4.sizePolicy().hasHeightForWidth())
        self.groupBox_4.setSizePolicy(sizePolicy3)
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
        icon3 = QIcon()
        icon3.addFile(u":/icon/light/garbage_can.png", QSize(), QIcon.Normal, QIcon.Off)
        self.toolButtonClearConsole.setIcon(icon3)
        self.toolButtonClearConsole.setCheckable(False)

        self.verticalLayout_5.addWidget(self.toolButtonClearConsole)

        self.toolButtonConsoleScrollToEnd = QToolButton(self.frame_5)
        self.toolButtonConsoleScrollToEnd.setObjectName(u"toolButtonConsoleScrollToEnd")
        self.toolButtonConsoleScrollToEnd.setMinimumSize(QSize(25, 25))
        icon4 = QIcon()
        icon4.addFile(u":/icon/light/scroll_to_end.png", QSize(), QIcon.Normal, QIcon.Off)
        self.toolButtonConsoleScrollToEnd.setIcon(icon4)
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

        self.frameStatusBar = QFrame(TabWorkspace)
        self.frameStatusBar.setObjectName(u"frameStatusBar")
        self.frameStatusBar.setMinimumSize(QSize(0, 25))
        self.frameStatusBar.setMaximumSize(QSize(16777215, 25))
        self.frameStatusBar.setFrameShape(QFrame.StyledPanel)
        self.frameStatusBar.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frameStatusBar)
        self.horizontalLayout_2.setSpacing(2)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 2, 0)
        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_3)

        self.labelStatusMessage = QLabel(self.frameStatusBar)
        self.labelStatusMessage.setObjectName(u"labelStatusMessage")

        self.horizontalLayout_2.addWidget(self.labelStatusMessage)

        self.horizontalSpacer_4 = QSpacerItem(5, 20, QSizePolicy.Minimum, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_4)

        self.progressBar = QProgressBar(self.frameStatusBar)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setMinimumSize(QSize(0, 20))
        self.progressBar.setMaximumSize(QSize(200, 16777215))
        self.progressBar.setContextMenuPolicy(Qt.DefaultContextMenu)
        self.progressBar.setValue(0)
        self.progressBar.setTextVisible(False)
        self.progressBar.setInvertedAppearance(False)

        self.horizontalLayout_2.addWidget(self.progressBar)


        self.verticalLayout.addWidget(self.frameStatusBar)


        self.retranslateUi(TabWorkspace)

        QMetaObject.connectSlotsByName(TabWorkspace)
    # setupUi

    def retranslateUi(self, TabWorkspace):
        TabWorkspace.setWindowTitle(QCoreApplication.translate("TabWorkspace", u"Form", None))
#if QT_CONFIG(tooltip)
        self.toolButtonRefresh.setToolTip(QCoreApplication.translate("TabWorkspace", u"Refresh", None))
#endif // QT_CONFIG(tooltip)
        self.toolButtonRefresh.setText("")
#if QT_CONFIG(tooltip)
        self.toolButtonSaveConfiguration.setToolTip(QCoreApplication.translate("TabWorkspace", u"Save Configuration", None))
#endif // QT_CONFIG(tooltip)
        self.toolButtonSaveConfiguration.setText("")
#if QT_CONFIG(tooltip)
        self.toolButtonLoadConfiguration.setToolTip(QCoreApplication.translate("TabWorkspace", u"Load Configuration", None))
#endif // QT_CONFIG(tooltip)
        self.toolButtonLoadConfiguration.setText("")
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
#if QT_CONFIG(tooltip)
        self.toolButtonClearConsole.setToolTip(QCoreApplication.translate("TabWorkspace", u"Clear Console", None))
#endif // QT_CONFIG(tooltip)
        self.toolButtonClearConsole.setText("")
#if QT_CONFIG(tooltip)
        self.toolButtonConsoleScrollToEnd.setToolTip(QCoreApplication.translate("TabWorkspace", u"Scroll to End", None))
#endif // QT_CONFIG(tooltip)
        self.toolButtonConsoleScrollToEnd.setText("")
        self.console.setPlainText("")
        self.labelStatusMessage.setText("")
    # retranslateUi

