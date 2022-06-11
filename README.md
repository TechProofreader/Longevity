# Longevity (Current Version: 1.0.1)

Longevity is a simple, but powerful cross-platform blood pressure analysis and tracking tool written in Python.
![](https://raw.githubusercontent.com/TechProofreader/Longevity/master/LongevityPic.png)

With Longevity, you can create and update "csv" files with your daily blood pressure readings, view a time trend of your readings, or you can view a violin plot of your where your readings commonly trend toward.

![](https://github.com/TechProofreader/Longevity/blob/master/LongevityTimeTrend.png)
![](https://github.com/TechProofreader/Longevity/blob/master/LongevityViolinPic.png)

A cool feature of Longevity is its active and extensive error checking functionality. During all user interaction, Longevity is actively monitoring for incorrect and/or bad input data so as to preserve the integrity of the user's data. It will prevent the user from inputting erroneous data so that there is no concern over the accuracy of its analysis and user created file structures.

Longevity utilizes [Matplotlib](https://matplotlib.org/) and [Seaborn](http://seaborn.pydata.org/) for its graphing functionality, [Pandas](https://github.com/pandas-dev/pandas) to create, save, and read dataframes and csv files, and the [PySimpleGUI](https://github.com/PySimpleGUI/PySimpleGUI) framework to generate the graphical user interface.

This software can be turned into a standalone program on various platforms such as Mac OS, Windows OS, and Linux via freezing the script itself by way of packages such as [py2app](https://pypi.org/project/py2app/), [py2exe](http://www.py2exe.org/), etc.

<h2>To get and use Longevity on your machine</h2> 

**Dependencies required to run this program:**
* Python script freezing package such as py2app, py2exe, or whichever you prefer
* Matplotlib
* Seaborn
* Pandas
* NumPy

*Note: It is best to use the [pip package](https://pip.pypa.io/en/stable/) (which should already be installed if you have Python installed on your machine) to install Matplotlib, Seaborn, Pandas, and NumPy.*

Simply download the [LongevityPressureProgram.py](https://github.com/TechProofreader/Longevity/blob/master/LongevityPressureProgram.py) file and use one of the freezing packages above (or whichever you prefer) to freeze it into a standalone program.

If you would like to create some test data for research purposes or for any other reason, you should also download the [test module I wrote for Longevity](https://github.com/TechProofreader/Longevity/blob/master/bloodPressureTesting.py) and adjust the parameters as you see fit. This test module generates random blood pressure and heart rate data coupled with randomized dates and times. It's great for generating artificial patient data for general healthcare research, as well as data to test Longevity's functions against, or simply to analyze the time trends of certain data types.

<h2>For the Future</h2>

Over time, I plan on adding more functionality to Longevity, such as:

* the ability to choose a time period to analyze
* the ability to choose different graph/plot types
* the ability to analyze differences in data between morning/noon/evening readings
* and of course a cool logo!

<h2>Known Bugs</h2>

* This program was written with Python 3.7.3, but right now, something with Python 3.7.4 and PySimpleGUI is not playing nice, so just be aware of this. The main issue is that while running the program with Python 3.7.4 and clicking either of the graphing buttons results in a proper graph displaying, as well as a file browser window in the foreground (for no reason). This is being actively investigated and is not program breaking, just annoying, but be aware of it. **Note: I later learned from the creater of PySimpleGUI, that he dislikes OOP concepts and has thus written PySimpleGUI to not work with regards to those concepts, which has caused many restrictions and workarounds, which is what is leading to this behavior. Unfortunately, the best course of action at this point in time is to port Longevity over to another more industry-standard platform.**

<h2>Additional Notes</h2>

* I'm currently contemplating porting this over to a language such as Java to not only make it more accessible to audiences outside of the tech world, but to also **prettify** it, but we'll see.
* Yes, I love camel case, and yes, I do know that standard Python protocol utilizes snake case, but since this is a personal project, I chose my preference, camel case. Rest assured, a full-blown enterprise edition would certainly be up to PEP standards.
* At this point in time, I am considering the work on Longevity to be complete in-relation to its open source edition. Thus, there will be no further updates to the currently listed code, at this point in time. Thank you, and I hope the software brings you increased health, as it is a solid, tweakable code base that is available to anyone who is interested. Outside of providing an open source blood pressure management option to the general public, I also hope this project can serve as a codebase for students, as well as serve to inspire others to release software tools for their communities in a sort of tech pay it forward kind of way!

**Enjoy and stay healthy!**
