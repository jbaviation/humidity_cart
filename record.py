''' Record.py is a file that houses all the requirements to produce a recording. '''

import pandas as pd
import numpy as np
import time, datetime, os
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

        # Set adjustable self variables
        self.recEnabled = False
        self.continuationLC = False
        self.continuationSS = False

        self.time_start = time.time()       # initialize time start
        self.time_end = self.time_start+self.record_length
        self.rdg = init_reading_number      # reading number
        self.avg_on = True                  # turn on averaging

        self.headers = ['Reading','DateTime']  # start with default headers

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
        out_df = self.convertToDataFrame()

        # If a file has already been created append data to it, otherwise create
        #  the file and write data to it
        if os.path.isfile(self.filename) or os.path.isfile(self.filename+'.csv'):  # if the file exists
            # f = open(self.filename,'a')  # open the file and append to it
            # f.write(self.df)
            out_df.to_csv(self.filename+'.csv', index=False)
        else:   # file does NOT exist, so create it and write the first point
            # f = open(self.filename,'w')  # open the file to write
            # f.write(self.df)
            out_df.to_csv(self.filename+'.csv', index=False)

        # f.close()


        # Determine the output option (start with averaged)




    def convertToDataFrame(self):
        # Create initial dataset from dataLC and dataSS
        df = pd.DataFrame(self.dataLC, columns=self.headers)


        # Determine what to do with the data based on averaging
        if self.avg_on:
            # Work with time first
            most_recent = df.DateTime.max()   # Take max date for use in averaged data
            date = most_recent.strftime('%Y-%m-%d')
            time = most_recent.strftime('%H:%M:%S.%f')

            # Prep to combine averaged data
            row_name = 'mean'
            df.loc[row_name] = df.mean(axis=0)   # Average all columns in the last row of the dataframe
            ini_cols = pd.DataFrame({'Rdg': [self.rdg], 'Date': [date], 'Time': [time]}, index=[row_name])
            out_df = pd.concat([ini_cols,df.iloc[[-1],2:]], axis=1, sort=False)
        else:
            out_df = df

        return out_df
