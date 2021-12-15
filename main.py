# -*- coding: utf-8 -*-
"""
Created on Tue Dec 14 10:31:17 2021

@author: crsmi
"""

from get_data import get_data
from parse_clean_data import parse_and_clean
import pandas as pd
import os

def main():
    
    ### USER SET WORKING DIRECTORY ###
    working_directory = r"C:\Users\crsmi\OneDrive\Desktop\SPO-radiation-analysis-main"
    
    #Fetching data
    get_data(working_directory)
    
    #Parse data
    raw_data_files, cleaned_data_files, filenames = parse_and_clean(working_directory)  
    
    #Clean data
    # df = {}
    # for i in range(len(cleaned_data_files)):
    # df = pd.read_csv(cleaned_data_files[4],sep=',',header=None)
    # print(df)
    
    
    
if __name__ == "__main__":
    main()