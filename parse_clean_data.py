# -*- coding: utf-8 -*-
"""
Created on Tue Dec 14 10:30:30 2021

@author: Cody Smith
"""

import os
import shutil
import csv


def parse_and_clean(working_directory):

    if os.path.isdir(working_directory + '\\parsed-data\\') == False:
        os.mkdir(working_directory + '\\parsed-data')
        
    if os.path.isdir(working_directory + '\\cleaned-data\\') == True:
        shutil.rmtree(working_directory + '\\cleaned-data')
    
    os.mkdir(working_directory + '\\cleaned-data')
    
    
    #Removing incomplete dataset
    if os.path.isfile(working_directory + "\\raw-data\\spo_1978_01.dat") == True:
        os.remove(working_directory + "\\raw-data\\spo_1978_01.dat")
        
    if os.path.isfile(working_directory + "\\raw-data\\spo_1978_02.dat") == True:
        os.remove(working_directory + "\\raw-data\\spo_1978_02.dat")
        
    #Making list of all raw data files
    raw_data_files = []
    for dirpath, subdirs, files in os.walk(working_directory + "\\raw-data"):
        for f in files:
            raw_data_files.append(os.path.join(dirpath, f))
    
    #Reading raw data files, removing header and whitespace, and parsing into new files
    n = 3
    nfirstlines = []
    
    for i in range(len(raw_data_files)):
        with open(raw_data_files[i]) as f, open(working_directory + '\\parsed-data\\'  + f"{files[i]}", 'w') as out:
            first_line = f.readline().strip()
            if 'SPO_RAD' in first_line:
                for x in range(n):
                    nfirstlines.append(next(f))
            for line in f:
                out.write(line.strip() + '\n')
    
                
    #Making list of all parsed data files
    parsed_data_files = []
    for dirpath, subdirs, files in os.walk(working_directory + "\\parsed-data"):
        for f in files:
            parsed_data_files.append(os.path.join(dirpath, f))
            
    #Stripping file names of .dat extension
    filenames = []
    for i in range(len(files)):
        filenames.append(files[i].strip('.dat'))
            
    #Removing unnecessary data
    for i in range(len(parsed_data_files)):
        f =  open(parsed_data_files[i], 'r')
        g =  open(working_directory + '\\cleaned-data\\' + files[i] + '.csv', 'a+')
        
        writer = csv.writer(g)
            
        for lines in f:
            line = lines.split()
            
            writer.writerow((line[0],line[1],line[2],line[3],line[4],line[5]))
        
        f.close()
        g.close()
    
                
    #Make list of all cleaned data files
    cleaned_data_files = []
    for dirpath, subdirs, files in os.walk(working_directory + "\\cleaned-data"):
        for f in files:
            cleaned_data_files.append(os.path.join(dirpath, f))

    return raw_data_files, cleaned_data_files, filenames
        


            
            
            
            