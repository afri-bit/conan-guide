from PyQt5 import QtWidgets
from PyQt5.Qt import QStandardItemModel, QStandardItem

from conanblade.api.conan_api import ConanApi


class ConanRecipeController:
    def __init__(self, view: QtWidgets.QTreeView, model: QStandardItemModel):
        self.view = view
        self.model = model
        self.api = ConanApi()

    def init(self):
        # TODO: Read the data from the conan api and translate to model
        recipe_list = self.api.get_all_recipes()
        for recipe in recipe_list:
            item_recipe = QStandardItem(recipe.get_info())
            item_recipe.setEditable(False)
            self.model.appendRow(item_recipe)

            package_list = self.api.get_package_list(recipe.get_info())

            for pkg in package_list:
                item_package = QStandardItem(pkg["id"])
                item_package.setEditable(False)
                item_recipe.appendRow(item_package)


