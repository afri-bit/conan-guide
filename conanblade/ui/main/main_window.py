import datetime
import pyperclip
from PyQt5 import QtWidgets
from PyQt5.Qt import QStandardItemModel

from conanblade.api.conan_api import ConanApi
from conanblade.ui.controller.conan_profile import ConanProfileController
from conanblade.ui.controller.conan_recipe import ConanRecipeController
from conanblade.ui.main.main_window_ui import Ui_MainWindow


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, *args, obj=None, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.setupUi(self)

        self.conan_api = ConanApi()

        # Line Edit Initialization for the conan cache path
        self.lineEditConanPath.setText(self.conan_api.get_cache_folder())

        # Treeview initialization for the conan package list
        self.model_tv_conan_recipe = QStandardItemModel()
        self.treeViewRecipe.setHeaderHidden(True)
        self.treeViewRecipe.setModel(self.model_tv_conan_recipe)
        self.ctrl_tv_conan_recipe = ConanRecipeController(self.treeViewRecipe, self.model_tv_conan_recipe)
        self.ctrl_tv_conan_recipe.init()
        self.treeViewRecipe.clicked.connect(self.on_treeViewRecipe_clicked)
        self.treeViewRecipe.clicked.connect(self.on_treeViewRecipe_doubleClicked)

        # Listview initialization for the profile list
        self.model_lv_profile = QStandardItemModel()
        self.listViewProfile.setModel(self.model_lv_profile)
        self.ctrl_lv_conan_profile = ConanProfileController(self.listViewProfile, self.model_lv_profile)
        self.ctrl_lv_conan_profile.init()

        # PlainTextEdit initialization for console
        self.console.ensureCursorVisible()


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

    def log_to_console(self, msg: str):
        log_msg = str(datetime.datetime.now()) + ": " + msg + "\n"
        self.console.insertPlainText(log_msg)
        self.console.verticalScrollBar().setValue(self.console.verticalScrollBar().maximum())