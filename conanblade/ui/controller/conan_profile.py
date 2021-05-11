from PyQt5 import QtWidgets
from PyQt5.Qt import QStandardItemModel, QStandardItem

from conanblade.api.conan_api import ConanApi


class ConanProfileController():
    def __init__(self, view: QtWidgets.QListView, model: QStandardItemModel):
        self.view = view
        self.model = model
        self.api = ConanApi()

    def init(self):
        # TODO: Read the data from the conan api and translate to model
        profile_list = self.api.profile_list()
        for profile in profile_list:
            item = QStandardItem(profile)
            item.setEditable(False)
            self.model.appendRow(item)