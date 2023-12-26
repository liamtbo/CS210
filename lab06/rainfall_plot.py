'''
CIS lab06
Liam Bouffard
'''

import doctest
# import numpy as np
# import matplotlib.pyplot as plt


def read_csv(path: str):
    """Read one column from a CSV file with headers into a list of strings.
     """
    # Part-1- read the csv file and make a list 
    with open(path, 'r') as f:
        lines = [line.rstrip() for line in f]  # skip the '\n' in csv file
    # pseudo code: separate each line by "," and store list in data_list
        data_list = [data_rainfall.split(',') for data_rainfall in lines]

    # Part-2 - convert list of list into dissctionary, where key is year
    data_dict = {row[0][:4]:(float(row[1])) for row in data_list}
    
    return data_dict

def average_rainfall(rainfall_values: dict)-> float:
    mean_rainfall = 0
    # pseudo code: calculate the average rainfall value
    for year_key in rainfall_values:
        mean_rainfall += (rainfall_values[year_key])
    mean_rainfall = mean_rainfall / len(rainfall_values)
    
    print('This is the mean of rainfall: ', mean_rainfall)
    return mean_rainfall

def high_rain(rainfall_values: dict, mean_rainfall: float):
    high_rain_years = [year_key for year_key in rainfall_values if rainfall_values[year_key] > (1.5 * mean_rainfall)]

    print("High rain year: " + str(high_rain_years))
    return high_rain_years

def main():
    rainfall_values = read_csv("november_rain.csv")
    result = average_rainfall(rainfall_values)
    high_rain(rainfall_values, result)

    # for plotting the graph
    years = list(rainfall_values.keys())
    values = list(rainfall_values.values())
    mean_rainfall = result
    # plt.xlabel('Years')
    # plt.ylabel('Precipitation')
    # plt.title('Years vs precipitation with Average (red)')
    # plt.bar(years, values, width=0.8)
    # csv list long, only couple of years are shown within 10 years interval.
    # plt.xticks(np.arange(min(years), max(years), 5), rotation=45)
    # plt.axhline(y=mean_rainfall, color='r', linestyle='-')
    # plt.show()

if __name__ == "__main__":
    main()