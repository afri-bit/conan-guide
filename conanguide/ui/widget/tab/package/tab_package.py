from PySide2 import QtWidgets
from PySide2.QtCore import Slot

from conanguide.api.conan_api import ConanApi
from conanguide.ui.widget.tab.package.tab_package_ui import Ui_TabPackage
from conanguide.ui.controller.conan_recipe import ConanRecipeController, ConanRecipeInspectController


class TabPackage(QtWidgets.QWidget, Ui_TabPackage):
    def __init__(self, conan_api: ConanApi, *args, obj=None, **kwargs):
        super(TabPackage, self).__init__(*args, **kwargs)

        self.setupUi(self)

        self.conan_api = conan_api