''' Record.py is a file that houses all the requirements to produce a recording. '''

import pandas as pd
import numpy as np
import time
from PyQt5 import QtGui, QtCore



class Recording:
    # Declare signal variables for the class

    def __init__(self, record_length, init_reading_number=1):
        super(Recording, self).__init__()
        '''Set input variables based on inputs
            record_length = length in seconds of each recording
            init_reading_number = starting reading number'''
        self.record_length = record_length

        # Set adjustable self variables
        self.recEnabled = False
        self.continuationLC = False
        self.continuationSS = False

        self.time_start = time.time()       # initialize time start
        self.time_end = self.time_start+self.record_length
        self.rdg = init_reading_number      # reading number


    def convertToDataFrame(self):
        pass

    def captureDataLC(self, values):
        '''Captures data for the humidity generator.'''
        # Copy the values so that we don't modify the original list
        vals = values.copy()

        # Track reading number

        # Humidity Generator Data ------------------------------------------
        # Indicate if recording is enabled and if this is a continuation
        if self.recEnabled and time.time()<=self.time_end:
            if self.continuationLC:
                # This is a continuation so we must append the data to the list
                # [TddegF, mmr, rh, counts, voltage, ppmv, gam, rho]
                self.dataLC.append(vals.insert(0,time.localtime()))
            else:
                # This is the first point to record, so we must create the new variable to store data
                self.dataLC = []   # reinitialize to clear data from previous recording
                self.dataLC.append(vals.insert(0,time.localtime()))

                # Turn ON continuation mode
                self.continuationLC = True

        else:   #  we are not in record mode
            if self.continuationLC:  # we just came out of a record
                print('Recording Captured')
                print('Data Length = {} rows in {} seconds'.format(len(self.dataLC), time.time()-self.time_start))

            self.continuationLC = False  # turn off continuation



        # Spectra Sensor Data ------------------------------------------
