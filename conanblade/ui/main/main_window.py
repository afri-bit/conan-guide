import os

import datetime

import pyperclip
from PyQt5 import QtWidgets

from conanblade.api.conan_api import ConanApi
from conanblade.ui.controller.conan_profile import ConanProfileController, ConanProfileDetailController
from conanblade.ui.controller.conan_recipe import ConanRecipeController
from conanblade.ui.controller.conan_remote import ConanRemoteListController
from conanblade.ui.main.main_window_ui import Ui_MainWindow


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, *args, obj=None, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.setupUi(self)

        self.conan_api = ConanApi()

        # Line Edit Initialization for the conan cache path
        self.lineEditConanPath.setText(self.conan_api.get_cache_folder())

        # Treeview initialization for the conan package list
        self.treeViewRecipe.setHeaderHidden(True)
        self.ctrl_treeview_conan_recipe = ConanRecipeController(self.treeViewRecipe, self.conan_api)
        self.ctrl_treeview_conan_recipe.update()

        # Listview initialization for the profile list
        self.ctrl_listview_conan_profile = ConanProfileController(self.listViewProfile, self.conan_api)
        self.ctrl_listview_conan_profile.update()

        # Treeview initialization for the profile details
        self.ctrl_treeview_conan_profile_detail = ConanProfileDetailController(self.treeViewProfileDetail,
                                                                               self.conan_api)

        # Tableview initialization for the remote list
        self.ctrl_tableview_conan_remote = ConanRemoteListController(self.tableViewRemoteList, self.conan_api)
        self.ctrl_tableview_conan_remote.update()

    def on_treeViewRecipe_clicked(self):
        if self.treeViewRecipe.currentIndex().parent().data() is not None:
            recipe_id = self.treeViewRecipe.currentIndex().parent().data()
            package_hash = self.treeViewRecipe.currentIndex().data()

            real_path, package_path = self.conan_api.get_package_cache_path(recipe_id, package_hash)

            self.lineEditRealPath.setText(real_path)
            self.lineEditPackagePath.setText(package_path)
        else:
            self.lineEditRealPath.setText("")
            self.lineEditPackagePath.setText("")

    def on_treeViewRecipe_doubleClicked(self):
        if self.lineEditPackagePath.text() != "":
            pyperclip.copy(self.lineEditPackagePath.text())
            self.log_to_console("Package path is copied to clipboard!")

            if self.checkBoxOpenExplorer.isChecked():
                os.startfile(self.lineEditPackagePath.text())

    def on_listViewProfile_clicked(self):
        self.ctrl_treeview_conan_profile_detail.show_detail(self.listViewProfile.currentIndex().data())

    def on_toolBtnExplorerRecipePath_pressed(self):
        self.__set_folder_path(self.lineEditRecipePath)

    def on_toolBtnExplorerInstallPath_pressed(self):
        self.__set_folder_path(self.lineEditInstallPath)

    def on_toolBtnExplorerBuildPath_pressed(self):
        self.__set_folder_path(self.lineEditBuildPath)

    def on_toolBtnExplorerSourcePath_pressed(self):
        self.__set_folder_path(self.lineEditSourcePath)

    def on_toolBtnExplorerPackagePath_pressed(self):
        self.__set_folder_path(self.lineEditPackageExpPath)

    def log_to_console(self, msg: str):
        log_msg = str(datetime.datetime.now()) + ": " + msg + "\n"
        self.console.insertPlainText(log_msg)
        self.console.verticalScrollBar().setValue(self.console.verticalScrollBar().maximum())

    def __set_folder_path(self, view: QtWidgets.QLineEdit):
        folder_path = QtWidgets.QFileDialog.getExistingDirectory(self, "Select Folder")

        if folder_path != "":
            view.setText(os.path.abspath(folder_path))

