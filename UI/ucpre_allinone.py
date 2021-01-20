# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ucpre_allinone.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(258, 203)
        # icon = QtGui.QIcon()
        # icon.addPixmap(QtGui.QPixmap(":/icon/spear.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        # MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.aic = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.aic.sizePolicy().hasHeightForWidth())
        self.aic.setSizePolicy(sizePolicy)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/icon/armourer_sketch.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.aic.setIcon(icon1)
        self.aic.setIconSize(QtCore.QSize(36, 36))
        self.aic.setObjectName("aic")
        self.verticalLayout.addWidget(self.aic)
        self.trp = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.trp.sizePolicy().hasHeightForWidth())
        self.trp.setSizePolicy(sizePolicy)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/icon/army_sketch.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.trp.setIcon(icon2)
        self.trp.setIconSize(QtCore.QSize(36, 36))
        self.trp.setObjectName("trp")
        self.verticalLayout.addWidget(self.trp)
        self.stg = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.stg.sizePolicy().hasHeightForWidth())
        self.stg.setSizePolicy(sizePolicy)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/icon/stockpile_sketch.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.stg.setIcon(icon3)
        self.stg.setIconSize(QtCore.QSize(36, 36))
        self.stg.setObjectName("stg")
        self.verticalLayout.addWidget(self.stg)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 258, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "UCPRE Launcher"))
        self.aic.setText(_translate("MainWindow", "AIC Editor"))
        self.trp.setText(_translate("MainWindow", "Troop Config Editor"))
        self.stg.setText(_translate("MainWindow", "Start Goods Editor"))
import rsrc_rc
