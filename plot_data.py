"""

@author: Cody Smith | codysmith.contact@gmail.com
https://github.com/codysmith-tech
https://www.linkedin.com/in/codysmithprofile/

"""

import matplotlib.pyplot as plt
import plotly.express as px
import os
import shutil

def html_scatter_plot(data, labels, title, path):
    """
    Creates interactive HTML scatter plots from DataFrames.

    Parameters
    ----------
    data : DataFrame
        DF containg data to be scatter plotted
        
    labels : dict
        Dictionary of x and y axis labels
        
    title : string
        Title of graph
        
    path : string
        Path to save to

    Returns
    -------
    None.

    """
    fig = px.scatter(x = data.index, y = data,
                     labels = labels,
                     title = title)
    fig.write_html(path)

def plot_data(working_directory, all_data, nov_mean_binary, dec_mean_binary, jan_mean_binary):
    """
    Plots all data into raw radiation plots and binary radiation plots.
    
    Parameters
    ----------
    working_directory : string
        The directory that contains your the scripts
        for this project, including this one.
        
    all_data : list
        A list of DataFrames containing all data.
        
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
    
    #Turning off anaconda plots
    plt.ioff()

    #Making directories
    if os.path.isdir(working_directory + '\\graphs\\') == True:
        shutil.rmtree(working_directory + '\\graphs')
    
    os.mkdir(working_directory + '\\graphs\\')
    
    os.mkdir(working_directory + '\\graphs\\radiation-graphs')
    os.mkdir(working_directory + '\\graphs\\radiation-graphs\\november-radiation-graphs')
    os.mkdir(working_directory + '\\graphs\\radiation-graphs\\december-radiation-graphs')
    os.mkdir(working_directory + '\\graphs\\radiation-graphs\\january-radiation-graphs')
    
    os.mkdir(working_directory + '\\graphs\\binary-graphs')
    os.mkdir(working_directory + '\\graphs\\binary-graphs\\november-binary-graphs')
    os.mkdir(working_directory + '\\graphs\\binary-graphs\\december-binary-graphs')
    os.mkdir(working_directory + '\\graphs\\binary-graphs\\january-binary-graphs')
    
    for i in range(len(all_data)):
        
        year = 1978
        
        for j in range(len(all_data[i])):
            
            year = year + 1
            
            #Graphing raw radiation
            plt.figure()
            plt.scatter(all_data[i][j].index, all_data[i][j][0], s=1)
            plt.xlabel('Time (3 Minute Intervals)')
            plt.ylabel('Direct Solar Radiation (W/m^2)')
            
            #Setting title & saving raw radiation plots
            if i == 0:
                plt.title(f'November {year} Direct Radiation')
                plt.savefig(working_directory + '\\graphs\\radiation-graphs\\november-radiation-graphs\\' + f'nov_{year}_radiation.png', dpi=300)
               
            elif i == 1:
                plt.title(f'December {year} Direct Radiation')
                plt.savefig(working_directory + '\\graphs\\radiation-graphs\\december-radiation-graphs\\' + f'dec_{year}_radiation.png', dpi=300)
            
            else:
                plt.title(f'January {year} Direct Radiation')
                plt.savefig(working_directory + '\\graphs\\radiation-graphs\\january-radiation-graphs\\' + f'jan_{year}_radiation.png', dpi=300)
                
            #Graphing binary
            plt.figure()
            plt.scatter(all_data[i][j].index, all_data[i][j][1], s=1)
            plt.xlabel('Time (3 Minute Intervals)')
            plt.ylabel('Binary Radiation')
            
            #Setting title & saving binary radiation plots
            if i == 0:
                plt.title(f'November {year} Binary Radiation')
                plt.savefig(working_directory + '\\graphs\\binary-graphs\\november-binary-graphs\\' + f'nov_{year}_binary.png', dpi=300)
               
            elif i == 1:
                plt.title(f'December {year} Binary Radiation')
                plt.savefig(working_directory + '\\graphs\\binary-graphs\\december-binary-graphs\\' + f'dec_{year}_binary.png', dpi=300)
            
            else:
                plt.title(f'January {year} Binary Radiation')
                plt.savefig(working_directory + '\\graphs\\binary-graphs\\january-binary-graphs\\' + f'jan_{year}_binary.png', dpi=300)
    
    #Plotting average binary radiation for each month
    #November
    html_scatter_plot(nov_mean_binary, 
                      labels = dict(x='Time (3 Minute Intervals)',y='Binary Radiation'), 
                      title = 'Average November Binary Radiation',
                      path = working_directory + '\\graphs\\' + 'nov_avg_binary.html'
                      )
    
    #December
    html_scatter_plot(dec_mean_binary, 
                      labels = dict(x='Time (3 Minute Intervals)',y='Binary Radiation'), 
                      title = 'Average December Binary Radiation',
                      path = working_directory + '\\graphs\\' + 'dec_avg_binary.html'
                      )
    
    #January
    html_scatter_plot(jan_mean_binary, 
                      labels = dict(x='Time (3 Minute Intervals)',y='Binary Radiation'), 
                      title = 'Average January Binary Radiation',
                      path = working_directory + '\\graphs\\' + 'jan_avg_binary.html'
                      )