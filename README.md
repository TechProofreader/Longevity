# Longevity

![](https://raw.githubusercontent.com/TechProofreader/Longevity/master/LongevityPic.png)

Longevity is a simple, but powerful cross-platform blood pressure analysis and tracking tool written with Python.

With Longevity, you can create and update "csv" files with your daily blood pressure readings, view a time trend of your readings, or you can view a violin plot of your where your readings commonly trend toward.

Over time, I plan on adding more functionality to Longevity, such as:

* the ability to choose a time period to analyze
* the ability to choose different graph/plot types
* the ability to analyze differences in data between morning/noon/evening readings
* and of course a cool logo!

A cool feature of Longevity is its active error checking functionality. During all user interaction, Longevity is actively monitoring for incorrect and/or bad input data so as to preserve the integrity of the user's data. It will prevent the user from inputting erroneous data so that there is no concern over the accuracy of its analysis and file structures.

Longevity utilizes [Matplotlib](https://matplotlib.org/) and [Seaborn](http://seaborn.pydata.org/) for its graphing functionality.

Longevity utilizes [Pandas](https://github.com/pandas-dev/pandas) to create, save, and read the dataframe/csv files.

The [PySimpleGUI](https://github.com/PySimpleGUI/PySimpleGUI) framework was utilized to create Longevity's graphical user interface.

This software can be turned into a standalone program on various platforms such as Mac OS, Windows OS, and Linux via freezing the script itself by way of packages such as [py2app](https://pypi.org/project/py2app/), [py2exe](http://www.py2exe.org/), etc.
