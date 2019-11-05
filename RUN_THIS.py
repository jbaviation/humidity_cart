''''Use this program to generate all references needed to run a spectra sensor validation.'''

import ADC
import pdb




## Basic console scanning application-------------------------------------------
# import time
# try:
#     s = ADC.DataQ_DI145(comm_port='COM4')
#     s.scan()
#     s.live_data()
# except:
#     pass
#
# ADC._Gui().run()
#
#
#
# time.sleep(2)
# s.sts()
## End basic console scanning application-------------------------------------------

## GUI application------------------------------------------------------------------
import basic_GUI_original as gui
from PyQt5 import QtCore, QtGui, QtWidgets
import sys

class MainUiClass(QtWidgets.QMainWindow, gui.Ui_MainWindow):
    sig_start = QtCore.pyqtSignal()   # initialize signal

    def __init__(self, parent=None):
        super(MainUiClass, self).__init__(parent)
        self.setupUi(self)

        # Initialize instance of DI-145
        self.s = ADC.DataQ_DI145()

        # Connect update activity
        self.updateButtons()

        # Initialize variables
        self.th_1 = None   # Thread 1


    def scanClicked(self):
        self.s.scan()    # Start scan

        # Start thread
        try:
            self.th_1 = QtCore.QThread(target=self.s._run)
            self.th_1.start()
            print('Thread started')
        except:
            print('Thread NOT started')

    def stopClicked(self):
        self.s.sts()    # Stop scan

        # Stop thread
        try:
            self.s.stop_thread = True
            self.th_1.exit()
            print('Thread stopped')
        except:
            print('Could NOT stop thread')



    def updateButtons(self):
        self.StartButton.clicked.connect(self.scanClicked)
        self.StopButton.clicked.connect(self.stopClicked)



if __name__=='__main__':
    a = QtWidgets.QApplication(sys.argv)
    app = MainUiClass()
    app.show()
    a.exec_()
