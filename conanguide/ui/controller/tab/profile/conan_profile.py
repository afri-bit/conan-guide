import abc
import collections

from PySide2 import QtCore, QtWidgets
from PySide2.QtGui import QStandardItemModel, QStandardItem

from conanguide.api.conan_api import ConanApi
from conanguide.ui.widget.profile.profile_attribute import ProfileAttribute


class ConanProfileListController:
    """
    Controller class to control view and model of the conan profile list
    """

    def __init__(self, view: QtWidgets.QListView, conan_api: ConanApi):
        self.view = view
        self.conan_api = conan_api

        self.model = QStandardItemModel()
        self.proxy_model = QtCore.QSortFilterProxyModel()
        self.proxy_model.setSourceModel(self.model)

        self.view.setModel(self.proxy_model)

    def update(self):
        self.model.clear()
        profile_list = self.conan_api.profile_list()
        for profile in profile_list:
            item = QStandardItem(profile)
            item.setEditable(False)
            self.model.appendRow(item)

    def filter(self, keyword: str):
        """
        Function to filter the model based on the keyword
        """
        self.proxy_model.setFilterRegExp(QtCore.QRegExp(keyword, QtCore.Qt.CaseInsensitive, QtCore.QRegExp.RegExp2))

    def sort_ascending(self):
        self.proxy_model.sort(0, QtCore.Qt.AscendingOrder)

    def sort_descending(self):
        self.proxy_model.sort(0, QtCore.Qt.DescendingOrder)

    def remove_selected(self):
        self.proxy_model.removeRow(self.view.currentIndex().row())

    @property
    def items(self) -> list:
        items = list()
        for i in range(self.proxy_model.rowCount()):
            items.append(self.proxy_model.index(i, 0).data())

        return items


class ConanProfileAttributeController(abc.ABC):
    def __init__(self, view: ProfileAttribute, conan_api: ConanApi):
        self.view = view
        self.model = view.model
        self.conan_api = conan_api

    def clear(self):
        self.view.init_model()

    @abc.abstractmethod
    def update(self, profile_name: str):
        """
        Method to update the view
        """

    def get_data(self) -> collections.OrderedDict:
        """
        Method to return the data from the model
        """
        data = collections.OrderedDict()

        for i in range(self.model.rowCount()):
            key = self.model.item(i, 0).text()
            value = self.model.item(i, 1).text() if self.model.item(i, 1) is not None else None

            if key != "":
                data[key] = value

        return data


class ConanProfileSettingsController(ConanProfileAttributeController):

    def __init__(self, view: ProfileAttribute, conan_api: ConanApi):
        super().__init__(view, conan_api)

    def update(self, profile_name: str):
        self.view.init_model()

        profile = self.conan_api.read_profile(profile_name)

        for key, value in profile.settings.items():
            self.model.appendRow([QStandardItem(key), QStandardItem(value)])


class ConanProfileOptionsController(ConanProfileAttributeController):

    def __init__(self, view: ProfileAttribute, conan_api: ConanApi):
        super().__init__(view, conan_api)

    def update(self, profile_name: str):
        self.view.init_model()

        profile = self.conan_api.read_profile(profile_name)

        for opt in profile.options.as_list():
            self.model.appendRow([QStandardItem(opt[0]), QStandardItem(opt[1])])


class ConanProfileBuildReqsController(ConanProfileAttributeController):

    def __init__(self, view: ProfileAttribute, conan_api: ConanApi):
        super().__init__(view, conan_api)

    def update(self, profile_name: str):
        self.view.init_model()

        profile = self.conan_api.read_profile(profile_name)

        if len(profile.build_requires) > 0:
            for i in profile.build_requires["*"]:
                item = QStandardItem(str(i))
                self.model.appendRow(item)


class ConanProfileEnvController(ConanProfileAttributeController):

    def __init__(self, view: ProfileAttribute, conan_api: ConanApi):
        super().__init__(view, conan_api)

    def update(self, profile_name: str):
        self.view.init_model()

        profile = self.conan_api.read_profile(profile_name)

        for k, v in profile.env_values.data[None].items():
            item_key = QStandardItem(str(k))
            item_value = QStandardItem(str(v))
            self.model.appendRow([item_key, item_value])
