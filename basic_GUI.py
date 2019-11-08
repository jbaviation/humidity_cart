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
        MainWindow.resize(712, 877)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.HumGenLCD1 = QtWidgets.QLCDNumber(self.centralwidget)
        self.HumGenLCD1.setGeometry(QtCore.QRect(60, 200, 191, 121))
        self.HumGenLCD1.setSmallDecimalPoint(False)
        self.HumGenLCD1.setDigitCount(6)
        self.HumGenLCD1.setSegmentStyle(QtWidgets.QLCDNumber.Filled)
        self.HumGenLCD1.setProperty("intValue", 0)
        self.HumGenLCD1.setObjectName("HumGenLCD1")
        self.HumGenLabel = QtWidgets.QLabel(self.centralwidget)
        self.HumGenLabel.setGeometry(QtCore.QRect(50, 20, 371, 71))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.HumGenLabel.setFont(font)
        self.HumGenLabel.setTextFormat(QtCore.Qt.AutoText)
        self.HumGenLabel.setObjectName("HumGenLabel")
        self.HumGenUnits1 = QtWidgets.QLabel(self.centralwidget)
        self.HumGenUnits1.setGeometry(QtCore.QRect(270, 220, 151, 81))
        self.HumGenUnits1.setObjectName("HumGenUnits1")
        self.HumGenUnits2 = QtWidgets.QLabel(self.centralwidget)
        self.HumGenUnits2.setGeometry(QtCore.QRect(270, 430, 151, 81))
        self.HumGenUnits2.setObjectName("HumGenUnits2")
        self.HumGenLCD2 = QtWidgets.QLCDNumber(self.centralwidget)
        self.HumGenLCD2.setGeometry(QtCore.QRect(60, 410, 191, 121))
        self.HumGenLCD2.setDigitCount(6)
        self.HumGenLCD2.setObjectName("HumGenLCD2")
        self.StartButton = QtWidgets.QRadioButton(self.centralwidget)
        self.StartButton.setGeometry(QtCore.QRect(50, 90, 99, 21))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.StartButton.setFont(font)
        self.StartButton.setObjectName("StartButton")
        self.StopButton = QtWidgets.QRadioButton(self.centralwidget)
        self.StopButton.setGeometry(QtCore.QRect(200, 90, 99, 21))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.StopButton.setFont(font)
        self.StopButton.setAutoExclusive(True)
        self.StopButton.setObjectName("StopButton")
        self.HumGenDDbox1 = QtWidgets.QComboBox(self.centralwidget)
        self.HumGenDDbox1.setGeometry(QtCore.QRect(60, 150, 301, 41))
        self.HumGenDDbox1.setObjectName("HumGenDDbox1")
        self.HumGenDDbox2 = QtWidgets.QComboBox(self.centralwidget)
        self.HumGenDDbox2.setGeometry(QtCore.QRect(60, 360, 301, 41))
        self.HumGenDDbox2.setObjectName("HumGenDDbox2")
        self.HumGenUnits3 = QtWidgets.QLabel(self.centralwidget)
        self.HumGenUnits3.setGeometry(QtCore.QRect(270, 660, 151, 81))
        self.HumGenUnits3.setObjectName("HumGenUnits3")
        self.HumGenLCD3 = QtWidgets.QLCDNumber(self.centralwidget)
        self.HumGenLCD3.setGeometry(QtCore.QRect(60, 640, 191, 121))
        self.HumGenLCD3.setDigitCount(6)
        self.HumGenLCD3.setObjectName("HumGenLCD3")
        self.HumGenDDbox3 = QtWidgets.QComboBox(self.centralwidget)
        self.HumGenDDbox3.setGeometry(QtCore.QRect(60, 590, 301, 41))
        self.HumGenDDbox3.setObjectName("HumGenDDbox3")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 712, 21))
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
        self.HumGenLabel.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-weight:600;\">Humidity Generator</span></p></body></html>"))
        self.HumGenUnits1.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:48pt;\">V</span></p></body></html>"))
        self.HumGenUnits2.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:48pt;\">°F</span></p></body></html>"))
        self.StartButton.setText(_translate("MainWindow", "Scan"))
        self.StopButton.setText(_translate("MainWindow", "Stop"))
        self.HumGenUnits3.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:48pt;\">°F</span></p></body></html>"))
