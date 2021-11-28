from PySide2 import QtCore, QtWidgets
from PySide2.QtGui import QStandardItemModel, QStandardItem

from conanguide.api.conan_api import ConanApi


class ConanPackageInspectController:
    """
    Controller class to control view and model of the conan package inspection
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

    def inspect(self, recipe_id: str, package_id: str):
        """
        Method to show the detail information about the recipe
        :param recipe_id: Name of the recipe to search for the packages
        :param package_id: Package id to be inspected
        :return: -
        """

        self.initialize()

        package_info = self.conan_api.get_package_info(recipe_id, package_id)

        # ========== Settings section
        item_key = QStandardItem("settings")
        item_value = QStandardItem("")
        for sub_key, sub_value in package_info["settings"].items():
            item_sub_key = QStandardItem(sub_key)
            item_sub_value = QStandardItem(str(sub_value))
            item_sub_key.setEditable(False)
            item_sub_value.setEditable(False)
            item_key.appendRow([item_sub_key, item_sub_value])

        item_key.setEditable(False)
        item_value.setEditable(False)
        self.model.appendRow([item_key, item_value])

        # ========== Options section
        item_key = QStandardItem("options")
        item_value = QStandardItem("")
        for sub_key, sub_value in package_info["options"].items():
            item_sub_key = QStandardItem(sub_key)
            item_sub_value = QStandardItem(str(sub_value))
            item_sub_key.setEditable(False)
            item_sub_value.setEditable(False)
            item_key.appendRow([item_sub_key, item_sub_value])

        item_key.setEditable(False)
        item_value.setEditable(False)
        self.model.appendRow([item_key, item_value])

        # ========== Requires section
        item_key = QStandardItem("requires")
        item_value = QStandardItem("")
        for req in package_info["requires"]:
            item_sub_key = QStandardItem("")
            item_sub_value = QStandardItem(req)
            item_sub_key.setEditable(False)
            item_sub_value.setEditable(False)
            item_key.appendRow([item_sub_key, item_sub_value])

        item_key.setEditable(False)
        item_value.setEditable(False)
        self.model.appendRow([item_key, item_value])

        # Expand the tree node with hard coded index, since the sequence is determined manually
        self.view.expand(self.model.index(0, 0))  # Expand the 'settings' tree node
        self.view.expand(self.model.index(2, 0))  # Expand the 'requires' tree node

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