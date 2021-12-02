import os
import datetime

from PySide2 import QtWidgets
from PySide2.QtCore import Slot

from conanguide.api.conan_api import ConanApi
from conanguide.client.runner.command_runner import CommandRunner
from conanguide.utils.cmd.command_builder import ConanCommandBuilder
from conanguide.ui.widget.tab.workspace.tab_workspace_ui import Ui_TabWorkspace


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
