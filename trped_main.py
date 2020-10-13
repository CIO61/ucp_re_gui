import param_types
from resource_types import TroopConfig
import json
import sys
import os
from utils import *
from UI.trped_mw import Ui_MainWindow
from PyQt5 import QtWidgets


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.show()
        self.latest_lordtab = 0
        self.latest_modetab = 0
        self.Lord_Tab.setCurrentIndex(0)
        self.mode_tab.setCurrentIndex(0)
        self.descr_tab.setCurrentIndex(0)
        self.mode_tab.currentChanged.connect(self.modetab_change)
        self.Lord_Tab.currentChanged.connect(self.lordtab_change)
        self.actionOpen.triggered.connect(lambda: self.load_from_file())
        self.actionSave.triggered.connect(lambda: self.save_to_file())
        self.set_blank_lord()
        if os.path.exists("./resources/troops/vanilla.json"):
            self.load_from_file("./resources/troops/vanilla.json")

    def lordtab_change(self, idx):
        self.update_view(self.mode_tab.currentIndex(), idx, upd_lord=True)

    def modetab_change(self, idx):
        self.update_view(idx, upd_mode=True)

    def update_view(self, mode_tab, lord_tab=None, upd_lord=False, upd_mode=False):
        if self.latest_modetab != -1:
            if self.latest_lordtab != -1 and upd_lord:
                self.update_lord("lord")
            elif upd_mode:
                self.update_lord()
        mode = self.mode_tab.tabText(mode_tab)
        lord = lords[self.Lord_Tab.currentIndex()]
        if lord_tab is not None:
            self.latest_lordtab = lord_tab
            self.Name.setText(lord.Name)
            _l = lord.Lord
            try:
                self.StrengthMultiplier.setValue(_l["StrengthMultiplier"])
                self.DotCount.setValue(_l["DotCount"])
                self.DotColour.setCurrentText(_l["DotColour"])
                self.Type.setCurrentText(_l["Type"])
            except TypeError:
                pass
        m = getattr(lord, mode.lower())
        for unit in param_types.Unit:
            try:
                getattr(self, unit).setValue(0)
            except AttributeError:
                pass
        for i, unit in enumerate(m["Units"]):
            getattr(self, unit).setValue(m["Counts"][i])
        self.latest_modetab = mode_tab

    def set_blank_lord(self):
        lord = blank_lord
        lord.Name = self.Name.text()
        lord.Lord["StrengthMultiplier"] = self.StrengthMultiplier.value()
        lord.Lord["DotColour"] = self.DotColour.currentText()
        lord.Lord["DotCount"] = self.DotCount.value()
        lord.Lord["Type"] = self.Type.currentText()

    def update_lord(self, scheme=""):
        lord = lords[self.latest_lordtab]
        mode = self.mode_tab.tabText(self.latest_modetab)
        if scheme == "lord":
            lord.Name = self.Name.text()
            _l = lord.Lord
            _l["StrengthMultiplier"] = self.StrengthMultiplier.value()
            _l["DotCount"] = self.DotCount.value()
            _l["DotColour"] = self.DotColour.currentText()
            _l["Type"] = self.Type.currentText()
        m = getattr(lord, mode.lower())
        m["Units"] = []
        m["Counts"] = []
        for unit in param_types.Unit:
            try:
                count = getattr(self, unit).value()
                if count != 0:
                    m["Units"].append(unit)
                    m["Counts"].append(count)
            except AttributeError:
                pass

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
        try:
            info = config["description"]
            for lang in info:
                getattr(self, lang+"_3").setPlainText(info[lang])
        except KeyError:
            pass
        load_parameters(config)
        self.update_view(self.mode_tab.currentIndex(), self.Lord_Tab.currentIndex())

    def save_to_file(self, file=None):
        if file is None:
            dialog = QtWidgets.QFileDialog()
            dialog.setDefaultSuffix("json")
            dialog.setAcceptMode(1)
            dialog.exec()
            if len(dialog.selectedFiles()) > 0:
                file = dialog.selectedFiles()[0]
            else:
                return
        self.update_lord("lord")
        output = dict()
        output["description"] = dict()
        output["description"] = {
            "German": self.German_3.toPlainText(),
            "English": self.English_3.toPlainText(),
            "Polish": self.Polish_3.toPlainText(),
            "Russian": self.Russian_3.toPlainText(),
            "Chinese": self.Chinese_3.toPlainText(),
            "Hungarian": self.Hungarian_3.toPlainText()
        }
        for i, lord in enumerate(lords):
            idx = str(i+1)
            output[idx] = dict()
            output[idx]["Name"] = lords[i].Name
            if lords[i].Lord is not None:
                output[idx]["Lord"] = lords[i].Lord
            output[idx]["normal"] = lords[i].normal
            output[idx]["crusader"] = lords[i].crusader
            output[idx]["deathmatch"] = lords[i].deathmatch
        json.dump(output, open(file, encoding="utf-8", newline="\n", mode="w"), indent="\t", ensure_ascii=False)


def load_parameters(config):
    for i, lord in enumerate(lords):
        try:
            char = config[str(i+1)]
            for param in char:
                lord.__setattr__(param, char[param])
        except KeyError:
            continue


if __name__ == '__main__':
    lords = [TroopConfig() for _ in range(18)]
    blank_lord = TroopConfig()
    app = QtWidgets.QApplication([])
    w = MainWindow()

    sys.exit(app.exec_())
