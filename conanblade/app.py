from PyQt5 import QtWidgets

from conanblade.ui.main.main_window import MainWindow

if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)

    window = MainWindow()
    window.show()
    app.exec()
