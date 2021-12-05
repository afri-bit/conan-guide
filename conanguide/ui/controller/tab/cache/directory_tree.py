from PySide2 import QtCore, QtWidgets
from PySide2.QtGui import QStandardItemModel, QStandardItem


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
