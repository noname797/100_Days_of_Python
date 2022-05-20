import csv

import pandas as pd
import numpy as np



# with open('226 weather-data.csv') as file:
#     weather_data = [i for i in file.readlines()]
#
# print(weather_data[1:])

# with open('226 weather-data.csv') as file:
#     data = csv.reader(file)
#     temp = []
#
#     for row in data:
#         print(row)
#         if row[1] != 'temp':
#             temp.append(int(row[1]))
#
#     print(temp)


# data = pd.read_csv('226 weather-data.csv')
# print(data)
# print(data['temp'])
# data_dict = data.to_dict(data)
# print(data.describe())
# print(data.temp.mean())

# print(data[data.temp == max(data.temp)])

# data = pd.read_csv('228 2018-Central-Park-Squirrel-Census-Squirrel-Data.csv')
#
# print(data.head())

# fur_data = data["Primary Fur Color"].dropna().to_numpy()
# color, count = np.unique(fur_data,return_counts=True)[0], np.unique(fur_data,return_counts=True)[1]
#
# new_data = {
#     "Fur Color": color,
#     "Count": count,
# }
#
# df = pd.DataFrame(new_data)
# print(df)
# df.to_csv("squirrel_counts.csv")



