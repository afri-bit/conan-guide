from PySide2 import QtWidgets
from PySide2.QtCore import Slot

from conanguide.api.conan_api import ConanApi
from conanguide.ui.widget.tab.profile.tab_profile_ui import Ui_TabProfile
from conanguide.ui.widget.profile.profile_attribute import ProfileAttribute
from conanguide.ui.controller.conan_profile import ConanProfileListController, ConanProfileSettingsController, \
    ConanProfileOptionsController, ConanProfileBuildReqsController, ConanProfileEnvController


class TabProfile(QtWidgets.QWidget, Ui_TabProfile):
    def __init__(self, conan_api: ConanApi, *args, obj=None, **kwargs):
        super(TabProfile, self).__init__(*args, **kwargs)

        self.setupUi(self)

        self.conan_api = conan_api

        self.__init()

    def __init(self):
        # Listview initialization for the profile list
        self.ctrl_listview_conan_profile = ConanProfileListController(self.listViewProfile, self.conan_api)
        self.ctrl_listview_conan_profile.update()

        # Tableview widget initialization
        self.profile_settings = ProfileAttribute("Settings", ["Key", "Value"])
        self.profile_options = ProfileAttribute("Options", ["Key", "Value"])
        self.profile_build_reqs = ProfileAttribute("Build Requires", ["Value"])
        self.profile_environments = ProfileAttribute("Environment", ["Key", "Value"])
        self.frameConanProfileAttribute.layout().insertWidget(1, self.profile_settings)
        self.frameConanProfileAttribute.layout().insertWidget(2, self.profile_options)
        self.frameConanProfileAttribute.layout().insertWidget(3, self.profile_build_reqs)
        self.frameConanProfileAttribute.layout().insertWidget(4, self.profile_environments)

        self.ctrl_widget_profile_settings = ConanProfileSettingsController(self.profile_settings, self.conan_api)
        self.ctrl_widget_profile_options = ConanProfileOptionsController(self.profile_options, self.conan_api)
        self.ctrl_widget_profile_build_reqs = ConanProfileBuildReqsController(self.profile_build_reqs, self.conan_api)
        self.ctrl_widget_profile_environments = ConanProfileEnvController(self.profile_environments, self.conan_api)

        self.lineEditSearchProfile.textChanged.connect(lambda: self.ctrl_listview_conan_profile.filter(
            self.lineEditSearchProfile.text()))

        self.toolButtonSortAscending.toggled.connect(lambda: self.toolButtonSortDescending.setChecked(False))
        self.toolButtonSortDescending.toggled.connect(lambda: self.toolButtonSortAscending.setChecked(False))

    def update(self):
        self.ctrl_listview_conan_profile.update()

    @Slot()
    def on_listViewProfile_clicked(self):
        self.labelProfileName.setText(self.listViewProfile.currentIndex().data())
        self.ctrl_widget_profile_settings.update(self.listViewProfile.currentIndex().data())
        self.ctrl_widget_profile_options.update(self.listViewProfile.currentIndex().data())
        self.ctrl_widget_profile_build_reqs.update(self.listViewProfile.currentIndex().data())
        self.ctrl_widget_profile_environments.update(self.listViewProfile.currentIndex().data())

    @Slot()
    def on_toolButtonSortAscending_clicked(self):
        self.toolButtonSortAscending.setChecked(True)
        self.toolButtonSortDescending.setChecked(False)

        self.ctrl_listview_conan_profile.sort_ascending()

    @Slot()
    def on_toolButtonSortDescending_clicked(self):
        self.toolButtonSortDescending.setChecked(True)
        self.toolButtonSortAscending.setChecked(False)

        self.ctrl_listview_conan_profile.sort_descending()
