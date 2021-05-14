import os
import subprocess

import datetime

import pyperclip
from PyQt5 import QtWidgets

from conanblade.api.conan_api import ConanApi
from conanblade.ui.controller.conan_profile import ConanProfileController, ConanProfileDetailController
from conanblade.ui.controller.conan_recipe import ConanRecipeController, ConanRecipeInspectController
from conanblade.ui.controller.conan_remote import ConanRemoteListController
from conanblade.ui.main.main_window_ui import Ui_MainWindow


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, *args, obj=None, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.setupUi(self)

        self.conan_api = ConanApi()

        self.__init()

    def __init(self):
        # Line Edit Initialization for the conan cache path
        self.lineEditConanPath.setText(self.conan_api.get_cache_folder())

        # Treeview initialization for the conan recipe list
        self.treeViewRecipe.setHeaderHidden(True)
        self.ctrl_treeview_conan_recipe = ConanRecipeController(self.treeViewRecipe, self.conan_api)
        self.ctrl_treeview_conan_recipe.update()

        self.ctrl_treeview_conan_recipe_inspect = ConanRecipeInspectController(self.treeViewRecipeInspect,
                                                                               self.conan_api)

        # Listview initialization for the profile list
        self.ctrl_listview_conan_profile = ConanProfileController(self.listViewProfile, self.conan_api)
        self.ctrl_listview_conan_profile.update()

        # Treeview initialization for the profile details
        self.ctrl_treeview_conan_profile_detail = ConanProfileDetailController(self.treeViewProfileDetail,
                                                                               self.conan_api)
        # Tableview initialization for the remote list
        self.ctrl_tableview_conan_remote = ConanRemoteListController(self.tableViewRemoteList, self.conan_api)
        self.ctrl_tableview_conan_remote.update()

        # Fill combobox with profile name
        self.comboBoxProfile.addItems(self.conan_api.profile_list())

        # Initialize status bar
        # Initialize progress bar for the status bar
        self.progressBar = QtWidgets.QProgressBar()
        self.progressBar.setMaximum(100)
        self.progressBar.setMinimum(0)
        self.progressBar.setValue(0)
        self.progressBar.setMaximumWidth(200)
        self.progressBar.setTextVisible(False)
        # Initialize status message
        self.labelStatusMessage = QtWidgets.QLabel()
        # Add permanent widgets to the status bar
        self.statusBar.addPermanentWidget(self.labelStatusMessage)
        self.statusBar.addPermanentWidget(self.progressBar)

        # Initialize console
        self.console.ensureCursorVisible()

    def on_dockWidgetRecipe_visibilityChanged(self):
        self.actionViewRecipe.setChecked(self.dockWidgetRecipe.isVisible())

    def on_dockWidgetProfile_visibilityChanged(self):
        self.actionViewProfile.setChecked(self.dockWidgetProfile.isVisible())

    def on_dockWidgetConsole_visibilityChanged(self):
        self.actionViewConsole.setChecked(self.dockWidgetConsole.isVisible())

    def on_treeViewRecipe_clicked(self):
        if self.treeViewRecipe.currentIndex().parent().data() is not None:
            recipe_id = self.treeViewRecipe.currentIndex().parent().data()
            package_hash = self.treeViewRecipe.currentIndex().data()

            real_path, package_path = self.conan_api.get_package_cache_path(recipe_id, package_hash)

            self.lineEditRealPath.setText(real_path)
            self.lineEditPackagePath.setText(package_path)

        else:
            recipe_id = self.treeViewRecipe.currentIndex().data()
            self.ctrl_treeview_conan_recipe_inspect.inspect(recipe_id)
            self.lineEditRealPath.setText("")
            self.lineEditPackagePath.setText("")

    def on_treeViewRecipe_doubleClicked(self):
        self.log_to_console("kwhfiwehfui")
        if self.lineEditPackagePath.text() != "":
            if self.checkBoxCopyClipboard.isChecked():
                pyperclip.copy(self.lineEditPackagePath.text())
                self.statusBar.showMessage("Package path is copied to clipboard!", 3000)

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

    def set_loading_state(self, state: bool):
        self.dockWidgetProfile.setEnabled(not state)
        self.dockWidgetRecipe.setEnabled(not state)
        self.frameMain.setEnabled(not state)

        if state:
            self.progressBar.setMaximum(0)
            self.labelStatusMessage.setText("Loading...  ")
        else:
            self.labelStatusMessage.setText("")
            self.progressBar.setMaximum(100)
