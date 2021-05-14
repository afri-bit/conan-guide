from PyQt5 import QtCore, QtWidgets
from PyQt5.Qt import QStandardItemModel, QStandardItem

from conanblade.api.conan_api import ConanApi


class ConanProfileController:
    def __init__(self, view: QtWidgets.QListView, conan_api: ConanApi):
        self.view = view
        self.model = QStandardItemModel()
        self.conan_api = conan_api

        self.view.setModel(self.model)

    def update(self):
        profile_list = self.conan_api.profile_list()
        for profile in profile_list:
            item = QStandardItem(profile)
            item.setEditable(False)
            self.model.appendRow(item)


class ConanProfileDetailController:
    def __init__(self, view: QtWidgets.QTreeView, conan_api: ConanApi):
        self.view = view
        self.conan_api = conan_api

        self.model = QStandardItemModel()
        self.model.setColumnCount(2)
        self.model.setHeaderData(0, QtCore.Qt.Horizontal, "Property")
        self.model.setHeaderData(1, QtCore.Qt.Horizontal, "Value")
        self.view.setModel(self.model)

    def show_detail(self, profile_name: str):
        self.model.clear()
        self.model.setColumnCount(2)

        self.model.setHeaderData(0, QtCore.Qt.Horizontal, "Property")
        self.model.setHeaderData(1, QtCore.Qt.Horizontal, "Value")

        profile = self.conan_api.read_profile(profile_name)

        # Profile - settings section
        model_setting_item = QStandardItem("settings")
        model_setting_item.setEditable(False)
        for k, v in profile.settings.items():
            item_key = QStandardItem(str(k))
            item_key.setEditable(False)
            item_value = QStandardItem(str(v))
            model_setting_item.appendRow([item_key, item_value])
        self.model.appendRow(model_setting_item)

        # Profile - build_requires section
        model_build_requires_item = QStandardItem("build_requires")
        model_build_requires_item.setEditable(False)
        if len(profile.build_requires) > 0:
            for i in profile.build_requires["*"]:
                item = QStandardItem(str(i))
                model_build_requires_item.appendRow(item)
        self.model.appendRow(model_build_requires_item)

        # Profile - options section
        model_options_item = QStandardItem("options")
        model_options_item.setEditable(False)

        options = str(profile.options)  # Plain strings
        if options != "":
            options = options.split("\n")

            for opt in options:
                opt = opt.split("=")
                item_key = QStandardItem(str(opt[0]))
                item_value = QStandardItem(str(opt[1]))
                model_options_item.appendRow([item_key, item_value])
        self.model.appendRow(model_options_item)

        # Profile - environment section
        model_environment_item = QStandardItem("env")
        model_environment_item.setEditable(False)

        for k, v in profile.env_values.data[None].items():
            item_key = QStandardItem(str(k))
            item_key.setEditable(False)
            item_value = QStandardItem(str(v))
            model_environment_item.appendRow([item_key, item_value])
        self.model.appendRow(model_environment_item)

        # Expand the tree view
        self.view.expandAll()
