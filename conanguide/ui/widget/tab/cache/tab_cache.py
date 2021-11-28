import os
import pyperclip

from PySide2 import QtWidgets
from PySide2.QtCore import Slot

from conanguide.api.conan_api import ConanApi
from conanguide.ui.widget.tab.cache.tab_cache_ui import Ui_TabCache
from conanguide.ui.controller.tab.cache.conan_recipe import ConanRecipeController
from conanguide.ui.controller.tab.cache.conan_recipe_inspect import ConanRecipeInspectController
from conanguide.ui.controller.tab.cache.conan_package import ConanPackageController
from conanguide.ui.controller.tab.cache.conan_package_inspect import ConanPackageInspectController


class TabCache(QtWidgets.QWidget, Ui_TabCache):
    def __init__(self, conan_api: ConanApi, *args, obj=None, **kwargs):
        super(TabCache, self).__init__(*args, **kwargs)

        self.setupUi(self)

        self.conan_api = conan_api

        # Line Edit Initialization for the conan cache path
        self.lineEditCachePath.setText(self.conan_api.cache_folder)

        # Treeview initialization for the conan recipe list
        self.ctrl_treeview_conan_recipe = ConanRecipeController(self.treeViewRecipe,
                                                                self.conan_api)
        self.ctrl_treeview_conan_recipe.update()

        self.ctrl_treeview_conan_recipe_inspect = ConanRecipeInspectController(self.treeViewRecipeInspect,
                                                                               self.conan_api)

        self.ctrl_listview_conan_package = ConanPackageController(self.listViewPackage,
                                                                  self.conan_api)

        self.ctrl_treeview_conan_package_inspect = ConanPackageInspectController(self.treeViewPackageInspect,
                                                                                 self.conan_api)

        self.lineEditSearchRecipe.textChanged.connect(lambda: self.ctrl_treeview_conan_recipe.filter(
            self.lineEditSearchRecipe.text()))

    @Slot()
    def on_treeViewRecipe_clicked(self):
        recipe_id = self.ctrl_treeview_conan_recipe.get_selected_item()

        # Step 1: Fill the path information to the text edit widget
        data_path = self.conan_api.get_package_data_path(recipe_id)
        self.lineEditDataPath.setText(data_path)
        self.lineEditRealPath.setText("")
        self.lineEditPackagePath.setText("")

        # Step 2: Inspect the package and fill the information to the treeview
        self.ctrl_treeview_conan_recipe_inspect.inspect(recipe_id)

        # Step 3: Fill the list of the package binaries to the list
        self.ctrl_listview_conan_package.update(recipe_id)

        # Step 4: Set the conan package inspect treeview to initial state
        self.ctrl_treeview_conan_package_inspect.initialize()

    @Slot()
    def on_listViewPackage_clicked(self):
        recipe_id = self.ctrl_treeview_conan_recipe.get_selected_item()
        package_id = self.ctrl_listview_conan_package.get_selected_item()

        # ========== Section to update the path
        real_path, package_path = self.conan_api.get_package_cache_path(recipe_id, package_id)

        data_path = self.conan_api.get_package_data_path(recipe_id)

        self.lineEditDataPath.setText(data_path)
        self.lineEditRealPath.setText(real_path)
        self.lineEditPackagePath.setText(package_path)

        # ========== Section to inspect the package
        self.ctrl_treeview_conan_package_inspect.inspect(recipe_id, package_id)

    @Slot()
    def on_treeViewRecipe_doubleClicked(self):
        if self.lineEditDataPath.text() != "":
            if self.checkBoxCopyClipboard.isChecked():
                pyperclip.copy(self.lineEditDataPath.text())

            if self.checkBoxOpenExplorer.isChecked():
                os.startfile(self.lineEditDataPath.text())

    @Slot()
    def on_listViewPackage_doubleClicked(self):
        if self.lineEditPackagePath.text() != "":
            if self.checkBoxCopyClipboard.isChecked():
                pyperclip.copy(self.lineEditPackagePath.text())

            if self.checkBoxOpenExplorer.isChecked():
                os.startfile(self.lineEditPackagePath.text())

    @Slot()
    def on_btnCopyCachePath_pressed(self):
        if self.lineEditConanPath.text() != "":
            pyperclip.copy(self.lineEditConanPath.text())

    @Slot()
    def on_btnCopyDataPath_pressed(self):
        if self.lineEditDataPath.text() != "":
            pyperclip.copy(self.lineEditDataPath.text())

    @Slot()
    def on_btnCopyRealPath_pressed(self):
        if self.lineEditRealPath.text() != "":
            pyperclip.copy(self.lineEditRealPath.text())

    @Slot()
    def on_btnCopyPackagePath_pressed(self):
        if self.lineEditPackagePath.text() != "":
            pyperclip.copy(self.lineEditPackagePath.text())

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

    @Slot()
    def on_toolButtonRemoveRecipe_clicked(self):
        recipe_id = self.ctrl_treeview_conan_recipe.get_selected_item()
        if recipe_id is not None:
            reply = QtWidgets.QMessageBox.question(self, f"Delete Recipe",
                                                   f"Are you sure to delete the recipe '{recipe_id}'",
                                                   QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No,
                                                   QtWidgets.QMessageBox.No)

            if reply == QtWidgets.QMessageBox.Yes:
                self.ctrl_treeview_conan_recipe.remove_recipe(recipe_id)

                # Refiltered if the filter is applied
                # During removing process the filter was reseted to empty, now apply the filter again cover the user
                # experience. This is kinda of workaround.
                self.ctrl_treeview_conan_recipe.filter(self.lineEditSearchRecipe.text())

                self.ctrl_treeview_conan_recipe_inspect.initialize()

                self.ctrl_listview_conan_package.clear()
                self.ctrl_treeview_conan_package_inspect.initialize()



    @Slot()
    def on_toolButtonRemovePackage_clicked(self):
        package_id = self.ctrl_listview_conan_package.get_selected_item()
        if package_id is not None:
            recipe_id = self.ctrl_treeview_conan_recipe.get_selected_item()

            reply = QtWidgets.QMessageBox.question(self, f"Delete Package - {recipe_id}",
                                                   f"Are you sure to delete the package {package_id}",
                                                   QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No,
                                                   QtWidgets.QMessageBox.No)

            if reply == QtWidgets.QMessageBox.Yes:
                self.ctrl_listview_conan_package.remove_selected_package(recipe_id)
                self.ctrl_treeview_conan_package_inspect.initialize()
                self.refresh()

    @Slot()
    def on_toolButtonRefresh_clicked(self):
        self.refresh()

    def refresh(self):
        self.ctrl_treeview_conan_recipe.update()

        self.ctrl_treeview_conan_recipe_inspect.initialize()
        self.ctrl_listview_conan_package.clear()
        self.ctrl_treeview_conan_package_inspect.initialize()
