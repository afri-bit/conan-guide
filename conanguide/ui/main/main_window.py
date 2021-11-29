import datetime
import os

from PySide2 import QtWidgets
from PySide2.QtCore import Slot

from conanguide.api.conan_api import ConanApi
from conanguide.client.runner.command_runner import CommandRunner
from conanguide.ui.config.ui_config import UIConfiguration
from conanguide.ui.main.main_window_ui import Ui_MainWindow
from conanguide.utils.cmd.command_builder import ConanCommandBuilder
from conanguide.ui.widget.tab.profile.tab_profile import TabProfile
from conanguide.ui.widget.tab.cache.tab_cache import TabCache
from conanguide.ui.widget.tab.remote.tab_remote import TabRemote


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, *args, obj=None, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.setupUi(self)

        self.conan_api = ConanApi()
        self.ui_config = UIConfiguration()

        self.__init()

    def __init(self):
        # Initialize the package tab
        self.tab_cache = TabCache(self.conan_api)
        self.layoutTabCache.addWidget(self.tab_cache)

        # Initialize the profile tab
        self.tab_profile = TabProfile(self.conan_api)
        self.layoutTabProfile.addWidget(self.tab_profile)

        # Initialize the remote tab
        self.tab_remote = TabRemote(self.conan_api)
        self.layoutTabRemote.addWidget(self.tab_remote)

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

        # Initialize command runner thread
        self.command_runner = CommandRunner()
        self.command_runner.signals.start.connect(self.on_command_start)
        self.command_runner.signals.error.connect(self.on_command_error)
        self.command_runner.signals.progress.connect(self.on_command_progress)
        self.command_runner.signals.result.connect(self.on_command_result)
        self.command_runner.signals.finished.connect(self.on_command_finished)

        # self.__load_ui_state()

    def closeEvent(self, event) -> None:
        self.__save_ui_state()

    def on_command_start(self, data: str):
        self.set_loading_state(True)
        self.log_to_console("\n")
        self.log_to_console("--------------------------------------------", dt=True)
        self.log_to_console(data + "\n")

    def on_command_result(self, data: str):
        self.log_to_console(data)

    def on_command_error(self, data: str):
        self.log_to_console(data)

    def on_command_finished(self):
        self.set_loading_state(False)
        self.__refresh()

    def on_command_progress(self, data: str):
        self.log_to_console(data)

    @Slot()
    def on_actionViewCache_triggered(self):
        self.tabWidgetMain.setCurrentWidget(self.tabCache)

    @Slot()
    def on_actionViewWorkspace_triggered(self):
        self.tabWidgetMain.setCurrentWidget(self.tabWorkspace)

    @Slot()
    def on_actionViewProfile_triggered(self):
        self.tabWidgetMain.setCurrentWidget(self.tabProfile)

    @Slot()
    def on_actionViewRemote_triggered(self):
        self.tabWidgetMain.setCurrentWidget(self.tabRemote)

    @Slot()
    def on_actionViewSettings_triggered(self):
        self.tabWidgetMain.setCurrentWidget(self.tabSettings)

    @Slot()
    def on_actionConanCreate_triggered(self):
        self.__execute_conan_create()

    @Slot()
    def on_actionConanInstall_triggered(self):
        self.__execute_conan_install()

    @Slot()
    def on_actionConanBuild_triggered(self):
        self.__execute_conan_build()

    @Slot()
    def on_actionConanSource_triggered(self):
        self.__execute_conan_source()

    @Slot()
    def on_actionConanPackage_triggered(self):
        self.__execute_conan_package()

    @Slot()
    def on_actionConanExport_triggered(self):
        self.__execute_conan_export()

    @Slot()
    def on_actionConanExportPackage_triggered(self):
        self.__execute_conan_export_package()

    @Slot()
    def on_actionRefresh_triggered(self):
        self.__refresh()

    @Slot()
    def on_actionHelpConanio_triggered(self):
        import webbrowser

        webbrowser.open("https://conan.io/")

    @Slot()
    def on_toolBtnExplorerRecipePath_pressed(self):
        self.__set_folder_path(self.lineEditRecipePath)

    @Slot()
    def on_toolBtnExplorerInstallPath_pressed(self):
        self.__set_folder_path(self.lineEditInstallPath)

    @Slot()
    def on_toolBtnExplorerBuildPath_pressed(self):
        self.__set_folder_path(self.lineEditBuildPath)

    @Slot()
    def on_toolBtnExplorerSourcePath_pressed(self):
        self.__set_folder_path(self.lineEditSourcePath)

    @Slot()
    def on_toolBtnExplorerPackagePath_pressed(self):
        self.__set_folder_path(self.lineEditPackageExpPath)

    def run_command(self, cmd):
        self.command_runner.set_command(cmd)
        self.command_runner.start()

    def log_to_console(self, msg: str, dt=False):
        if dt:
            log_msg = str(datetime.datetime.now()) + " " + msg + "\n"
        else:
            log_msg = msg
        self.console.insertPlainText(log_msg)
        if self.toolButtonConsoleScrollToEnd.isChecked():
            self.console.verticalScrollBar().setValue(self.console.verticalScrollBar().maximum())

    def set_loading_state(self, state: bool):
        if state:
            self.progressBar.setMaximum(0)
            self.labelStatusMessage.setText("Loading...  ")
        else:
            self.labelStatusMessage.setText("")
            self.progressBar.setMaximum(100)

    def __refresh(self):
        self.ctrl_treeview_conan_recipe.update()
        self.ctrl_tableview_conan_remote.update()
        self.ctrl_listview_conan_profile.update()

    def __execute_conan_create(self):
        self.run_command(ConanCommandBuilder.build_command_create(path_recipe=self.lineEditRecipePath.text(),
                                                                  user=self.lineEditUser.text(),
                                                                  channel=self.lineEditChannel.text(),
                                                                  profile=self.comboBoxProfile.currentText(),
                                                                  params=self.lineEditAdditionalParams.text()))

    def __execute_conan_install(self):
        if self.lineEditInstallPath.text() == "":
            self.log_to_console("ERROR: Please specify the installation path.", dt=True)
            return

        self.run_command(ConanCommandBuilder.build_command_install(path_recipe=self.lineEditRecipePath.text(),
                                                                   install_folder=self.lineEditInstallPath.text(),
                                                                   user=self.lineEditUser.text(),
                                                                   channel=self.lineEditChannel.text(),
                                                                   profile=self.comboBoxProfile.currentText(),
                                                                   params=self.lineEditAdditionalParams.text()))

    def __execute_conan_build(self):
        if self.lineEditBuildPath.text() == "":
            self.log_to_console("ERROR: Please specify the build path.", dt=True)
            return

        self.run_command(ConanCommandBuilder.build_command_build(path_recipe=self.lineEditRecipePath.text(),
                                                                 build_folder=self.lineEditBuildPath.text(),
                                                                 install_folder=self.lineEditInstallPath.text(),
                                                                 package_folder=self.lineEditPackagePath.text(),
                                                                 source_folder=self.lineEditSourcePath.text(),
                                                                 params=self.lineEditAdditionalParams.text()))

    def __execute_conan_source(self):
        if self.lineEditSourcePath.text() == "":
            self.log_to_console("ERROR: Please specify the source path.", dt=True)
            return

        self.run_command(ConanCommandBuilder.build_command_source(path_recipe=self.lineEditRecipePath.text(),
                                                                  source_folder=self.lineEditSourcePath.text(),
                                                                  install_folder=self.lineEditInstallPath.text()))

    def __execute_conan_package(self):
        self.run_command(ConanCommandBuilder.build_command_package(path_recipe=self.lineEditRecipePath.text(),
                                                                   build_folder=self.lineEditBuildPath.text(),
                                                                   install_folder=self.lineEditInstallPath.text(),
                                                                   package_folder=self.lineEditPackagePath.text(),
                                                                   source_folder=self.lineEditSourcePath.text()))

    def __execute_conan_export(self):
        self.run_command(ConanCommandBuilder.build_command_export(path_recipe=self.lineEditRecipePath.text(),
                                                                  params=self.lineEditAdditionalParams.text()))

    def __execute_conan_export_package(self):
        self.run_command(
            ConanCommandBuilder.build_command_export_package(path_recipe=self.lineEditRecipePath.text(),
                                                             build_folder=self.lineEditBuildPath.text(),
                                                             install_folder=self.lineEditInstallPath.text(),
                                                             package_folder=self.lineEditPackagePath.text(),
                                                             source_folder=self.lineEditSourcePath.text(),
                                                             params=self.lineEditAdditionalParams.text())
        )

    def __set_folder_path(self, view: QtWidgets.QLineEdit):
        folder_path = QtWidgets.QFileDialog.getExistingDirectory(self, "Select Folder")

        if folder_path != "":
            view.setText(os.path.abspath(folder_path))

    def __save_ui_state(self):

        # TODO: Get all the UI state from all TABS

        # TODO: Write to file

        # Configuration
        # self.ui_config.add_value("user", self.lineEditUser.text())
        # self.ui_config.add_value("channel", self.lineEditChannel.text())
        # self.ui_config.add_value("recipe_path", self.lineEditRecipePath.text())
        # self.ui_config.add_value("install_path", self.lineEditInstallPath.text())
        # self.ui_config.add_value("build_path", self.lineEditBuildPath.text())
        # self.ui_config.add_value("source_path", self.lineEditSourcePath.text())
        # self.ui_config.add_value("package_path", self.lineEditPackageExpPath.text())
        # self.ui_config.add_value("parameter", self.lineEditAdditionalParams.text())
        # self.ui_config.add_value("profile", self.comboBoxProfile.currentText())
        #
        # # Main Window
        # self.ui_config.add_header("main_window")
        # self.ui_config.add_value("x", self.pos().x(), "main_window")
        # self.ui_config.add_value("y", self.pos().y() + 30, "main_window")
        # self.ui_config.add_value("width", self.width(), "main_window")
        # self.ui_config.add_value("height", self.height(), "main_window")
        #
        # # DockWidget - Recipe
        # # self.ui_config.add_header("dock_recipe")
        # # self.ui_config.add_value("open_explorer", self.checkBoxOpenExplorer.isChecked(), "dock_recipe")
        # # self.ui_config.add_value("copy_clipboard", self.checkBoxCopyClipboard.isChecked(), "dock_recipe")
        #
        # # DockWidget - Console
        # self.ui_config.add_header("dock_console")
        # self.ui_config.add_value("scroll_end", self.toolButtonConsoleScrollToEnd.isChecked(), "dock_console")
        #
        # self.ui_config.save_config()
        pass

    def __load_ui_state(self):

        # TODO: Load UI State and distribute to all TABS
        # config = self.ui_config.load_config()
        # if config is not None:
        #     # Configuration
        #     self.lineEditUser.setText(config["user"])
        #     self.lineEditChannel.setText(config["channel"])
        #     self.lineEditRecipePath.setText(config["recipe_path"])
        #     self.lineEditInstallPath.setText(config["install_path"])
        #     self.lineEditBuildPath.setText(config["build_path"])
        #     self.lineEditSourcePath.setText(config["source_path"])
        #     self.lineEditPackageExpPath.setText(config["package_path"])
        #     self.lineEditAdditionalParams.setText(config["parameter"])
        #     self.comboBoxProfile.setCurrentText(config["profile"])
        #
        #     # Window
        #     self.setGeometry(config["main_window"]["x"],
        #                      config["main_window"]["y"],
        #                      config["main_window"]["width"],
        #                      config["main_window"]["height"])
        #
        #     # DockWidget - Recipe
        #     self.checkBoxOpenExplorer.setChecked(config["dock_recipe"]["open_explorer"])
        #     self.checkBoxCopyClipboard.setChecked(config["dock_recipe"]["copy_clipboard"])
        #
        #     # DockWidget - Console
        #     self.toolButtonConsoleScrollToEnd.setChecked(config["dock_console"]["scroll_end"])
        pass
