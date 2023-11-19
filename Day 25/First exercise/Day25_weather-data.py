# csv = comma separated values


""" import csv
with open('227 - weather-data.csv') as data:
    df = csv.reader(data)
    temp = []
    for row in df:
        if row[1] == 'temp':
            pass
        else:
            temp.append(int(row[1]))
    print(temp) """

import pandas as pd


df = pd.read_csv('227 - weather-data.csv')

#print(type(df)) # it gives type of dataframe which is 2 d
#print(type(df['temp'])) # it gives type of series which is 1 d
#print(df.to_dict())

temp_list = df['temp'].to_list()
avg = sum(temp_list) / len(temp_list)
#print(avg)

#print(df['temp'].mean())
#print(df['temp'].max())

# GEt data in coulmn
#print(df['temp'])
#print(df.temp)

# get data in row
#print(df[df.day =="Wednesday"])
#print(df[df.temp == df['temp'].max()])

monday = df[df.day == "Monday"]
monday_temp = int(monday.temp) * (9/5) + 32
print(monday_temp)

# create a dataframe from scratch

dict_22 = {
    "Students":["Amy","Abbas","ALi","Mohmaed"],
    "Scores":[12,43,45,16]
}

df22 = pd.DataFrame(dict_22)
print(df22)
df22.to_csv('New.csv')