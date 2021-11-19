from PySide2 import QtCore, QtWidgets
from PySide2.QtGui import QStandardItemModel, QStandardItem

from conanguide.api.conan_api import ConanApi


class ConanRecipeController:
    """
    Controller class to control view and model of the conan recipe list
    """
    def __init__(self, view: QtWidgets.QTreeView, conan_api: ConanApi):
        self.view = view
        self.conan_api = conan_api

        self.model = QStandardItemModel()
        self.proxy_model = QtCore.QSortFilterProxyModel()
        self.proxy_model.setSourceModel(self.model)

        self.view.setModel(self.proxy_model)

    def update(self):
        self.model.clear()

        recipe_list = self.conan_api.get_all_recipes()

        for recipe in recipe_list:
            item_recipe = QStandardItem(recipe.get_info())
            item_recipe.setEditable(False)
            self.model.appendRow(item_recipe)

            package_list = self.conan_api.get_package_list(recipe.get_info())

            # Get all the packages under the current recipe
            for pkg in package_list:
                item_package = QStandardItem(pkg["id"])
                item_package.setEditable(False)
                item_recipe.appendRow(item_package)

    def filter(self, keyword: str):
        """
        Function to filter the model based on the keyword
        """
        self.proxy_model.setFilterRegExp(QtCore.QRegExp(keyword, QtCore.Qt.CaseInsensitive, QtCore.QRegExp.RegExp2))

    def sort_ascending(self):
        self.proxy_model.sort(0, QtCore.Qt.AscendingOrder)

    def sort_descending(self):
        self.proxy_model.sort(0, QtCore.Qt.DescendingOrder)
