''''Use this program to generate all references needed to run a spectra sensor validation.'''

import ADC
import pdb


## GUI application------------------------------------------------------------------
from PyQt5 import QtCore, QtGui, QtWidgets
import sys


## The following allows you to access the auto-generated gui from pyuic5
import basic_GUI as gui
class MainUiClass(QtWidgets.QMainWindow, gui.Ui_MainWindow):
    def __init__(self, parent=None):
        super(MainUiClass, self).__init__(parent)
        self.setupUi(self)
#----------------------------------------------------------------------------------

        # Initialize variables
        self.element = None
        self.box = None
        self.unit = None
        self.thread = None
        self.DDitems = ['Dew Point','Mass Mixing Ratio','Relative Humidity','Counts','Voltage']
        self.boxes = [self.HumGenDDbox1, self.HumGenDDbox2, self.HumGenDDbox3]
        self.units = [self.HumGenUnits1, self.HumGenUnits2, self.HumGenUnits3]

        # Window setup information that doesn't get auto-generated by pyuic5
        icon = QtGui.QIcon('icon.jpg')
        self.setWindowIcon(icon)  # set the icon in the upper left corner of window
        self.addDDOptions()   # add options to dropdown boxes

        # Initialize instance of DI-145
        self.s = ADC.DataQ_DI145()

        # Connect update activity
        self.updateHumGenButtons()
        self.updateDDBoxes()


    def addDDOptions(self):
        for box in self.boxes:
            box.addItems(self.DDitems)

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

    def updateHumGenButtons(self):
        self.StartButton.clicked.connect(self.scanClicked)
        self.StopButton.clicked.connect(self.stopClicked)

    def updateDDBoxes(self):
        for self.box, self.unit in zip(self.boxes, self.units):
            self.box.activated[str].connect(self.updateUnits)

    def updateUnits(self, text):
        if text == 'Dew Point':
            self.unit.setText('°F')
        elif text == 'Mass Mixing Ratio':
            self.unit.setText('kgH2O/kgAir')



    def updateLCD(self, volts):
        # self.VoltageLCD.display('{:.3f}'.format(round(volts, 3)))
        # TDdegC = volts*10
        # TDdegF = TDdegC*1.8 + 32
        # self.DPLCD.display('{:.2f}'.format(round(TDdegF, 2)))
        pass



if __name__=='__main__':
    a = QtWidgets.QApplication(sys.argv)
    app = MainUiClass()
    app.show()
    a.exec_()
