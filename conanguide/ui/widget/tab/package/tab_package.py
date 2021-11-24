import os
import pyperclip

from PySide2 import QtWidgets
from PySide2.QtCore import Slot

from conanguide.api.conan_api import ConanApi
from conanguide.ui.widget.tab.package.tab_package_ui import Ui_TabPackage
from conanguide.ui.controller.conan_package_inspect import ConanPackageInspectController
from conanguide.ui.controller.conan_package import ConanPackageController
from conanguide.ui.controller.conan_package_binary import ConanPackageBinaryController


class TabPackage(QtWidgets.QWidget, Ui_TabPackage):
    def __init__(self, conan_api: ConanApi, *args, obj=None, **kwargs):
        super(TabPackage, self).__init__(*args, **kwargs)

        self.setupUi(self)

        self.conan_api = conan_api

        # Line Edit Initialization for the conan cache path
        self.lineEditCachePath.setText(self.conan_api.cache_folder)

        # Treeview initialization for the conan package list
        self.ctrl_treeview_conan_package = ConanPackageController(self.treeViewPackage,
                                                                  self.conan_api)
        self.ctrl_treeview_conan_package.update()

        self.ctrl_treeview_conan_recipe_inspect = ConanPackageInspectController(self.treeViewPackageInspect,
                                                                                self.conan_api)

        self.ctrl_listview_conan_package_binary = ConanPackageBinaryController(self.listViewPackageBinary,
                                                                               self.conan_api)

        self.lineEditSearchPackage.textChanged.connect(lambda: self.ctrl_treeview_conan_package.filter(
            self.lineEditSearchPackage.text()))

    @Slot()
    def on_treeViewPackage_clicked(self):
        package_name = self.ctrl_treeview_conan_package.get_selected_item()

        # Step 1: Fill the path information to the text edit widget
        data_path = self.conan_api.get_package_data_path(package_name)
        self.lineEditDataPath.setText(data_path)
        self.lineEditRealPath.setText("")
        self.lineEditPackagePath.setText("")

        # Step 2: Inspect the package and fill the information to the treeview
        self.ctrl_treeview_conan_recipe_inspect.inspect(package_name)

        # Step 3: Fill the list of the package binaries to the list
        self.ctrl_listview_conan_package_binary.update(package_name)

    @Slot()
    def on_listViewPackageBinary_clicked(self):
        package_name = self.ctrl_treeview_conan_package.get_selected_item()
        package_binary_id = self.ctrl_listview_conan_package_binary.get_selected_item()

        real_path, package_path = self.conan_api.get_package_cache_path(package_name, package_binary_id)

        data_path = self.conan_api.get_package_data_path(package_name)

        self.lineEditDataPath.setText(data_path)
        self.lineEditRealPath.setText(real_path)
        self.lineEditPackagePath.setText(package_path)

    @Slot()
    def on_treeViewPackage_doubleClicked(self):
        if self.lineEditDataPath.text() != "":
            if self.checkBoxCopyClipboard.isChecked():
                pyperclip.copy(self.lineEditDataPath.text())

            if self.checkBoxOpenExplorer.isChecked():
                os.startfile(self.lineEditDataPath.text())

    @Slot()
    def on_listViewPackageBinary_doubleClicked(self):
        if self.lineEditPackagePath.text() != "":
            if self.checkBoxCopyClipboard.isChecked():
                pyperclip.copy(self.lineEditPackagePath.text())

            if self.checkBoxOpenExplorer.isChecked():
                os.startfile(self.lineEditPackagePath.text())

    @Slot()
    def on_btnCopyCachePath_pressed(self):
        if self.lineEditConanPath.text() != "":
            pyperclip.copy(self.lineEditConanPath.text())
            # self.statusBar.showMessage("Conan cache path is copied to clipboard!", 2000)

    @Slot()
    def on_btnCopyDataPath_pressed(self):
        if self.lineEditDataPath.text() != "":
            pyperclip.copy(self.lineEditDataPath.text())
            # self.statusBar.showMessage("Conan package data path is copied to clipboard!", 2000)

    @Slot()
    def on_btnCopyRealPath_pressed(self):
        if self.lineEditRealPath.text() != "":
            pyperclip.copy(self.lineEditRealPath.text())
            # self.statusBar.showMessage("Conan package real path is copied to clipboard!", 2000)

    @Slot()
    def on_btnCopyPackagePath_pressed(self):
        if self.lineEditPackagePath.text() != "":
            pyperclip.copy(self.lineEditPackagePath.text())
            # self.statusBar.showMessage("Conan package path is copied to clipboard!", 2000)

    @Slot()
    def on_btnOpenCachePath_pressed(self):
        if self.lineEditCachePath.text() != "":
            os.startfile(self.lineEditCachePath.text())

    @Slot()
    def on_btnOpenDataPath_pressed(self):
        if self.lineEditDataPath.text() != "":
            os.startfile(self.lineEditDataPath.text())

    @Slot()
    def on_btnOpenRealPath_pressed(self):
        if self.lineEditRealPath.text() != "":
            os.startfile(self.lineEditRealPath.text())

    @Slot()
    def on_btnOpenPackagePath_pressed(self):
        if self.lineEditPackagePath.text() != "":
            os.startfile(self.lineEditPackagePath.text())

    @Slot()
    def on_toolButtonSortAscending_clicked(self):
        self.toolButtonSortAscending.setChecked(True)
        self.toolButtonSortDescending.setChecked(False)

        self.ctrl_treeview_conan_package.sort_ascending()

    @Slot()
    def on_toolButtonSortDescending_clicked(self):
        self.toolButtonSortDescending.setChecked(True)
        self.toolButtonSortAscending.setChecked(False)

        self.ctrl_treeview_conan_package.sort_descending()

    def refresh(self):
        # TODO: Implement the refresh function and the button
        pass
