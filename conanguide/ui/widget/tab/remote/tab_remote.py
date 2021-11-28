import os
import pyperclip

from PySide2 import QtWidgets
from PySide2.QtCore import Slot

from conanguide.api.conan_api import ConanApi
from conanguide.ui.widget.tab.remote.tab_remote_ui import Ui_TabRemote

from conanguide.ui.controller.tab.remote.conan_remote import ConanRemoteListController


class TabRemote(QtWidgets.QWidget, Ui_TabRemote):
    def __init__(self, conan_api: ConanApi, *args, obj=None, **kwargs):
        super(TabRemote, self).__init__(*args, **kwargs)

        self.setupUi(self)

        self.conan_api = conan_api

        # Tableview initialization for the remote list
        self.ctrl_tableview_conan_remote = ConanRemoteListController(self.tableViewRemoteList, self.conan_api)
        self.ctrl_tableview_conan_remote.update()

    def refresh(self):
        # TODO: Implement refresh function.
        pass
