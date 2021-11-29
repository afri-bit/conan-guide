from PySide2 import QtWidgets
from PySide2.QtGui import QStandardItemModel, QStandardItem

from conanguide.api.conan_api import ConanApi


class ConanRemoteReferenceListController:
    """
    Controller class to control view and model of the conan remote list
    """

    def __init__(self, view: QtWidgets.QListView, conan_api: ConanApi):
        self.view = view
        self.conan_api = conan_api

        self.model = QStandardItemModel()
        self.view.setModel(self.model)

    def update(self, remote_name: str):
        """
        This method provides list of recipes thats are referenced to the given remote name.
        The conan API method 'remote_list_ref' gives a dictionary with recipe name as key and remote name as value. In
        this method we will make a list of key based on the value of the dictionary. Basically this is a reverse search
        of an dictionary.

        :param remote_name: Remote name
        """
        self.model.clear()

        # Get the reference list from the conan API
        remote_reference = self.conan_api.remote_list_ref()

        # Put the key and values into a list
        recipe_keys = list(remote_reference.keys())
        remote_values = list(remote_reference.values())

        # Get the index numbers into a list where the value is matched to the given remote name
        index_list = [i for i, j in enumerate(remote_values) if j == remote_name]

        # Finally based on the index list, we will get the keys from dictionary. This list will contain the recipes
        # that are referenced to the given remote name
        recipe_reference_list = [recipe_keys[i] for i in index_list]

        # Feed the list of recipe to the QlistView widget
        for recipe in recipe_reference_list:
            item = QStandardItem(recipe)
            item.setEditable(False)

            self.model.appendRow(item)

    def clear(self):
        self.model.clear()
