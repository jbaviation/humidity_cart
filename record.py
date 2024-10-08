''' Record.py is a file that houses all the requirements to produce a recording. '''

import pandas as pd
import numpy as np
import time, datetime, os
import common_def
from pathlib import Path
from PyQt5 import QtGui, QtCore
from PyQt5.QtWidgets import QMessageBox
import xlwings as xw


class Recording:
    date = time.strftime('%Y%m%d')
    def __init__(
        self, 
        record_length=10, 
        filename='humidity_cart_{}.xlsx'.format(date),
        fileloc=os.getcwd(),
        init_reading_number=1, 
        headers=[]
    ):
        super(Recording, self).__init__()
        '''Set input variables based on inputs
            record_length = length in seconds of each recording
            filename = name of the file to be output
            init_reading_number = starting reading number'''
        iheaders = ['Reading','Date','Time','Recording Length','Total Air Pressure']  # start with initial headers
        self.headers = iheaders + headers
        self.record_length = record_length
        self.filename = filename
        self.fileLoc = fileloc
        self.getFullFile()
        self.connectWorkbook()

        # Set adjustable self variables
        self.recEnabled = False
        self.continuationLC = False
        self.continuationSS = False

        self.time_start = time.time()       # initialize time start
        self.time_end = self.time_start+self.record_length
        self.avg_on = True                  # turn on averaging

    def getFullFile(self):
        # Encourage the use of .xls[x]
        if '.xls' not in self.filename.lower():
            date = time.strftime('%Y%m%d')

            msg = common_def.error_msg()
            msg.setWindowTitle("FILE NAME ERROR")
            msg.setText("Please insure that the desired filename has a .xls or .xlsx extension. Setting " +
                "filename and path to default.")
            msg.exec_()

            self.full_filename = Path(self.fileLoc) / 'humidity_cart_{}.xlsx'.format(date)
        else:
            # Combine all necessary elements of filename into full_filename
            self.full_filename = Path(self.fileLoc) / self.filename

    def connectWorkbook(self):
        # Establish a connection to the workbook, set header (if applicable), and set reading number
        if os.path.isfile(self.full_filename):
            # Connect to existing workbook
            self.wb = xw.Book(self.full_filename)
            self.sht = self.wb.sheets[0]

            # Get latest reading
            try:
                self.rdg = int(self.sht.used_range.value[-1][0])
            except:
                # Handle exception where only headers exist with no reading number
                msg = common_def.error_msg()
                msg.setWindowTitle("NO DATA DETECTED!")
                msg.setText("The requested output file already exists but no data recordings were " +
                    "detected in the file. Confirm this is correct, otherwise data can be mislabeled " +
                    "or overwritten."
                )
                msg.exec_()
                self.rdg = 0

        else:
            # Start a new workbook and set header
            self.wb = xw.Book()
            self.sht = self.wb.sheets[0]
            self.sht["A1"].value = [self.headers]

            # Set reading to 1
            self.rdg = 0

            # Save new workbook
            self.save_data()

    def save_data(self, max_attempts=5, wait_between=1):
        # Easy way to quickly save newly written data
        for n in range(max_attempts):
            try:
                self.wb.save(self.full_filename)
                print("Workbook saved!")
                return
            except:
                print("Failed attempt to save ({}). Retrying after {} seconds.".format(n, wait_between))
                time.sleep(wait_between)
                continue

        msg = common_def.error_msg()
        msg.setText('Failed to autosave the Spreadsheet after {} attempts. '.format(max_attempts) + 
            'Consider manually saving to avoid losing work.')
        msg.exec_()

    def captureDataSS(self, values):
        '''Captures data for the spectra sensor.'''
        # Copy the values so that we don't modify the original list
        vals = values.copy()

        # Spectra Sensor Data ------------------------------------------
        # Indicate if recording is enabled and if this is a continuation
        if self.recEnabled and time.time()<=self.time_end:
            # Insert reading num and time into dataset
            vals.insert(0,datetime.datetime.now())
            vals.insert(0,self.rdg)

            if self.continuationSS:
                pass   # This is a continuation so we must append the data to the list

            else:
                # This is the first point to record, so we must create the new variable to store data
                self.dataSS = []   # reinitialize to clear data from previous recording

                # Turn ON continuation mode
                self.continuationSS = True

            self.dataSS.append(vals)


        else:   #  we are not in record mode
            if self.continuationSS:  # we just came out of a record
                self.continuationSS = False   # Force out of continuation

                # Go to interpret output function
                try:
                    self.interpretOutput(self.dataSS, 'WVSS')

                    # Notate info about recording
                    print('WVSS Recording Captured')
                    print('WVSS Data Length = {} rows in {} seconds'.format(len(self.dataSS), time.time()-self.time_start))

                except:  # file is open cannot write so throw an error
                    msg = common_def.error_msg()
                    msg.setText('Data recording error, this recording was not captured in the Spreadsheet. ' + 
                        'Please contact developer!')
                    msg.exec_()

                # Attempt to save
                self.save_data()
            self.continuationSS = False  # turn off continuation

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
                self.continuationLC = False   # Force out of continuation

                # Go to interpret output function
                try:
                    self.interpretOutput(self.dataLC, 'HumGen')

                    # Notate info about recording
                    print('HumGen Recording Captured')
                    print('HumGen Data Length = {} rows in {} seconds'.format(len(self.dataLC), time.time()-self.time_start))

                except:  # file is open cannot write so throw an error
                    msg = common_def.error_msg()
                    msg.setText('Data recording error, this recording was not captured in the Spreadsheet. ' + 
                        'Please contact developer!')
                    msg.exec_()

                # Attempt to save
                self.save_data()
            self.continuationLC = False  # turn off continuation

    def interpretOutput(self, data, src):
        '''After reading has been captured, this method evaluates what to do with it.'''
        out_df = self.insertDataToWorkbook(data, src)

    def insertDataToWorkbook(self, dataArray, src):
        # Create initial dataset from dataLC and dataSS
        dataArray_columns = [
            'Reading',
            'DateTime',
            'Temperature degF',
            'Temperature degC',
            'Dew Point degF',
            'Dew Point degC',
            'Relative Humidity',
            'Mass Mixing Ratio',
            'Vapor Concentration',
            'Vapor Pressure',
            'Gamma',
            'Density',
            'Total Air Pressure'
        ]
        df = pd.DataFrame(dataArray, columns=dataArray_columns)

        # Determine what to do with the data based on averaging 
        # if self.avg_on: (averaging is only option now 2024-08-13)

        # Work with time first
        most_recent = df.DateTime.max()   # Take max date for use in averaged data
        date = most_recent.strftime('%Y-%m-%d')
        Time = most_recent.strftime('%H:%M:%S')

        rec_time = time.time() - self.time_start

        # Drop unneeded columns that don't work with averaging
        df = df.drop(['Reading', 'DateTime'], axis=1)

        # Average from each columns
        df = df.mean(axis=0).to_frame().T

        # Insert required metadata columns
        df.loc[0, 'Reading'] = self.rdg
        df.loc[0, 'Date'] = date
        df.loc[0, 'Time'] = Time
        df.loc[0, 'Source'] = src
        df.loc[0, 'Recording Length'] = rec_time

        # Find first cell of row to write to
        last_row = int(self.sht.used_range.last_cell.row)
        row_str = "$A${}".format(last_row+1)
        empty_row = self.sht[row_str]  # Should be column A of next row
        print("Writing reading {} to cell {} of Workbook".format(self.rdg, empty_row.get_address()))

        # Prep for write data into spreadsheet
        df = df[self.headers]
        empty_row.value = df.iloc[0,:].to_list()

        return


class Recording_OLD:
    date = time.strftime('%Y%m%d')
    def __init__(self, record_length=10, filename='humidity_cart_{}'.format(date),\
                  init_reading_number=1):
        super(Recording_OLD, self).__init__()
        '''Set input variables based on inputs
            record_length = length in seconds of each recording
            filename = name of the file to be output
            init_reading_number = starting reading number'''
        self.record_length = record_length
        self.filename = filename
        self.fileLoc = os.getcwd()
        self.getFullFile()

        # Set adjustable self variables
        self.recEnabled = False
        self.continuationLC = False
        self.continuationSS = False

        self.time_start = time.time()       # initialize time start
        self.time_end = self.time_start+self.record_length
        self.avg_on = True                  # turn on averaging
        self.rdg = init_reading_number      # initialized reading number
        self.check_for_latest_reading()     # pull in reading from existing file (if exists)

        self.iheaders = ['Reading','DateTime']  # start with initial headers
        self.headers = []

    def getFullFile(self):
        # If .csv is in filename, strip it out
        if '.csv' not in self.filename.lower():
            self.filename = self.filename + '.csv'

        # Combine all necessary elements of filename into full_filename
        self.full_filename = Path(self.fileLoc) / self.filename

    def check_for_latest_reading(self):
        if os.path.isfile(self.full_filename):
            rdg_from_file = int(pd.read_csv(self.full_filename, usecols=['Reading']).max())
            self.rdg = rdg_from_file+1
        else:
            self.rdg = 1

    def captureDataSS(self, values):
        '''Captures data for the spectra sensor.'''
        # Copy the values so that we don't modify the original list
        vals = values.copy()

        # Spectra Sensor Data ------------------------------------------
        # Indicate if recording is enabled and if this is a continuation
        if self.recEnabled and time.time()<=self.time_end:
            # Insert reading num and time into dataset
            vals.insert(0,datetime.datetime.now())
            vals.insert(0,self.rdg)

            if self.continuationSS:
                pass   # This is a continuation so we must append the data to the list

            else:
                # This is the first point to record, so we must create the new variable to store data
                self.dataSS = []   # reinitialize to clear data from previous recording

                # Turn ON continuation mode
                self.continuationSS = True

            self.dataSS.append(vals)


        else:   #  we are not in record mode
            if self.continuationSS:  # we just came out of a record
                self.continuationSS = False   # Force out of continuation

                # Go to interpret output function
                try:
                    self.interpretOutput(self.dataSS, 'WVSS')

                    # Notate info about recording
                    print('WVSS Recording Captured')
                    print('WVSS Data Length = {} rows in {} seconds'.format(len(self.dataSS), time.time()-self.time_start))

                except:  # file is open cannot write so throw an error
                    msg = common_def.error_msg()
                    msg.setText('DATA NOT WRITTEN TO FILE:\n\n{} is open; '.format(self.filename_ext) + \
                                'please close the file before continuing')
                    msg.exec_()

            self.continuationSS = False  # turn off continuation

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
                self.continuationLC = False   # Force out of continuation

                # Go to interpret output function
                try:
                    self.interpretOutput(self.dataLC, 'HumGen')

                    # Notate info about recording
                    print('HumGen Recording Captured')
                    print('HumGen Data Length = {} rows in {} seconds'.format(len(self.dataLC), time.time()-self.time_start))

                except:  # file is open cannot write so throw an error
                    msg = common_def.error_msg()
                    msg.setText('DATA NOT WRITTEN TO FILE:\n\n{} is open; '.format(self.filename_ext) + \
                                'please close the file before continuing')
                    msg.exec_()


            self.continuationLC = False  # turn off continuation

    def interpretOutput(self, data, src):
        '''After reading has been captured, this method evaluates what to do with it.'''
        # Convert to dataframe
        out_df = self.convertToDataFrame(data, src)

        # If a file has already been created append data to it, otherwise create
        #  the file and write data to it
        if os.path.isfile(self.full_filename):  # if the file exists append data (mode='a')
            out_df.to_csv(self.full_filename, mode='a', index=False, header=False)
        else:   # file does NOT exist, so create it and write the first point with header
            out_df.to_csv(self.full_filename, mode='w', index=False, header=True)

    def convertToDataFrame(self, dataArray, src):
        # Create initial dataset from dataLC and dataSS
        df = pd.DataFrame(dataArray, columns=self.headers)

        # Determine what to do with the data based on averaging
        if self.avg_on:
            # Work with time first
            most_recent = df.DateTime.max()   # Take max date for use in averaged data
            date = most_recent.strftime('%Y-%m-%d')
            Time = most_recent.strftime('%H:%M:%S.%f')

            rec_time = time.time() - self.time_start

            # Prep to combine averaged data
            row_name = 'mean'
            df.loc[row_name] = df.mean(axis=0)   # Average all columns in the last row of the dataframe
            ini_cols = pd.DataFrame({'Reading': [self.rdg], 'Source': [src], 'Seconds Avg': [rec_time],\
                           'Date': [date], 'Time': [Time]}, index=[row_name])  # Initial (fixed) columns
            sel_cols = df.iloc[[-1],2:]   # Last row and Columns that were selected by the user
            out_df = pd.concat([ini_cols,sel_cols], axis=1, sort=False)
        else:
            out_df = df

        return out_df
