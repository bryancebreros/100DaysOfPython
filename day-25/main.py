# import csv
# with open("weather_data.csv") as file:
#     data = csv.reader(file)
#     temperatures = []
#     for row in data:
#         if row[1] != 'temp':
#             temperatures.append(int(row[1]))
#     print(temperatures)
import pandas

data = pandas.read_csv("weather_data.csv")
data_dict = data.to_dict()
print(data_dict)
def faren(c):
  return (c * 1.8 +32 )
temp_list = data["temp"].to_list()
# AVERAGE
avg = sum(temp_list) / len(temp_list)
mean = data["temp"].mean()
count = data["temp"].count()
print("---------")
print(count)
# HIGHEST DATA
data["temp"].max()
# ALSO SELECTS [NEEDS CAPITALIZE]
print(data.temp)

# GET DATA IN ROWS
print(data[data.day == "Monday"])
print(data[data.temp == data.temp.max()])

#GET DATA IN A ROW
monday = data[data.day == "Monday"]
print(faren(monday.temp))

# CREATE DATAFRAME
thisdict = {
  "brand": ["Ford", "JEEP", "Honda"],
  "model": ["Mustang", "jeep", "civic"],
  "year": [1964, 2010, 2020]
}
cars = pandas.DataFrame(thisdict)
cars.to_csv("cars.cvs")
print(avg)