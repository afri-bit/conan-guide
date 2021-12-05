import webbrowser

from PySide2 import QtWidgets, QtCore
from PySide2.QtCore import Slot

from conanguide.api.conan_api import ConanApi
from conanguide.ui.config.ui_config import UIConfiguration
from conanguide.ui.main.main_window_ui import Ui_MainWindow
from conanguide.ui.widget.tab.cache.tab_cache import TabCache, TabCacheSettings
from conanguide.ui.widget.tab.workspace.tab_workspace import TabWorkspace, TabWorkspaceSettings
from conanguide.ui.widget.tab.profile.tab_profile import TabProfile
from conanguide.ui.widget.tab.remote.tab_remote import TabRemote
from conanguide.ui.dialog.about.about import DialogAbout


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
        self.__show_workspace_toolbar(False)

        # Always show index 0 on starting the application
        # Currently the index 0 is the conan local cache tab
        self.tabWidgetMain.setCurrentWidget(self.tabCache)

        self.__load_ui_state()

    def closeEvent(self, event) -> None:
        self.__save_ui_state()

    @Slot()
    def on_tabWidgetMain_currentChanged(self):
        tab_index = self.tabWidgetMain.currentIndex()

        if tab_index == 1:  # Tab Workspace
            self.__show_workspace_toolbar(True)
        else:
            self.__show_workspace_toolbar(False)

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
        self.tab_workspace.conan_create()

    @Slot()
    def on_actionConanInstall_triggered(self):
        self.tab_workspace.conan_install()

    @Slot()
    def on_actionConanBuild_triggered(self):
        self.tab_workspace.conan_build()

    @Slot()
    def on_actionConanSource_triggered(self):
        self.tab_workspace.conan_source()

    @Slot()
    def on_actionConanPackage_triggered(self):
        self.tab_workspace.conan_package()

    @Slot()
    def on_actionConanExport_triggered(self):
        self.tab_workspace.conan_export()

    @Slot()
    def on_actionConanExportPackage_triggered(self):
        self.tab_workspace.conan_export_package()

    @Slot()
    def on_actionRefresh_triggered(self):
        self.__refresh_all()

    @Slot()
    def on_actionHelpConanIo_triggered(self):
        webbrowser.open("https://conan.io/")

    @Slot()
    def on_actionHelpConanDocs_triggered(self):
        webbrowser.open("https://docs.conan.io/en/latest/")

    @Slot()
    def on_actionHelpAbout_triggered(self):
        dialog = DialogAbout()
        dialog.setWindowFlags(QtCore.Qt.Tool | QtCore.Qt.FramelessWindowHint)
        dialog.exec()

    def __show_workspace_toolbar(self, visible: bool):
        self.actionConanCreate.setVisible(visible)
        self.actionConanInstall.setVisible(visible)
        self.actionConanBuild.setVisible(visible)
        self.actionConanSource.setVisible(visible)
        self.actionConanPackage.setVisible(visible)
        self.actionConanExport.setVisible(visible)
        self.actionConanExportPackage.setVisible(visible)

    def __refresh_all(self):
        # Refresh all the tabs
        self.tab_cache.refresh()
        self.tab_workspace.refresh()
        self.tab_profile.refresh()
        self.tab_remote.refresh()

    def __save_ui_state(self):
        tab_cache_settings = self.tab_cache.get_settings()
        tab_workspace_settings = self.tab_workspace.get_settings()

        # Configuration
        self.ui_config.add_header("main_window")
        self.ui_config.add_value("width", self.width(), "main_window")
        self.ui_config.add_value("height", self.height(), "main_window")

        self.ui_config.add_value("tab_cache", tab_cache_settings.__dict__)
        self.ui_config.add_value("tab_workspace", tab_workspace_settings.__dict__)

        self.ui_config.save_config()

    def __load_ui_state(self):
        config = self.ui_config.load_config()
        if config is not None:
            try:
                # Window
                self.resize(config["main_window"]["width"], config["main_window"]["height"])

                tab_cache_config = config["tab_cache"]
                self.tab_cache.set_settings(TabCacheSettings(
                    toggle_open_path=bool(tab_cache_config["toggle_open_path"]),
                    toggle_copy_path=bool(tab_cache_config["toggle_copy_path"]),
                    toggle_show_directory=bool(tab_cache_config["toggle_show_directory"])
                ))

                tab_workspace_config = config["tab_workspace"]
                self.tab_workspace.set_settings(TabWorkspaceSettings(
                    user=tab_workspace_config["user"],
                    channel=tab_workspace_config["channel"],
                    recipe_path=tab_workspace_config["recipe_path"],
                    install_path=tab_workspace_config["install_path"],
                    build_path=tab_workspace_config["build_path"],
                    source_path=tab_workspace_config["source_path"],
                    package_path=tab_workspace_config["package_path"],
                    parameter=tab_workspace_config["parameter"],
                    profile=tab_workspace_config["profile"],
                    scroll_to_end=bool(tab_workspace_config["scroll_to_end"]),
                ))

            except:
                QtWidgets.QMessageBox.warning(self,
                                              "Warning - Reload UI Settings!",
                                              "Unable to reload UI configuration!\n"
                                              "Please check the configuration file or delete it completely.")
