# Author: Ryan Reyes, github.com/TechProofreader
# Version: 1.0.1
# Copyright 2019 Ryan Reyes, github.com/Techproofreader
# This program is distributed under the GNU Lesser General Public License v3.0
#
# this file is for testing that our blood pressure and heart rate data stored in our .csv file 
# is properly generated, formatted, read, and analyzed by our functions.

import csv
from numpy.random import seed
from numpy.random import randint
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plot
from dateutil.parser import parse
from mpl_toolkits.mplot3d import Axes3D

pressureChart = pd.DataFrame(columns=['Date', 'Time', 'Systolic', 'Diastolic', 'Heart Rate'])
pressureChart.to_csv(r'file path and name of your .csv file goes here', index=False)

# seed() allows for controlling the random sample because it returns the same numbers every time.
# each seed stores the same set of numbers that it initially generated
# if you wish to generate random data sets over each run, then simply remove the seed() function

seed(1)
systolicValues =randint(110, 180, 30) # generates random systolic numbers
diastolicValues = randint(60, 95, 30) # generates random diastolic numbers
heartRateValues = randint(65, 100, 30) # generates random heart rate values
month = randint(1, 12, 30)
day = randint(1, 28, 30)
hour = randint(1, 12, 30)
minute = randint(1, 59, 30)

for syst, dias, hrt, mnth, dys, hrs, mins in zip(systolicValues, diastolicValues, heartRateValues, month, day, hour, minute): # the zip() function allows you to iterate through multiple, separate sets of data
    pressureChart = pressureChart.append({'Date': parse(str(mnth)+'-'+str(dys)+'-'+'2019').date(), 'Time': parse(str(hrs)+':'+str(mins)).time(), 'Systolic': syst, 'Diastolic': dias, 'Heart Rate': hrt}, ignore_index='True')

pressureChart.to_csv(r'file path and name of your .csv file goes here', index=False) # saves dataframe as a .csv file for later use

creatingChartFromFile = pd.read_csv('file path and name of your .csv file goes here') # reads the .csv file, that we saved to our computer in the previous line, into our program

#creatingChartFromFile = creatingChartFromFile.append({'Date': parse('04/27/2019').date(), 'Time': parse('2:35pm').time(), 'Systolic': 142, 'Diastolic': 73, 'Heart Rate': 59}, ignore_index='True') # adds a new line of data to the .csv file

#creatingChartFromFile.to_csv(r'file path and name of your .csv file goes here', index=False) # saves the appended .csv file with as an updated version of the original that we created

# the two functions commented out above are there in-case you wish to manually generate test data

print(pressureChart) # shows our chart before we saved it as a .csv file and appended new info
print(creatingChartFromFile) # shows our charter after we saved it as a .csv file and appended new info
sns.violinplot(data=creatingChartFromFile[['Systolic', 'Diastolic', 'Heart Rate']]) # creates violin graphs of our .csv file data
plot.show() # displays the violin graphs
