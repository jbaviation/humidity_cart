''''Use this program to generate all references needed to run a spectra sensor validation.'''

import ADC
import pdb


## GUI application------------------------------------------------------------------
import basic_GUI_original as gui
from PyQt5 import QtCore, QtGui, QtWidgets
import sys

class MainUiClass(QtWidgets.QMainWindow, gui.Ui_MainWindow):
    def __init__(self, parent=None):
        super(MainUiClass, self).__init__(parent)
        self.setupUi(self)

        # Initialize instance of DI-145
        self.s = ADC.DataQ_DI145()

        # Connect update activity
        self.updateButtons()

        # Initialize variables
        self.thread = None


    def scanClicked(self):
        self.s.scan()    # Start scan

        # Start thread
        try:
            ## Group of Code base on https://www.youtube.com/watch?v=eYJTcLBQKug
            self.thread = self.s
            self.thread.change_value.connect(self.updateLCD)
            self.thread.start()
            #---------------------------------------------------------------------------------
            print('Thread started')
        except:
            print('Thread NOT started')


    def stopClicked(self):
        self.s.sts()    # Stop scan

        # Stop thread
        try:
            self.thread.stop_thread = True
            self.thread.exit()
            print('Thread stopped')
        except:
            print('Could NOT stop thread')


    def updateButtons(self):
        self.StartButton.clicked.connect(self.scanClicked)
        self.StopButton.clicked.connect(self.stopClicked)

    def updateLCD(self, val):
        self.VoltageLCD.display(val)

if __name__=='__main__':
    a = QtWidgets.QApplication(sys.argv)
    app = MainUiClass()
    app.show()
    a.exec_()
