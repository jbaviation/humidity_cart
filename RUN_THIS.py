''''Use this program to generate all references needed to run a spectra sensor validation.'''

from humref import spectra_equiv
import ADC
import WVSS

## GUI application------------------------------------------------------------------
from PyQt5 import QtCore, QtGui, QtWidgets
import sys


## The following allows you to access the auto-generated gui from pyuic5
import basic_GUI as gui
class MainUiClass(QtWidgets.QMainWindow, gui.Ui_MainWindow):
    def __init__(self, parent=None):
        # super(MainUiClass, self).__init__(parent)
        super().__init__(parent)
        self.setupUi(self)
#----------------------------------------------------------------------------------

        # Initialize variables
        self.pressure = None  # psi, reference static pressure (set to SL press for now)
        self.temperature = None   # degF, reference static temperature
        self.setTP()   # set initial values
        self.old_pressure = self.pressure   # in case of needing to revert
        self.old_temperature = self.temperature  # in case of needing to revert

        self.thread = None   # Humidity generator thread
        self.threadSS = None # WVSS thread

        # Put similar widgets in lists
        self.createLists()

        # Window setup information that doesn't get auto-generated by pyuic5
        self.menuFile.addAction('Exit', self.close)  # add option for exiting program from menubar
        self.addDDOptions()   # add options to dropdown boxes
        self.updateBackgroundConditions()   # set temperature and pressure based on input
        self.defaultDD()   # set default dropdowns

        # Change default formatting
        icon = QtGui.QIcon('icon.jpg')
        self.setWindowIcon(icon)  # set the icon in the upper left corner of window
        self.viewFormatting()   # set aestetics of the page

        # Initialize instance of DI-145 and WVSS
        self.s = None
        self.initializeLC()
        self.ss = None
        self.initializeWVSS()

        # Connect update activity
        self.updateDDBoxes()
        self.updateStartStopButtons()
        self.closeProgram()

    def createLists(self):
        self.DDitems = ['Dew Point','Mass Mixing Ratio','Relative Humidity','Water Vapor Concentration',\
          'Gamma','Air Density','Counts','Voltage']
        self.boxes = [self.HumGenDDbox1, self.HumGenDDbox2, self.HumGenDDbox3]

        self.units = [self.HumGenUnits1, self.HumGenUnits2, self.HumGenUnits3]
        self.LCDs = [self.HumGenLCD1, self.HumGenLCD2, self.HumGenLCD3]

        self.unitss = [self.WVSSUnits1, self.WVSSUnits2, self.WVSSUnits3]
        self.LCDss = [self.WVSSLCD1, self.WVSSLCD2, self.WVSSLCD3]

        self.lcLabels = [self.lcLabel1, self.lcLabel2, self.lcLabel3]
        self.ssLabels = [self.ssLabel1, self.ssLabel2, self.ssLabel3]

        self.all_labels = self.lcLabels + self.ssLabels
        self.all_LCDs = self.LCDs + self.LCDss

    def initializeLC(self):
        self.s = ADC.DataQ_DI145()
        pass

    def initializeWVSS(self):
        self.ss = WVSS.WVSS_II()
        pass

    def viewFormatting(self):
        # Change label colors
        for label in self.all_labels:
            label.setStyleSheet('color: black')

        # Change LCD colors
        for lcd in self.all_LCDs:
            lcd.setStyleSheet('''QLCDNumber {
                                        background-color: black;
                                        color: white; }''')

    def addDDOptions(self):
        ''' Add all options to all dropdown boxes'''
        for box in self.boxes:
            box.addItems(self.DDitems)

    def defaultDD(self):
        ''' Set default selections for dropdown menus '''
        self.HumGenDDbox1.setCurrentIndex(1)  # box1 = MMR
        self.HumGenDDbox2.setCurrentIndex(0)  # box2 = dew point
        self.HumGenDDbox3.setCurrentIndex(2)  # box3 = relative humidity

        # Update the units for each label
        for box, unit, units in zip(self.boxes, self.units, self.unitss):
            self.updateUnits(box.currentText(), unit)
            self.updateUnits(box.currentText(), units)

    def SScanClicked(self):   # Start wvss scan
        try:
            self.threadSS = self.ss
            self.threadSS.change_value.connect(self.updateLCDss)
            self.threadSS.heartbeat.connect(self.indicateScan)
            self.threadSS.start()
            print('WVSS thread started')
        except:
            print('WVSS thread NOT started')

    def SStopClicked(self):   # Stop wvss scan
        try:
            self.threadSS.stop_thread = True
            self.threadSS.exit()
            print('WVSS thread stopped')
        except:
            print('WVSS thread could NOT be stopped')

    def scanClicked(self):
        self.s.scan()    # Start scan

        # Start thread
        try:
            ## Group of Code base on https://www.youtube.com/watch?v=eYJTcLBQKug
            self.thread = self.s
            self.thread.change_value.connect(self.updateLCD)
            self.thread.heartbeat.connect(self.indicateScan)
            self.thread.start()
            #---------------------------------------------------------------------------------
            print('LiCor thread started')
        except:
            print('LiCor thread NOT started')

    def stopClicked(self):
        self.s.sts()    # Stop scan

        # Stop thread
        try:
            self.thread.stop_thread = True
            self.thread.exit()
            print('LiCor thread stopped')
        except:
            print('LiCor thread could NOT be stopped')

    def indicateScan(self, yes_no):
        ''' Connected to heartbeat to tell if we are communicating with devices.'''
        # LiCor Heartbeat
        if yes_no == 'yesLC':
            # Change label colors
            for label in self.lcLabels:
                label.setStyleSheet('color: green')

            # Change LCD colors
            for lcd in self.LCDs:
                lcd.setStyleSheet('''QLCDNumber {
                                            background-color: black;
                                            color: green; }''')
        elif yes_no == 'noLC':
            # Change label colors
            for label in self.lcLabels:
                label.setStyleSheet('color: red')

            # Change LCD colors
            for lcd in self.LCDs:
                lcd.setStyleSheet('''QLCDNumber {
                                            background-color: black;
                                            color: red; }''')
        # Spectra Heartbeat
        elif yes_no == 'yesSS':
            # Change label colors
            for label in self.ssLabels:
                label.setStyleSheet('color: green')

            # Change LCD colors
            for lcd in self.LCDss:
                lcd.setStyleSheet('''QLCDNumber {
                                            background-color: black;
                                            color: green; }''')
        elif yes_no == 'noSS':
            # Change label colors
            for label in self.ssLabels:
                label.setStyleSheet('color: red')

            # Change LCD colors
            for lcd in self.LCDss:
                lcd.setStyleSheet('''QLCDNumber {
                                            background-color: black;
                                            color: red; }''')
        else:
            print('WARNING: heartbeat unable to determine state of a device')



    def setTP(self):
        checkP = float(self.PressureEdit.text())
        checkT = float(self.TemperatureEdit.text())

        def error_msg():
            msg = QtWidgets.QMessageBox()
            msg.setIcon(QtWidgets.QMessageBox.Critical)
            msg.setText('Error')
            msg.setWindowTitle('Error')
            return msg


        # Check pressure
        if 0 < checkP <= 50:
            self.pressure = checkP
        else:
            self.pressure = self.old_pressure
            self.PressureEdit.setText(str(self.pressure))

            msg = error_msg()
            msg.setInformativeText('{} psia is NOT in the range 0-50 psia'.format(checkP))
            msg.exec_()

        # Check temperature
        if -200 <= checkT <= 200:
            self.temperature = checkT
        else:
            self.temperature = self.old_temperature
            self.TemperatureEdit.setText(str(self.temperature))

            msg = error_msg()
            msg.setInformativeText('{} °F is NOT in the range -200-200 °F'.format(checkT))
            msg.exec_()

        self.old_pressure = self.pressure
        self.old_temperature = self.temperature

    def updateBackgroundConditions(self):
        self.SetConditionsButton.clicked.connect(self.setTP)

    def updateStartStopButtons(self):
        self.StartButton.clicked.connect(self.scanClicked)
        self.StopButton.clicked.connect(self.stopClicked)

        self.WVSSstartButton.clicked.connect(self.SScanClicked)
        self.WVSSstopButton.clicked.connect(self.SStopClicked)

    def updateDDBoxes(self):
        for box, unit, units in zip(self.boxes, self.units, self.unitss):
            box.activated[str].connect(
               lambda text, unit=unit: self.updateUnits(text, unit))
            box.activated[str].connect(
               lambda text, units=units: self.updateUnits(text, units))

    def updateUnits(self, text, unit):
        unit.setFont(QtGui.QFont('Arial', 20))
        if text == 'Dew Point':
            unit.setText('°F')
        elif text == 'Mass Mixing Ratio':
            unit.setText('kgH2O/kgAir')
        elif text == 'Relative Humidity':
            unit.setText('%')
        elif text == 'Counts':
            unit.setText('')
        elif text == 'Voltage':
            unit.setText('V')
        elif text == 'PPMv':
            unit.setText('H2Oppmv')

    def updateLCD(self, counts):
        # Calculate various atmospheric conditions
        voltage = 0.0003*counts
        TddegC = voltage*10
        TddegF = TddegC*1.8 + 32
        TK = (self.temperature-32)*5/9 + 273.15
        TdK = TddegC + 273.15
        pPa = self.pressure / (spectra_equiv.KPA2PSI/1000)
        mmr = spectra_equiv.humidity_ratio(TK, TdK, pPa)
        rh = spectra_equiv.relative_humidity2(TK, TdK, pPa)*100
        ppmv = spectra_equiv.mole_ratio(mmr)
        gam = spectra_equiv.gamma(self.temperature, self.pressure, mmr)
        rho = spectra_equiv.density(self.temperature, self.pressure, mmr)

        # Combine the calculated values
        values = [TddegF, mmr, rh, counts, voltage, ppmv, gam, rho]

        # Set each LCD to the respective value based on combobox selection
        self.box_loop(self.LCDs, values)

    def updateLCDss(self, raw_string):
        # Convert raw_string to list of values
        vals = WVSS.parse_string(raw_string)
        voltage = 9999.0
        counts = vals[3]
        ppmv = vals[0]
        mmr = spectra_equiv.humidity_ratio2(ppmv)
        TddegF = spectra_equiv.dew_point(mmr, self.pressure)
        rh = spectra_equiv.relative_humidity1(self.temperature, mmr, self.pressure)*100
        gam = spectra_equiv.gamma(self.temperature, self.pressure, mmr)
        rho = spectra_equiv.density(self.temperature, self.pressure, mmr)

        # Combine the calculated values
        values = [TddegF, mmr, rh, counts, voltage, ppmv, gam, rho]

        # Set each LCD to the respective value based on combobox selection
        self.box_loop(self.LCDss, values)

    def box_loop(self, LCDS, values):
        for lcd, box in zip(LCDS, self.boxes):
            box_val = str(box.currentText())
            if box_val == 'Dew Point':
                lcd.display('{:.2f}'.format(round(values[0], 2)))
            elif box_val == 'Mass Mixing Ratio':  # Mass mixing ratio
                lcd.display('{:.5f}'.format(round(values[1], 5)))
            elif box_val == 'Relative Humidity':  # Relative humidity
                lcd.display('{:.2f}'.format(round(values[2], 2)))
            elif box_val == 'Counts':  # Counts
                lcd.display('{0:d}'.format(int(values[3])))
            elif box_val == 'Voltage':  # Voltage
                lcd.display('{:.3f}'.format(round(values[4], 3)))
            elif box_val == 'Water Vapor Concentration':
                lcd.display('{:.1f}'.format(round(values[5], 1)))
            elif box_val == 'Gamma':
                lcd.display('{:.3f}'.format(round(values[6], 3)))
            elif box_val == 'Air Density':
                lcd.display('{:.4f}'.format(round(values[7], 4)))

    def closeProgram(self):
        # self.CloseButton.clicked.connect(QtWidgets.QApplication.instance().quit)  # close program with button
        self.CloseButton.clicked.connect(QtWidgets.qApp.quit)  # close program with button



if __name__=='__main__':
    a = QtWidgets.QApplication(sys.argv)
    app = MainUiClass()
    app.show()
    sys.exit(a.exec_())
