# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'tab_cache.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

from conanguide.ui.res import resources_rc

class Ui_TabCache(object):
    def setupUi(self, TabCache):
        if not TabCache.objectName():
            TabCache.setObjectName(u"TabCache")
        TabCache.resize(1233, 825)
        self.horizontalLayout_4 = QHBoxLayout(TabCache)
        self.horizontalLayout_4.setSpacing(5)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.splitter_5 = QSplitter(TabCache)
        self.splitter_5.setObjectName(u"splitter_5")
        self.splitter_5.setOrientation(Qt.Horizontal)
        self.frame_6 = QFrame(self.splitter_5)
        self.frame_6.setObjectName(u"frame_6")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_6.sizePolicy().hasHeightForWidth())
        self.frame_6.setSizePolicy(sizePolicy)
        self.frame_6.setMinimumSize(QSize(300, 0))
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_6)
        self.verticalLayout_3.setSpacing(3)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 3)
        self.frame_16 = QFrame(self.frame_6)
        self.frame_16.setObjectName(u"frame_16")
        self.frame_16.setLayoutDirection(Qt.LeftToRight)
        self.frame_16.setFrameShape(QFrame.StyledPanel)
        self.frame_16.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_15 = QHBoxLayout(self.frame_16)
        self.horizontalLayout_15.setSpacing(0)
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.horizontalLayout_15.setContentsMargins(1, 1, 0, 0)
        self.toolButtonRefresh = QToolButton(self.frame_16)
        self.toolButtonRefresh.setObjectName(u"toolButtonRefresh")
        self.toolButtonRefresh.setMinimumSize(QSize(25, 25))
        icon = QIcon()
        icon.addFile(u":/icon/light/refresh.png", QSize(), QIcon.Normal, QIcon.Off)
        self.toolButtonRefresh.setIcon(icon)
        self.toolButtonRefresh.setCheckable(False)
        self.toolButtonRefresh.setChecked(False)
        self.toolButtonRefresh.setAutoRaise(False)

        self.horizontalLayout_15.addWidget(self.toolButtonRefresh)

        self.horizontalSpacer_5 = QSpacerItem(10, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_15.addItem(self.horizontalSpacer_5)

        self.checkBoxOpenExplorer = QToolButton(self.frame_16)
        self.checkBoxOpenExplorer.setObjectName(u"checkBoxOpenExplorer")
        self.checkBoxOpenExplorer.setMinimumSize(QSize(25, 25))
        self.checkBoxOpenExplorer.setMaximumSize(QSize(25, 25))
        icon1 = QIcon()
        icon1.addFile(u":/icon/light/open_folder.png", QSize(), QIcon.Normal, QIcon.Off)
        self.checkBoxOpenExplorer.setIcon(icon1)
        self.checkBoxOpenExplorer.setCheckable(True)
        self.checkBoxOpenExplorer.setChecked(True)

        self.horizontalLayout_15.addWidget(self.checkBoxOpenExplorer)

        self.checkBoxCopyClipboard = QToolButton(self.frame_16)
        self.checkBoxCopyClipboard.setObjectName(u"checkBoxCopyClipboard")
        self.checkBoxCopyClipboard.setMinimumSize(QSize(25, 25))
        self.checkBoxCopyClipboard.setMaximumSize(QSize(25, 25))
        icon2 = QIcon()
        icon2.addFile(u":/icon/light/copy.png", QSize(), QIcon.Normal, QIcon.Off)
        self.checkBoxCopyClipboard.setIcon(icon2)
        self.checkBoxCopyClipboard.setCheckable(True)
        self.checkBoxCopyClipboard.setChecked(True)

        self.horizontalLayout_15.addWidget(self.checkBoxCopyClipboard)

        self.checkBoxShowDirectory = QToolButton(self.frame_16)
        self.checkBoxShowDirectory.setObjectName(u"checkBoxShowDirectory")
        self.checkBoxShowDirectory.setMinimumSize(QSize(25, 25))
        self.checkBoxShowDirectory.setMaximumSize(QSize(25, 25))
        icon3 = QIcon()
        icon3.addFile(u":/icon/light/directory_tree.png", QSize(), QIcon.Normal, QIcon.Off)
        self.checkBoxShowDirectory.setIcon(icon3)
        self.checkBoxShowDirectory.setIconSize(QSize(18, 18))
        self.checkBoxShowDirectory.setCheckable(True)
        self.checkBoxShowDirectory.setChecked(True)

        self.horizontalLayout_15.addWidget(self.checkBoxShowDirectory)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_15.addItem(self.horizontalSpacer)


        self.verticalLayout_3.addWidget(self.frame_16)

        self.lineEditSearchRecipe = QLineEdit(self.frame_6)
        self.lineEditSearchRecipe.setObjectName(u"lineEditSearchRecipe")
        self.lineEditSearchRecipe.setMinimumSize(QSize(0, 25))
        self.lineEditSearchRecipe.setFrame(True)
        self.lineEditSearchRecipe.setEchoMode(QLineEdit.Normal)
        self.lineEditSearchRecipe.setCursorPosition(0)

        self.verticalLayout_3.addWidget(self.lineEditSearchRecipe)

        self.splitter_3 = QSplitter(self.frame_6)
        self.splitter_3.setObjectName(u"splitter_3")
        self.splitter_3.setOrientation(Qt.Vertical)
        self.splitter = QSplitter(self.splitter_3)
        self.splitter.setObjectName(u"splitter")
        self.splitter.setOrientation(Qt.Horizontal)
        self.layoutWidget = QWidget(self.splitter)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.horizontalLayout_5 = QHBoxLayout(self.layoutWidget)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setSpacing(2)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.toolButtonSortAscending = QToolButton(self.layoutWidget)
        self.toolButtonSortAscending.setObjectName(u"toolButtonSortAscending")
        self.toolButtonSortAscending.setMinimumSize(QSize(25, 25))
        icon4 = QIcon()
        icon4.addFile(u":/icon/light/sort_ascending.png", QSize(), QIcon.Normal, QIcon.Off)
        self.toolButtonSortAscending.setIcon(icon4)
        self.toolButtonSortAscending.setCheckable(True)
        self.toolButtonSortAscending.setChecked(True)
        self.toolButtonSortAscending.setAutoRaise(False)

        self.verticalLayout.addWidget(self.toolButtonSortAscending)

        self.toolButtonSortDescending = QToolButton(self.layoutWidget)
        self.toolButtonSortDescending.setObjectName(u"toolButtonSortDescending")
        self.toolButtonSortDescending.setMinimumSize(QSize(25, 25))
        icon5 = QIcon()
        icon5.addFile(u":/icon/light/sort_descending.png", QSize(), QIcon.Normal, QIcon.Off)
        self.toolButtonSortDescending.setIcon(icon5)
        self.toolButtonSortDescending.setCheckable(True)

        self.verticalLayout.addWidget(self.toolButtonSortDescending)

        self.toolButtonRemoveRecipe = QToolButton(self.layoutWidget)
        self.toolButtonRemoveRecipe.setObjectName(u"toolButtonRemoveRecipe")
        self.toolButtonRemoveRecipe.setMinimumSize(QSize(25, 25))
        icon6 = QIcon()
        icon6.addFile(u":/icon/light/remove.png", QSize(), QIcon.Normal, QIcon.Off)
        self.toolButtonRemoveRecipe.setIcon(icon6)

        self.verticalLayout.addWidget(self.toolButtonRemoveRecipe)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)


        self.horizontalLayout_5.addLayout(self.verticalLayout)

        self.treeViewRecipe = QTreeView(self.layoutWidget)
        self.treeViewRecipe.setObjectName(u"treeViewRecipe")

        self.horizontalLayout_5.addWidget(self.treeViewRecipe)

        self.splitter.addWidget(self.layoutWidget)
        self.treeViewRecipeInspect = QTreeView(self.splitter)
        self.treeViewRecipeInspect.setObjectName(u"treeViewRecipeInspect")
        self.splitter.addWidget(self.treeViewRecipeInspect)
        self.splitter_3.addWidget(self.splitter)
        self.splitter_2 = QSplitter(self.splitter_3)
        self.splitter_2.setObjectName(u"splitter_2")
        self.splitter_2.setOrientation(Qt.Horizontal)
        self.layoutWidget1 = QWidget(self.splitter_2)
        self.layoutWidget1.setObjectName(u"layoutWidget1")
        self.horizontalLayout_6 = QHBoxLayout(self.layoutWidget1)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setSpacing(2)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.toolButtonRemovePackage = QToolButton(self.layoutWidget1)
        self.toolButtonRemovePackage.setObjectName(u"toolButtonRemovePackage")
        self.toolButtonRemovePackage.setMinimumSize(QSize(25, 25))
        self.toolButtonRemovePackage.setIcon(icon6)

        self.verticalLayout_2.addWidget(self.toolButtonRemovePackage)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer_2)


        self.horizontalLayout_6.addLayout(self.verticalLayout_2)

        self.listViewPackage = QListView(self.layoutWidget1)
        self.listViewPackage.setObjectName(u"listViewPackage")

        self.horizontalLayout_6.addWidget(self.listViewPackage)

        self.splitter_2.addWidget(self.layoutWidget1)
        self.treeViewPackageInspect = QTreeView(self.splitter_2)
        self.treeViewPackageInspect.setObjectName(u"treeViewPackageInspect")
        self.treeViewPackageInspect.setEnabled(True)
        self.splitter_2.addWidget(self.treeViewPackageInspect)
        self.splitter_3.addWidget(self.splitter_2)

        self.verticalLayout_3.addWidget(self.splitter_3)

        self.splitter_5.addWidget(self.frame_6)
        self.frame_15 = QFrame(self.splitter_5)
        self.frame_15.setObjectName(u"frame_15")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(1)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.frame_15.sizePolicy().hasHeightForWidth())
        self.frame_15.setSizePolicy(sizePolicy1)
        self.frame_15.setFrameShape(QFrame.StyledPanel)
        self.frame_15.setFrameShadow(QFrame.Raised)
        self.verticalLayout_13 = QVBoxLayout(self.frame_15)
        self.verticalLayout_13.setSpacing(5)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.verticalLayout_13.setContentsMargins(2, 2, 2, 2)
        self.splitter_4 = QSplitter(self.frame_15)
        self.splitter_4.setObjectName(u"splitter_4")
        self.splitter_4.setOrientation(Qt.Vertical)
        self.groupBox = QGroupBox(self.splitter_4)
        self.groupBox.setObjectName(u"groupBox")
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy2)
        self.groupBox.setMinimumSize(QSize(0, 137))
        self.groupBox.setMaximumSize(QSize(16777215, 137))
        self.verticalLayout_8 = QVBoxLayout(self.groupBox)
        self.verticalLayout_8.setSpacing(0)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.verticalLayout_8.setContentsMargins(2, 2, 2, 2)
        self.frame = QFrame(self.groupBox)
        self.frame.setObjectName(u"frame")
        sizePolicy2.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy2)
        self.frame.setFrameShape(QFrame.NoFrame)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame)
        self.horizontalLayout.setSpacing(5)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.horizontalLayout.setContentsMargins(2, 2, 2, 2)
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(75, 0))

        self.horizontalLayout.addWidget(self.label)

        self.lineEditCachePath = QLineEdit(self.frame)
        self.lineEditCachePath.setObjectName(u"lineEditCachePath")
        self.lineEditCachePath.setEnabled(True)
        self.lineEditCachePath.setReadOnly(True)

        self.horizontalLayout.addWidget(self.lineEditCachePath)

        self.btnCopyCachePath = QPushButton(self.frame)
        self.btnCopyCachePath.setObjectName(u"btnCopyCachePath")
        self.btnCopyCachePath.setIcon(icon2)

        self.horizontalLayout.addWidget(self.btnCopyCachePath)

        self.btnOpenCachePath = QPushButton(self.frame)
        self.btnOpenCachePath.setObjectName(u"btnOpenCachePath")
        self.btnOpenCachePath.setIcon(icon1)

        self.horizontalLayout.addWidget(self.btnOpenCachePath)


        self.verticalLayout_8.addWidget(self.frame)

        self.frame_21 = QFrame(self.groupBox)
        self.frame_21.setObjectName(u"frame_21")
        sizePolicy2.setHeightForWidth(self.frame_21.sizePolicy().hasHeightForWidth())
        self.frame_21.setSizePolicy(sizePolicy2)
        self.frame_21.setFrameShape(QFrame.StyledPanel)
        self.frame_21.setFrameShadow(QFrame.Raised)
        self.frame_21.setLineWidth(1)
        self.horizontalLayout_21 = QHBoxLayout(self.frame_21)
        self.horizontalLayout_21.setSpacing(5)
        self.horizontalLayout_21.setObjectName(u"horizontalLayout_21")
        self.horizontalLayout_21.setContentsMargins(2, 2, 2, 2)
        self.label_20 = QLabel(self.frame_21)
        self.label_20.setObjectName(u"label_20")
        self.label_20.setMinimumSize(QSize(75, 0))

        self.horizontalLayout_21.addWidget(self.label_20)

        self.lineEditDataPath = QLineEdit(self.frame_21)
        self.lineEditDataPath.setObjectName(u"lineEditDataPath")
        self.lineEditDataPath.setEnabled(True)
        self.lineEditDataPath.setReadOnly(True)

        self.horizontalLayout_21.addWidget(self.lineEditDataPath)

        self.btnCopyDataPath = QPushButton(self.frame_21)
        self.btnCopyDataPath.setObjectName(u"btnCopyDataPath")
        self.btnCopyDataPath.setIcon(icon2)

        self.horizontalLayout_21.addWidget(self.btnCopyDataPath)

        self.btnOpenDataPath = QPushButton(self.frame_21)
        self.btnOpenDataPath.setObjectName(u"btnOpenDataPath")
        self.btnOpenDataPath.setIcon(icon1)

        self.horizontalLayout_21.addWidget(self.btnOpenDataPath)


        self.verticalLayout_8.addWidget(self.frame_21)

        self.frame_2 = QFrame(self.groupBox)
        self.frame_2.setObjectName(u"frame_2")
        sizePolicy2.setHeightForWidth(self.frame_2.sizePolicy().hasHeightForWidth())
        self.frame_2.setSizePolicy(sizePolicy2)
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
        self.btnCopyRealPath.setIcon(icon2)

        self.horizontalLayout_2.addWidget(self.btnCopyRealPath)

        self.btnOpenRealPath = QPushButton(self.frame_2)
        self.btnOpenRealPath.setObjectName(u"btnOpenRealPath")
        self.btnOpenRealPath.setIcon(icon1)

        self.horizontalLayout_2.addWidget(self.btnOpenRealPath)


        self.verticalLayout_8.addWidget(self.frame_2)

        self.frame_3 = QFrame(self.groupBox)
        self.frame_3.setObjectName(u"frame_3")
        sizePolicy2.setHeightForWidth(self.frame_3.sizePolicy().hasHeightForWidth())
        self.frame_3.setSizePolicy(sizePolicy2)
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
        self.btnCopyPackagePath.setIcon(icon2)

        self.horizontalLayout_3.addWidget(self.btnCopyPackagePath)

        self.btnOpenPackagePath = QPushButton(self.frame_3)
        self.btnOpenPackagePath.setObjectName(u"btnOpenPackagePath")
        self.btnOpenPackagePath.setIcon(icon1)

        self.horizontalLayout_3.addWidget(self.btnOpenPackagePath)


        self.verticalLayout_8.addWidget(self.frame_3)

        self.splitter_4.addWidget(self.groupBox)
        self.tabWidgetOthers = QTabWidget(self.splitter_4)
        self.tabWidgetOthers.setObjectName(u"tabWidgetOthers")
        sizePolicy3 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(1)
        sizePolicy3.setHeightForWidth(self.tabWidgetOthers.sizePolicy().hasHeightForWidth())
        self.tabWidgetOthers.setSizePolicy(sizePolicy3)
        self.tabDirectory = QWidget()
        self.tabDirectory.setObjectName(u"tabDirectory")
        self.verticalLayout_4 = QVBoxLayout(self.tabDirectory)
        self.verticalLayout_4.setSpacing(5)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.treeViewDirectory = QTreeView(self.tabDirectory)
        self.treeViewDirectory.setObjectName(u"treeViewDirectory")

        self.verticalLayout_4.addWidget(self.treeViewDirectory)

        self.tabWidgetOthers.addTab(self.tabDirectory, "")
        self.splitter_4.addWidget(self.tabWidgetOthers)

        self.verticalLayout_13.addWidget(self.splitter_4)

        self.splitter_5.addWidget(self.frame_15)

        self.horizontalLayout_4.addWidget(self.splitter_5)


        self.retranslateUi(TabCache)

        self.tabWidgetOthers.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(TabCache)
    # setupUi

    def retranslateUi(self, TabCache):
        TabCache.setWindowTitle(QCoreApplication.translate("TabCache", u"Form", None))
#if QT_CONFIG(tooltip)
        self.toolButtonRefresh.setToolTip(QCoreApplication.translate("TabCache", u"Refresh", None))
#endif // QT_CONFIG(tooltip)
        self.toolButtonRefresh.setText("")
#if QT_CONFIG(tooltip)
        self.checkBoxOpenExplorer.setToolTip(QCoreApplication.translate("TabCache", u"Open Path", None))
#endif // QT_CONFIG(tooltip)
        self.checkBoxOpenExplorer.setText("")
#if QT_CONFIG(tooltip)
        self.checkBoxCopyClipboard.setToolTip(QCoreApplication.translate("TabCache", u"Copy Path", None))
#endif // QT_CONFIG(tooltip)
        self.checkBoxCopyClipboard.setText(QCoreApplication.translate("TabCache", u"...", None))
#if QT_CONFIG(tooltip)
        self.checkBoxShowDirectory.setToolTip(QCoreApplication.translate("TabCache", u"Show Directory", None))
#endif // QT_CONFIG(tooltip)
        self.checkBoxShowDirectory.setText(QCoreApplication.translate("TabCache", u"...", None))
#if QT_CONFIG(whatsthis)
        self.lineEditSearchRecipe.setWhatsThis("")
#endif // QT_CONFIG(whatsthis)
        self.lineEditSearchRecipe.setPlaceholderText(QCoreApplication.translate("TabCache", u"Search Recipe...", None))
#if QT_CONFIG(tooltip)
        self.toolButtonSortAscending.setToolTip(QCoreApplication.translate("TabCache", u"Sort Ascending", None))
#endif // QT_CONFIG(tooltip)
        self.toolButtonSortAscending.setText("")
#if QT_CONFIG(tooltip)
        self.toolButtonSortDescending.setToolTip(QCoreApplication.translate("TabCache", u"Sort Descending", None))
#endif // QT_CONFIG(tooltip)
        self.toolButtonSortDescending.setText("")
#if QT_CONFIG(tooltip)
        self.toolButtonRemoveRecipe.setToolTip(QCoreApplication.translate("TabCache", u"Remove Recipe", None))
#endif // QT_CONFIG(tooltip)
        self.toolButtonRemoveRecipe.setText("")
#if QT_CONFIG(tooltip)
        self.toolButtonRemovePackage.setToolTip(QCoreApplication.translate("TabCache", u"Remove Package", None))
#endif // QT_CONFIG(tooltip)
        self.toolButtonRemovePackage.setText("")
        self.groupBox.setTitle(QCoreApplication.translate("TabCache", u"Local Cache", None))
        self.label.setText(QCoreApplication.translate("TabCache", u"Cache Path", None))
        self.btnCopyCachePath.setText(QCoreApplication.translate("TabCache", u"Copy", None))
        self.btnOpenCachePath.setText(QCoreApplication.translate("TabCache", u" Open", None))
        self.label_20.setText(QCoreApplication.translate("TabCache", u"Data Path", None))
        self.btnCopyDataPath.setText(QCoreApplication.translate("TabCache", u"Copy", None))
        self.btnOpenDataPath.setText(QCoreApplication.translate("TabCache", u" Open", None))
        self.label_2.setText(QCoreApplication.translate("TabCache", u"Real Path", None))
        self.btnCopyRealPath.setText(QCoreApplication.translate("TabCache", u"Copy", None))
        self.btnOpenRealPath.setText(QCoreApplication.translate("TabCache", u" Open", None))
        self.label_3.setText(QCoreApplication.translate("TabCache", u"Package Path", None))
        self.btnCopyPackagePath.setText(QCoreApplication.translate("TabCache", u"Copy", None))
        self.btnOpenPackagePath.setText(QCoreApplication.translate("TabCache", u" Open", None))
        self.tabWidgetOthers.setTabText(self.tabWidgetOthers.indexOf(self.tabDirectory), QCoreApplication.translate("TabCache", u"Directory", None))
    # retranslateUi

