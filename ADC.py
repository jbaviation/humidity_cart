''' ADC.py is a class to establish communication with DataQ Instruments DI-145
        for more information on the DI-145 communication protocol goto:
        https://www.dataq.com/resources/installations/web-help/sdk/Content/Function%20Reference/di_open.htm
'''
import serial
import time
import sys
import threading
from PyQt5 import QtGui, QtCore


class DataQ_DI145(QtCore.QThread):  # added inheritance from QThread for signals
    # Declare signal variables for the class
    change_value = QtCore.pyqtSignal(float)   # Code based on https://www.youtube.com/watch?v=eYJTcLBQKug

    def __init__(self, comm_port='COM5', baud_rate=4800):
        ''' Initialize instance variable defaults for the DataQ_DI145 class

        Variable Descriptions:
            comm_port - USB communication port of ADC device (default: COM4 on 17021058 Machine)
            baud_rate - baud rate of the device (default: 4800 for DI145)
            C1 - Slope coefficient of counts vs Volts (default: 0.0003 for nominal conversion)
            C0 - Offset coefficient of counts vs Volts (default: 0.0 for nominal conversion)
        '''
        super(DataQ_DI145, self).__init__()   # Code based on https://www.youtube.com/watch?v=ivcxZSHL7jM

        self.comm_port = comm_port
        self.baud_rate = baud_rate

        # Cancel any threading that may be taking place already
        self.stop_thread = True
        self.t1 = None    # initialize class variable

        # Declare instance variables
        self.counts = None

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
            print('Scan stopped')
        except:
            print('Could NOT stop scan the device...try re-initializing')

    @QtCore.pyqtSlot()
    def run(self):
        ''' Meant to run as a thread for taking voltage and counts from the ADC device'''
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
                        # self.voltage = self.C1*self.counts + self.C0    # convert to voltage

                        ## Code based on https://www.youtube.com/watch?v=eYJTcLBQKug
                        self.change_value.emit(self.counts)
                        #---------------------------------------------------------------------------------


            except:
                pass
