''' WVSS.py is a class to establish communication with the SpectraSensors WVSS-II
      RS-232 connection.
'''

import serial
import time
import sys
import threading
from PyQt5 import QtGui, QtCore

class WVSS_II(QtCore.QThread):
    # Declare signal variables for the class
    change_value = QtCore.pyqtSignal(float)  # Code based on https://www.youtube.com/watch?v=eYJTcLBQKug

    def __init__(self, comm_port='COM1'):
        ''' Initialize instance variable defaults for the WVSS_II class

        Variable Descriptions:
            comm_port - RS232 communication port of WVSS device
        '''
        super(WVSS_II, self).__init__()

        # Setup communication variables
        self.comm_port = comm_port
        self.baud_rate = 9600
        self.parity = None
        self.data_bits = 8
        self.stop_bits = 1

        # Threading variables
        self.stop_thread = True

        self.serWVSS = serial.Serial(self.comm_port, self.baud_rate)  # initiate communication with WVSS

    @QtCore.pyqtSlot()
    def run(self):
        ''' Thread to run for continuously taking data from WVSS '''

        while True:
            try:
                if self.stop_thread:
                    break

                s = self.serWVSS.read()
                [wv_ppmv,p_mbar,t_C,pp2f_cts,lasPow_cnts,pkI_cnts,
                  null_cnts,midPt_mA,amidPt_mA,p_cf,bl_cf] =
                  s.split(' ')
                self.change_value.emit(wv_ppmv)

            except:
                pass
