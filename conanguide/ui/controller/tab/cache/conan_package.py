import logging

from PySide2 import QtCore, QtWidgets
from PySide2.QtGui import QStandardItemModel, QStandardItem

from conanguide.api.conan_api import ConanApi


class ConanPackageController:
    def __init__(self, view: QtWidgets.QListView, conan_api: ConanApi):
        self.view = view
        self.conan_api = conan_api
        self.model = QStandardItemModel()

        self.view.setModel(self.model)

    def update(self, package_name: str):
        self.model.clear()

        package_list = self.conan_api.get_package_list(package_name)

        # Fill the list with package binary items
        for pkg in package_list:
            item_package = QStandardItem(pkg["id"])
            item_package.setEditable(False)
            self.model.appendRow(item_package)

    def get_selected_item(self) -> str or None:
        list_selected_items = self.view.selectedIndexes()

        # Checking the list of selected index
        # Currently only supporting single selection of items
        if len(list_selected_items) > 0:  # Only pick the first item in the list
            return self.view.selectedIndexes()[0].data()
        else:  # Empty list will return None
            return None

    def remove_package(self, recipe_id: str, package_id: str):
        self.conan_api.remove(recipe_id, packages=[package_id], force=True)

        self.model.removeRow(self.view.currentIndex().row())

    def remove_selected_package(self, recipe_id: str):
        selected_pkg_id = self.get_selected_item()

        self.remove_package(recipe_id, selected_pkg_id)

    def clear(self):
        self.model.clear()

