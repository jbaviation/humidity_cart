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
        MainWindow.resize(1002, 831)
        MainWindow.setToolTip("")
        MainWindow.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.HumGenLCD1 = QtWidgets.QLCDNumber(self.centralwidget)
        self.HumGenLCD1.setGeometry(QtCore.QRect(126, 100, 221, 61))
        self.HumGenLCD1.setSmallDecimalPoint(False)
        self.HumGenLCD1.setDigitCount(8)
        self.HumGenLCD1.setSegmentStyle(QtWidgets.QLCDNumber.Filled)
        self.HumGenLCD1.setProperty("intValue", 0)
        self.HumGenLCD1.setObjectName("HumGenLCD1")
        self.HumGenUnits1 = QtWidgets.QLabel(self.centralwidget)
        self.HumGenUnits1.setGeometry(QtCore.QRect(350, 90, 171, 81))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(20)
        self.HumGenUnits1.setFont(font)
        self.HumGenUnits1.setObjectName("HumGenUnits1")
        self.HumGenUnits2 = QtWidgets.QLabel(self.centralwidget)
        self.HumGenUnits2.setGeometry(QtCore.QRect(349, 330, 181, 81))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(20)
        self.HumGenUnits2.setFont(font)
        self.HumGenUnits2.setObjectName("HumGenUnits2")
        self.HumGenLCD2 = QtWidgets.QLCDNumber(self.centralwidget)
        self.HumGenLCD2.setGeometry(QtCore.QRect(126, 340, 221, 61))
        self.HumGenLCD2.setDigitCount(8)
        self.HumGenLCD2.setObjectName("HumGenLCD2")
        self.HumGenDDbox1 = QtWidgets.QComboBox(self.centralwidget)
        self.HumGenDDbox1.setGeometry(QtCore.QRect(60, 50, 301, 41))
        self.HumGenDDbox1.setObjectName("HumGenDDbox1")
        self.HumGenDDbox2 = QtWidgets.QComboBox(self.centralwidget)
        self.HumGenDDbox2.setGeometry(QtCore.QRect(60, 290, 301, 41))
        self.HumGenDDbox2.setObjectName("HumGenDDbox2")
        self.HumGenUnits3 = QtWidgets.QLabel(self.centralwidget)
        self.HumGenUnits3.setGeometry(QtCore.QRect(350, 570, 181, 81))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(20)
        self.HumGenUnits3.setFont(font)
        self.HumGenUnits3.setObjectName("HumGenUnits3")
        self.HumGenLCD3 = QtWidgets.QLCDNumber(self.centralwidget)
        self.HumGenLCD3.setGeometry(QtCore.QRect(126, 580, 221, 61))
        self.HumGenLCD3.setDigitCount(8)
        self.HumGenLCD3.setObjectName("HumGenLCD3")
        self.HumGenDDbox3 = QtWidgets.QComboBox(self.centralwidget)
        self.HumGenDDbox3.setGeometry(QtCore.QRect(60, 530, 301, 41))
        self.HumGenDDbox3.setObjectName("HumGenDDbox3")
        self.PressureEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.PressureEdit.setGeometry(QtCore.QRect(580, 90, 271, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.PressureEdit.setFont(font)
        self.PressureEdit.setObjectName("PressureEdit")
        self.TemperatureEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.TemperatureEdit.setGeometry(QtCore.QRect(580, 180, 271, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.TemperatureEdit.setFont(font)
        self.TemperatureEdit.setObjectName("TemperatureEdit")
        self.PressureLabel = QtWidgets.QLabel(self.centralwidget)
        self.PressureLabel.setGeometry(QtCore.QRect(580, 70, 211, 16))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.PressureLabel.setFont(font)
        self.PressureLabel.setObjectName("PressureLabel")
        self.TemperatureLabel = QtWidgets.QLabel(self.centralwidget)
        self.TemperatureLabel.setGeometry(QtCore.QRect(581, 157, 211, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.TemperatureLabel.setFont(font)
        self.TemperatureLabel.setObjectName("TemperatureLabel")
        self.PressureUnitLabel = QtWidgets.QLabel(self.centralwidget)
        self.PressureUnitLabel.setGeometry(QtCore.QRect(854, 82, 71, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.PressureUnitLabel.setFont(font)
        self.PressureUnitLabel.setObjectName("PressureUnitLabel")
        self.TemperatureUnitLabel = QtWidgets.QLabel(self.centralwidget)
        self.TemperatureUnitLabel.setGeometry(QtCore.QRect(854, 176, 51, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.TemperatureUnitLabel.setFont(font)
        self.TemperatureUnitLabel.setObjectName("TemperatureUnitLabel")
        self.SetConditionsButton = QtWidgets.QPushButton(self.centralwidget)
        self.SetConditionsButton.setGeometry(QtCore.QRect(640, 231, 151, 51))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.SetConditionsButton.setFont(font)
        self.SetConditionsButton.setToolTip("")
        self.SetConditionsButton.setObjectName("SetConditionsButton")
        self.CloseButton = QtWidgets.QPushButton(self.centralwidget)
        self.CloseButton.setGeometry(QtCore.QRect(640, 700, 151, 61))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.CloseButton.setFont(font)
        self.CloseButton.setObjectName("CloseButton")
        self.lcLabel1 = QtWidgets.QLabel(self.centralwidget)
        self.lcLabel1.setGeometry(QtCore.QRect(10, 110, 111, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lcLabel1.setFont(font)
        self.lcLabel1.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lcLabel1.setWordWrap(True)
        self.lcLabel1.setObjectName("lcLabel1")
        self.lcLabel2 = QtWidgets.QLabel(self.centralwidget)
        self.lcLabel2.setGeometry(QtCore.QRect(10, 350, 111, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lcLabel2.setFont(font)
        self.lcLabel2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lcLabel2.setWordWrap(True)
        self.lcLabel2.setObjectName("lcLabel2")
        self.lcLabel3 = QtWidgets.QLabel(self.centralwidget)
        self.lcLabel3.setGeometry(QtCore.QRect(10, 590, 111, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lcLabel3.setFont(font)
        self.lcLabel3.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lcLabel3.setWordWrap(True)
        self.lcLabel3.setObjectName("lcLabel3")
        self.AirCondLabel = QtWidgets.QLabel(self.centralwidget)
        self.AirCondLabel.setGeometry(QtCore.QRect(580, 30, 371, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setUnderline(False)
        self.AirCondLabel.setFont(font)
        self.AirCondLabel.setTextFormat(QtCore.Qt.AutoText)
        self.AirCondLabel.setObjectName("AirCondLabel")
        self.LiCorGroupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.LiCorGroupBox.setGeometry(QtCore.QRect(539, 310, 201, 181))
        self.LiCorGroupBox.setTitle("")
        self.LiCorGroupBox.setObjectName("LiCorGroupBox")
        self.StopButton = QtWidgets.QRadioButton(self.LiCorGroupBox)
        self.StopButton.setGeometry(QtCore.QRect(20, 140, 99, 21))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.StopButton.setFont(font)
        self.StopButton.setToolTip("")
        self.StopButton.setToolTipDuration(-1)
        self.StopButton.setAutoExclusive(True)
        self.StopButton.setObjectName("StopButton")
        self.StartButton = QtWidgets.QRadioButton(self.LiCorGroupBox)
        self.StartButton.setGeometry(QtCore.QRect(20, 110, 99, 21))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.StartButton.setFont(font)
        self.StartButton.setToolTip("")
        self.StartButton.setToolTipDuration(-1)
        self.StartButton.setStatusTip("")
        self.StartButton.setObjectName("StartButton")
        self.HumGenLabel = QtWidgets.QLabel(self.LiCorGroupBox)
        self.HumGenLabel.setGeometry(QtCore.QRect(10, 4, 141, 101))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setUnderline(False)
        self.HumGenLabel.setFont(font)
        self.HumGenLabel.setToolTip("")
        self.HumGenLabel.setToolTipDuration(-1)
        self.HumGenLabel.setTextFormat(QtCore.Qt.AutoText)
        self.HumGenLabel.setWordWrap(True)
        self.HumGenLabel.setObjectName("HumGenLabel")
        self.WVSSgroupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.WVSSgroupBox.setGeometry(QtCore.QRect(739, 310, 221, 181))
        self.WVSSgroupBox.setTitle("")
        self.WVSSgroupBox.setObjectName("WVSSgroupBox")
        self.WVSSstartButton = QtWidgets.QRadioButton(self.WVSSgroupBox)
        self.WVSSstartButton.setGeometry(QtCore.QRect(20, 110, 82, 21))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.WVSSstartButton.setFont(font)
        self.WVSSstartButton.setToolTip("")
        self.WVSSstartButton.setToolTipDuration(-1)
        self.WVSSstartButton.setObjectName("WVSSstartButton")
        self.WVSSstopButton = QtWidgets.QRadioButton(self.WVSSgroupBox)
        self.WVSSstopButton.setGeometry(QtCore.QRect(20, 140, 82, 21))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.WVSSstopButton.setFont(font)
        self.WVSSstopButton.setToolTip("")
        self.WVSSstopButton.setToolTipDuration(-1)
        self.WVSSstopButton.setObjectName("WVSSstopButton")
        self.WVSSLabel = QtWidgets.QLabel(self.WVSSgroupBox)
        self.WVSSLabel.setGeometry(QtCore.QRect(10, 4, 211, 101))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setUnderline(False)
        self.WVSSLabel.setFont(font)
        self.WVSSLabel.setTextFormat(QtCore.Qt.AutoText)
        self.WVSSLabel.setWordWrap(True)
        self.WVSSLabel.setObjectName("WVSSLabel")
        self.ssLabel1 = QtWidgets.QLabel(self.centralwidget)
        self.ssLabel1.setGeometry(QtCore.QRect(10, 190, 111, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.ssLabel1.setFont(font)
        self.ssLabel1.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.ssLabel1.setObjectName("ssLabel1")
        self.ssLabel2 = QtWidgets.QLabel(self.centralwidget)
        self.ssLabel2.setGeometry(QtCore.QRect(10, 430, 111, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.ssLabel2.setFont(font)
        self.ssLabel2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.ssLabel2.setObjectName("ssLabel2")
        self.ssLabel3 = QtWidgets.QLabel(self.centralwidget)
        self.ssLabel3.setGeometry(QtCore.QRect(10, 660, 111, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.ssLabel3.setFont(font)
        self.ssLabel3.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.ssLabel3.setObjectName("ssLabel3")
        self.WVSSLCD1 = QtWidgets.QLCDNumber(self.centralwidget)
        self.WVSSLCD1.setGeometry(QtCore.QRect(126, 180, 221, 61))
        self.WVSSLCD1.setSmallDecimalPoint(False)
        self.WVSSLCD1.setDigitCount(8)
        self.WVSSLCD1.setSegmentStyle(QtWidgets.QLCDNumber.Filled)
        self.WVSSLCD1.setProperty("intValue", 0)
        self.WVSSLCD1.setObjectName("WVSSLCD1")
        self.WVSSLCD2 = QtWidgets.QLCDNumber(self.centralwidget)
        self.WVSSLCD2.setGeometry(QtCore.QRect(126, 420, 221, 61))
        self.WVSSLCD2.setSmallDecimalPoint(False)
        self.WVSSLCD2.setDigitCount(8)
        self.WVSSLCD2.setSegmentStyle(QtWidgets.QLCDNumber.Filled)
        self.WVSSLCD2.setProperty("intValue", 0)
        self.WVSSLCD2.setObjectName("WVSSLCD2")
        self.WVSSLCD3 = QtWidgets.QLCDNumber(self.centralwidget)
        self.WVSSLCD3.setGeometry(QtCore.QRect(126, 654, 221, 61))
        self.WVSSLCD3.setSmallDecimalPoint(False)
        self.WVSSLCD3.setDigitCount(8)
        self.WVSSLCD3.setSegmentStyle(QtWidgets.QLCDNumber.Filled)
        self.WVSSLCD3.setProperty("intValue", 0)
        self.WVSSLCD3.setObjectName("WVSSLCD3")
        self.WVSSUnits1 = QtWidgets.QLabel(self.centralwidget)
        self.WVSSUnits1.setGeometry(QtCore.QRect(350, 170, 171, 81))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(20)
        self.WVSSUnits1.setFont(font)
        self.WVSSUnits1.setObjectName("WVSSUnits1")
        self.WVSSUnits2 = QtWidgets.QLabel(self.centralwidget)
        self.WVSSUnits2.setGeometry(QtCore.QRect(350, 410, 181, 81))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(20)
        self.WVSSUnits2.setFont(font)
        self.WVSSUnits2.setObjectName("WVSSUnits2")
        self.WVSSUnits3 = QtWidgets.QLabel(self.centralwidget)
        self.WVSSUnits3.setGeometry(QtCore.QRect(350, 642, 181, 81))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(20)
        self.WVSSUnits3.setFont(font)
        self.WVSSUnits3.setObjectName("WVSSUnits3")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(540, 520, 421, 151))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.groupBox.setFont(font)
        self.groupBox.setObjectName("groupBox")
        self.recordButton = QtWidgets.QPushButton(self.groupBox)
        self.recordButton.setGeometry(QtCore.QRect(40, 20, 101, 41))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(170, 170, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(212, 212, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(85, 85, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(113, 113, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(170, 170, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(212, 212, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(170, 170, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(212, 212, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(85, 85, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(113, 113, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(170, 170, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(212, 212, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(85, 85, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(170, 170, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(212, 212, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(85, 85, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(113, 113, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(85, 85, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(85, 85, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(170, 170, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(170, 170, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(170, 170, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ToolTipText, brush)
        self.recordButton.setPalette(palette)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.recordButton.setFont(font)
        self.recordButton.setObjectName("recordButton")
        self.statusLED = QtWidgets.QLabel(self.groupBox)
        self.statusLED.setGeometry(QtCore.QRect(12, 30, 21, 21))
        self.statusLED.setText("")
        self.statusLED.setScaledContents(False)
        self.statusLED.setObjectName("statusLED")
        self.recordStopButton = QtWidgets.QPushButton(self.groupBox)
        self.recordStopButton.setGeometry(QtCore.QRect(35, 80, 111, 41))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(170, 170, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(212, 212, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(85, 85, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(113, 113, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(170, 170, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(212, 212, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(170, 170, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(212, 212, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(85, 85, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(113, 113, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(170, 170, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(212, 212, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(85, 85, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(170, 170, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(212, 212, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(85, 85, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(113, 113, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(85, 85, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(85, 85, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(170, 170, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(170, 170, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(170, 170, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ToolTipText, brush)
        self.recordStopButton.setPalette(palette)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.recordStopButton.setFont(font)
        self.recordStopButton.setObjectName("recordStopButton")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1002, 21))
        self.menubar.setObjectName("menubar")
        self.menuSetup = QtWidgets.QMenu(self.menubar)
        self.menuSetup.setObjectName("menuSetup")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menuHardware = QtWidgets.QAction(MainWindow)
        self.menuHardware.setObjectName("menuHardware")
        self.menuRecording = QtWidgets.QAction(MainWindow)
        self.menuRecording.setObjectName("menuRecording")
        self.menuRecord = QtWidgets.QAction(MainWindow)
        self.menuRecord.setObjectName("menuRecord")
        self.menuSetup.addAction(self.menuHardware)
        self.menuSetup.addAction(self.menuRecording)
        self.menuFile.addAction(self.menuRecord)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuSetup.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Humidity Cart Calibration"))
        self.HumGenUnits1.setText(_translate("MainWindow", "°F"))
        self.HumGenUnits2.setText(_translate("MainWindow", "°F"))
        self.HumGenUnits3.setText(_translate("MainWindow", "°F"))
        self.PressureEdit.setText(_translate("MainWindow", "14.696"))
        self.TemperatureEdit.setText(_translate("MainWindow", "59"))
        self.PressureLabel.setText(_translate("MainWindow", "Pressure"))
        self.TemperatureLabel.setText(_translate("MainWindow", "Temperature"))
        self.PressureUnitLabel.setText(_translate("MainWindow", "psia"))
        self.TemperatureUnitLabel.setText(_translate("MainWindow", "°F"))
        self.SetConditionsButton.setText(_translate("MainWindow", "Set Conditions"))
        self.CloseButton.setText(_translate("MainWindow", "Close"))
        self.lcLabel1.setText(_translate("MainWindow", "Humidity Generator"))
        self.lcLabel2.setText(_translate("MainWindow", "Humidity Generator"))
        self.lcLabel3.setText(_translate("MainWindow", "Humidity Generator"))
        self.AirCondLabel.setText(_translate("MainWindow", "Airstream Conditions"))
        self.StopButton.setText(_translate("MainWindow", "Stop"))
        self.StartButton.setText(_translate("MainWindow", "Scan"))
        self.HumGenLabel.setText(_translate("MainWindow", "Humidity Generator"))
        self.WVSSstartButton.setText(_translate("MainWindow", "Scan"))
        self.WVSSstopButton.setText(_translate("MainWindow", "Stop"))
        self.WVSSLabel.setText(_translate("MainWindow", "Water Vapor Monitor System"))
        self.ssLabel1.setText(_translate("MainWindow", "WVSS"))
        self.ssLabel2.setText(_translate("MainWindow", "WVSS"))
        self.ssLabel3.setText(_translate("MainWindow", "WVSS"))
        self.WVSSUnits1.setText(_translate("MainWindow", "°F"))
        self.WVSSUnits2.setText(_translate("MainWindow", "°F"))
        self.WVSSUnits3.setText(_translate("MainWindow", "°F"))
        self.groupBox.setTitle(_translate("MainWindow", "Recordings"))
        self.recordButton.setText(_translate("MainWindow", "Record"))
        self.recordStopButton.setText(_translate("MainWindow", "Record Stop"))
        self.menuSetup.setTitle(_translate("MainWindow", "Setup"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuHardware.setText(_translate("MainWindow", "Port Configuration"))
        self.menuRecording.setText(_translate("MainWindow", "Recording Configuration"))
        self.menuRecord.setText(_translate("MainWindow", "Record"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
