"""

@author: Cody Smith | codysmith.contact@gmail.com
https://github.com/codysmith-tech
https://www.linkedin.com/in/codysmithprofile/

"""

import os
import shutil
import csv


def parse_data(working_directory):
    """
    Takes raw data files and parses them into .csv files for better
    handling

    Parameters
    ----------
    working_directory : string
        The directory that contains your the scripts
        for this project, including this one.

    Returns
    -------
    raw_data_files : list
        A list of strings containing the paths to all raw data files.
        
    parsed_data_files : list
        A list of strings containing the paths to all raw data files.
        
    filenames : list
        A list of strings containing the names of each data file.
    """

    #Making directories
    if os.path.isdir(working_directory + '\\parsed-data\\') == False:
        os.mkdir(working_directory + '\\parsed-data')
        
    if os.path.isdir(working_directory + '\\filtered-data\\') == True:
        shutil.rmtree(working_directory + '\\filtered-data')
    
    os.mkdir(working_directory + '\\filtered-data\\')
    os.mkdir(working_directory + '\\filtered-data\\november-data')
    os.mkdir(working_directory + '\\filtered-data\\december-data')
    os.mkdir(working_directory + '\\filtered-data\\january-data')
        
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
    parse_data_files = []
    for dirpath, subdirs, files in os.walk(working_directory + "\\parsed-data"):
        for f in files:
            parse_data_files.append(os.path.join(dirpath, f))
            
    #Stripping file names of .dat extension
    filenames = []
    for i in range(len(files)):
        filenames.append(files[i].strip('.dat'))
            
    #Removing unnecessary data
    for i in range(len(parse_data_files)):
        f =  open(parse_data_files[i], 'r')
        if '_11' in parse_data_files[i]:
            g =  open(working_directory + '\\filtered-data\\november-data\\' + filenames[i] + '.csv', 'a+')
        elif '_12' in parse_data_files[i]:
            g =  open(working_directory + '\\filtered-data\\december-data\\' + filenames[i] + '.csv', 'a+')
        else:
            g =  open(working_directory + '\\filtered-data\\january-data\\' + filenames[i] + '.csv', 'a+')
        
        writer = csv.writer(g)
            
        for lines in f:
            line = lines.split()
            
            writer.writerow((line[0],line[1],line[2],line[3],line[4],line[5]))
        
        f.close()
        g.close()
    
                
    #Make list of all cleaned data files
    parsed_data_files = []
    for dirpath, subdirs, files in os.walk(working_directory + "\\filtered-data"):
        for f in files:
            parsed_data_files.append(os.path.join(dirpath, f))
            
    shutil.rmtree(working_directory + '\\parsed-data')

    return raw_data_files, parsed_data_files, filenames
        


            
            
            
            