import os
import sys
import subprocess
import time

from PyQt5 import QtCore


class WorkerSignal(QtCore.QObject):
    start = QtCore.pyqtSignal(object)
    finished = QtCore.pyqtSignal(object)
    error = QtCore.pyqtSignal(object)
    result = QtCore.pyqtSignal(object)
    progress = QtCore.pyqtSignal(object)


class ConanCommandRunner(QtCore.QThread):
    def __init__(self):
        super().__init__()

        self.signals = WorkerSignal()
        self.command = []

    def set_command(self, command: list):
        self.command = command

    def run(self) -> None:
        # Start the thread
        self.signals.start.emit(" ".join(self.command))

        p = subprocess.Popen(self.command,
                             shell=True,
                             stdout=subprocess.PIPE,
                             stderr=subprocess.PIPE)

        for c in iter(p.stdout.readline, b''):
            self.signals.progress.emit(c.decode("utf-8", errors='replace'))
        self.signals.progress.emit("\n")

        stdout, stderr = p.communicate()

        self.signals.error.emit(stderr.decode("utf-8") + "\n")
        # self.signals.result.emit(stdout.decode("utf-8", errors='replace'))

        self.signals.finished.emit(object)
