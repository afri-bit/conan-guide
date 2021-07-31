import abc

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
        self.model = QStandardItemModel()
        self.conan_api = conan_api

        self.view.setModel(self.model)

    def update(self):
        self.model.clear()
        profile_list = self.conan_api.profile_list()
        for profile in profile_list:
            item = QStandardItem(profile)
            item.setEditable(False)
            self.model.appendRow(item)


class ConanProfileAttributeController(abc.ABC):
    def __init__(self, view: ProfileAttribute, conan_api: ConanApi):
        self.view = view
        self.model = view.model
        self.conan_api = conan_api

    @abc.abstractmethod
    def update(self, profile_name: str):
        return

    @abc.abstractmethod
    def set(self, profile_name: str):
        return


class ConanProfileSettingsController(ConanProfileAttributeController):

    def __init__(self, view: ProfileAttribute, conan_api: ConanApi):
        super().__init__(view, conan_api)

    def update(self, profile_name: str):
        self.view.init_model()

        profile = self.conan_api.read_profile(profile_name)

        for key, value in profile.settings.items():
            self.model.appendRow([QStandardItem(key), QStandardItem(value)])

    def set(self, profile_name: str):
        # TODO: Implement the functionality to set the SETTINGS attributes
        pass


class ConanProfileOptionsController(ConanProfileAttributeController):

    def __init__(self, view: ProfileAttribute, conan_api: ConanApi):
        super().__init__(view, conan_api)

    def update(self, profile_name: str):
        self.view.init_model()

        profile = self.conan_api.read_profile(profile_name)

        for key, value in profile.options.items():
            self.model.appendRow([QStandardItem(key), QStandardItem(value)])

    def set(self, profile_name: str):
        # TODO: Implement the functionality to set the OPTIONS attributes
        pass


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

        for key, value in profile.options.items():
            self.model.appendRow([QStandardItem(key), QStandardItem(value)])

    def set(self, profile_name: str):
        # TODO: Implement the functionality to set the BUILD REQS attributes
        pass


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

    def set(self, profile_name: str):
        # TODO: Implement the functionality to set the ENVIRONMENTS attributes
        pass
