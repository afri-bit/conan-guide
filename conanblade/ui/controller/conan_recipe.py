from PyQt5 import QtWidgets
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
