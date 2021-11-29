from PySide2 import QtCore, QtWidgets
from PySide2.QtGui import QStandardItemModel, QStandardItem

from conanguide.api.conan_api import ConanApi

from conanguide.data.conan_remote import ConanRemote


class ConanRemoteListController:
    """
    Controller class to control view and model of the conan remote list
    """

    def __init__(self, view: QtWidgets.QTableView, conan_api: ConanApi):
        self.view = view
        self.conan_api = conan_api

        self.model = QStandardItemModel()
        self.view.setModel(self.model)
        self.view.horizontalHeader().setStretchLastSection(False)
        self.view.setShowGrid(True)
        self.view.setSortingEnabled(True)

        self.header_width = []

    def update(self):
        self.__store_column_width()

        self.model.clear()
        self.model.setColumnCount(3)

        self.model.setHeaderData(0, QtCore.Qt.Horizontal, "Name")
        self.model.setHeaderData(1, QtCore.Qt.Horizontal, "URL")
        self.model.setHeaderData(2, QtCore.Qt.Horizontal, "Verify SSL")

        remote_list = self.conan_api.remote_list()

        for remote in remote_list:
            item_name = QStandardItem(remote.name)
            item_name.setEditable(False)
            item_url = QStandardItem(remote.url)
            item_url.setEditable(False)
            item_ssl = QStandardItem(str(remote.verify_ssl))
            item_ssl.setEditable(False)

            self.model.appendRow([item_name, item_url, item_ssl])

        self.view.horizontalHeader().setSectionResizeMode(1, QtWidgets.QHeaderView.Stretch)

        # Set the column width with the previous value
        self.__set_column_width()

    def __store_column_width(self):
        """
        Store current column width to the class variable
        :return: -
        """
        self.header_width = []
        for i in range(0, self.view.horizontalHeader().count()):
            self.header_width.append(self.view.columnWidth(i))

    def __set_column_width(self):
        """
        Restore the previous column width
        :return: -
        """
        for i in range(0, len(self.header_width)):
            self.view.setColumnWidth(i, self.header_width[i])

    def get_selected_item(self) -> ConanRemote or None:
        row_index = self.view.currentIndex().row()

        if row_index > -1:
            return ConanRemote(self.model.index(row_index, 0).data(),
                               self.model.index(row_index, 1).data(),
                               True if self.model.index(row_index, 2).data() == "True" else False)
        else:
            return None

    def add_remote(self, remote: ConanRemote):
        self.conan_api.remote_add(remote.name, remote.url, verify_ssl=remote.ssl)

        item_name = QStandardItem(remote.name)
        item_name.setEditable(False)
        item_url = QStandardItem(remote.url)
        item_url.setEditable(False)
        item_ssl = QStandardItem(str(remote.ssl))
        item_ssl.setEditable(False)

        self.model.appendRow([item_name, item_url, item_ssl])

    def remove_selected_remote(self):
        selected_remote = self.get_selected_item()

        self.conan_api.remote_remove(selected_remote.name)

        self.model.removeRow(self.view.currentIndex().row())
