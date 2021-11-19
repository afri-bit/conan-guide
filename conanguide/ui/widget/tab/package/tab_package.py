import os
import pyperclip

from PySide2 import QtWidgets
from PySide2.QtCore import Slot

from conanguide.api.conan_api import ConanApi
from conanguide.ui.widget.tab.package.tab_package_ui import Ui_TabPackage
from conanguide.ui.controller.conan_recipe import ConanRecipeController
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

        # Treeview initialization for the conan recipe list
        self.treeViewRecipe.setHeaderHidden(True)
        self.ctrl_treeview_conan_recipe = ConanRecipeController(self.treeViewRecipe, self.conan_api)
        self.ctrl_treeview_conan_recipe.update()

        self.ctrl_treeview_conan_recipe_inspect = ConanPackageInspectController(self.treeViewPackageInspect,
                                                                                self.conan_api)

        self.ctrl_treeview_conan_package = ConanPackageController(self.treeViewPackage,
                                                                  self.conan_api)
        self.ctrl_treeview_conan_package.update()

        self.ctrl_listview_conan_package_binary = ConanPackageBinaryController(self.listViewPackageBinary,
                                                                               self.conan_api)

        self.lineEditSearchPackage.textChanged.connect(lambda: self.ctrl_treeview_conan_recipe.filter(
            self.lineEditSearchPackage.text()))

    @Slot()
    def on_toolButtonSortAscending_clicked(self):
        self.toolButtonSortAscending.setChecked(True)
        self.toolButtonSortDescending.setChecked(False)

        # self.ctrl_listview_conan_profile.sort_ascending()

    @Slot()
    def on_toolButtonSortDescending_clicked(self):
        self.toolButtonSortDescending.setChecked(True)
        self.toolButtonSortAscending.setChecked(False)

        # self.ctrl_listview_conan_profile.sort_descending()

    @Slot()
    def on_treeViewPackage_clicked(self):
        package_name = str(self.treeViewPackage.selectedIndexes()[0].data())
        self.ctrl_treeview_conan_recipe_inspect.inspect(package_name)
        data_path = self.conan_api.get_package_data_path(package_name)
        self.lineEditDataPath.setText(data_path)
        self.lineEditRealPath.setText("")
        self.lineEditPackagePath.setText("")

        self.ctrl_listview_conan_package_binary.update(package_name)

    @Slot()
    def on_treeViewRecipe_clicked(self):
        if self.treeViewRecipe.currentIndex().parent().data() is not None:  # Package with hash id
            recipe_id = self.treeViewRecipe.currentIndex().parent().data()
            package_hash = self.treeViewRecipe.currentIndex().data()

            real_path, package_path = self.conan_api.get_package_cache_path(recipe_id, package_hash)

            data_path = self.conan_api.get_package_data_path(recipe_id)
            self.lineEditDataPath.setText(data_path)
            self.lineEditRealPath.setText(real_path)
            self.lineEditPackagePath.setText(package_path)

        else:  # Parent of the package
            recipe_id = self.treeViewRecipe.currentIndex().data()
            self.ctrl_treeview_conan_recipe_inspect.inspect(recipe_id)
            data_path = self.conan_api.get_package_data_path(recipe_id)
            self.lineEditDataPath.setText(data_path)
            self.lineEditRealPath.setText("")
            self.lineEditPackagePath.setText("")

    @Slot()
    def on_treeViewRecipe_doubleClicked(self):
        if self.lineEditPackagePath.text() != "":
            if self.checkBoxCopyClipboard.isChecked():
                pyperclip.copy(self.lineEditPackagePath.text())
                # self.statusBar.showMessage("Package path is copied to clipboard!", 2000)

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

        self.ctrl_treeview_conan_recipe.sort_ascending()

    @Slot()
    def on_toolButtonSortDescending_clicked(self):
        self.toolButtonSortDescending.setChecked(True)
        self.toolButtonSortAscending.setChecked(False)

        self.ctrl_treeview_conan_recipe.sort_descending()
