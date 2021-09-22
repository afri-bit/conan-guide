from conanguide.ui.dialog.edit.name.edit_name_ui import Ui_DialogEditName

from PySide2.QtCore import Slot

from PySide2 import QtWidgets, QtCore


class DialogEditName(QtWidgets.QDialog, Ui_DialogEditName):
    def __init__(self, title: str, list_name: list, init_name="", *args, obj=None, **kwargs):
        super(DialogEditName, self).__init__(*args, **kwargs)
        self.setupUi(self)

        self.title = title
        self.list_name: list = list_name
        self.init_name = init_name

        self.setWindowTitle(title)

        self.lineEdit.setText(self.init_name)
        self.lineEdit.textChanged.connect(self._on_edit_text)

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
    def text(self):
        return self.lineEdit.text()

    def _on_edit_text(self):
        if self.lineEdit.text() == "":
            self.btnOK.setEnabled(False)
        elif self.lineEdit.text() == self.init_name and self.lineEdit.text() != "":
            self.btnOK.setEnabled(False)
            self.labelInfo.setText("Choose another name.")
        else:
            if self.lineEdit.text() in self.list_name:
                self.labelInfo.setText("Name already exists.")
                self.btnOK.setEnabled(False)
            else:
                self.labelInfo.setText("")
                self.btnOK.setEnabled(True)


