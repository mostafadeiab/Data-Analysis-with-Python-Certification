import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv')

    # Create scatter plot
    plt.figure(figsize=(10, 6))
    plt.scatter(df['Year'], df['CSIRO Adjusted Sea Level'], color='blue')

    # Create first line of best fit
    slope, intercept, _, _, _ = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
    sea_lvl = intercept + slope * pd.Series(range(df['Year'].min(), 2051))
    plt.plot(pd.Series(range(df['Year'].min(), 2051)), sea_lvl, color='red')

    # Create second line of best fit
    data = df[df['Year'] >= 2000]
    slope, intercept, _, _, _ = linregress(data['Year'], data['CSIRO Adjusted Sea Level'])
    sea_lvl = intercept + slope * pd.Series(range(2000, 2051))
    plt.plot(pd.Series(range(2000, 2051)), sea_lvl, color='green')

    # Add labels and title
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.title('Rise in Sea Level')

    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()