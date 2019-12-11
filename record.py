''' Record.py is a file that houses all the requirements to produce a recording. '''

import pandas as pd
import numpy as np
import time, datetime, os
import common_def
from PyQt5 import QtGui, QtCore



class Recording:
    date = time.strftime('%Y%m%d')
    def __init__(self, record_length=2, filename='humidity_cart_{}'.format(date),\
                  init_reading_number=1):
        super(Recording, self).__init__()
        '''Set input variables based on inputs
            record_length = length in seconds of each recording
            filename = name of the file to be output
            init_reading_number = starting reading number'''
        self.record_length = record_length
        self.filename = filename
        self.filename_ext = filename+'.csv'

        # Set adjustable self variables
        self.recEnabled = False
        self.continuationLC = False
        self.continuationSS = False

        self.time_start = time.time()       # initialize time start
        self.time_end = self.time_start+self.record_length
        self.avg_on = True                  # turn on averaging
        self.rdg = init_reading_number      # initialized reading number
        self._check_for_latest_reading()     # pull in reading from existing file (if exists)


        self.headers = ['Reading','DateTime']  # start with default headers

    def _check_for_latest_reading(self):
        if os.path.isfile(self.filename_ext):
            rdg_from_file = int(pd.read_csv(self.filename_ext, usecols=['Reading']).max())
            self.rdg = rdg_from_file+1

    def captureDataSS(self, values):
        pass

    def captureDataLC(self, values):
        '''Captures data for the humidity generator.'''
        # Copy the values so that we don't modify the original list
        vals = values.copy()

        # Humidity Generator Data ------------------------------------------
        # Indicate if recording is enabled and if this is a continuation
        if self.recEnabled and time.time()<=self.time_end:
            # Insert reading num and time into dataset
            vals.insert(0,datetime.datetime.now())
            vals.insert(0,self.rdg)

            if self.continuationLC:
                pass   # This is a continuation so we must append the data to the list

            else:
                # This is the first point to record, so we must create the new variable to store data
                self.dataLC = []   # reinitialize to clear data from previous recording

                # Turn ON continuation mode
                self.continuationLC = True

            self.dataLC.append(vals)


        else:   #  we are not in record mode
            if self.continuationLC:  # we just came out of a record
                # Notate info about recording
                print('Recording Captured')
                print('Data Length = {} rows in {} seconds'.format(len(self.dataLC), time.time()-self.time_start))

                # Go to interpret output function
                self.interpretOutput()

                # Get ready for next recording
                self.rdg += 1  # increment reading number

            self.continuationLC = False  # turn off continuation

    def interpretOutput(self):
        '''After reading has been captured, this method evaluates what to do with it.'''
        # Convert to dataframe
        out_df = self.convertToDataFrame(self.dataLC)

        # If a file has already been created append data to it, otherwise create
        #  the file and write data to it
        if os.path.isfile(self.filename_ext):  # if the file exists append data (mode='a')
            out_df.to_csv(self.filename_ext, mode='a', index=False, header=False)

            # try:  # to append data
            #     out_df.to_csv(self.filename_ext, mode='a', index=False, header=False)
            # except:  # file is open cannot write so throw an error
            #     msg = common_def.error_msg()
            #     msg.setText('DATA NOT WRITTEN TO FILE:\n\n{} is open; '.format(self.filename) + \
            #                 'please close the file before continuing')
            #     msg.exec_()
        else:   # file does NOT exist, so create it and write the first point with header
            out_df.to_csv(self.filename_ext, mode='w', index=False, header=True)

        # f.close()


        # Determine the output option (start with averaged)




    def convertToDataFrame(self, dataArray):
        # Create initial dataset from dataLC and dataSS
        df = pd.DataFrame(dataArray, columns=self.headers)


        # Determine what to do with the data based on averaging
        if self.avg_on:
            # Work with time first
            most_recent = df.DateTime.max()   # Take max date for use in averaged data
            date = most_recent.strftime('%Y-%m-%d')
            time = most_recent.strftime('%H:%M:%S.%f')

            # Prep to combine averaged data
            row_name = 'mean'
            df.loc[row_name] = df.mean(axis=0)   # Average all columns in the last row of the dataframe
            ini_cols = pd.DataFrame({'Reading': [self.rdg], 'Date': [date], 'Time': [time]}, index=[row_name])  # Initial (fixed) columns
            sel_cols = df.iloc[[-1],2:]   # Last row and Columns that were selected by the user
            out_df = pd.concat([ini_cols,sel_cols], axis=1, sort=False)
        else:
            out_df = df

        return out_df
