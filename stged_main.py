import json
import sys
import os
from utils import *
from UI.stged_mw import Ui_MainWindow
from PyQt5 import QtWidgets
from resource_types import StartGoods


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.startgoods = StartGoods()
        self.setupUi(self)
        self.latest_tab = "normal"
        self.modetab.setCurrentIndex(0)
        self.modetab.currentChanged.connect(lambda index: self.tab_change(self.modetab.tabText(index).lower()))
        self.actionOpen.triggered.connect(lambda: self.load_from_file())
        self.actionSave.triggered.connect(lambda: self.save_to_file())
        self.gold = {
            "human": [self.humangold0, self.humangold1, self.humangold2, self.humangold3, self.humangold4],
            "ai": [self.aigold0, self.aigold1, self.aigold2, self.aigold3, self.aigold4]
        }
        if os.path.exists("./resources/goods/vanilla.json"):
            self.load_from_file("./resources/goods/vanilla.json")
        self.show()

    def tab_change(self, mode):
        self.update_mode(self.latest_tab)
        self.update_view(mode)
        self.latest_tab = mode

    def update_view(self, mode):
        current = getattr(self.startgoods, mode)
        for param in current:
            if type(current[param]) == dict:
                _sbl: dict = getattr(self, param)
                for i, entry in enumerate(current[param]["human"]):
                    _sbl["human"][i].setValue(entry)
                for i, entry in enumerate(current[param]["ai"]):
                    _sbl["ai"][i].setValue(entry)
            else:
                _sb: QtWidgets.QSpinBox = getattr(self, param)
                _sb.setValue(current[param])

    def update_mode(self, mode):
        current = getattr(self.startgoods, mode)
        for param in current:
            if type(current[param]) == dict:
                _sbl: dict = getattr(self, param)
                for i in range(5):
                    current[param]["human"][i] = _sbl["human"][i].value()
                    current[param]["ai"][i] = _sbl["ai"][i].value()
            else:
                _sb: QtWidgets.QSpinBox = getattr(self, param)
                current[param] = _sb.value()

    def load_from_file(self, file=None):
        if file is None:
            dialog = QtWidgets.QFileDialog()
            dialog.setFileMode(1)
            dialog.setAcceptMode(0)
            dialog.exec()
            if len(dialog.selectedFiles()) > 0:
                file = dialog.selectedFiles()[0]
            else:
                return

        file_str = open(file, encoding="utf-8 sig").read()
        file_str = preprocess_json_multilines(file_str)

        config = json.loads(file_str)
        for attrib in config:
            setattr(self.startgoods, attrib, config[attrib])
        self.update_view(self.latest_tab)

    def save_to_file(self, file=None):
        pass

    def load_parameters(self, config):
        pass


if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    w = MainWindow()
    sys.exit(app.exec_())
