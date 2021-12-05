from PySide2 import QtCore, QtWidgets
from PySide2.QtGui import QStandardItemModel, QStandardItem

from conanguide.api.conan_api import ConanApi


class ConanRecipeController:
    """
    Controller class to control view and model of the conan package
    """

    def __init__(self, view: QtWidgets.QTreeView, conan_api: ConanApi):
        self.view = view
        self.conan_api = conan_api

        self.model = QStandardItemModel()
        self.proxy_model = QtCore.QSortFilterProxyModel()
        self.proxy_model.setSourceModel(self.model)
        # With this function set the column as the key column to filter data later
        self.proxy_model.setFilterKeyColumn(1)

        self.view.setModel(self.proxy_model)

        # Initialize header at the beginning to show the column at the beginning
        self.model.setColumnCount(2)
        self.model.setHeaderData(0, QtCore.Qt.Horizontal, "Count")
        self.model.setHeaderData(1, QtCore.Qt.Horizontal, "Name")

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
        self.model.setHeaderData(0, QtCore.Qt.Horizontal, "Count")
        self.model.setHeaderData(1, QtCore.Qt.Horizontal, "Name")

        recipe_list = self.conan_api.get_recipe_list()

        for recipe in recipe_list:
            item_recipe = QStandardItem(recipe.get_info())
            item_recipe.setEditable(False)

            package_list = self.conan_api.get_package_list(recipe.get_info())
            package_count = QStandardItem(str(len(package_list)))
            package_count.setEditable(False)

            self.model.appendRow([package_count, item_recipe])

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

    def filter(self, keyword: str):
        """
        Function to filter the model based on the keyword
        """
        self.proxy_model.setFilterRegExp(QtCore.QRegExp(keyword, QtCore.Qt.CaseInsensitive, QtCore.QRegExp.RegExp2))

    def sort_ascending(self):
        self.proxy_model.sort(1, QtCore.Qt.AscendingOrder)

    def sort_descending(self):
        self.proxy_model.sort(1, QtCore.Qt.DescendingOrder)

    def get_selected_item(self) -> str or None:
        list_selected_items = self.view.selectedIndexes()

        # Checking the list of selected index
        # Currently only supporting single selection of items
        if len(list_selected_items) > 0:  # Only pick the first item in the list
            return self.view.selectedIndexes()[1].data()
        else:  # Empty list will return None
            return None

    def remove_recipe(self, recipe_id: str):
        self.conan_api.remove(recipe_id, force=True)

        # Remove filter to avoid removing the wrong index
        # This is kinda workaround currently
        self.filter("")
        self.model.removeRow(self.view.currentIndex().row())
