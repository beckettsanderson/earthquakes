# -*- coding: utf-8 -*-
"""
Mon Oct 25 2021

Homework 6 - Problem 3:
     Use matplotlib to create a bar chart with three bars per month
     -- one for low-magntiude quakes, one for medium, and one for high. 
     Use different colors for low/medium/high, and include a legend in
     your plot.

@author: Beckett Sanderson
"""

import csv
import matplotlib.pyplot as plt

EARTHQUAKES = "earthquake_data.csv"

def read_csv(file_name):
    
    """
    Read in a file and return a 2d list of earthquakes

    Parameters
    ----------
    file_name : file containing earthquake data

    Returns
    -------
    quake_data : 2d list containing rows of data for different quakes

    """    
    
    # initialize empty list variable
    quake_data = []
    
    # open file we are reading in
    with open(file_name, 'r') as file:
        
        # set up csv reader to read in each line
        reader = csv.reader(file)

        # loops through entire csv file by each row
        for line in reader:
            
            # adds each row to the positions_data variable
            quake_data.append(line)
    
    # removes headers from quake data
    labels = quake_data.pop(0)
    
    return quake_data


def get_mon_and_mags(quake_data):
    
    """
    Gather months and magnitudes from earthquakes and add to a list 
    of all months

    Parameters
    ----------
    quake_data : 2d list containing rows of data for different quakes

    Returns
    -------
    quakes_month_and_mag : a 2d list containing all quake's months 
                           and magnitudes

    """
    
    # initializes empty return variable and counter to keep track
    quakes_month_and_mag = []
    quake_counter = 0
    
    # loops through each earthquake in dataset
    for quake in quake_data:
        
        # gets quake's month and adds it to month list
        date_data = quake[0].split("-")
        quakes_month_and_mag.append([date_data[1]])
        
        # get quakes magnitude and add it to list of corresponding month
        mag_data = float(quake[4])
        quakes_month_and_mag[quake_counter].append(mag_data)
        
        # changes counter by 1 after reading one quake
        quake_counter += 1
    
    return quakes_month_and_mag
    

def get_one_month_count(quake_months, month_num):
    
    """
    Goes through quake months and returns number of quakes in chosen month

    Parameters
    ----------
    quakes_month_and_mag : a 2d list containing all quake's months 
                           and magnitudes
    month_num : two digit number of month looking to count

    Returns
    -------
    mon_by_mag_count : a list of the number of earthquakes in a chosen 
                         month split into magnitudes split into high,
                         medium, and low EX: [120, 435, 238]

    """
    
    # initializes empty counter for each magnitude
    mon_by_mag_count = [0, 0, 0]

    # loops through all quake months counting num equal to chosen month
    for mon_and_mag in quake_months:
        
        # adds 1 to counter if chosen month equals month from list
        if mon_and_mag[0] == month_num: 
            
            # adds one to corresponding index depending on magnitude
            if mon_and_mag[1] < 3.0:
                
                mon_by_mag_count[2] += 1
                
            elif mon_and_mag[1] > 3.5:
                
                mon_by_mag_count[0] += 1
                
            else:
                
                mon_by_mag_count[1] += 1
                
    return mon_by_mag_count
    

def get_quakes_per_month(quake_mons_and_mags):
    
    """
    Goes through months list and counts number of earthquakes in each
    month and returning a dictionary sorted by month

    Parameters
    ----------
    quakes_mons_and_mags : a 2d list containing all quake's months 
                           and magnitudes

    Returns
    -------
    quake_mon_and_mag_dict : a dictionary sorted by month for number of
                             quakes by magnitude

    """
    
    # initialize empty dictionary of months and number of quakes
    quake_months_dict = {}
    
    # uses singular month function to count num quakes each month
    quake_months_dict["January"] = get_one_month_count(quake_mons_and_mags,
                                                       "01")  
    quake_months_dict["February"] = get_one_month_count(quake_mons_and_mags,
                                                        "02")
    quake_months_dict["March"] = get_one_month_count(quake_mons_and_mags,
                                                     "03")
    quake_months_dict["April"] = get_one_month_count(quake_mons_and_mags,
                                                     "04")
    quake_months_dict["May"] = get_one_month_count(quake_mons_and_mags,
                                                   "05")
    quake_months_dict["June"] = get_one_month_count(quake_mons_and_mags,
                                                    "06")
    quake_months_dict["July"] = get_one_month_count(quake_mons_and_mags,
                                                    "07")
    quake_months_dict["August"] = get_one_month_count(quake_mons_and_mags,
                                                      "08")
    quake_months_dict["September"] = get_one_month_count(quake_mons_and_mags,
                                                         "09")
    quake_months_dict["October"] = get_one_month_count(quake_mons_and_mags,
                                                       "10")
    quake_months_dict["November"] = get_one_month_count(quake_mons_and_mags,
                                                        "11")
    quake_months_dict["December"] = get_one_month_count(quake_mons_and_mags,
                                                        "12") 
    
    return quake_months_dict


def plot_one_month(quake_mon_and_mag_dict, month):
    """
    Goes through months list and counts number of earthquakes in each
    month and returning a dictionary sorted by month

    Parameters
    ----------
    quake_mon_and_mag_dict : a dictionary sorted by month for number of
                             quakes by magnitude
    month : chosen month to plot as a string

    Returns
    -------
    None.

    """
    
    # plots number of quakes that were low magnitude in chosen month
    plt.bar(month, quake_mon_and_mag_dict[month][2], color = "lightcoral") 
    
    # plots number of quakes that were medium magnitude in chosen month
    plt.bar(month, quake_mon_and_mag_dict[month][1], 
            bottom = quake_mon_and_mag_dict[month][2], color = "orangered") 
    
    # plots number of quakes that were high magnitude in chosen month
    plt.bar(month, quake_mon_and_mag_dict[month][0],
            bottom = quake_mon_and_mag_dict[month][2] + 
            quake_mon_and_mag_dict[month][1], color = "maroon") 
    

def graph_num_quakes(quake_mon_and_mag_dict):
    
    """
    Graphs number of quakes per month into a bar graph sorted by
    magnitude

    Parameters
    ----------
    quake_mon_and_mag_dict : a dictionary sorted by month for number of
                             quakes by magnitude

    Returns
    -------
    None.

    """
    
    # plots number of quakes in each month with a corresponding label
    plot_one_month(quake_mon_and_mag_dict, "January")
    plot_one_month(quake_mon_and_mag_dict, "February")    
    plot_one_month(quake_mon_and_mag_dict, "March")    
    plot_one_month(quake_mon_and_mag_dict, "April")        
    plot_one_month(quake_mon_and_mag_dict, "May")      
    plot_one_month(quake_mon_and_mag_dict, "June")        
    plot_one_month(quake_mon_and_mag_dict, "July")        
    plot_one_month(quake_mon_and_mag_dict, "August")        
    plot_one_month(quake_mon_and_mag_dict, "September")      
    plot_one_month(quake_mon_and_mag_dict, "October")      
    plot_one_month(quake_mon_and_mag_dict, "November")
    plot_one_month(quake_mon_and_mag_dict, "December")    

    # graph organization functions
    plt.xticks(rotation = 65)
    plt.title("Earthquakes by Month")
    plt.xlabel("Month")
    plt.ylabel("Number of Earthquakes")
    plt.legend(["Low (< 2.5)", "Medium (>= 2.5 & <= 3.5)", "High (> 3.5)"], 
               title = "Magnitude")


def main():
    print("PROBLEM 2:\n")
    
    # gather data from file into 2d list
    quake_data = read_csv(EARTHQUAKES)
        
    # collect months and magnitudes from data list
    quake_mons_and_mags = get_mon_and_mags(quake_data)
    
    # calculate quakes per month into dictionary
    quakes_per_month = get_quakes_per_month(quake_mons_and_mags)
    
    # inform user of number of quakes by month sorted as [high, medium, low]
    print("Quakes per month:", quakes_per_month)
    
    # prints graph of number of quakes in each month
    graph_num_quakes(quakes_per_month)
    
main()
