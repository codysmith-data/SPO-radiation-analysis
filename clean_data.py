"""

@author: Cody Smith | codysmith.contact@gmail.com
https://github.com/codysmith-tech
https://www.linkedin.com/in/codysmithprofile/

"""

import pandas as pd
import numpy as np

def clean_data(parsed_data_files):
    """
    Drops unnecessary data and replaces bad data with np.nan

    Parameters
    ----------
    parsed_data_files : list
        A list of strings containing the paths to all raw data files.

    Returns
    -------
    all_data : list
        A list of DataFrames containing all data.

    """
    

    #Instantiating lists to hold dataframes of data
    all_data = []
    november_data = []
    december_data = []
    january_data =[]
    
    for i in range(len(parsed_data_files)):
        
        if '_11' in parsed_data_files[i]:
            df = pd.read_csv(parsed_data_files[i], sep=',', header=None)
            df.drop([0,1,2,3,4], axis=1, inplace=True)
            df.columns=[0]
            november_data.append(df)
            
        elif '_12' in parsed_data_files[i]:
            df = pd.read_csv(parsed_data_files[i], sep=',', header=None)
            df.drop([0,1,2,3,4], axis=1, inplace=True)
            df.columns=[0]
            december_data.append(df)
            
        else:
            df = pd.read_csv(parsed_data_files[i], sep=',', header=None)
            df.drop([0,1,2,3,4], axis=1, inplace=True)
            df.columns=[0]
            january_data.append(df)
            
    all_data.append(november_data)
    all_data.append(december_data)
    all_data.append(january_data)
    
    #Cleaning
    for i in range(len(all_data)):
        for j in range(len(all_data[i])):
            
            #Ignorning all missing data (i.e. -999)
            all_data[i][j][0].replace(-999, np.nan, inplace=True)
            
            #Averaging every 3 rows for 1 min interval years
            if len(all_data[i][j]) > 40000:
                all_data[i][j] = all_data[i][j].groupby(np.arange(len(all_data[i][j]))//3).mean()
                all_data[i][j].reset_index(drop=True, inplace=True)
            
        
    return all_data