# SPO-radiation-analysis

@author: Cody Smith | codysmith.contact@gmail.com

https://github.com/codysmith-tech

https://www.linkedin.com/in/codysmithprofile/

------------------------
***OVERVIEW***

This is an example project showcasing data parsing & cleaning, basic analysis & visualiztion, and webscraping.

This is an analysis of the data on solar radiation measurements at the South Pole from NOAA.
This is used as a proxy for measuring a clear sky during the Antartic summer for solar astronomy.
This time period is defined as November, December, and January.
The data used for this project includes these months from the year 1978 to the year 2017.

The goal of this project is to provide context as to why the South Pole is a good choice for solar astronomers. As of now, solar astronomers
will spend the South Pole's summers (November through January) stationed at the South Pole's observatory. The main reasoning for choosing this
location is that the sun never sets during this time period at the South Pole. But, the weather can be volatile at this location, and things like
storms and overcast days can get in the way of the never-ending sun.

So, this project is showing that even with those things in mind, that the South Pole is still a better choice for solar astronomy than a place like
Georgia, U.S., for example.

------------------------
***GETTING STARTED***

This project was made in a Windows OS.
This project was made in Python 3.8.8.
This project was made in the Anaconda environment.
*Download Anaconda here*
https://www.anaconda.com/products/individual

Please use this setup for best results.

Modules needed for this project:

	requests

	zipfile

	io

	BeautifulSoup

	shutil

	csv

	pandas

	numpy

	matplotlib

	plotly

	webbrowser

The only module not included with Anaconda is plotly.

For a quick install, type in your Anaconda console:

**pip install plotly**

From this GitHub project, dowload the .zip of the files. Then extract to your folder of choice.

Once setup is complete, open main.py in Anaconda.

This is the master for the whole project, and the only file that needs to be opened (specifcally for running the project)

Before running, please set the working directory (line 31). This should be the directory that main.py is contained in.

To run the project, press Run (green arrow at the top) or F5.

Wait for the running for the process to complete!

Now check graphs and results folders!

------------------------
**Files:**

main.py - master file for running all other files

get_data.py - obtains the data from the NOAA database and saves the files to the working directory defined in main.py

parse_data.py - takes raw data files and parses them into .csv files for better handling

clean_data.py - drops unnecessary data and replaces bad data

analyze_data.py - takes all data and creates binary information for each month

plot_data.py - plots all data into raw radiation plots and binary radiation plots

find_results.py - finds the total amount of hours of radiation for each month and writes the results to a .txt file

**Folders:**

raw-data: holds all the raw data from the NOAA database

filtered-data: holds all the parsed/filtered .csv files

graphs: holds all the graphs made for the radiation data

results: holds the .txt file containing the results

------------------------
**RESULTS DISCUSSION**

Now, the interactive plots on the average sufficient solar radiation for each month will have been automatically opened in a browser.

The sun's radiation at the Earth's surface is measured at 1000 W/m^2.
So anything less than that means that the skies aren't clear.

The sun's radiation was plotted just to give a visual representation of what a clear sky and a non-clear sky looks like on a plot.
The graph for Dec. 1995 is given as an example.

![dec_1995_radiation](https://user-images.githubusercontent.com/58944210/146716914-785f1d91-7ebe-4b23-a210-225a000524f2.png)

As you can see, a clear sky can be seen as the mostly straight runs of points hovering around 1000 W/m^2. The non-clear skies are easily seen by the cascading point in between.
(Each point represents 3 minutes).

To get a good count of these clear sky times, I made this data into a binary format, where 1 means that there was sufficient radiation. 
(I.e. the 1000 figure, but I did 990 to account for measurement error.)

And where 0 means insufficient radiation, or anything less than 990.
The binary graph for Dec. 1995 is given as an example again.

![dec_1995_binary](https://user-images.githubusercontent.com/58944210/146717462-ed629d5b-f858-47f5-a33f-4081a7739c13.png)

The binary data for each month was averaged across every year. This was to get an idea of what the "average" December in the South Pole can expect for clear skies time.

**Navigate to the graphs folder to see what these plots look like.**

These plots are interactive HTML files. Feel free to play around with the plots!

Using the binary data for each month, I could then add up the total amount of clear skies time for each month.
This gives us a number of what we can expect for observation time for the Antartic summer.

The average amount of hours of sufficient radiation for November: **232.55**

The average amount of hours of sufficient radiation for December: **591.15**

The average amount of hours of sufficient radiation for January: **120.55**

This comes out to a total of **944.25 hours** of clear skies time at the South Pole for the months of November, December, and January.

According to currentresults.com (sources listed are National Climatic Data Center and World Data Center for Meteorology), the average
amount of clear sky time for the summer (June, July, & August) in Georgia is **882**.

As we can see, Antartica has 62.25 more hours of clear skies on average!
