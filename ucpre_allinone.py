from trped_main import MainWindow as trpedmw
from aiced_main import MainWindow as aicedmw
from stged_main import MainWindow as stgedmw
from UI.ucpre_allinone import Ui_MainWindow as LauncherMain
from PyQt5 import QtWidgets
from PyQt5.QtCore import pyqtSlot
import sys


class UCPAllInOne(QtWidgets.QMainWindow, LauncherMain):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.windows = {
            "trp": trpedmw,
            "aic": aicedmw,
            "stg": stgedmw
        }
        self.trp_window = None
        self.aic_window = None
        self.stg_window = None

        self.trp.clicked.connect(self.launch)
        self.aic.clicked.connect(self.launch)
        self.stg.clicked.connect(self.launch)

    @pyqtSlot(name="Kek")
    def launch(self):
        button: QtWidgets.QPushButton = self.sender()
        name = button.objectName()
        wdw: QtWidgets.QMainWindow = getattr(self, name + "_window")
        if wdw:
            wdw.showNormal()
        else:
            setattr(self, name+"_window", self.windows[name]())


if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    mainwindow = UCPAllInOne()
    mainwindow.show()
    sys.exit(app.exec_())
