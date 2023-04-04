import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import os
import pdb


# Function to get filename as parameter and return 2 dataframes.
def my_func_to_read_world_bank_data(filename):
    dataframe_one = pd.read_csv(filename, skiprows=4)
    dataframe_one = dataframe_one.drop(columns=['Country Code', 'Indicator Name', 'Indicator Code'])
    dataframe_one = dataframe_one.dropna(how='all')
    dataframe_one = dataframe_one.set_index('Country Name')
    data_frame_two_years_dataframe_one = dataframe_one.T
    return dataframe_one, data_frame_two_years_dataframe_one


def main_function():
    # Calling my function and returning two dataframes
    dataframe_one, data_frame_two_years_dataframe_one = my_func_to_read_world_bank_data(
        os.getcwd() + "\\ClimateChange.csv")

    # Initializing the list and using describe method for summary.
    countries = ['United States', 'China', 'India', 'Germany', 'United Kingdom']
    print("\nUsing describe method\n")
    print(dataframe_one.loc[countries, '2016'].describe())

    # Plotting First Graph
    sns.boxplot(x='Country Name', y='2016', data=dataframe_one.loc[countries].reset_index())
    plt.ylabel('CO2 emissions per capita (metric tons)')
    plt.show()

    # Plotting Second Graph
    countries = ['United States', 'China', 'India', 'Germany', 'United Kingdom']
    dataframe_one.loc[countries, '1990':].plot()
    plt.ylabel('CO2 emissions (metric tons per capita)')
    plt.show()

    # Plotting Bar Graph
    my_df = pd.read_csv('ClimateChange.csv', skiprows=4)
    my_df = my_df.drop_duplicates(subset=["Country Name"], keep='first').head(10)
    my_df.plot.bar(x="Country Name", y="2000", rot=70, title="Bar Graph")
    plt.show(block=True)

    # Plotting Fourth graph
    my_df = pd.read_csv('ClimateChange.csv', skiprows=4)
    my_df = my_df.drop_duplicates(subset=["Country Name"], keep='first').head(3)
    plt.plot(my_df["Country Name"], my_df["2000"])
    plt.show()

    # Plotting Fifth graph
    countries = ['Angola', 'Albania', 'Bahrain', 'Latvia']
    dataframe_one.loc[countries, '2019':].plot()
    plt.ylabel('Energy use (kg of oil equivalent per capita)')
    plt.show()


if __name__ == "__main__":
    print("********************** Tool Started **********************\n")

    # Calling main_function()
    main_function()

    print("\n\n********************** Tool Finished **********************")
