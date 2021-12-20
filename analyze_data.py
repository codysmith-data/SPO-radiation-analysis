"""

@author: Cody Smith | codysmith.contact@gmail.com
https://github.com/codysmith-tech
https://www.linkedin.com/in/codysmithprofile/

"""

import pandas as pd
import numpy as np

def mean_round_binary(df_of_binary):
    """
    Finds the mean across all rows of a DataFrame.
    Then rounds up or down to the nearest 1 or 0 respectively.

    Parameters
    ----------
    df_of_signals : DataFrame
        A dataframe of signals to perform
        averaging and rounding on.

    Returns
    -------
    mean_signal : list
        A list of the averaged signal values

    """
    
    #Averaging rows
    mean_signal = df_of_binary.mean(axis=1)
    
    #Rounding to nearest 0 or 1
    for i in range(len(mean_signal)):
        if mean_signal[i] < 0.5:
            mean_signal[i] = 0
        else:
            mean_signal[i] = 1
            
    return mean_signal
    
def analyze_data(all_data):
    """
    Takes all data and creates binary information for each month.

    Parameters
    ----------
    all_data : list
        A list of DataFrames containing all data.

    Returns
    -------
    all_data : list
        A list of DataFrames containing all data.
        
    nov_mean_binary : DataFrame
        The average binary data for all years of November.
        
    dec_mean_binary : DataFrame
        The average binary data for all years of December.

    jan_mean_binary : DataFrame
        The average binary data for all years of January.

    """

    #Instantiating dataframes to hold signals for each month
    nov_binary = pd.DataFrame()
    dec_binary = pd.DataFrame()
    jan_binary = pd.DataFrame()
    
    #Base stat work
    for i in range(len(all_data)):
        for j in range(len(all_data[i])):
            
            #Creating a binary signal based on suffiecient radiation
            binary = []
            for k in range(len(all_data[i][j][0])):
                if all_data[i][j][0][k] <= 990:
                    binary.append(0)
                elif all_data[i][j][0][k] == np.nan:
                    binary.append(np.nan)
                else:
                      binary.append(1)
                     
            all_data[i][j][1] = binary
            
            #Congregating binary intom their respective dataframes
            if i == 0:
                nov_binary[j] = binary
            elif i == 1:
                dec_binary[j] = binary
            else:
                jan_binary[j] = binary
                
    #Averaging and rounding the signals for each month
    nov_mean_binary = mean_round_binary(nov_binary)
    dec_mean_binary = mean_round_binary(dec_binary)
    jan_mean_binary = mean_round_binary(jan_binary)
        
    return all_data, nov_mean_binary, dec_mean_binary, jan_mean_binary