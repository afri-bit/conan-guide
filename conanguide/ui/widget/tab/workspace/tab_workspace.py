import os
import datetime
import json

from PySide2 import QtWidgets
from PySide2.QtCore import Slot

from conanguide.api.conan_api import ConanApi
from conanguide.client.runner.command_runner import CommandRunner
from conanguide.utils.cmd.command_builder import ConanCommandBuilder
from conanguide.ui.widget.tab.workspace.tab_workspace_ui import Ui_TabWorkspace


class TabWorkspaceSettings:
    def __init__(self, user: str, channel: str, recipe_path: str,
                 install_path: str, build_path: str, source_path: str,
                 package_path: str, parameter: str, profile: str,
                 scroll_to_end: bool):
        self.user = user
        self.channel = channel
        self.recipe_path = recipe_path
        self.install_path = install_path
        self.build_path = build_path
        self.source_path = source_path
        self.package_path = package_path
        self.parameter = parameter
        self.profile = profile
        self.scroll_to_end = scroll_to_end


class TabWorkspace(QtWidgets.QWidget, Ui_TabWorkspace):
    def __init__(self, conan_api: ConanApi, *args, obj=None, **kwargs):
        super(TabWorkspace, self).__init__(*args, **kwargs)

        self.setupUi(self)

        self.conan_api = conan_api

        # Fill combobox with profile name
        self.comboBoxProfile.addItems(self.conan_api.profile_list())

        # Initialize console
        self.console.ensureCursorVisible()

        # Initialize command runner thread
        self.command_runner = CommandRunner()
        self.command_runner.signals.start.connect(self.on_command_start)
        self.command_runner.signals.error.connect(self.on_command_error)
        self.command_runner.signals.progress.connect(self.on_command_progress)
        self.command_runner.signals.result.connect(self.on_command_result)
        self.command_runner.signals.finished.connect(self.on_command_finished)

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

    def on_command_progress(self, data: str):
        self.log_to_console(data)

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

    @Slot()
    def on_toolButtonSaveConfiguration_pressed(self):
        config_file: tuple = QtWidgets.QFileDialog.getSaveFileName(self,
                                                                   "Save Configuration File",
                                                                   "",
                                                                   "Config File (*.cgjson)")
        if config_file[0] != "":
            self.__save_configuration(config_file[0])

    @Slot()
    def on_toolButtonLoadConfiguration_pressed(self):
        config_file: tuple = QtWidgets.QFileDialog.getOpenFileName(self,
                                                                   "Open Configuration File",
                                                                   "",
                                                                   "Config File (*.cgjson)")

        if config_file[0] != "":
            self.__load_configuration(config_file[0])

    @Slot()
    def on_toolButtonClearConsole_pressed(self):
        self.console.clear()

    @Slot()
    def on_toolButtonRefresh_pressed(self):
        self.refresh()

    def get_settings(self) -> TabWorkspaceSettings:
        return TabWorkspaceSettings(
            user=self.lineEditUser.text(),
            channel=self.lineEditChannel.text(),
            recipe_path=self.lineEditRecipePath.text(),
            install_path=self.lineEditInstallPath.text(),
            build_path=self.lineEditBuildPath.text(),
            source_path=self.lineEditSourcePath.text(),
            package_path=self.lineEditPackagePath.text(),
            parameter=self.lineEditAdditionalParams.text(),
            profile=self.comboBoxProfile.currentText(),
            scroll_to_end=self.toolButtonConsoleScrollToEnd.isChecked()
        )

    def set_settings(self, settings: TabWorkspaceSettings):
        self.lineEditUser.setText(settings.user)
        self.lineEditChannel.setText(settings.channel)
        self.lineEditRecipePath.setText(settings.recipe_path)
        self.lineEditInstallPath.setText(settings.install_path)
        self.lineEditBuildPath.setText(settings.build_path)
        self.lineEditSourcePath.setText(settings.source_path)
        self.lineEditPackagePath.setText(settings.package_path)
        self.lineEditAdditionalParams.setText(settings.parameter)

        profile_list = [self.comboBoxProfile.itemText(i) for i in range(self.comboBoxProfile.count())]

        if settings.profile in profile_list:
            self.comboBoxProfile.setCurrentText(settings.profile)

        self.toolButtonConsoleScrollToEnd.setChecked(settings.scroll_to_end)

    def refresh(self):
        # Refresh the profile list in combo box
        # Get the current selected profile before refreshing the profile list
        selected_profile = self.comboBoxProfile.currentText()

        # Renew the profile list is the combobox
        self.comboBoxProfile.clear()
        # Fill combobox with profile name
        self.comboBoxProfile.addItems(self.conan_api.profile_list())

        profile_list = [self.comboBoxProfile.itemText(i) for i in range(self.comboBoxProfile.count())]

        # Check if the previous selected profile exists in the current list
        # If not the first profile in the combobox will be selected automatically
        if selected_profile in profile_list:
            self.comboBoxProfile.setCurrentText(selected_profile)

    def conan_create(self):
        self.__execute_conan_create()

    def conan_install(self):
        self.__execute_conan_install()

    def conan_build(self):
        self.__execute_conan_build()

    def conan_source(self):
        self.__execute_conan_source()

    def conan_package(self):
        self.__execute_conan_package()

    def conan_export(self):
        self.__execute_conan_export()

    def conan_export_package(self):
        self.__execute_conan_export_package()

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
        self.frameWorkspace.setEnabled(not state)
        self.frameToolbar.setEnabled(not state)

        if state:
            self.progressBar.setMaximum(0)
            self.labelStatusMessage.setText("Loading...  ")
        else:
            self.labelStatusMessage.setText("")
            self.progressBar.setMaximum(100)

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

    def __save_configuration(self, config_file: str) -> None:
        try:
            config_dict = dict()
            content_dict = dict()

            config_dict["cg_workspace"] = content_dict

            content_dict["user"] = self.lineEditUser.text()
            content_dict["channel"] = self.lineEditChannel.text()
            content_dict["recipe_path"] = self.lineEditRecipePath.text()
            content_dict["install_path"] = self.lineEditInstallPath.text()
            content_dict["build_path"] = self.lineEditBuildPath.text()
            content_dict["source_path"] = self.lineEditSourcePath.text()
            content_dict["package_path"] = self.lineEditPackagePath.text()
            content_dict["parameter"] = self.lineEditAdditionalParams.text()
            content_dict["profile"] = self.comboBoxProfile.currentText()

            with open(config_file, "w+") as f:
                f.write(json.dumps(config_dict, indent=2))
        except:
            QtWidgets.QMessageBox.critical(self, "Error on Saving File", "Unable to save configuration file!")

    def __load_configuration(self, config_file: str) -> None:
        if os.path.isfile(config_file):
            try:
                config_dict = dict()
                with open(config_file, "r") as f:
                    config_dict = json.loads(f.read())

                config_content = config_dict["cg_workspace"]

                self.lineEditUser.setText(config_content["user"])
                self.lineEditChannel.setText(config_content["channel"])
                self.lineEditRecipePath.setText(config_content["recipe_path"])
                self.lineEditInstallPath.setText(config_content["install_path"])
                self.lineEditBuildPath.setText(config_content["build_path"])
                self.lineEditSourcePath.setText(config_content["source_path"])
                self.lineEditPackagePath.setText(config_content["package_path"])
                self.lineEditAdditionalParams.setText(config_content["parameter"])

                profile_list = [self.comboBoxProfile.itemText(i) for i in range(self.comboBoxProfile.count())]

                if config_content["profile"] in profile_list:
                    self.comboBoxProfile.setCurrentText(config_content["profile"])
            except:
                QtWidgets.QMessageBox.critical(self,
                                               "Error on Loading File",
                                               "Unable to load the configuration file! Please check the configuration file")

        else:
            QtWidgets.QMessageBox.critical(self, "Error on Loading File", "Unable to locate the configuration file!")
