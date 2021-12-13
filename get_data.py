# -*- coding: utf-8 -*-
"""
Created on Mon Dec 13 11:40:26 2021

@author: Cody Smith
"""

import requests, zipfile, io
from bs4 import BeautifulSoup

def get_data():
    #Defining URL that links to NOAA Data Repository
    base_url = 'https://gml.noaa.gov/aftp/data/radiation/baseline/spo/old_vax_files/'
    
    #Defining which months we are interested in (i.e. Sout Pole summer)
    file_months = ['_12.zip', '_01.zip', '_02.zip']
    
    #Getting the HTML makeup of the Data Repository
    page = requests.get(base_url)
    soup = BeautifulSoup(page.content, "html.parser")
    
    #Finding all filenames based on their HTML
    files = soup.find_all("a")
    
    #Stripping the filenames from their HTML
    filenames = []
    for file in files:
        filenames.append(file.text)
    
    #Making a list of only the summer months filenames
    summer_filenames = []    
    for i in range(len(filenames)):
        if file_months[0] in filenames[i]:
            summer_filenames.append(filenames[i])
        elif file_months[1] in filenames[i]:
            summer_filenames.append(filenames[i])
        elif file_months[2] in filenames[i]:
            summer_filenames.append(filenames[i])
    
    #Downloading and extracting all summer month data files        
    for i in range(len(summer_filenames)):
        download = requests.get(base_url + summer_filenames[i], stream=True)
        zipped = zipfile.ZipFile(io.BytesIO(download.content))
        zipped.extractall(r"C:\Users\crsmith\Desktop\Python\south-pole-radiation\raw-data")