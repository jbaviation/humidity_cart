''''Use this program to generate all references needed to run a spectra sensor validation.'''

from humref import spectra_equiv
import ADC
import WVSS
import time

## GUI application------------------------------------------------------------------
from PyQt5 import QtCore, QtGui, QtWidgets
import sys, os

## For the hardware setup GUI
# The following allows you to access the auto-generated gui from pyuic5
import setup_GUI as sgui
class HardwareGUI(QtWidgets.QDialog, sgui.Ui_dialog):
    def __init__(self, parent):
        super().__init__(parent)
        self.setupUi(self)

        global comLC, comSS

        self.lineLC.setText(comLC)
        self.lineWVSS.setText(comSS)
        self.buttonBox.button(QtWidgets.QDialogButtonBox.Ok).setText('Apply')  # Change text from Ok to Apply

#----------------------------------------------------------------------------------

comLC = 'COM4'   # Default LiCor COM port
comSS = 'COM1'  # Default SS COM port

## For the main window gui
# The following allows you to access the auto-generated gui from pyuic5
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
        self.values = None    # humidity generator values
        self.valuesSS = None    # spectra values
        self.setTP()   # set initial values
        self.old_pressure = self.pressure   # in case of needing to revert
        self.old_temperature = self.temperature  # in case of needing to revert

        self.thread = None   # Humidity generator thread
        self.threadSS = None # WVSS thread

        # Put similar widgets in lists
        self.createLists()

        # Window setup information that doesn't get auto-generated by pyuic5
        self.setupImages()      # generate self images
        self.menuActions()    # generate activity from menubar
        self.addDDOptions()   # add options to dropdown boxes
        self.updateBackgroundConditions()   # set temperature and pressure based on input
        self.defaultDD()   # set default dropdowns
        self.editRadioButtons()   # grey out radio buttons before initializing
        self.genRecordButton()   # generate the record button from instance of RecordButton class

        # Change default formatting
        icon = QtGui.QIcon('icon.jpg')
        self.setWindowIcon(icon)  # set the icon in the upper left corner of window
        self.viewFormatting()   # set aestetics of the page

        # Initialize instance of DI-145 and WVSS (modified from setupGUIclicked())
        self.s = None
        self.ss = None

        # Connect update activity
        self.updateDDBoxes()
        self.updateStartStopButtons()
        self.closeProgram()

    def setupImages(self):
        # Change directory for image
        owd = os.getcwd()           # original working directory
        os.chdir(owd+'\\images')    # change directory to location of images

        # Define LED images
        self.greenLED = QtGui.QPixmap('green_led.png')
        self.amberLED = QtGui.QPixmap('amber_led.png')
        self.offLED =   QtGui.QPixmap('off_led.png')

        # Go back to original directory
        os.chdir(owd)    # change directory to original working directory

    def genRecordButton(self):
        # First generate the LED
        self.statusLED.setPixmap(self.offLED)
        self.statusLED.setScaledContents(True)

        # Connect button to new function
        self.recEnabled = False   # initiate variable that tracks if recording is enabled

# NOT SURE WHAT TO DO WITH THIS YET ------------------------------
        import record
        self.rec = record.Recording(2)   # create DUMMY instance of Recording
#-----------------------------------------------------------------

        self.recordButton.clicked.connect(self.recordButtonPress)
        self.recordStopButton.clicked.connect(self.recordStopButtonPress)

    def recordControls(self):
        '''Changes components that need to be modified when record changes state'''
        if self.rec.continuationLC:     # we are in record mode
            self.statusLED.setPixmap(self.greenLED)
        else:       # we are not in record mode
            self.statusLED.setPixmap(self.amberLED)

    def recordStopButtonPress(self):
        '''Setup record stop button capability'''
        self.statusLED.setPixmap(self.amberLED)

        self.rec.recEnabled = False          # Indicate we are in record mode

    def recordButtonPress(self):
        '''Setup record button capability'''
        self.statusLED.setPixmap(self.greenLED)

        self.rec.recEnabled = True          # Indicate we are in record mode
        self.rec.time_start = time.time()   # Track start time with button push
        self.rec.time_end = self.rec.time_start + self.rec.record_length
        print('Record Button Clicked')

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

        self.lcRbuttons = [self.StartButton, self.StopButton]
        self.ssRbuttons = [self.WVSSstartButton, self.WVSSstopButton]

        self.all_labels = self.lcLabels + self.ssLabels
        self.all_LCDs = self.LCDs + self.LCDss
        self.all_Rbuttons = self.lcRbuttons + self.ssRbuttons

    def menuActions(self):
        self.menuFile.addAction('Exit', self.close).setShortcut('Ctrl+X')  # add option for exiting program from menubar
        self.menuHardware.triggered.connect(self.setupGUIclicked)

        # Set shortcuts
        self.menuHardware.setShortcut('Ctrl+P')
        self.menuRecording.setShortcut('Ctrl+R')
        self.menuRecord.setShortcut('Ctrl+A')

    def setupGUIclicked(self):
        ''' Control content from setup_GUI by attempting to initiate instances
            of the LiCor and SpectraSensor'''
        global comLC, comSS
        dlg = HardwareGUI(self)
        dlg.buttonBox.accepted.connect(dlg.accept)
        dlg.buttonBox.rejected.connect(dlg.reject)

        # The following executes the dialog box and returns whether it was
        # accepted or rejected
        result = dlg.exec_()
        if result == QtWidgets.QDialog.Accepted:
            '''Try to accept the changes and initialize COM ports.  If unsuccessful,
               show a message box that request cannot be completed'''
            active = False
            try:
                comLC = dlg.lineLC.text()
                self.s = ADC.DataQ_DI145(comLC)
                active = True    # Triggers to activate record button if one is true
                for button in self.lcRbuttons:
                    button.setEnabled(True)
            except:
                msg = self._error_msg()
                msg.setText('Could NOT initialize DataQ DI-145 from port {}'.format(comLC))
                msg.exec_()

            try:
                comSS = dlg.lineWVSS.text()
                self.ss = WVSS.WVSS_II(comSS)
                active = True    # Triggers to activate record button if one is true
                for button in self.ssRbuttons:
                    button.setEnabled(True)
            except:
                msg = self._error_msg()
                msg.setText('Could NOT initialize Water Vapor Monitor System from port {}'.format(comSS))
                msg.exec_()

            # Modify record button if one of the devices is setup correctly
            if active:
                self.recordButton.setEnabled(True)
                self.recordButton.setToolTip('Press this button to trigger a recording')

            else:
                self.recordButton.setEnabled(False)
                self.recordButton.setToolTip('You are no longer connected to a device ' +
                                'press Ctrl+H to configure devices before recording data')

    def viewFormatting(self):
        # Set tooltips
        self.StartButton.setToolTip('Start scanning the humidity generator')
        self.StopButton.setToolTip('Stop scanning the humidity generator')
        self.WVSSstartButton.setToolTip('Start scanning the WVSS')
        self.WVSSstopButton.setToolTip('Stop scanning the WVSS')
        self.SetConditionsButton.setToolTip('Conditions entered above are applied')

        # Change theme

        # Change label colors
        for label in self.all_labels:
            label.setStyleSheet('color: black')

        # Change LCD colors
        for lcd in self.all_LCDs:
            lcd.setStyleSheet('''QLCDNumber {
                                        background-color: black;
                                        color: white; }''')

        # Record button
        self.recordButton.setEnabled(False)
        self.recordButton.setToolTip('Press Ctrl+H to configure devices before recording data')

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
        txtmsg = "Can't establish a connection with the humidity generator, " + \
        "you may need to unplug and then replug in the DataQ DI-145 then press 'Ctrl+H' to " + \
        "reconfigure COM port."

        try:
            self.s.scan()    # Start scan

            # Start thread
            ## Group of Code base on https://www.youtube.com/watch?v=eYJTcLBQKug
            self.thread = self.s
            self.thread.change_value.connect(self.updateLCD)
            # [self.thread.change_value.connect(x) for x in [self.updateLCD, self.captureDataLC]]  # Connect to multiple slots
            self.thread.heartbeat.connect(self.indicateScan)
            self.thread.start()
            #---------------------------------------------------------------------------------
        except:
            # This means that we've lost comms with device
            msg = self._error_msg()
            msg.setText(txtmsg)
            msg.exec_()

    def stopClicked(self):
        txtmsg = "Can't establish a connection with the humidity generator, " + \
        "you may need to unplug and then replug in the DataQ DI-145 then press 'Ctrl+H' to " + \
        "reconfigure COM port."

        try:
            # Try to stop scan
            self.s.sts()    # Stop scan
            self.thread.stop_thread = True
            self.thread.exit()
        except:
            # This means that we've lost comms with device
            msg = self._error_msg()
            msg.setText(txtmsg)
            msg.exec_()

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

        # Check pressure
        if 0 < checkP <= 50:
            self.pressure = checkP
        else:
            self.pressure = self.old_pressure
            self.PressureEdit.setText(str(self.pressure))

            msg = self._error_msg()
            msg.setText('{} psia is NOT in the range 0-50 psia'.format(checkP))
            msg.exec_()

        # Check temperature
        if -200 <= checkT <= 200:
            self.temperature = checkT
        else:
            self.temperature = self.old_temperature
            self.TemperatureEdit.setText(str(self.temperature))

            msg = self._error_msg()
            msg.setText('{} °F is NOT in the range -200-200 °F'.format(checkT))
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
        elif text == 'Water Vapor Concentration':
            unit.setText('H2Oppmv')
        elif text == 'Gamma':
            unit.setText('')
        elif text == 'Air Density':
            unit.setText('lbm/ft\N{SUPERSCRIPT THREE}')

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
        self.values = [TddegF, mmr, rh, counts, voltage, ppmv, gam, rho]

        # Push data to recording
        self.rec.captureDataLC(self.values)
        self.recordControls()

        # Set each LCD to the respective value based on combobox selection
        self.box_loop(self.LCDs, self.values)


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
        self.valuesSS = [TddegF, mmr, rh, counts, voltage, ppmv, gam, rho]

        # Set each LCD to the respective value based on combobox selection
        self.box_loop(self.LCDss, self.valuesSS)

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

    def editRadioButtons(self):
        for Rbutton in self.all_Rbuttons:
            Rbutton.setEnabled(False)   # Default disable radio buttons

    def closeProgram(self):
        # self.CloseButton.clicked.connect(QtWidgets.QApplication.instance().quit)  # close program with button
        self.CloseButton.clicked.connect(QtWidgets.qApp.quit)  # close program with button

    def _error_msg(self):
        msg = QtWidgets.QMessageBox()
        msg.setIcon(QtWidgets.QMessageBox.Critical)
        msg.setWindowTitle('Error')
        return msg


# This class is used more of a demostration to show how to configure classes which
# instances are children of the MainWindow
class RecordButton(QtWidgets.QPushButton):
    def __init__(self, text, parent):
        super().__init__(text, parent=parent)
        self.setAutoFillBackground(True)

    def _set_color(self, col):
        palette = self.palette()
        palette.setColor(self.backgroundRole(), col)
        self.setPalette(palette)

    color = QtCore.pyqtProperty(QtGui.QColor, fset=_set_color)


if __name__=='__main__':
    a = QtWidgets.QApplication(sys.argv)
    a.setStyle('windowsvista')

    app = MainUiClass()
    app.show()
    sys.exit(a.exec_())
