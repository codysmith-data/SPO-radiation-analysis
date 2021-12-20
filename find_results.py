"""

@author: Cody Smith | codysmith.contact@gmail.com
https://github.com/codysmith-tech
https://www.linkedin.com/in/codysmithprofile/

"""
import pandas as pd
import os
import shutil

def total_hours(data):
    """
    Finds the total amount of hours from a binary radiation DF.

    Parameters
    ----------
    data : DataFrame
        The binary DataFrame to be converted into total hours.

    Returns
    -------
    total_hours : int
        The total amount of time in hours of radiation.

    """
    total_hours = (pd.DataFrame.sum(data))*3./60
    
    return total_hours
    

def find_results(working_directory, nov_mean_binary, dec_mean_binary, jan_mean_binary):
    """
    Finds the total amount of hours of radiation for each month and writes the results to a .txt file.

    Parameters
    ----------
    working_directory : string
        The directory that contains your the scripts
        for this project, including this one.
        
    nov_mean_binary : DataFrame
        The average binary data for all years of November.
        
    dec_mean_binary : DataFrame
        The average binary data for all years of December.

    jan_mean_binary : DataFrame
        The average binary data for all years of January.

    Returns
    -------
    None.

    """
    
    #Making results directory
    if os.path.isdir(working_directory + '\\results\\') == True:
        shutil.rmtree(working_directory + '\\results')
    
    os.mkdir(working_directory + '\\results\\')
    
    #Finding total number of hours that had sufficient radiation
    #November
    nov_hours = total_hours(nov_mean_binary)
    
    #December
    dec_hours = total_hours(dec_mean_binary)
    
    #January
    jan_hours = total_hours(jan_mean_binary)
    
    #Writing results to text file
    with open(working_directory + '\\results\\results.txt', 'w') as results:
        results.write('___RESULTS___:\n')
        results.write('The average amount of hours of sufficient radiation for November:\n')
        results.write(f'{nov_hours}\n')
        results.write('\n')
        results.write('The average amount of hours of sufficient radiation for December:\n')
        results.write(f'{dec_hours}\n')
        results.write('\n')
        results.write('The average amount of hours of sufficient radiation for January:\n')
        results.write(f'{jan_hours}\n')
        
        