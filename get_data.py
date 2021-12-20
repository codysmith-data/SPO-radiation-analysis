"""

@author: Cody Smith | codysmith.contact@gmail.com
https://github.com/codysmith-tech
https://www.linkedin.com/in/codysmithprofile/

"""

import requests, zipfile, io
from bs4 import BeautifulSoup


def get_data(working_directory):
    """
    This function obtains the data from the NOAA data and saves
    the files to the working directory defined in main.py.

    Parameters
    ----------
    working_directory : string
        The directory that contains your the scripts
        for this project, including this one.

    Returns
    -------
    None.

    """
    
    #Defining URL that links to NOAA Data Repository
    data_base_url = 'https://gml.noaa.gov/aftp/data/radiation/baseline/spo/old_vax_files/'
    
    #Defining which months we are interested in (i.e. Sout Pole summer)
    file_months = ['_11.zip', '_12.zip', '_01.zip']
    
    #Getting the HTML makeup of the Data Repository
    page = requests.get(data_base_url)
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
        download = requests.get(data_base_url + summer_filenames[i], stream=True)
        zipped = zipfile.ZipFile(io.BytesIO(download.content))
        zipped.extractall(fr"{working_directory}" + "\\raw-data")