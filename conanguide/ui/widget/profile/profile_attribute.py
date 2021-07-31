import abc

from PySide2 import QtCore, QtWidgets
from PySide2.QtCore import Slot
from PySide2.QtGui import QStandardItemModel, QStandardItem

from conanguide.ui.widget.profile.profile_attribute_ui import Ui_WidgetProfileAttribute


class ProfileAttribute(QtWidgets.QWidget, Ui_WidgetProfileAttribute):
    def __init__(self, name: str, header: list, *args, obj=None, **kwargs):
        super(ProfileAttribute, self).__init__(*args, **kwargs)

        self.setupUi(self)

        self.groupBox.setTitle(name)
        self.model = QStandardItemModel()
        self.header = header
        self.header_width = []

        self.tableViewAttributes.setModel(self.model)
        self.tableViewAttributes.verticalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Fixed)
        self.tableViewAttributes.verticalHeader().setDefaultSectionSize(20)

        self.init_model()

    @Slot()
    def on_toolButtonAdd_clicked(self):
        row_items = list()
        for i in range(len(self.header)):
            row_items.append(QStandardItem(""))

        self.model.appendRow(row_items)
        self.tableViewAttributes.scrollToBottom()

        self.tableViewAttributes.selectRow(self.model.rowCount() - 1)

        index = self.tableViewAttributes.model().index(self.model.rowCount() - 1, 0)
        self.tableViewAttributes.setCurrentIndex(index)
        self.tableViewAttributes.edit(index)

    @Slot()
    def on_toolButtonRemove_clicked(self):
        self.model.removeRow(self.tableViewAttributes.currentIndex().row())

    @Slot()
    def on_toolButtonClear_clicked(self):
        self.init_model()

    def _store_column_width(self):
        """
        Store current column width to the class variable
        :return: -
        """
        self.header_width = []
        for i in range(0, self.tableViewAttributes.horizontalHeader().count()):
            self.header_width.append(self.tableViewAttributes.columnWidth(i))

    def _set_column_width(self):
        """
        Restore the previous column width
        :return: -
        """
        for i in range(0, len(self.header_width)):
            self.tableViewAttributes.setColumnWidth(i, self.header_width[i])

    def init_model(self):
        # Store the current column width before deleting the model
        self._store_column_width()

        # Init the model with the header
        self.model.clear()
        self.model.setColumnCount(len(self.header))

        for i in range(len(self.header)):
            self.model.setHeaderData(i, QtCore.Qt.Horizontal, self.header[i])

        if len(self.header) > 0:
            self.tableViewAttributes.horizontalHeader().setSectionResizeMode(len(self.header) - 1,
                                                                             QtWidgets.QHeaderView.Stretch)

        # Set the column width with the previous value
        self._set_column_width()
