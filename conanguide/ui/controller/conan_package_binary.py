import logging

from PySide2 import QtCore, QtWidgets
from PySide2.QtGui import QStandardItemModel, QStandardItem

from conanguide.api.conan_api import ConanApi


class ConanPackageBinaryController:
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
