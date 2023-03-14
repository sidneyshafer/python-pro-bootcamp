# with open("weather_data.csv") as data_file:
#     data = data_file.readlines()
#     print(data)

import csv

# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperatures = []
#     for row in data:
#         if row[1] != "temp":
#             temperatures.append(int(row[1]))
#     print(temperatures)

import pandas
# pandas doc: https://pandas.pydata.org/docs/

data = pandas.read_csv("weather_data.csv")
# print(type(data)) # DataFrame
# print(type(data["temp"])) # Series

# Convert data to a dictionary
data_dict = data.to_dict()
# print(data_dict)

temp_list = data["temp"].to_list()

# Calculate Average
average = sum(temp_list) / len(temp_list)
# print(average)

# Calculate Average using Pandas method
print(data["temp"].mean())

print(data["temp"].max())

# Get Data columns
# print(data["condition"])
print(data.condition)

# Get data in row
print(data[data.day == "Monday"])
print(data[data.temp == data.temp.max()])

monday = data[data.day == "Monday"]
print(monday.condition)
monday_temp = int(monday.temp)
f_temp = (monday_temp * 9/5) + 32
print(f_temp)

# Create a dataframe from scratch
data_dict = {
    "students": ["Allie", "Sidney", "Lisa", "Brent"],
    "scores": [100, 95, 99, 60]
}

data = pandas.DataFrame(data=data_dict)
print(data)
data.to_csv("new_data.csv")
