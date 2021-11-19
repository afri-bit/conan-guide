from PySide2 import QtCore, QtWidgets
from PySide2.QtGui import QStandardItemModel, QStandardItem

from conanguide.api.conan_api import ConanApi


class ConanPackageController:
    """
    Controller class to control view and model of the conan package
    """

    def __init__(self, view: QtWidgets.QTreeView, conan_api: ConanApi):
        self.view = view
        self.conan_api = conan_api

        self.model = QStandardItemModel()

        # Initialize header at the beginning to show the column at the beginning
        self.model.setColumnCount(2)
        self.model.setHeaderData(0, QtCore.Qt.Horizontal, "Name")
        self.model.setHeaderData(1, QtCore.Qt.Horizontal, "Count")
        self.view.setModel(self.model)

        # Place holder list to store previous header with, so the width will not be set to default after updating
        self.header_width = []

    def update(self):
        """
        Method to update the list of conan packages
        :return: -
        """

        # Store the current column width before deleting the model
        self.__store_column_width()

        # Init the model with the header
        self.model.clear()
        self.model.setColumnCount(2)
        self.model.setHeaderData(0, QtCore.Qt.Horizontal, "Name")
        self.model.setHeaderData(1, QtCore.Qt.Horizontal, "Count")

        package_list = self.conan_api.get_all_recipes()

        for pkg in package_list:
            item_package = QStandardItem(pkg.get_info())
            item_package.setEditable(False)

            package_list = self.conan_api.get_package_list(pkg.get_info())
            package_count = QStandardItem(str(len(package_list)))
            package_count.setEditable(False)

            self.model.appendRow([item_package, package_count])

        self.view.header().setSectionResizeMode(0, QtWidgets.QHeaderView.ResizeToContents)
        self.view.header().setSectionResizeMode(1, QtWidgets.QHeaderView.Stretch)

        # Set the column width with the previous value
        self.__set_column_width()

    def __store_column_width(self):
        """
        Store current column width to the class variable
        :return: -
        """
        self.header_width = []
        for i in range(0, self.view.header().count()):
            self.header_width.append(self.view.columnWidth(i))

    def __set_column_width(self):
        """
        Restore the previous column width
        :return: -
        """
        for i in range(0, len(self.header_width)):
            self.view.setColumnWidth(i, self.header_width[i])