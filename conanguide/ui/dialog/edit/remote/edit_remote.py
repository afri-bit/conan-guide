from conanguide.ui.dialog.edit.remote.edit_remote_ui import Ui_DialogEditRemote

from PySide2.QtCore import Slot

from PySide2 import QtWidgets, QtCore


class DialogEditRemote(QtWidgets.QDialog, Ui_DialogEditRemote):
    def __init__(self, title: str, list_name: list, name="", url="", ssl=True, edit_mode=False, *args, obj=None,
                 **kwargs):
        super(DialogEditRemote, self).__init__(*args, **kwargs)
        self.setupUi(self)

        self.title = title
        self.list_name = list_name
        self.name = name
        self.url = url
        self.ssl = ssl
        self.edit_mode = edit_mode

        self.setWindowTitle(title)

        self.lineEditName.setText(self.name)
        self.lineEditName.textChanged.connect(self._on_edit_text_name)

        self.lineEditURL.setText(self.url)

        self.checkBoxVerifySSL.setChecked(self.ssl)

        if self.edit_mode:
            self.btnOK.setEnabled(True)
        else:
            self.btnOK.setEnabled(False)

        self.setWindowFlag(QtCore.Qt.WindowContextHelpButtonHint, False)

    @Slot()
    def on_btnOK_clicked(self):
        self.accept()
        self.close()

    @Slot()
    def on_btnCancel_clicked(self):
        self.close()

    @property
    def remote_name(self) -> str:
        return self.lineEditName.text()

    @property
    def remote_url(self) -> str:
        return self.lineEditURL.text()

    @property
    def remote_ssl(self) -> bool:
        return self.checkBoxVerifySSL.isChecked()

    def _on_edit_text_name(self):
        if self.lineEditName.text() == "":
            self.btnOK.setEnabled(False)
        elif self.lineEditName.text() == self.name and self.lineEditName.text() != "":
            self.btnOK.setEnabled(False)
            self.labelInfo.setText("Choose another name.")
        else:
            if self.lineEditName.text() in self.list_name:
                self.labelInfo.setText("Name already exists.")
                self.btnOK.setEnabled(False)
            else:
                self.labelInfo.setText("")
                self.btnOK.setEnabled(True)
