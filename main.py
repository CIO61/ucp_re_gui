import param_types
import json
import sys
import os
from UI.mainwindow import Ui_MainWindow
from PyQt5 import QtWidgets, QtCore
from aic import aic


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.show()
        self.latest_tab = -1
        self.Lord_Tab.setCurrentIndex(0)
        self.Param_Tab.setCurrentIndex(0)
        self.Lord_Tab.currentChanged.connect(self.tab_change)
        self.actionOpen.triggered.connect(lambda: self.load_from_file())
        self.actionSave.triggered.connect(lambda: self.save_to_file())
        if os.path.exists("vanilla.json"):
            self.load_from_file("vanilla.json")

    def retranslateUi(self, MainWindow):
        super().retranslateUi(MainWindow)
        fields_dict = param_types.param_fields
        for section in fields_dict:
            for field in fields_dict[section]:
                getattr(self, field).insertItems(0, getattr(param_types, section))

    def tab_change(self, idx):
        self.update_view(idx, True)

    def update_view(self, idx, upd=False):
        if upd:
            self.update_aic(self.latest_tab)
        lord = lords[idx]
        for param_name in param_types.param_names:
            obj = getattr(self, param_name)
            obj_name = obj.__class__.__name__
            val = getattr(lord, param_name)
            if val is None:
                continue
            for field_name in param_types.param_fields:
                field = param_types.param_fields[field_name]
                if param_name in field:
                    param_type = getattr(param_types, field_name)
            if obj_name == "QComboBox":
                obj.setCurrentIndex(param_type.index(val))
            elif obj_name == "QSpinBox":
                if param_name.find("Popularity") != -1:
                    val /= 100
                obj.setValue(val)
            elif obj_name == "QCheckBox":
                obj.setChecked(bool(val))
            elif obj_name == "QLineEdit":
                obj.setText(val)
        self.latest_tab = idx

    @QtCore.pyqtSlot()
    def update_aic(self, idx):
        lord = lords[idx]
        for param_name in param_types.param_names:
            obj = getattr(self, param_name)
            obj_name = obj.__class__.__name__
            if obj_name == "QComboBox":
                val = obj.currentText()
            elif obj_name == "QSpinBox":
                val = obj.value()
                if param_name.find("Popularity") != -1:
                    val *= 100
            elif obj_name == "QCheckBox":
                val = str(obj.isChecked())
            elif obj_name == "QLineEdit":
                val = obj.text()
            lord.__setattr__(param_name, val)

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

        config = json.load(open(file, encoding="utf-8"))
        info = config["AICShortDescription"]
        for lang in info:
            getattr(self, lang).setPlainText(info[lang])
        load_parameters(config)
        self.update_view(self.Lord_Tab.currentIndex())

    def save_to_file(self, file=None):
        if file is None:
            dialog = QtWidgets.QFileDialog()
            dialog.setAcceptMode(1)
            dialog.exec()
            if len(dialog.selectedFiles()) > 0:
                file = dialog.selectedFiles()[0]
            else:
                return

        output = dict()
        output["AICShortDescription"] = {
            "German": self.German.toPlainText(),
            "English": self.English.toPlainText(),
            "Polish": self.Polish.toPlainText(),
            "Russian": self.Russian.toPlainText(),
            "Chinese": self.Chinese.toPlainText()
        }
        output["AICharacters"] = dict()
        output["AICharacters"]["Personality"] = dict()
        for lord in lords:
            for param_name in param_types.param_names:
                if param_name == "Name" or param_name == "Description":
                    output["AICharacters"][param_name] = getattr(lord, param_name)
                else:
                    output["AICharacters"]["Personality"][param_name] = getattr(lord, param_name)
        json.dump(output, open(file, encoding="utf-8", mode="w+"), indent=4, ensure_ascii=False)


def load_parameters(config):
    chars = config["AICharacters"]
    for i, lord in enumerate(lords):
        lord.Name = chars[i]["Name"]
        lord.Description = chars[i]["Description"]
        for attrib in chars[i]["Personality"]:
            lord.__setattr__(attrib, chars[i]["Personality"][attrib])


if __name__ == '__main__':
    lords = [
        aic(), aic(), aic(), aic(), aic(), aic(), aic(), aic(),
        aic(), aic(), aic(), aic(), aic(), aic(), aic(), aic()
    ]
    app = QtWidgets.QApplication([])
    w = MainWindow()

    sys.exit(app.exec_())