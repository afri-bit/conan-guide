import os

from PySide2 import QtCore, QtWidgets, QtGui


class DirectoryTreeController:
    def __init__(self, view: QtWidgets.QTreeView):
        self.view = view
        self.model = QtWidgets.QFileSystemModel()
        self.model.setRootPath("")

        self.view.setAnimated(True)
        self.view.setIndentation(20)
        self.view.setSortingEnabled(True)

    def show(self, directory_path: str):
        self.view.setModel(self.model)
        self.view.setRootIndex(self.model.index(directory_path))

    def clear(self):
        self.view.setModel(None)

    def open_selected_item(self):
        item_path = self.model.filePath(self.view.currentIndex())

        if os.path.isfile(item_path):
            QtGui.QDesktopServices.openUrl(QtCore.QUrl.fromLocalFile(item_path))
