import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv')
    df = df[['Year', 'CSIRO Adjusted Sea Level']]

    fig, ax = plt.subplots(figsize=(6,6))
    # Create scatter plot
    ax.scatter(df['Year'], df['CSIRO Adjusted Sea Level'])


    # Create first line of best fit
    lr_result = linregress(x=df['Year'], y=df['CSIRO Adjusted Sea Level'])
    # create a dataframe of the linreg intercepts for all years in df (x values) to to 2050
    l = []
    for year in range(df['Year'].min(), 2051):
        l.append([year, year * lr_result[0] + lr_result[1]])
    df_to_add = pd.DataFrame(l, columns=df.columns)
    ax.plot(df_to_add['Year'], df_to_add['CSIRO Adjusted Sea Level'], color='orange')


    # Create second line of best fit
    df_recent_years = df.loc[df['Year'] >= 2000]
    lr2_result = linregress(x=df_recent_years['Year'], y=df_recent_years['CSIRO Adjusted Sea Level']) 
    # create a dataframe of the linreg intercepts for all years sicne 2000 (x values) to to 2050
    l = []
    for year in range(2000, 2051):
        l.append([year, year * lr2_result[0] + lr2_result[1]])
    df_to_add = pd.DataFrame(l, columns=df.columns)
    ax.plot(df_to_add['Year'], df_to_add['CSIRO Adjusted Sea Level'], color='r')


    # Add labels and title
    ax.set_xlabel('Year')
    ax.set_ylabel('Sea Level (inches)')
    ax.set_title('Rise in Sea Level')

    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()