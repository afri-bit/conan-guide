from PySide2 import QtWidgets
from PySide2.QtCore import Slot

from conanguide.api.conan_api import ConanApi
from conanguide.ui.widget.tab.remote.tab_remote_ui import Ui_TabRemote
from conanguide.ui.dialog.edit.remote.edit_remote import DialogEditRemote
from conanguide.data.conan_remote import ConanRemote

from conanguide.ui.controller.tab.remote.conan_remote import ConanRemoteListController
from conanguide.ui.controller.tab.remote.conan_remote_reference import ConanRemoteReferenceListController


class TabRemote(QtWidgets.QWidget, Ui_TabRemote):
    def __init__(self, conan_api: ConanApi, *args, obj=None, **kwargs):
        super(TabRemote, self).__init__(*args, **kwargs)

        self.setupUi(self)

        self.conan_api = conan_api

        # Tableview initialization for the remote list
        self.ctrl_tableview_conan_remote = ConanRemoteListController(self.tableViewRemoteList, self.conan_api)
        self.ctrl_tableview_conan_remote.update()

        self.ctrl_tableview_conan_remote_reference = ConanRemoteReferenceListController(
            self.listViewRemoteRecipeReference,
            self.conan_api)

    @Slot()
    def on_toolButtonRefresh_clicked(self):
        self.refresh()

    @Slot()
    def on_toolButtonAdd_clicked(self):
        self.__add_remote()

    @Slot()
    def on_toolButtonRemove_clicked(self):
        self.__remove_remote()

    @Slot()
    def on_toolButtonEdit_clicked(self):
        self.__edit_remote()

    @Slot()
    def on_tableViewRemoteList_clicked(self):
        selected_remote = self.ctrl_tableview_conan_remote.get_selected_item()
        self.ctrl_tableview_conan_remote_reference.update(selected_remote.name)

    def refresh(self):
        self.ctrl_tableview_conan_remote.update()

        self.ctrl_tableview_conan_remote_reference.clear()

    def __add_remote(self):
        remote_name_list = [i.name for i in self.conan_api.remote_list()]

        dialog = DialogEditRemote("Add New Remote", remote_name_list)
        res = dialog.exec()

        if res == QtWidgets.QDialog.Accepted:
            self.ctrl_tableview_conan_remote.add_remote(ConanRemote(name=dialog.remote_name,
                                                                    url=dialog.remote_url,
                                                                    ssl=dialog.remote_ssl))

    def __remove_remote(self):
        selected_item = self.ctrl_tableview_conan_remote.get_selected_item()

        if selected_item is not None:  # No remote selecteds
            reply = QtWidgets.QMessageBox.question(self, f"Remove Remote - {selected_item.name}",
                                                   f"Are you sure to delete the remote '{selected_item.name}'?",
                                                   QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No,
                                                   QtWidgets.QMessageBox.No)

            if reply == QtWidgets.QMessageBox.Yes:
                self.ctrl_tableview_conan_remote.remove_selected_remote()

    def __edit_remote(self):
        selected_remote = self.ctrl_tableview_conan_remote.get_selected_item()

        if selected_remote is not None:
            remote_name_list = [i.name for i in self.conan_api.remote_list()]
            dialog = DialogEditRemote("Edit Remote", remote_name_list,
                                      name=selected_remote.name,
                                      url=selected_remote.url,
                                      ssl=selected_remote.ssl,
                                      edit_mode=True)

            res = dialog.exec()

            if res == QtWidgets.QDialog.Accepted:
                if selected_remote.url != dialog.remote_url or selected_remote.ssl != dialog.remote_ssl:
                    self.conan_api.remote_update(selected_remote.name, dialog.remote_url, dialog.remote_ssl)
                if selected_remote.name != dialog.remote_name:
                    self.conan_api.remote_rename(selected_remote.name, dialog.remote_name)

                self.refresh()
