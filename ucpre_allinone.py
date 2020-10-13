from trped_main import MainWindow as trpedmw
from aiced_main import MainWindow as aicedmw
from stged_main import MainWindow as stgedmw
from UI.ucpre_allinone import Ui_MainWindow as LauncherMain
from PyQt5 import QtWidgets
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
        self.trp.clicked.connect(lambda: self.launch("trp"))
        self.aic.clicked.connect(lambda: self.launch("aic"))
        self.stg.clicked.connect(lambda: self.launch("stg"))

    def launch(self, name):
        self.windows[name]()


if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    mainwindow = UCPAllInOne()
    mainwindow.show()
    sys.exit(app.exec_())
