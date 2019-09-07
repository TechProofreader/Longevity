# Author: Ryan Reyes, github.com/TechProofreader
# Version: 1.0.1
# Copyright 2019 Ryan Reyes, github.com/Techproofreader
# This program is distributed under the GNU Lesser General Public License v3.0

from dateutil.parser import parse
import matplotlib.pyplot as plot
import PySimpleGUI as sg
import seaborn as sns
import pandas as pd
import threading
import datetime
import time
import sys

menu_def = [['File', ['About']]]

layout = [
    [sg.Menu(menu_def, tearoff=False)],
    [sg.Text('To create a new file, type a file name, click Where To Save, and then click Create.', justification='left', background_color='#F69191', font=('Marcellus', 15), text_color='beige')],
    [sg.InputText(key='fileName'), sg.Text('< Name Your File', size=(16, 1), background_color='#F69191', font='Marcellus', text_color='beige', justification='left')],
    [sg.Txt('', key='fileNameError', size=(40, 1), background_color='#F69191', font='Marcellus', text_color='purple', justification='left')],
    [sg.Input(key='location'), sg.FolderBrowse('Where To Save', key='Save File', font='Marcellus'), sg.Button('Create', key='Create', size=(16, 1), font='Marcellus')],
    [sg.Txt('', key='locationError', size=(40, 1), background_color='#F69191', font='Marcellus', text_color='purple', justification='left')],
    [sg.Text('--------------------------------------------------------------------------------', justification='center', background_color='#F69191', font=('Marcellus', 15), text_color='beige')],
    [sg.Text('Select your .csv file with the file browser to analyze or update your record.', justification='left', background_color='#F69191', font=('Marcellus', 15), text_color='beige')],
    [sg.Input(key='File'), sg.FileBrowse('File Browser', key='File Browse', font='Marcellus')],
    [sg.Button('Graph Averages', key='Average', size=(16, 1), font='Marcellus'), sg.Button('Trend Over Time', key='Trend', size=(16, 1), font='Marcellus')],
    [sg.Text('To update your file, please fill out the form below and click \"Submit.\"', justification='left', background_color='#F69191', font=('Marcellus', 15), text_color='beige')],
    [sg.Text('Date (MM/DD/YYYY):', size=(16, 1), background_color='#F69191', font='Marcellus', text_color='beige', justification='left')],
    [sg.InputText(key='Date'), sg.Txt('', key='dateError', size=(25, 1), background_color='#F69191', font='Marcellus', text_color='purple', justification='left')],
    [sg.Text('Time (HH:MM):', size=(16, 1), background_color='#F69191', font='Marcellus', text_color='beige', justification='left')],
    [sg.InputText(key='Time'), sg.Txt('', key='timeError', size=(25, 1), background_color='#F69191', font='Marcellus', text_color='purple', justification='left')],
    [sg.Text('Systolic:', size=(16, 1), background_color='#F69191', font='Marcellus', text_color='beige', justification='left')],    
    [sg.InputText(key='Systolic'), sg.Txt('', key='systolicError', size=(25, 1), background_color='#F69191', font='Marcellus', text_color='purple', justification='left')],
    [sg.Text('Diastolic:', size=(16, 1), background_color='#F69191', font='Marcellus', text_color='beige', justification='left')],
    [sg.InputText(key='Diastolic'), sg.Txt('', key='diastolicError', size=(25, 1), background_color='#F69191', font='Marcellus', text_color='purple', justification='left')],
    [sg.Text('Heart Rate:', size=(16, 1), background_color='#F69191', font='Marcellus', text_color='beige', justification='left')],
    [sg.InputText(key='Heart Rate'), sg.Txt('', key='heartRateError', size=(25, 1), background_color='#F69191', font='Marcellus', text_color='purple', justification='left')],
    [sg.Submit(key='Submit', font='Marcellus'), sg.Exit(key='Exit', font='Marcellus'), sg.Txt('', key='Success', size=(16, 1), background_color='#F69191', font=('Marcellus', 17), text_color='purple', justification='left')],
    [sg.Txt('', key='Error', size=(50, 1), background_color='#F69191', font='Marcellus', text_color='purple', justification='left')]
   ]

window = sg.Window('Longevity', layout, background_color='#F69191')

while True:

    event, values = window.Read()

    x = values['File']

    def checkDate2(xu):
        try:
            datetime.datetime.strptime(xu, '%m/%d/%Y')
            return True
        except ValueError:
            return False

    def checkTime2(xe):
        try:
            parse(xe).time()
            return True
        except ValueError:
            return False

    if ((values['Systolic'].isnumeric() is False) or (values['Diastolic'].isnumeric() is False) or (values['Heart Rate'].isnumeric() is False) or (checkDate2(values['Date']) == False) or (checkTime2(values['Time']) == False)) and (event != 'Average') and (event != 'Trend') and (event != 'Exit') and (event != 'Create') and (event != 'About'):
        window.Element('dateError').Update('')
        window.Element('timeError').Update('')
        window.Element('systolicError').Update('')
        window.Element('diastolicError').Update('')
        window.Element('heartRateError').Update('')
    
        def checkRangeSys2(we):
            if we.isnumeric():
                return True
            else:
                return False
    
        def checkRangeDia2(de):
            if de.isnumeric():
                return True
            else:
                return False
    
        def checkRangeHR2(fe):
            if fe.isnumeric():
                return True
            else:
                return False
    
        errorChecks2 = {
            'date': checkDate2(values['Date']),
            'time': checkTime2(values['Time']),
            'systolic': checkRangeSys2(values['Systolic']),
            'diastolic': checkRangeDia2(values['Diastolic']),
            'heartRate': checkRangeHR2(values['Heart Rate'])
        }
                
        errorsFound2 = []

        for i in errorChecks2:
            if errorChecks2[i] == False:
                errorsFound2.append(i)
            else:
                pass

        errorCodes2 = {
            'date': 'MM/DD/YYYY format only',
            'time': 'HH:MM format only',
            'systolic': 'Numbers between 0 & 199 only',
            'diastolic': 'Numbers between 0 & 199 only',
            'heartRate': 'Numbers between 0 & 199 only'
        }


        if len(errorsFound2) > 0:
            window.Element('dateError').Update('')
            window.Element('timeError').Update('')
            window.Element('systolicError').Update('')
            window.Element('diastolicError').Update('')
            window.Element('heartRateError').Update('')

            for i in errorsFound2:
                window.Element(i+'Error').Update(errorCodes2[i])

    elif ((values['Systolic'].isnumeric() is False) or (values['Diastolic'].isnumeric() is False) or (values['Heart Rate'].isnumeric() is False) or (checkDate2(values['Date']) == False) or (checkTime2(values['Time']) == False)) and (event == 'Average') or (event == 'Trend'):
        window.Element('Error').Update('')
        
    elif ((values['Systolic'].isnumeric() is False) or (values['Diastolic'].isnumeric() is False) or (values['Heart Rate'].isnumeric() is False) or (checkDate2(values['Date']) == False) or (checkTime2(values['Time']) == False)) and (event == 'Exit'):
        break

    elif ((values['Systolic'].isnumeric() is False) or (values['Diastolic'].isnumeric() is False) or (values['Heart Rate'].isnumeric() is False) or (checkDate2(values['Date']) == False) or (checkTime2(values['Time']) == False)) and (event == 'Create'):
        pass

    elif ((values['Systolic'].isnumeric() is False) or (values['Diastolic'].isnumeric() is False) or (values['Heart Rate'].isnumeric() is False) or (checkDate2(values['Date']) == False) or (checkTime2(values['Time']) == False)) and (event == 'About'):
        pass

    else:
        def checkDate(a):
            try:
                datetime.datetime.strptime(a, '%m/%d/%Y')
                return True
            except ValueError:
                return False
    
        def checkTime(b):
            try:
                parse(b).time()
                return True
            except ValueError:
                return False
    
        def checkRangeSys(c):
            if 0 < c < 200:
                return True
            else:
                return False
    
        def checkRangeDia(d):
            if 0 < d < 200:
                return True
            else:
                return False
    
        def checkRangeHR(e):
            if 0 < e < 200:
                return True
            else:
                return False
    
        errorChecks = {
            'date': checkDate(values['Date']),
            'time': checkTime(values['Time']),
            'systolic': checkRangeSys(int(values['Systolic'])),
            'diastolic': checkRangeDia(int(values['Diastolic'])),
            'heartRate': checkRangeHR(int(values['Heart Rate']))
        }
    
        errorsFound = []

        for i in errorChecks:
            if errorChecks[i] == False:
                errorsFound.append(i)
            else:
                pass

        errorCodes = {
            'date': 'MM/DD/YYYY format only',
            'time': 'HH:MM format only',
            'systolic': 'Numbers between 0 & 199 only',
            'diastolic': 'Numbers between 0 & 199 only',
            'heartRate': 'Numbers between 0 & 199 only'
        }

    if event == 'Average' and ('.csv' == str(values['File'])[-4:]):
        window.Element('Error').Update('')
        x = pd.read_csv(values['File'])
        x.set_index('Date').sort_values(by='Date')
        sns.violinplot(data=x[['Systolic', 'Diastolic', 'Heart Rate']])
        plot.show()

    elif event == 'Average' and ('.csv' != str(values['File'])[-4:]):
        window.Element('Error').Update('Please select a valid file type ending in ".csv"')

    elif event == 'Submit' and ('.csv' == str(values['File'])[-4:]):

        if ((values['Systolic'].isnumeric() is False) or (values['Diastolic'].isnumeric() is False) or (values['Heart Rate'].isnumeric() is False) or (checkDate(values['Date']) == False) or (checkTime(values['Time']) == False)):
            window.Element('Error').Update('Cannot add invalid data to file')

        elif len(errorsFound) == 0:    
            window.Element('dateError').Update('')
            window.Element('timeError').Update('')
            window.Element('systolicError').Update('')
            window.Element('diastolicError').Update('')
            window.Element('heartRateError').Update('')
            window.Element('Error').Update('')
            y = pd.read_csv(values['File'])
            y = y.append({'Date': parse(values['Date']).date(), 'Time': parse(values['Time']).time(), 'Systolic': values['Systolic'], 'Diastolic': values['Diastolic'], 'Heart Rate': values['Heart Rate']}, ignore_index='True')
            y.to_csv(values['File'], index=False)

            start_time = int(time.time()) # the start of the success alert

            def successAlert(): # the function that implements the timed success alert to display and remove to reappear when new data is successfully submitted again
                elapsed = int(time.time()) - int(start_time)
                if elapsed != 2:
                    threading.Timer(2.0, successAlert).start()
                    window.Element('Success').Update('Success!')
                elif elapsed == 2:
                    window.Element('Success').Update('')

            successAlert() # calling the success alert function to activate

        elif len(errorsFound) > 0:
            window.Element('dateError').Update('')
            window.Element('timeError').Update('')
            window.Element('systolicError').Update('')
            window.Element('diastolicError').Update('')
            window.Element('heartRateError').Update('')
            for i in errorsFound:
                window.Element(i+'Error').Update(errorCodes[i])

    elif event == 'Submit' and ('.csv' != str(values['File'])[-4:]):
        window.Element('Error').Update('Please select a valid file type ending in ".csv"')

    elif event == 'Trend' and ('.csv' == str(values['File'])[-4:]):
        try:
            window.Element('Error').Update('')
            w = pd.read_csv(values['File'])
            w = w.set_index('Date').sort_values(by='Date')
            trend_From_Read_File = w.plot.line()
            plot.xticks(rotation=45)
            plot.show()
        except:
            TypeError
            window.Element('Error').Update('File is empty, there is nothing to plot.')
                
    elif event == 'Trend' and ('.csv' != str(values['File'])[-4:]):
        window.Element('Error').Update('Please select a valid file type ending in ".csv"')
    
    elif event == 'Create':

        def locationEmpty(h):
            if values['location'] is '':
                return False
            else:
                return True
        def fileNameInvalid(f):
            if values['fileName'].isalnum() is True:
                return True
            else:
                return False

        errorChecks2 = {
            'location': locationEmpty(values['location']),
            'fileName': fileNameInvalid(values['fileName'])
        }
    
        errorsFound2 = []

        for i in errorChecks2:
            if errorChecks2[i] == False:
                errorsFound2.append(i)
            else:
                pass

        errorCodes2 = {
            'location': 'Please select where to save your file',
            'fileName': 'Please select a valid file name, alphanumeric only'
        }
        
        if len(errorsFound2) != 0:
            window.Element('locationError').Update('')
            window.Element('fileNameError').Update('')
            for i in errorsFound2:
                window.Element(i+'Error').Update(errorCodes2[i])
        else:
            window.Element('locationError').Update('')
            window.Element('fileNameError').Update('')
            new_File = pd.DataFrame(columns=['Date', 'Time', 'Systolic', 'Diastolic', 'Heart Rate'])
            new_File.to_csv(values['location']+'/'+values['fileName']+'.csv', index=False)
            
            start_time2 = int(time.time()) # the start of the success alert

            def successAlert2(): # the function that implements the timed success alert to display and remove to reappear when new data is successfully submitted again
                elapsed2 = int(time.time()) - int(start_time2)
                if elapsed2 != 2:
                    threading.Timer(2.0, successAlert2).start()
                    window.Element('locationError').Update('Success!')
                elif elapsed2 == 2:
                    window.Element('locationError').Update('')

            successAlert2() # calling the success alert function to activate
    
    elif event == 'About':
        sg.Popup('Author: Ryan Reyes, https://github.com/TechProofreader',
                 'Program Name: Longevity',
                 'Version: 1.0.1',
                 'The GUI of this program was created with the PySimpleGUI Framework',
                 'PySimpleGUI is licensed under the GNU Lesser General Public License v3.0',
                 'The creator of PySimpleGUI is: https://github.com/MikeTheWatchGuy',
                 'This \"Longevity\" program is licensed under the GNU Lesser General Public License v3.0', font=('Marcellus', 15), text_color='beige', background_color='#F69191')

    elif event is None or event == 'Exit':
        break

window.Close()
