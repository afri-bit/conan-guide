import subprocess

from PySide2 import QtCore


class WorkerSignal(QtCore.QObject):
    start = QtCore.Signal(object)
    finished = QtCore.Signal(object)
    error = QtCore.Signal(object)
    result = QtCore.Signal(object)
    progress = QtCore.Signal(object)


class CommandRunner(QtCore.QThread):
    def __init__(self):
        super().__init__()

        self.signals = WorkerSignal()
        self.command = []

    def set_command(self, command: list):
        self.command = command

    def run(self):
        # Start the thread
        self.signals.start.emit(" ".join(self.command))

        p = subprocess.Popen(self.command,
                             shell=True,
                             stdout=subprocess.PIPE,
                             stderr=subprocess.PIPE)

        # Emitting signal on every output, it shows the progress of the command
        for c in iter(p.stdout.readline, b''):
            self.signals.progress.emit(c.decode("utf-8", errors='replace'))

        self.signals.progress.emit("\n")

        stdout, stderr = p.communicate()

        self.signals.error.emit(stderr.decode("utf-8") + "\n")
        # self.signals.result.emit(stdout.decode("utf-8", errors='replace'))

        self.signals.finished.emit(object)
