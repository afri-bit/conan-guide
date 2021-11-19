# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'tab_package.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

from conanguide.ui.res import resources_rc

class Ui_TabPackage(object):
    def setupUi(self, TabPackage):
        if not TabPackage.objectName():
            TabPackage.setObjectName(u"TabPackage")
        TabPackage.resize(891, 649)
        self.horizontalLayout_4 = QHBoxLayout(TabPackage)
        self.horizontalLayout_4.setSpacing(5)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.splitter_5 = QSplitter(TabPackage)
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
        self.verticalLayout = QVBoxLayout(self.frame_6)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.frame_16 = QFrame(self.frame_6)
        self.frame_16.setObjectName(u"frame_16")
        self.frame_16.setLayoutDirection(Qt.LeftToRight)
        self.frame_16.setFrameShape(QFrame.StyledPanel)
        self.frame_16.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_15 = QHBoxLayout(self.frame_16)
        self.horizontalLayout_15.setSpacing(0)
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.horizontalLayout_15.setContentsMargins(2, 2, 0, 2)
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

        self.toolButtonSortAscending = QToolButton(self.frame_16)
        self.toolButtonSortAscending.setObjectName(u"toolButtonSortAscending")
        self.toolButtonSortAscending.setMinimumSize(QSize(25, 25))
        icon1 = QIcon()
        icon1.addFile(u":/icon/light/sort_ascending.png", QSize(), QIcon.Normal, QIcon.Off)
        self.toolButtonSortAscending.setIcon(icon1)
        self.toolButtonSortAscending.setCheckable(True)
        self.toolButtonSortAscending.setChecked(True)
        self.toolButtonSortAscending.setAutoRaise(False)

        self.horizontalLayout_15.addWidget(self.toolButtonSortAscending)

        self.toolButtonSortDescending = QToolButton(self.frame_16)
        self.toolButtonSortDescending.setObjectName(u"toolButtonSortDescending")
        self.toolButtonSortDescending.setMinimumSize(QSize(25, 25))
        icon2 = QIcon()
        icon2.addFile(u":/icon/light/sort_descending.png", QSize(), QIcon.Normal, QIcon.Off)
        self.toolButtonSortDescending.setIcon(icon2)
        self.toolButtonSortDescending.setCheckable(True)

        self.horizontalLayout_15.addWidget(self.toolButtonSortDescending)

        self.horizontalSpacer_4 = QSpacerItem(10, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_15.addItem(self.horizontalSpacer_4)

        self.toolButtonRemovePackage = QToolButton(self.frame_16)
        self.toolButtonRemovePackage.setObjectName(u"toolButtonRemovePackage")
        self.toolButtonRemovePackage.setMinimumSize(QSize(25, 25))
        icon3 = QIcon()
        icon3.addFile(u":/icon/light/remove.png", QSize(), QIcon.Normal, QIcon.Off)
        self.toolButtonRemovePackage.setIcon(icon3)

        self.horizontalLayout_15.addWidget(self.toolButtonRemovePackage)

        self.checkBoxOpenExplorer = QToolButton(self.frame_16)
        self.checkBoxOpenExplorer.setObjectName(u"checkBoxOpenExplorer")
        self.checkBoxOpenExplorer.setMinimumSize(QSize(25, 25))
        self.checkBoxOpenExplorer.setMaximumSize(QSize(25, 25))
        icon4 = QIcon()
        icon4.addFile(u":/icon/light/open_folder.png", QSize(), QIcon.Normal, QIcon.Off)
        self.checkBoxOpenExplorer.setIcon(icon4)
        self.checkBoxOpenExplorer.setCheckable(True)
        self.checkBoxOpenExplorer.setChecked(True)

        self.horizontalLayout_15.addWidget(self.checkBoxOpenExplorer)

        self.checkBoxCopyClipboard = QToolButton(self.frame_16)
        self.checkBoxCopyClipboard.setObjectName(u"checkBoxCopyClipboard")
        self.checkBoxCopyClipboard.setMinimumSize(QSize(25, 25))
        self.checkBoxCopyClipboard.setMaximumSize(QSize(25, 25))
        icon5 = QIcon()
        icon5.addFile(u":/icon/light/copy.png", QSize(), QIcon.Normal, QIcon.Off)
        self.checkBoxCopyClipboard.setIcon(icon5)
        self.checkBoxCopyClipboard.setCheckable(True)
        self.checkBoxCopyClipboard.setChecked(True)

        self.horizontalLayout_15.addWidget(self.checkBoxCopyClipboard)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_15.addItem(self.horizontalSpacer)


        self.verticalLayout.addWidget(self.frame_16)

        self.lineEditSearchPackage = QLineEdit(self.frame_6)
        self.lineEditSearchPackage.setObjectName(u"lineEditSearchPackage")
        self.lineEditSearchPackage.setMinimumSize(QSize(0, 25))
        self.lineEditSearchPackage.setFrame(True)
        self.lineEditSearchPackage.setEchoMode(QLineEdit.Normal)
        self.lineEditSearchPackage.setCursorPosition(0)

        self.verticalLayout.addWidget(self.lineEditSearchPackage)

        self.splitter = QSplitter(self.frame_6)
        self.splitter.setObjectName(u"splitter")
        self.splitter.setOrientation(Qt.Vertical)
        self.treeViewRecipe = QTreeView(self.splitter)
        self.treeViewRecipe.setObjectName(u"treeViewRecipe")
        self.treeViewRecipe.setEnabled(True)
        self.splitter.addWidget(self.treeViewRecipe)
        self.treeViewPackage = QTreeView(self.splitter)
        self.treeViewPackage.setObjectName(u"treeViewPackage")
        self.splitter.addWidget(self.treeViewPackage)
        self.listViewPackageBinary = QListView(self.splitter)
        self.listViewPackageBinary.setObjectName(u"listViewPackageBinary")
        self.splitter.addWidget(self.listViewPackageBinary)
        self.treeViewPackageInspect = QTreeView(self.splitter)
        self.treeViewPackageInspect.setObjectName(u"treeViewPackageInspect")
        self.splitter.addWidget(self.treeViewPackageInspect)

        self.verticalLayout.addWidget(self.splitter)

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
        self.splitter_6 = QSplitter(self.frame_15)
        self.splitter_6.setObjectName(u"splitter_6")
        self.splitter_6.setContextMenuPolicy(Qt.DefaultContextMenu)
        self.splitter_6.setFrameShape(QFrame.NoFrame)
        self.splitter_6.setFrameShadow(QFrame.Plain)
        self.splitter_6.setLineWidth(1)
        self.splitter_6.setOrientation(Qt.Vertical)
        self.splitter_6.setHandleWidth(5)
        self.frame_19 = QFrame(self.splitter_6)
        self.frame_19.setObjectName(u"frame_19")
        self.frame_19.setMaximumSize(QSize(16777215, 135))
        self.frame_19.setFrameShape(QFrame.StyledPanel)
        self.frame_19.setFrameShadow(QFrame.Raised)
        self.verticalLayout_14 = QVBoxLayout(self.frame_19)
        self.verticalLayout_14.setSpacing(0)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.verticalLayout_14.setContentsMargins(0, 0, 0, 0)
        self.groupBox = QGroupBox(self.frame_19)
        self.groupBox.setObjectName(u"groupBox")
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy2)
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
        self.btnCopyCachePath.setIcon(icon5)

        self.horizontalLayout.addWidget(self.btnCopyCachePath)

        self.btnOpenCachePath = QPushButton(self.frame)
        self.btnOpenCachePath.setObjectName(u"btnOpenCachePath")
        self.btnOpenCachePath.setIcon(icon4)

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
        self.btnCopyDataPath.setIcon(icon5)

        self.horizontalLayout_21.addWidget(self.btnCopyDataPath)

        self.btnOpenDataPath = QPushButton(self.frame_21)
        self.btnOpenDataPath.setObjectName(u"btnOpenDataPath")
        self.btnOpenDataPath.setIcon(icon4)

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
        self.btnCopyRealPath.setIcon(icon5)

        self.horizontalLayout_2.addWidget(self.btnCopyRealPath)

        self.btnOpenRealPath = QPushButton(self.frame_2)
        self.btnOpenRealPath.setObjectName(u"btnOpenRealPath")
        self.btnOpenRealPath.setIcon(icon4)

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
        self.btnCopyPackagePath.setIcon(icon5)

        self.horizontalLayout_3.addWidget(self.btnCopyPackagePath)

        self.btnOpenPackagePath = QPushButton(self.frame_3)
        self.btnOpenPackagePath.setObjectName(u"btnOpenPackagePath")
        self.btnOpenPackagePath.setIcon(icon4)

        self.horizontalLayout_3.addWidget(self.btnOpenPackagePath)


        self.verticalLayout_8.addWidget(self.frame_3)


        self.verticalLayout_14.addWidget(self.groupBox)

        self.splitter_6.addWidget(self.frame_19)
        self.frameWebView = QFrame(self.splitter_6)
        self.frameWebView.setObjectName(u"frameWebView")
        sizePolicy3 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(1)
        sizePolicy3.setHeightForWidth(self.frameWebView.sizePolicy().hasHeightForWidth())
        self.frameWebView.setSizePolicy(sizePolicy3)
        self.frameWebView.setFrameShape(QFrame.StyledPanel)
        self.frameWebView.setFrameShadow(QFrame.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.frameWebView)
        self.verticalLayout_7.setSpacing(5)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(2, 2, 2, 2)
        self.label_15 = QLabel(self.frameWebView)
        self.label_15.setObjectName(u"label_15")

        self.verticalLayout_7.addWidget(self.label_15)

        self.graphicsView = QGraphicsView(self.frameWebView)
        self.graphicsView.setObjectName(u"graphicsView")
        self.graphicsView.setSceneRect(QRectF(0, 0, 0, 0))

        self.verticalLayout_7.addWidget(self.graphicsView)

        self.splitter_6.addWidget(self.frameWebView)

        self.verticalLayout_13.addWidget(self.splitter_6)

        self.splitter_5.addWidget(self.frame_15)

        self.horizontalLayout_4.addWidget(self.splitter_5)


        self.retranslateUi(TabPackage)

        QMetaObject.connectSlotsByName(TabPackage)
    # setupUi

    def retranslateUi(self, TabPackage):
        TabPackage.setWindowTitle(QCoreApplication.translate("TabPackage", u"Form", None))
#if QT_CONFIG(tooltip)
        self.toolButtonRefresh.setToolTip(QCoreApplication.translate("TabPackage", u"Refresh", None))
#endif // QT_CONFIG(tooltip)
        self.toolButtonRefresh.setText("")
#if QT_CONFIG(tooltip)
        self.toolButtonSortAscending.setToolTip(QCoreApplication.translate("TabPackage", u"Sort Ascending", None))
#endif // QT_CONFIG(tooltip)
        self.toolButtonSortAscending.setText("")
#if QT_CONFIG(tooltip)
        self.toolButtonSortDescending.setToolTip(QCoreApplication.translate("TabPackage", u"Sort Descending", None))
#endif // QT_CONFIG(tooltip)
        self.toolButtonSortDescending.setText("")
#if QT_CONFIG(tooltip)
        self.toolButtonRemovePackage.setToolTip(QCoreApplication.translate("TabPackage", u"Remove", None))
#endif // QT_CONFIG(tooltip)
        self.toolButtonRemovePackage.setText("")
#if QT_CONFIG(tooltip)
        self.checkBoxOpenExplorer.setToolTip(QCoreApplication.translate("TabPackage", u"Open Path", None))
#endif // QT_CONFIG(tooltip)
        self.checkBoxOpenExplorer.setText("")
#if QT_CONFIG(tooltip)
        self.checkBoxCopyClipboard.setToolTip(QCoreApplication.translate("TabPackage", u"Copy Path", None))
#endif // QT_CONFIG(tooltip)
        self.checkBoxCopyClipboard.setText(QCoreApplication.translate("TabPackage", u"...", None))
#if QT_CONFIG(whatsthis)
        self.lineEditSearchPackage.setWhatsThis("")
#endif // QT_CONFIG(whatsthis)
        self.lineEditSearchPackage.setPlaceholderText(QCoreApplication.translate("TabPackage", u"Search Package...", None))
        self.groupBox.setTitle(QCoreApplication.translate("TabPackage", u"Local Cache", None))
        self.label.setText(QCoreApplication.translate("TabPackage", u"Cache Path", None))
        self.btnCopyCachePath.setText(QCoreApplication.translate("TabPackage", u"Copy", None))
        self.btnOpenCachePath.setText(QCoreApplication.translate("TabPackage", u" Open", None))
        self.label_20.setText(QCoreApplication.translate("TabPackage", u"Data Path", None))
        self.btnCopyDataPath.setText(QCoreApplication.translate("TabPackage", u"Copy", None))
        self.btnOpenDataPath.setText(QCoreApplication.translate("TabPackage", u" Open", None))
        self.label_2.setText(QCoreApplication.translate("TabPackage", u"Real Path", None))
        self.btnCopyRealPath.setText(QCoreApplication.translate("TabPackage", u"Copy", None))
        self.btnOpenRealPath.setText(QCoreApplication.translate("TabPackage", u" Open", None))
        self.label_3.setText(QCoreApplication.translate("TabPackage", u"Package Path", None))
        self.btnCopyPackagePath.setText(QCoreApplication.translate("TabPackage", u"Copy", None))
        self.btnOpenPackagePath.setText(QCoreApplication.translate("TabPackage", u" Open", None))
        self.label_15.setText(QCoreApplication.translate("TabPackage", u"Dependencies Graph", None))
    # retranslateUi

