import platform
import webbrowser

import conans.client.conan_api as conan_api

import conanguide.info
from conanguide.ui.dialog.about.about_ui import Ui_DialogAbout

from PySide2.QtCore import Slot
from PySide2 import QtWidgets


class DialogAbout(QtWidgets.QDialog, Ui_DialogAbout):
    def __init__(self, *args, obj=None, **kwargs):
        super(DialogAbout, self).__init__(*args, **kwargs)
        self.setupUi(self)

        self.labelConanGuideVersion.setText(conanguide.info.__version__)
        self.labelPythonVersion.setText(platform.python_version())
        self.labelConanVersion.setText(conan_api.client_version)

    @Slot()
    def on_toolButtonPython_clicked(self):
        webbrowser.open("https://www.python.org/")

    @Slot()
    def on_toolButtonConan_clicked(self):
        webbrowser.open("https://conan.io/")

    @Slot()
    def on_toolButtonQt_clicked(self):
        webbrowser.open("https://www.qt.io/")

    @Slot()
    def on_pushButtonOK_clicked(self):
        self.close()
