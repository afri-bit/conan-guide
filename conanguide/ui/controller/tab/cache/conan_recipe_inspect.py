from PySide2 import QtCore, QtWidgets
from PySide2.QtGui import QStandardItemModel, QStandardItem

from conanguide.api.conan_api import ConanApi


class ConanRecipeInspectController:
    """
    Controller class to control view and model of the conan recipe inspection
    """
    def __init__(self, view: QtWidgets.QTreeView, conan_api: ConanApi):
        self.view = view
        self.conan_api = conan_api

        self.model = QStandardItemModel()

        # Initialize header at the beginning to show the column at the beginning
        self.model.setColumnCount(2)
        self.model.setHeaderData(0, QtCore.Qt.Horizontal, "Property")
        self.model.setHeaderData(1, QtCore.Qt.Horizontal, "Value")
        self.view.setModel(self.model)

        # Place holder list to store previous header with, so the width will not be set to default after updating
        self.header_width = []

    def inspect(self, recipe_id: str):
        """
        Method to show the detail information about the recipe
        :param recipe_id: Name of the recipe to be inspected
        :return: -
        """

        self.initialize()

        inspect_info = self.conan_api.inspect(recipe_id, None)

        for k, v in inspect_info.items():
            item_key = QStandardItem(k)
            item_value = QStandardItem("")

            if type(v) is dict:
                for s_k, s_v in v.items():
                    if type(s_v) == tuple:
                        s_v = list(s_v)
                    item_sub_key = QStandardItem(s_k)
                    item_sub_value = QStandardItem(str(s_v))
                    item_sub_key.setEditable(False)
                    item_sub_value.setEditable(False)
                    item_key.appendRow([item_sub_key, item_sub_value])
            else:
                if type(v) is tuple:
                    v = list(v)
                item_value = QStandardItem(str(v))

            item_key.setEditable(False)
            item_value.setEditable(False)

            self.model.appendRow([item_key, item_value])

        # Set the column width with the previous value
        self.__set_column_width()

    def initialize(self):
        # Store the current column width before deleting the model
        self.__store_column_width()

        # Init the model with the header
        self.model.clear()
        self.model.setColumnCount(2)
        self.model.setHeaderData(0, QtCore.Qt.Horizontal, "Property")
        self.model.setHeaderData(1, QtCore.Qt.Horizontal, "Value")

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