# SPO-radiation-analysis

@author: Cody Smith | codysmith.contact@gmail.com
https://github.com/codysmith-tech
https://www.linkedin.com/in/codysmithprofile/

An analysis of the data on solar radiation measurements at the South Pole from NOAA.
This is used as a proxy for measuring cloud cover to find the statistics on getting a clear sky during the Antartic summer for solar astronomy.

This is an example project showcasing data parsing & cleaning, data analysis & visualization, and web scraping.
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

The only module not included with Anaconda is plotly.
***
For a quick install, type:

pip install plotly
***

Once setup is complete, open main.py in Anaconda.
This is the master for the whole project, and the only file that needs to be opened (specifcally for running the project).
To run the project, press Run (green arrow at the top) or F5.
Wait for the running for the process to complete!
Now check the results in the results folder!

------------------------
Files:

main.py - master file for running all other files

get_data.py - obtains the data from the NOAA data and savesthe files to the working directory defined in main.py

parse_data.py - takes raw data files and parses them into .csv files for better handling

clean_data.py - drops unnecessary data and replaces bad data

analyze_data.py - takes all data and creates binary information for each month

plot_data.py - plots all data into raw radiation plots and binary radiation plots

find_results.py - finds the total amount of hours of radiation for each month and writes the results to a .txt file

Folders:

raw-data: holds all the raw data from the NOAA database

filtered-data: holds all the parsed/filtered .csv files

graphs: holds all the graphs made for the radiation data

results: holds the .txt file containing the results
