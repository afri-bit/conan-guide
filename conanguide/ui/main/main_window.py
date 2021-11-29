from PySide2 import QtWidgets
from PySide2.QtCore import Slot

from conanguide.api.conan_api import ConanApi
from conanguide.ui.config.ui_config import UIConfiguration
from conanguide.ui.main.main_window_ui import Ui_MainWindow
from conanguide.ui.widget.tab.cache.tab_cache import TabCache
from conanguide.ui.widget.tab.profile.tab_profile import TabProfile
from conanguide.ui.widget.tab.remote.tab_remote import TabRemote
from conanguide.ui.widget.tab.workspace.tab_workspace import TabWorkspace


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

        # Initialize the workspace tab
        self.tab_workspace = TabWorkspace(self.conan_api)
        self.layoutTabWorkspace.addWidget(self.tab_workspace)

        # self.__load_ui_state()

    def closeEvent(self, event) -> None:
        self.__save_ui_state()

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
        # TODO: Change view to workspace tab
        # TODO: Execute the command over the tab widget accordingly
        pass

    @Slot()
    def on_actionConanBuild_triggered(self):
        # TODO: Change view to workspace tab
        # TODO: Execute the command over the tab widget accordingly
        pass

    @Slot()
    def on_actionConanSource_triggered(self):
        # TODO: Change view to workspace tab
        # TODO: Execute the command over the tab widget accordingly
        pass

    @Slot()
    def on_actionConanPackage_triggered(self):
        # TODO: Change view to workspace tab
        # TODO: Execute the command over the tab widget accordingly
        pass

    @Slot()
    def on_actionConanExport_triggered(self):
        # TODO: Change view to workspace tab
        # TODO: Execute the command over the tab widget accordingly
        pass

    @Slot()
    def on_actionConanExportPackage_triggered(self):
        # TODO: Change view to workspace tab
        # TODO: Execute the command over the tab widget accordingly
        pass

    @Slot()
    def on_actionRefresh_triggered(self):
        self.__refresh()

    @Slot()
    def on_actionHelpConanio_triggered(self):
        import webbrowser

        webbrowser.open("https://conan.io/")

    def __refresh(self):
        # TODO: Refresh all the tabs. The tabs now have the refresh function
        pass

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
