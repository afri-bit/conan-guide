from PyQt5 import QtCore, QtWidgets
from PyQt5.Qt import QStandardItemModel, QStandardItem

from conanblade.api.conan_api import ConanApi


class ConanRecipeController:
    def __init__(self, view: QtWidgets.QTreeView, conan_api: ConanApi):
        self.view = view
        self.model = QStandardItemModel()
        self.conan_api = conan_api

        self.view.setModel(self.model)

    def update(self):
        recipe_list = self.conan_api.get_all_recipes()
        for recipe in recipe_list:
            item_recipe = QStandardItem(recipe.get_info())
            item_recipe.setEditable(False)
            self.model.appendRow(item_recipe)

            package_list = self.conan_api.get_package_list(recipe.get_info())

            for pkg in package_list:
                item_package = QStandardItem(pkg["id"])
                item_package.setEditable(False)
                item_recipe.appendRow(item_package)


class ConanRecipeInspectController:
    def __init__(self, view: QtWidgets.QTreeView, conan_api: ConanApi):
        self.view = view
        self.conan_api = conan_api

        self.model = QStandardItemModel()
        self.model.setColumnCount(2)
        self.model.setHeaderData(0, QtCore.Qt.Horizontal, "Property")
        self.model.setHeaderData(1, QtCore.Qt.Horizontal, "Value")
        self.view.setModel(self.model)

    def inspect(self, recipe_id: str):
        inspect_info = self.conan_api.inspect(recipe_id, None)

        self.model.clear()
        self.model.setColumnCount(2)

        self.model.setHeaderData(0, QtCore.Qt.Horizontal, "Property")
        self.model.setHeaderData(1, QtCore.Qt.Horizontal, "Value")

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
