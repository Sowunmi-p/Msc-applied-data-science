#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov 4 18:37:33 2023

@author: Olusoji peter sowunmi
"""
#import librabries
import pandas as pd
import matplotlib.pyplot as plt


"""" 
define a fuction  (plot_race_killed_each_month) to plot the line 
graph for total race/enthnicity killed by police in each month
"""


def plot_race_killed_each_month(data, x_column, y_column, title='', xlabel='',
                                ylabel=''):
    """
    Plot raceethnicity data using Matplotlib.

    Parameters:
    data is  DataFrame containing the data.
    x_column is Name of the column for the x-axis.
    y_column is Name of the column for the y-axis.
    title is Title of the plot.
    xlabel is Label for the x-axis.
    ylabel is Label for the y-axis.
    """

    plt.figure(figsize=(10, 6))
    """
    # Plotting data grouped by "raceethnicity"
    for each group, create a line plot with x_column on the x-axis
    and y_column on the y-axis, using a unique label for each raceethnicity.
    """

    for i, data_group in data.groupby(["raceethnicity"]):
        plt.plot(data_group[x_column],
                 data_group[y_column], label=i)

    # Set plot title and labels
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)

    # Removing white space left and right using pandas min/max
    plt.xlim(data_group[x_column].min(), data_group[x_column].max())

    # Display legend
    plt.legend()

    # Save the plot as png
    plt.savefig('my_plot1.png')

    # Show the plot
    plt.show()
    return


"""
define a function (plot_total_value_race) to plot a bar graph for the total
 value of race/ethnicities killed by the police
 """


def plot_total_value_race(data, title='', xlabel='', ylabel=''):
    """
    Plot total_value_race data using Matplotlib.

    Parameters:
    data is  DataFrame containing the data.
    title is Title of the plot.
    xlabel is Label for the x-axis.
    ylabel is Label for the y-axis.
    """

    plt.figure(figsize=(8, 6))
    # bar plot
    data.plot(kind="bar")

    # Title, labels, and legend
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)

    # Save the plot as a png
    plt.savefig('my_plot2.png')
    plt.show()
    return


"""
define a function (plot_age_distribution) 
to plot the Histogram for the age distribution of the people
killed by police
"""


def plot_age_distribution(data, xlabel='', ylabel=''):
    """
    Plot total_value_race data using Matplotlib.

    Parameters:
    data is  DataFrame containing the data.
    title is Title of the plot.
    xlabel is Label for the x-axis.
    ylabel is Label for the y-axis.
    """

    # Create a histogram for the age distribution
    plt.hist(data["age"], bins=20)

    # Labeling
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)

    # Title
    plt.title("The Age Distribution of the People Who Were Killed")

    # Save the plot as a png
    plt.savefig('my_plot3.png')
    plt.show()
    return


# Read excel file
df = pd.read_excel("police_killing.xlsx")

# Printing of the first 5 data from my data
print(df.head())

# Printing the information about my data
print(df.info())

# Printing the columns in my data
print(df.columns)

# Printing the sum of total null values in each column
print(df.isnull().sum())

# Checking for duplicates
print(df.duplicated().sum())

# Getting the unique data in raceethnicity group
print(df["raceethnicity"].unique())

# Getting the unique data in the month group
print(df["month"].unique())


"""
Created a new column(months) and used .map() function to map values from the
existing column (month) to their corresponding numerical values.
"""
df['months'] = df['month'].map({'January': 1, 'February': 2, 'March': 3,
                                'April': 4, 'May': 5, 'June': 6})

# Printing of the first 5 data from my data after creating a new column
print(df.head())


"""
1st Visualization
Creating a new variable that shows the number of each race killed by police 
in each month.
"""


race_killed_by_month = df.groupby(
    ["raceethnicity", "months"]).size().reset_index(name='values')

# Renamed the columns for the new variable(race_killed_by_month) as months
# and values
print(race_killed_by_month)

# Called the function with my variable(race_killed_by_month)
print(plot_race_killed_each_month(race_killed_by_month, 'months', 'values',
                            title='Trends in the Total Deaths by Race/Ethnicity for Each Month',
                            xlabel='Months', ylabel='Values'))


"""I grouped by the raceethnicity and months columns and count 
the value for each month. I called my function to plot bar chart for the total
count of each raceethnicity"""


"""
2st Visualization
Creating a new variable that shows that count the  number of each 
raceethnicity that got killed by police 
"""

# created a new variable for the value count of all race/ethnicities
total_value_race = df["raceethnicity"].value_counts()
print("The value count of each raceethnicity:", total_value_race)

# Called the function with my variable(total_value_race)
print(plot_total_value_race(total_value_race,
                      title='The Total Number of Each Race/Ethnicity',
                      xlabel='raceethnicity', ylabel='Values'))


"""
3rd Visualization
"""
# Replace "Unknown" values in the age column with 0
df["age"] = df["age"].replace(["Unknown"], 25)


# Called the function with my dataset (df)
print(plot_age_distribution(df, xlabel='Age', ylabel='Frequency'))

"""When I checked the data type of the age column, I realised that it was an 
object.instead of an integer, so I found out the age column has string values 
that made The age column data type is an object instead of an integer, so I 
looked for the string values, and I replaced them with an integer value (25),
 and they are 4 innumbers. 
 and I called my function to plot the age distribution. 
 """
