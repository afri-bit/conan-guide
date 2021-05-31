import sys

from PySide2 import QtWidgets

from conanguide.ui.main.main_window import MainWindow


def main():
    app = QtWidgets.QApplication(sys.argv)

    window = MainWindow()
    window.show()
    app.exec_()


if __name__ == "__main__":
    main()
