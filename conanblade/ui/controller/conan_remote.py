from PyQt5 import QtCore, QtWidgets
from PyQt5.Qt import QStandardItemModel, QStandardItem, QHeaderView

from conanblade.api.conan_api import ConanApi


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
            item_name.setCheckable(True)
            item_name.setCheckState(not remote.disabled)

            item_url = QStandardItem(remote.url)

            item_ssl = QStandardItem(str(remote.verify_ssl))

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


