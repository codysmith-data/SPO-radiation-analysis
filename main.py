"""

@author: Cody Smith | codysmith.contact@gmail.com
https://github.com/codysmith-tech
https://www.linkedin.com/in/codysmithprofile/

"""

from get_data import get_data
from parse_data import parse_data
from clean_data import clean_data
from analyze_data import analyze_data
from plot_data import plot_data
from find_results import find_results


def main():
    """
    This is the master function which calls on every other script for
    this project.
    
    PLEASE SET WORKING DIRECTORY BEFORE USE.
    
    Returns
    -------
    None.
    
    """
    
    ### USER SET WORKING DIRECTORY ###
    working_directory = r"C:\Users\crsmi\OneDrive\Desktop\SPO-radiation-analysis-main"
    
    #Fetching data (See get_data.py)
    get_data(working_directory)
    
    #Parse data (See parse_data.py)
    raw_data_files, parsed_data_files, filenames = parse_data(working_directory)  
    
    #Get data ready for analyzing/plotting (See clean_data.py)
    all_data = clean_data(parsed_data_files)
    
    #Analyzing data
    all_data, nov_mean_binary, dec_mean_binary, jan_mean_binary = analyze_data(all_data)
    
    #Plotting data
    plot_data(working_directory, all_data, nov_mean_binary, dec_mean_binary, jan_mean_binary)
    
    #Finding results
    find_results(working_directory, nov_mean_binary, dec_mean_binary, jan_mean_binary)
    
    
if __name__ == "__main__":
    main()