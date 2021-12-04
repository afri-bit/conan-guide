from PySide2 import QtWidgets
from PySide2.QtCore import Slot

from conanguide.api.conan_api import ConanApi
from conanguide.data.conan_profile import ConanProfile
from conanguide.ui.widget.tab.profile.tab_profile_ui import Ui_TabProfile
from conanguide.ui.widget.profile.profile_attribute import ProfileAttribute
from conanguide.ui.controller.tab.profile.conan_profile import ConanProfileListController, ConanProfileSettingsController, \
    ConanProfileOptionsController, ConanProfileBuildReqsController, ConanProfileEnvController
from conanguide.ui.dialog.edit.name.edit_name import DialogEditName


class TabProfile(QtWidgets.QWidget, Ui_TabProfile):
    def __init__(self, conan_api: ConanApi, *args, obj=None, **kwargs):
        super(TabProfile, self).__init__(*args, **kwargs)

        self.setupUi(self)

        self.conan_api = conan_api

        self.selected_profile: str = ""

        # Listview initialization for the profile list
        self.ctrl_listview_conan_profile = ConanProfileListController(self.listViewProfile, self.conan_api)
        self.ctrl_listview_conan_profile.update()

        # Tableview widget initialization
        self.profile_settings = ProfileAttribute("Settings", ["Key", "Value"])
        self.profile_options = ProfileAttribute("Options", ["Key", "Value"])
        self.profile_build_requires = ProfileAttribute("Build Requires", ["Value"])
        self.profile_environments = ProfileAttribute("Environment", ["Key", "Value"])
        self.frameConanProfileAttribute.layout().insertWidget(1, self.profile_settings)
        self.frameConanProfileAttribute.layout().insertWidget(2, self.profile_options)
        self.frameConanProfileAttribute.layout().insertWidget(3, self.profile_build_requires)
        self.frameConanProfileAttribute.layout().insertWidget(4, self.profile_environments)

        self.ctrl_widget_profile_settings = ConanProfileSettingsController(self.profile_settings, self.conan_api)
        self.ctrl_widget_profile_options = ConanProfileOptionsController(self.profile_options, self.conan_api)
        self.ctrl_widget_profile_build_requires = ConanProfileBuildReqsController(self.profile_build_requires,
                                                                                  self.conan_api)
        self.ctrl_widget_profile_environments = ConanProfileEnvController(self.profile_environments, self.conan_api)

        self.lineEditSearchProfile.textChanged.connect(lambda: self.ctrl_listview_conan_profile.filter(
            self.lineEditSearchProfile.text()))

        self.toolButtonSortAscending.toggled.connect(lambda: self.toolButtonSortDescending.setChecked(False))
        self.toolButtonSortDescending.toggled.connect(lambda: self.toolButtonSortAscending.setChecked(False))

        self._enable_profile_attributes(False)

    @Slot()
    def on_listViewProfile_clicked(self):
        self._show_selected_profile()

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

    @Slot()
    def on_toolButtonSaveChange_clicked(self):
        conan_profile = ConanProfile()

        conan_profile.settings = self.ctrl_widget_profile_settings.get_data()
        conan_profile.options = self.ctrl_widget_profile_options.get_data()
        conan_profile.build_requires = self.ctrl_widget_profile_build_requires.get_data()
        conan_profile.environments = self.ctrl_widget_profile_environments.get_data()

        self.conan_api.set_profile(self.selected_profile, conan_profile)

    @Slot()
    def on_toolButtonProfileRemove_clicked(self):
        selected_data = self.listViewProfile.currentIndex().data()
        if selected_data is not None:
            reply = QtWidgets.QMessageBox.question(self, f"Profile - {selected_data}",
                                                   f"Are you sure to delete the profile '{selected_data}?",
                                                   QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No,
                                                   QtWidgets.QMessageBox.No)
            if reply == QtWidgets.QMessageBox.Yes:
                self.conan_api.remove_profile(self.listViewProfile.currentIndex().data())
                self.ctrl_listview_conan_profile.remove_selected()
                self._show_selected_profile()

    @Slot()
    def on_toolButtonRevertChange_clicked(self):
        self._show_selected_profile()

    @Slot()
    def on_toolButtonProfileAdd_clicked(self):
        self._add_new_profile()

    @Slot()
    def on_toolButtonProfileRename_clicked(self):
        self._rename_profile()

    @Slot()
    def on_toolButtonRefresh_clicked(self):
        self.refresh()

    def refresh(self):
        self._clear_view()
        self.ctrl_listview_conan_profile.update()

    def _rename_profile(self):
        profile_name = self.listViewProfile.currentIndex().data()
        profile_list = self.ctrl_listview_conan_profile.items
        dialog = DialogEditName("Edit Profile Name", profile_list, profile_name)
        res = dialog.exec()

        if res == QtWidgets.QDialog.Accepted:
            profile_name_new = dialog.text
            self.conan_api.rename_profile(profile_name, profile_name_new)
            self.refresh()

    def _add_new_profile(self):
        profile_list = self.ctrl_listview_conan_profile.items
        dialog = DialogEditName("Add Profile", profile_list)
        res = dialog.exec()
        if res == QtWidgets.QDialog.Accepted:
            self.conan_api.create_profile(dialog.text)
            self.refresh()

    def _show_selected_profile(self):
        try:
            self._enable_profile_attributes(True)

            selected_profile = self.listViewProfile.currentIndex().data()

            self.selected_profile = selected_profile
            self.labelProfileName.setText(selected_profile)
            self.ctrl_widget_profile_settings.update(self.listViewProfile.currentIndex().data())
            self.ctrl_widget_profile_options.update(self.listViewProfile.currentIndex().data())
            self.ctrl_widget_profile_build_requires.update(self.listViewProfile.currentIndex().data())
            self.ctrl_widget_profile_environments.update(self.listViewProfile.currentIndex().data())
        except:
            self._clear_view()

    def _enable_profile_attributes(self, enable: bool):
        self.profile_settings.setEnabled(enable)
        self.profile_options.setEnabled(enable)
        self.profile_build_requires.setEnabled(enable)
        self.profile_environments.setEnabled(enable)

    def _clear_view(self):
        self.selected_profile = ""
        self.labelProfileName.setText(self.selected_profile)

        self.ctrl_widget_profile_settings.clear()
        self.ctrl_widget_profile_options.clear()
        self.ctrl_widget_profile_build_requires.clear()
        self.ctrl_widget_profile_environments.clear()

        self._enable_profile_attributes(False)
