# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_window.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

from  . import resources_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(948, 800)
        MainWindow.setMinimumSize(QSize(800, 800))
        MainWindow.setDockOptions(QMainWindow.AllowTabbedDocks|QMainWindow.AnimatedDocks)
        self.actionViewProfile = QAction(MainWindow)
        self.actionViewProfile.setObjectName(u"actionViewProfile")
        self.actionViewProfile.setChecked(False)
        self.actionFileExit = QAction(MainWindow)
        self.actionFileExit.setObjectName(u"actionFileExit")
        self.actionRefresh = QAction(MainWindow)
        self.actionRefresh.setObjectName(u"actionRefresh")
        icon = QIcon()
        icon.addFile(u":/icon/ws_refresh.png", QSize(), QIcon.Normal, QIcon.Off)
        self.actionRefresh.setIcon(icon)
        self.actionConanCreate = QAction(MainWindow)
        self.actionConanCreate.setObjectName(u"actionConanCreate")
        icon1 = QIcon()
        icon1.addFile(u":/icon/conan_create.png", QSize(), QIcon.Normal, QIcon.Off)
        self.actionConanCreate.setIcon(icon1)
        self.actionConanInstall = QAction(MainWindow)
        self.actionConanInstall.setObjectName(u"actionConanInstall")
        icon2 = QIcon()
        icon2.addFile(u":/icon/conan_install.png", QSize(), QIcon.Normal, QIcon.Off)
        self.actionConanInstall.setIcon(icon2)
        self.actionConanBuild = QAction(MainWindow)
        self.actionConanBuild.setObjectName(u"actionConanBuild")
        icon3 = QIcon()
        icon3.addFile(u":/icon/conan_build.png", QSize(), QIcon.Normal, QIcon.Off)
        self.actionConanBuild.setIcon(icon3)
        self.actionConanSource = QAction(MainWindow)
        self.actionConanSource.setObjectName(u"actionConanSource")
        icon4 = QIcon()
        icon4.addFile(u":/icon/conan_source.png", QSize(), QIcon.Normal, QIcon.Off)
        self.actionConanSource.setIcon(icon4)
        self.actionConanPackage = QAction(MainWindow)
        self.actionConanPackage.setObjectName(u"actionConanPackage")
        icon5 = QIcon()
        icon5.addFile(u":/icon/conan_package.png", QSize(), QIcon.Normal, QIcon.Off)
        self.actionConanPackage.setIcon(icon5)
        self.actionConanExport = QAction(MainWindow)
        self.actionConanExport.setObjectName(u"actionConanExport")
        icon6 = QIcon()
        icon6.addFile(u":/icon/conan_export.png", QSize(), QIcon.Normal, QIcon.Off)
        self.actionConanExport.setIcon(icon6)
        self.actionConanExportPackage = QAction(MainWindow)
        self.actionConanExportPackage.setObjectName(u"actionConanExportPackage")
        icon7 = QIcon()
        icon7.addFile(u":/icon/conan_package_export.png", QSize(), QIcon.Normal, QIcon.Off)
        self.actionConanExportPackage.setIcon(icon7)
        self.actionViewPackage = QAction(MainWindow)
        self.actionViewPackage.setObjectName(u"actionViewPackage")
        self.actionViewPackage.setChecked(False)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout_18 = QHBoxLayout(self.centralwidget)
        self.horizontalLayout_18.setSpacing(0)
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.horizontalLayout_18.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.horizontalLayout_18.setContentsMargins(2, 2, 2, 2)
        self.splitter_5 = QSplitter(self.centralwidget)
        self.splitter_5.setObjectName(u"splitter_5")
        self.splitter_5.setFrameShape(QFrame.NoFrame)
        self.splitter_5.setLineWidth(2)
        self.splitter_5.setMidLineWidth(0)
        self.splitter_5.setOrientation(Qt.Horizontal)
        self.splitter_5.setHandleWidth(1)
        self.frame_6 = QFrame(self.splitter_5)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setMinimumSize(QSize(300, 0))
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.frame_6)
        self.verticalLayout.setSpacing(2)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(2, 2, 2, 2)
        self.toolBoxConan = QToolBox(self.frame_6)
        self.toolBoxConan.setObjectName(u"toolBoxConan")
        self.pagePackage = QWidget()
        self.pagePackage.setObjectName(u"pagePackage")
        self.pagePackage.setGeometry(QRect(0, 0, 400, 650))
        self.verticalLayout_2 = QVBoxLayout(self.pagePackage)
        self.verticalLayout_2.setSpacing(2)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(2, 2, 2, 2)
        self.frame_16 = QFrame(self.pagePackage)
        self.frame_16.setObjectName(u"frame_16")
        self.frame_16.setLayoutDirection(Qt.LeftToRight)
        self.frame_16.setFrameShape(QFrame.StyledPanel)
        self.frame_16.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_15 = QHBoxLayout(self.frame_16)
        self.horizontalLayout_15.setSpacing(5)
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.horizontalLayout_15.setContentsMargins(2, 2, 0, 2)
        self.label_10 = QLabel(self.frame_16)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setMinimumSize(QSize(60, 0))
        self.label_10.setMaximumSize(QSize(70, 16777215))

        self.horizontalLayout_15.addWidget(self.label_10)

        self.checkBoxOpenExplorer = QCheckBox(self.frame_16)
        self.checkBoxOpenExplorer.setObjectName(u"checkBoxOpenExplorer")
        self.checkBoxOpenExplorer.setMaximumSize(QSize(90, 16777215))
        self.checkBoxOpenExplorer.setChecked(False)

        self.horizontalLayout_15.addWidget(self.checkBoxOpenExplorer)

        self.checkBoxCopyClipboard = QCheckBox(self.frame_16)
        self.checkBoxCopyClipboard.setObjectName(u"checkBoxCopyClipboard")
        self.checkBoxCopyClipboard.setChecked(True)

        self.horizontalLayout_15.addWidget(self.checkBoxCopyClipboard)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_15.addItem(self.horizontalSpacer)


        self.verticalLayout_2.addWidget(self.frame_16)

        self.splitter_3 = QSplitter(self.pagePackage)
        self.splitter_3.setObjectName(u"splitter_3")
        self.splitter_3.setOrientation(Qt.Vertical)
        self.treeViewRecipe = QTreeView(self.splitter_3)
        self.treeViewRecipe.setObjectName(u"treeViewRecipe")
        self.treeViewRecipe.setEnabled(True)
        self.splitter_3.addWidget(self.treeViewRecipe)
        self.treeViewRecipeInspect = QTreeView(self.splitter_3)
        self.treeViewRecipeInspect.setObjectName(u"treeViewRecipeInspect")
        self.splitter_3.addWidget(self.treeViewRecipeInspect)

        self.verticalLayout_2.addWidget(self.splitter_3)

        self.toolBoxConan.addItem(self.pagePackage, u"Package")
        self.pageProfile = QWidget()
        self.pageProfile.setObjectName(u"pageProfile")
        self.pageProfile.setGeometry(QRect(0, 0, 98, 153))
        self.verticalLayout_4 = QVBoxLayout(self.pageProfile)
        self.verticalLayout_4.setSpacing(2)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(2, 2, 2, 2)
        self.splitter = QSplitter(self.pageProfile)
        self.splitter.setObjectName(u"splitter")
        self.splitter.setOrientation(Qt.Vertical)
        self.listViewProfile = QListView(self.splitter)
        self.listViewProfile.setObjectName(u"listViewProfile")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(50)
        sizePolicy.setHeightForWidth(self.listViewProfile.sizePolicy().hasHeightForWidth())
        self.listViewProfile.setSizePolicy(sizePolicy)
        self.splitter.addWidget(self.listViewProfile)
        self.treeViewProfileDetail = QTreeView(self.splitter)
        self.treeViewProfileDetail.setObjectName(u"treeViewProfileDetail")
        self.splitter.addWidget(self.treeViewProfileDetail)

        self.verticalLayout_4.addWidget(self.splitter)

        self.toolBoxConan.addItem(self.pageProfile, u"Profile")

        self.verticalLayout.addWidget(self.toolBoxConan)

        self.splitter_5.addWidget(self.frame_6)
        self.frame_18 = QFrame(self.splitter_5)
        self.frame_18.setObjectName(u"frame_18")
        self.frame_18.setFrameShape(QFrame.StyledPanel)
        self.frame_18.setFrameShadow(QFrame.Raised)
        self.verticalLayout_10 = QVBoxLayout(self.frame_18)
        self.verticalLayout_10.setSpacing(2)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_10.setContentsMargins(2, 2, 2, 2)
        self.splitter_4 = QSplitter(self.frame_18)
        self.splitter_4.setObjectName(u"splitter_4")
        self.splitter_4.setOrientation(Qt.Vertical)
        self.frameMain = QFrame(self.splitter_4)
        self.frameMain.setObjectName(u"frameMain")
        self.frameMain.setFrameShape(QFrame.StyledPanel)
        self.frameMain.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.frameMain)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.splitter_2 = QSplitter(self.frameMain)
        self.splitter_2.setObjectName(u"splitter_2")
        self.splitter_2.setOrientation(Qt.Vertical)
        self.tabWidget = QTabWidget(self.splitter_2)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setEnabled(True)
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(100)
        sizePolicy1.setHeightForWidth(self.tabWidget.sizePolicy().hasHeightForWidth())
        self.tabWidget.setSizePolicy(sizePolicy1)
        self.tabWidget.setMinimumSize(QSize(0, 0))
        self.tabWidget.setMovable(True)
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.verticalLayout_3 = QVBoxLayout(self.tab)
        self.verticalLayout_3.setSpacing(2)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(2, 2, 2, 2)
        self.groupBox = QGroupBox(self.tab)
        self.groupBox.setObjectName(u"groupBox")
        self.verticalLayout_8 = QVBoxLayout(self.groupBox)
        self.verticalLayout_8.setSpacing(0)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(2, 2, 2, 2)
        self.frame = QFrame(self.groupBox)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame)
        self.horizontalLayout.setSpacing(5)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(2, 2, 2, 2)
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(75, 0))

        self.horizontalLayout.addWidget(self.label)

        self.lineEditConanPath = QLineEdit(self.frame)
        self.lineEditConanPath.setObjectName(u"lineEditConanPath")
        self.lineEditConanPath.setEnabled(True)
        self.lineEditConanPath.setReadOnly(True)

        self.horizontalLayout.addWidget(self.lineEditConanPath)

        self.btnCopyCachePath = QPushButton(self.frame)
        self.btnCopyCachePath.setObjectName(u"btnCopyCachePath")

        self.horizontalLayout.addWidget(self.btnCopyCachePath)

        self.btnOpenCachePath = QPushButton(self.frame)
        self.btnOpenCachePath.setObjectName(u"btnOpenCachePath")

        self.horizontalLayout.addWidget(self.btnOpenCachePath)


        self.verticalLayout_8.addWidget(self.frame)

        self.frame_2 = QFrame(self.groupBox)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_2)
        self.horizontalLayout_2.setSpacing(5)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(2, 2, 2, 2)
        self.label_2 = QLabel(self.frame_2)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMinimumSize(QSize(75, 0))

        self.horizontalLayout_2.addWidget(self.label_2)

        self.lineEditRealPath = QLineEdit(self.frame_2)
        self.lineEditRealPath.setObjectName(u"lineEditRealPath")
        self.lineEditRealPath.setEnabled(True)
        self.lineEditRealPath.setReadOnly(True)

        self.horizontalLayout_2.addWidget(self.lineEditRealPath)

        self.btnCopyRealPath = QPushButton(self.frame_2)
        self.btnCopyRealPath.setObjectName(u"btnCopyRealPath")

        self.horizontalLayout_2.addWidget(self.btnCopyRealPath)

        self.btnOpenRealPath = QPushButton(self.frame_2)
        self.btnOpenRealPath.setObjectName(u"btnOpenRealPath")

        self.horizontalLayout_2.addWidget(self.btnOpenRealPath)


        self.verticalLayout_8.addWidget(self.frame_2)

        self.frame_3 = QFrame(self.groupBox)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_3)
        self.horizontalLayout_3.setSpacing(5)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(2, 2, 2, 2)
        self.label_3 = QLabel(self.frame_3)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMinimumSize(QSize(75, 0))
        self.label_3.setBaseSize(QSize(0, 0))

        self.horizontalLayout_3.addWidget(self.label_3)

        self.lineEditPackagePath = QLineEdit(self.frame_3)
        self.lineEditPackagePath.setObjectName(u"lineEditPackagePath")
        self.lineEditPackagePath.setEnabled(True)
        self.lineEditPackagePath.setReadOnly(True)

        self.horizontalLayout_3.addWidget(self.lineEditPackagePath)

        self.btnCopyPackagePath = QPushButton(self.frame_3)
        self.btnCopyPackagePath.setObjectName(u"btnCopyPackagePath")

        self.horizontalLayout_3.addWidget(self.btnCopyPackagePath)

        self.btnOpenPackagePath = QPushButton(self.frame_3)
        self.btnOpenPackagePath.setObjectName(u"btnOpenPackagePath")

        self.horizontalLayout_3.addWidget(self.btnOpenPackagePath)


        self.verticalLayout_8.addWidget(self.frame_3)


        self.verticalLayout_3.addWidget(self.groupBox)

        self.groupBoxWorkspace = QGroupBox(self.tab)
        self.groupBoxWorkspace.setObjectName(u"groupBoxWorkspace")
        self.verticalLayout_9 = QVBoxLayout(self.groupBoxWorkspace)
        self.verticalLayout_9.setSpacing(0)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(2, 2, 2, 2)
        self.frame_4 = QFrame(self.groupBoxWorkspace)
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


        self.verticalLayout_9.addWidget(self.frame_4)

        self.frame_8 = QFrame(self.groupBoxWorkspace)
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
        self.lineEditRecipePath.setReadOnly(False)

        self.horizontalLayout_6.addWidget(self.lineEditRecipePath)

        self.toolBtnExplorerRecipePath = QToolButton(self.frame_8)
        self.toolBtnExplorerRecipePath.setObjectName(u"toolBtnExplorerRecipePath")

        self.horizontalLayout_6.addWidget(self.toolBtnExplorerRecipePath)


        self.verticalLayout_9.addWidget(self.frame_8)

        self.frame_9 = QFrame(self.groupBoxWorkspace)
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


        self.verticalLayout_9.addWidget(self.frame_9)

        self.frame_10 = QFrame(self.groupBoxWorkspace)
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


        self.verticalLayout_9.addWidget(self.frame_10)

        self.frame_11 = QFrame(self.groupBoxWorkspace)
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


        self.verticalLayout_9.addWidget(self.frame_11)

        self.frame_13 = QFrame(self.groupBoxWorkspace)
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


        self.verticalLayout_9.addWidget(self.frame_13)

        self.frame_12 = QFrame(self.groupBoxWorkspace)
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


        self.verticalLayout_9.addWidget(self.frame_12)

        self.frame_14 = QFrame(self.groupBoxWorkspace)
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


        self.verticalLayout_9.addWidget(self.frame_14)


        self.verticalLayout_3.addWidget(self.groupBoxWorkspace)

        self.groupBox_3 = QGroupBox(self.tab)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.horizontalLayout_16 = QHBoxLayout(self.groupBox_3)
        self.horizontalLayout_16.setSpacing(2)
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.horizontalLayout_16.setContentsMargins(2, 2, 2, 2)
        self.frame_7 = QFrame(self.groupBox_3)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.frame_7)
        self.verticalLayout_7.setSpacing(2)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.toolButton = QToolButton(self.frame_7)
        self.toolButton.setObjectName(u"toolButton")
        self.toolButton.setMinimumSize(QSize(25, 25))
        self.toolButton.setMaximumSize(QSize(20, 16777215))

        self.verticalLayout_7.addWidget(self.toolButton)

        self.toolButton_2 = QToolButton(self.frame_7)
        self.toolButton_2.setObjectName(u"toolButton_2")
        sizePolicy2 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.toolButton_2.sizePolicy().hasHeightForWidth())
        self.toolButton_2.setSizePolicy(sizePolicy2)
        self.toolButton_2.setMinimumSize(QSize(25, 25))

        self.verticalLayout_7.addWidget(self.toolButton_2)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_7.addItem(self.verticalSpacer_3)


        self.horizontalLayout_16.addWidget(self.frame_7)

        self.tableViewRemoteList = QTableView(self.groupBox_3)
        self.tableViewRemoteList.setObjectName(u"tableViewRemoteList")
        self.tableViewRemoteList.setHorizontalScrollMode(QAbstractItemView.ScrollPerPixel)

        self.horizontalLayout_16.addWidget(self.tableViewRemoteList)


        self.verticalLayout_3.addWidget(self.groupBox_3)

        self.tabWidget.addTab(self.tab, "")
        self.splitter_2.addWidget(self.tabWidget)

        self.verticalLayout_6.addWidget(self.splitter_2)

        self.splitter_4.addWidget(self.frameMain)
        self.frame_17 = QFrame(self.splitter_4)
        self.frame_17.setObjectName(u"frame_17")
        self.frame_17.setFrameShape(QFrame.StyledPanel)
        self.frame_17.setFrameShadow(QFrame.Raised)
        self.verticalLayout_11 = QVBoxLayout(self.frame_17)
        self.verticalLayout_11.setSpacing(0)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(0, 0, 2, 0)
        self.groupBox_4 = QGroupBox(self.frame_17)
        self.groupBox_4.setObjectName(u"groupBox_4")
        self.horizontalLayout_17 = QHBoxLayout(self.groupBox_4)
        self.horizontalLayout_17.setSpacing(2)
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.horizontalLayout_17.setContentsMargins(2, 2, 2, 2)
        self.frame_5 = QFrame(self.groupBox_4)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.frame_5)
        self.verticalLayout_5.setSpacing(2)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.toolButtonClearConsole = QToolButton(self.frame_5)
        self.toolButtonClearConsole.setObjectName(u"toolButtonClearConsole")
        self.toolButtonClearConsole.setMinimumSize(QSize(25, 25))
        self.toolButtonClearConsole.setCheckable(False)

        self.verticalLayout_5.addWidget(self.toolButtonClearConsole)

        self.toolButtonConsoleScrollToEnd = QToolButton(self.frame_5)
        self.toolButtonConsoleScrollToEnd.setObjectName(u"toolButtonConsoleScrollToEnd")
        self.toolButtonConsoleScrollToEnd.setMinimumSize(QSize(25, 25))
        self.toolButtonConsoleScrollToEnd.setCheckable(True)
        self.toolButtonConsoleScrollToEnd.setChecked(True)

        self.verticalLayout_5.addWidget(self.toolButtonConsoleScrollToEnd)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_5.addItem(self.verticalSpacer_2)


        self.horizontalLayout_17.addWidget(self.frame_5)

        self.console = QPlainTextEdit(self.groupBox_4)
        self.console.setObjectName(u"console")
        font = QFont()
        font.setFamily(u"Consolas")
        font.setPointSize(8)
        self.console.setFont(font)
        self.console.setReadOnly(True)
        self.console.setTextInteractionFlags(Qt.TextSelectableByMouse)
        self.console.setCenterOnScroll(False)

        self.horizontalLayout_17.addWidget(self.console)


        self.verticalLayout_11.addWidget(self.groupBox_4)

        self.splitter_4.addWidget(self.frame_17)

        self.verticalLayout_10.addWidget(self.splitter_4)

        self.splitter_5.addWidget(self.frame_18)

        self.horizontalLayout_18.addWidget(self.splitter_5)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 948, 21))
        self.menuView = QMenu(self.menubar)
        self.menuView.setObjectName(u"menuView")
        self.menuFile = QMenu(self.menubar)
        self.menuFile.setObjectName(u"menuFile")
        self.menuHelp = QMenu(self.menubar)
        self.menuHelp.setObjectName(u"menuHelp")
        self.menuConan = QMenu(self.menubar)
        self.menuConan.setObjectName(u"menuConan")
        MainWindow.setMenuBar(self.menubar)
        self.statusBar = QStatusBar(MainWindow)
        self.statusBar.setObjectName(u"statusBar")
        self.statusBar.setMaximumSize(QSize(16777215, 16777215))
        MainWindow.setStatusBar(self.statusBar)
        self.toolBar = QToolBar(MainWindow)
        self.toolBar.setObjectName(u"toolBar")
        sizePolicy2.setHeightForWidth(self.toolBar.sizePolicy().hasHeightForWidth())
        self.toolBar.setSizePolicy(sizePolicy2)
        self.toolBar.setMinimumSize(QSize(0, 0))
        self.toolBar.setBaseSize(QSize(0, 50))
        self.toolBar.setMovable(False)
        self.toolBar.setIconSize(QSize(30, 30))
        self.toolBar.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)
        self.toolBar.setFloatable(False)
        MainWindow.addToolBar(Qt.TopToolBarArea, self.toolBar)

        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuView.menuAction())
        self.menubar.addAction(self.menuConan.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())
        self.menuView.addAction(self.actionViewPackage)
        self.menuView.addAction(self.actionViewProfile)
        self.menuFile.addAction(self.actionRefresh)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionFileExit)
        self.menuConan.addAction(self.actionConanCreate)
        self.menuConan.addAction(self.actionConanInstall)
        self.menuConan.addAction(self.actionConanBuild)
        self.menuConan.addAction(self.actionConanSource)
        self.menuConan.addAction(self.actionConanPackage)
        self.menuConan.addAction(self.actionConanExport)
        self.menuConan.addAction(self.actionConanExportPackage)
        self.toolBar.addAction(self.actionRefresh)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actionConanCreate)
        self.toolBar.addAction(self.actionConanInstall)
        self.toolBar.addAction(self.actionConanBuild)
        self.toolBar.addAction(self.actionConanSource)
        self.toolBar.addAction(self.actionConanPackage)
        self.toolBar.addAction(self.actionConanExport)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actionConanExportPackage)

        self.retranslateUi(MainWindow)
        self.actionFileExit.triggered.connect(MainWindow.close)
        self.toolButtonClearConsole.pressed.connect(self.console.clear)

        self.toolBoxConan.setCurrentIndex(0)
        self.toolBoxConan.layout().setSpacing(0)
        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Conan GUIde", None))
        self.actionViewProfile.setText(QCoreApplication.translate("MainWindow", u"Profile", None))
        self.actionFileExit.setText(QCoreApplication.translate("MainWindow", u"Exit", None))
        self.actionRefresh.setText(QCoreApplication.translate("MainWindow", u"Refresh", None))
        self.actionConanCreate.setText(QCoreApplication.translate("MainWindow", u"Create", None))
        self.actionConanInstall.setText(QCoreApplication.translate("MainWindow", u"Install", None))
        self.actionConanBuild.setText(QCoreApplication.translate("MainWindow", u"Build", None))
        self.actionConanSource.setText(QCoreApplication.translate("MainWindow", u"Source", None))
        self.actionConanPackage.setText(QCoreApplication.translate("MainWindow", u"Package", None))
        self.actionConanExport.setText(QCoreApplication.translate("MainWindow", u"Export", None))
        self.actionConanExportPackage.setText(QCoreApplication.translate("MainWindow", u"Export Package", None))
        self.actionViewPackage.setText(QCoreApplication.translate("MainWindow", u"Package", None))
#if QT_CONFIG(tooltip)
        self.actionViewPackage.setToolTip(QCoreApplication.translate("MainWindow", u"Package", None))
#endif // QT_CONFIG(tooltip)
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"Double Click", None))
        self.checkBoxOpenExplorer.setText(QCoreApplication.translate("MainWindow", u"Open Explorer", None))
        self.checkBoxCopyClipboard.setText(QCoreApplication.translate("MainWindow", u"Copy to Clipboard", None))
        self.toolBoxConan.setItemText(self.toolBoxConan.indexOf(self.pagePackage), QCoreApplication.translate("MainWindow", u"Package", None))
        self.toolBoxConan.setItemText(self.toolBoxConan.indexOf(self.pageProfile), QCoreApplication.translate("MainWindow", u"Profile", None))
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"Local Cache", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Cache Path", None))
        self.btnCopyCachePath.setText(QCoreApplication.translate("MainWindow", u"Copy", None))
        self.btnOpenCachePath.setText(QCoreApplication.translate("MainWindow", u"Open", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Real Path", None))
        self.btnCopyRealPath.setText(QCoreApplication.translate("MainWindow", u"Copy", None))
        self.btnOpenRealPath.setText(QCoreApplication.translate("MainWindow", u"Open", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Package Path", None))
        self.btnCopyPackagePath.setText(QCoreApplication.translate("MainWindow", u"Copy", None))
        self.btnOpenPackagePath.setText(QCoreApplication.translate("MainWindow", u"Open", None))
        self.groupBoxWorkspace.setTitle(QCoreApplication.translate("MainWindow", u"Workspace", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"User", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"/", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"Channel", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Recipe Path", None))
        self.toolBtnExplorerRecipePath.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Install Path", None))
        self.toolBtnExplorerInstallPath.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Build Path", None))
        self.toolBtnExplorerBuildPath.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Source Path", None))
        self.toolBtnExplorerSourcePath.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"Package Path", None))
        self.toolBtnExplorerPackagePath.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Parameter", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"Profile", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("MainWindow", u"Remote", None))
        self.toolButton.setText(QCoreApplication.translate("MainWindow", u"+", None))
        self.toolButton_2.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("MainWindow", u"Core", None))
        self.groupBox_4.setTitle(QCoreApplication.translate("MainWindow", u"Console", None))
        self.toolButtonClearConsole.setText(QCoreApplication.translate("MainWindow", u"C", None))
        self.toolButtonConsoleScrollToEnd.setText(QCoreApplication.translate("MainWindow", u"D", None))
        self.console.setPlainText("")
        self.menuView.setTitle(QCoreApplication.translate("MainWindow", u"View", None))
        self.menuFile.setTitle(QCoreApplication.translate("MainWindow", u"File", None))
        self.menuHelp.setTitle(QCoreApplication.translate("MainWindow", u"Help", None))
        self.menuConan.setTitle(QCoreApplication.translate("MainWindow", u"Conan", None))
        self.toolBar.setWindowTitle(QCoreApplication.translate("MainWindow", u"toolBar", None))
    # retranslateUi

