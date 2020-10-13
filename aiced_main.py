import param_types
import json
import sys
import os
from utils import *
from UI.aic_gui import Ui_MainWindow
from PyQt5 import QtWidgets
from resource_types import aic


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.lords = [aic() for i in range(16)]
        self.blank_lord = aic()
        self.setupUi(self)
        self.show()
        self.latest_tab = 0
        self.Lord_Tab.setCurrentIndex(0)
        self.Param_Tab.setCurrentIndex(0)
        self.Lord_Tab.currentChanged.connect(self.tab_change)
        self.actionOpen.triggered.connect(lambda: self.load_from_file())
        self.actionSave.triggered.connect(lambda: self.save_to_file())
        self.set_blank_lord(self.blank_lord)
        if os.path.exists("./resources/aic/vanilla.json"):
            self.load_from_file("./resources/aic/vanilla.json")
        else:
            for lord in self.lords:
                self.set_blank_lord(lord)

    def retranslateUi(self, window):
        super().retranslateUi(window)
        fields_dict = param_types.param_fields
        for section in fields_dict:
            for field in fields_dict[section]:
                getattr(self, field).insertItems(0, getattr(param_types, section))

    def tab_change(self, idx):
        self.update_view(idx, True)

    def update_view(self, idx, upd=False):
        if upd and self.latest_tab != -1:
            self.update_lord(self.latest_tab)
        lord = self.lords[idx]
        self.Name.setText(lord.Name)
        self.Description.setText(lord.Description)
        self.CustomName.setText(lord.CustomName)
        for param_name in param_types.param_names:
            obj = getattr(self, param_name)
            obj_name = obj.__class__.__name__
            val = lord.Personality[param_name]
            if val is None:
                continue
            param_type = None
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
        self.latest_tab = idx

    def set_blank_lord(self, lord):
        lord.Name = self.Name.text()
        lord.Description = self.Description.text()
        lord.CustomName = self.CustomName.text()
        for param_name in param_types.param_names:
            obj = getattr(self, param_name)
            obj_name = obj.__class__.__name__
            val = None
            if obj_name == "QComboBox":
                val = obj.currentText()
            elif obj_name == "QSpinBox":
                val = obj.value()
                if param_name.find("Popularity") != -1:
                    val *= 100
            elif obj_name == "QCheckBox":
                val = str(obj.isChecked())
            lord.Personality[param_name] = val

    def update_lord(self, idx):
        lord = self.lords[idx]
        lord.Name = self.Name.text()
        lord.Description = self.Description.text()
        lord.CustomName = self.CustomName.text()
        for param_name in param_types.param_names:
            obj = getattr(self, param_name)
            obj_name = obj.__class__.__name__
            val = None
            if obj_name == "QComboBox":
                val = obj.currentText()
            elif obj_name == "QSpinBox":
                val = obj.value()
                if param_name.find("Popularity") != -1:
                    val *= 100
            elif obj_name == "QCheckBox":
                val = str(obj.isChecked())
            lord.Personality[param_name] = val

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
            info = config["AICShortDescription"]
            for lang in info:
                getattr(self, lang).setPlainText(info[lang])
        except KeyError:
            pass
        try:
            info_long = config["AICLongDescription"]
            for lang in info_long:
                getattr(self, lang+"_2").setPlainText(info_long[lang])
        except KeyError:
            pass
        self.load_parameters(config)
        self.update_view(self.Lord_Tab.currentIndex())

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
        self.update_lord(self.Lord_Tab.currentIndex())
        output = dict()
        output["AICShortDescription"] = {
            "German": self.German.toPlainText(),
            "English": self.English.toPlainText(),
            "Polish": self.Polish.toPlainText(),
            "Russian": self.Russian.toPlainText(),
            "Chinese": self.Chinese.toPlainText(),
            "Hungarian": self.Hungarian.toPlainText()
        }
        output["AICLongDescription"] = {
            "German": self.German_2.toPlainText(),
            "English": self.English_2.toPlainText(),
            "Polish": self.Polish_2.toPlainText(),
            "Russian": self.Russian_2.toPlainText(),
            "Chinese": self.Chinese_2.toPlainText(),
            "Hungarian": self.Hungarian_2.toPlainText()
        }
        output["AICharacters"] = list()
        for lord in self.lords:
            lord_info = {
                "Name": lord.Name,
                "Description": lord.Description,
                "Personality": lord.Personality,
                "CustomName": lord.CustomName
            }
            if any(lord.Personality[item] is None for item in lord.Personality):
                continue
            elif all(lord.Personality[item] == self.blank_lord.Personality[item] for item in lord.Personality):
                continue
            else:
                output["AICharacters"].append(lord_info)
        json.dump(output, open(file, encoding="utf-8", newline="\n", mode="w"), indent="\t", ensure_ascii=False)

    def load_parameters(self, config):
        chars = config["AICharacters"]
        for i, lord in enumerate(self.lords):
            try:
                lord.Name = chars[i]["Name"]
                lord.Personality = chars[i]["Personality"]
                lord.Description = chars[i]["Description"]
                lord.CustomName = chars[i]["CustomName"]
            except KeyError:
                continue


if __name__ == '__main__':

    app = QtWidgets.QApplication([])
    w = MainWindow()

    sys.exit(app.exec_())
