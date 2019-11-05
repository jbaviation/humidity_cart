# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './basic_GUI.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
import serial
import time
import sys
import keyboard
import threading

# Create the class 'Communicate'. The instance
# from this class shall be used later on for the
# signal/slot mechanism.
class Communicate(QtCore.QObject):
    myGUI_signal = QtCore.pyqtSignal(str)

class DataQ_DI145():
    # Declare threading variables for the class
    # stop_thread = True
    # t1 = None

    def __init__(self, comm_port='COM4', baud_rate=4800, C1=0.0003, C0=0.0):
        ''' Initialize instance variable defaults for the DataQ_DI145 class

        Variable Descriptions:
            comm_port - USB communication port of ADC device (default: COM4 on 17021058 Machine)
            baud_rate - baud rate of the device (default: 4800 for DI145)
            C1 - Slope coefficient of counts vs Volts (default: 0.0003 for nominal conversion)
            C0 - Offset coefficient of counts vs Volts (default: 0.0 for nominal conversion)
        '''
        self.comm_port = comm_port
        self.baud_rate = baud_rate
        self.C1 = C1
        self.C0 = C0

        # Cancel any threading that may be taking place already
        self.stop_thread = True
        self.t1 = None    # initialize class variable

        # Declare instance variables
        self.counts = None
        self.voltage = None

        try:
            self.serDataq = serial.Serial(comm_port, baud_rate)  # initiate communication with ADC device
            self.serDataq.write(b'S0\r')   # force device to stop scanning if was left scanning
            self.serDataq.write(b'C1')     # enable only channel 1
        except:
            pass


    def scan(self):
        ''' Initiate device scan '''
        self.stop_thread = False
        try:
            self.serDataq.write(b'S1')      # start scanning
            self.statemachine = 0           # initate synched variable
            print('Scan started')
        except:
            print('Could NOT scan the device...try re-initializing')


    def sts(self):
        ''' Initiate device stop '''
        self.stop_thread = True
        try:
            self.serDataq.write(b'S0')      # stop scanning
            self.serDataq.close()           # close connection so that port can be used
            print('Scan stopped')
        except:
            print('Could NOT stop scan the device...try re-initializing')

        try:
            self.stop_thread = True
            self.t1.join()
            print('Thread stopped')
        except:
            print('Could NOT stop thread')


    def _run(self):
        ''' Meant to run as a thread for taking voltage and counts from the ADC device'''
        # Setup the signal-slot mechanism
        mySrc = Communicate()


        while True:
            try:

                if self.stop_thread:
                    break

                string = self.serDataq.read()
                byte = ord(string)

                if self.statemachine==0:
                    # wait until we see bit 0=0
                    if (byte & 1)==0:       # unsynched
                        data=byte>>1        # bitwise shift to remove synch bit
                        self.statemachine=1 # indicate that we are synched
                else:
                    self.statemachine=0     # set the state of the machine to unsynched
                    if byte & 1:    # if the last bit is 1, this is a continuation or 2nd byte
                        byte2=(byte&254)<<6     # bitwise compare with 11111110 and shift left for 14-bit value
                        data=data+byte2         # combine with status bits from previous byte
                        data=data<<2            # shift left 2 bits for 16-bit value
                        self.counts=data-32768       # subract 1000 0000 0000 0000 for raw ADC count
                        self.voltage = self.C1*self.counts + self.C0    # convert to voltage
                        print(self.voltage)

            except:
                pass


    def live_data(self):
        ''' Allows user to view live data in a new window '''

        # Start thread
        try:
            self.t1 = threading.Thread(target=self._run)
            self.t1.start()
            print('Thread started')

        except:
            print('Thread NOT started')


class Ui_MainWindow(object):
    def __init__(self):
        super(Ui_MainWindow,self).__init__()
        self.sess = DataQ_DI145()

        # # Start Thread
        # self.t2 = threading.Thread(target=self.sess._run)
        # self.t2.start()

    def scanClicked(self):
        self.sess.scan()    # Start scan

        # Start thread
        # try:
        #     self.t2 = threading.Thread(target=self.sess._run)
        #     self.t2.start()
        #     print('Thread started')
        # except:
        #     print('Thread NOT started')

    def stopClicked(self):
        self.sess.sts()    # Stop scan

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.VoltageLCD = QtWidgets.QLCDNumber(self.centralwidget)
        self.VoltageLCD.setGeometry(QtCore.QRect(70, 80, 191, 121))
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

        # Jon Added Section
        self.StartButton.clicked.connect(self.scanClicked)
        self.StopButton.clicked.connect(self.stopClicked)



    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.VoltageLabel.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:14pt; font-weight:600;\">Source Voltage</span></p></body></html>"))
        self.UnitVoltageLabel.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:48pt;\">V</span></p></body></html>"))
        self.DPLabel.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:14pt; font-weight:600;\">Source Dew Point</span></p></body></html>"))
        self.UnitDPLabel.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:48pt;\">degF</span></p></body></html>"))
        self.CloseButton.setText(_translate("MainWindow", "Close"))
        self.StartButton.setText(_translate("MainWindow", "Scan"))
        self.StopButton.setText(_translate("MainWindow", "Stop"))




if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
