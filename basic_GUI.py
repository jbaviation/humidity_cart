# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'basic_GUI.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.VoltageLCD = QtWidgets.QLCDNumber(self.centralwidget)
        self.VoltageLCD.setGeometry(QtCore.QRect(70, 80, 191, 121))
        self.VoltageLCD.setSmallDecimalPoint(False)
        self.VoltageLCD.setDigitCount(6)
        self.VoltageLCD.setSegmentStyle(QtWidgets.QLCDNumber.Filled)
        self.VoltageLCD.setProperty("intValue", 0)
        self.VoltageLCD.setObjectName("VoltageLCD")
        self.VoltageLabel = QtWidgets.QLabel(self.centralwidget)
        self.VoltageLabel.setGeometry(QtCore.QRect(80, 40, 201, 41))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.VoltageLabel.setFont(font)
        self.VoltageLabel.setObjectName("VoltageLabel")
        self.UnitVoltageLabel = QtWidgets.QLabel(self.centralwidget)
        self.UnitVoltageLabel.setGeometry(QtCore.QRect(280, 100, 151, 81))
        self.UnitVoltageLabel.setObjectName("UnitVoltageLabel")
        self.DPLabel = QtWidgets.QLabel(self.centralwidget)
        self.DPLabel.setGeometry(QtCore.QRect(80, 220, 241, 51))
        self.DPLabel.setObjectName("DPLabel")
        self.UnitDPLabel = QtWidgets.QLabel(self.centralwidget)
        self.UnitDPLabel.setGeometry(QtCore.QRect(280, 290, 151, 81))
        self.UnitDPLabel.setObjectName("UnitDPLabel")
        self.DPLCD = QtWidgets.QLCDNumber(self.centralwidget)
        self.DPLCD.setGeometry(QtCore.QRect(70, 270, 191, 121))
        self.DPLCD.setDigitCount(6)
        self.DPLCD.setObjectName("DPLCD")
        self.CloseButton = QtWidgets.QPushButton(self.centralwidget)
        self.CloseButton.setGeometry(QtCore.QRect(60, 430, 231, 61))
        font = QtGui.QFont()
        font.setPointSize(22)
        self.CloseButton.setFont(font)
        self.CloseButton.setObjectName("CloseButton")
        self.StartButton = QtWidgets.QRadioButton(self.centralwidget)
        self.StartButton.setGeometry(QtCore.QRect(30, 10, 99, 21))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.StartButton.setFont(font)
        self.StartButton.setObjectName("StartButton")
        self.StopButton = QtWidgets.QRadioButton(self.centralwidget)
        self.StopButton.setGeometry(QtCore.QRect(190, 10, 99, 21))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.StopButton.setFont(font)
        self.StopButton.setAutoExclusive(True)
        self.StopButton.setObjectName("StopButton")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Humidity Cart Calibration"))
        self.VoltageLabel.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:14pt; font-weight:600;\">Source Voltage</span></p></body></html>"))
        self.UnitVoltageLabel.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:48pt;\">V</span></p></body></html>"))
        self.DPLabel.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:14pt; font-weight:600;\">Source Dew Point</span></p></body></html>"))
        self.UnitDPLabel.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:48pt;\">°F</span></p></body></html>"))
        self.CloseButton.setText(_translate("MainWindow", "Close"))
        self.StartButton.setText(_translate("MainWindow", "Scan"))
        self.StopButton.setText(_translate("MainWindow", "Stop"))
