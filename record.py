''' Record.py is a file that houses all the requirements to produce a recording. '''

import pandas as pd
import numpy as np
from PyQt5 import QtGui, QtCore



class Recording(QtCore.QThread):   # added inheritance from QThread for signals
    # Declare signal variables for the class

    def __init__(self, record_length):
        super(Recording, self).__init__()   # insure all inherited variables are included with self
        '''Set input variables based on inputs
            record_length = length in seconds of each recording'''
        self.record_length = record_length

    @pyqtSlot()
    def run(self):
        '''Runs as a thread to capture live data into a recording.'''
        pass
