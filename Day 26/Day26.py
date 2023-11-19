# normal way for calcaulting numbers and put them in list
""" lis = [1,2,3]
new_list = []
for n in lis:
    new_list.append(n+1)

print(new_list) """

# other way with list comperhiension

""" #lis = [1,2,3]

#new_lis = [x**7 for x in lis]
#print(new_lis)

#name = 'Hamo bta3 el smk'
#chars = [letter for letter in name]
#print(chars) 
lis22 = [x*2 for x in range(1,5)]
print(lis22)
"""





# List comperhinesion with conditonal if

""" lis22 = [x*2 for x in range(1,5) if x > 3]
#print(lis22)

names = ['Alex','Beth','Caroline','Dave','Eleanor','Freddie']
cap = [name.upper() for name in names if len(name) > 5]
print(cap) """

#####################################################################################################
# exercise1 square numbers
"""
numbers = [1,1,2,3,5,8,13,21,34,55]

squared_number = [number**2 for number in numbers]
print(squared_number) 

# get even numbers
even_number = [number for number in numbers if number % 2 == 0]
print(even_number)"""
#############################################################################################
# exercise 2

""" lis1 = []
lis2 = []

with open('file1.txt') as file1, open('file2.txt') as file2:
    lis1 = file1.read().split()
    lis2 = file2.read().split()

# choose lis2 as it has taller length
res = [int(item) for item in lis1 if item in lis2]
print(res) """

#########################################################
# dictionary comperheinson
""" import random

names = ['Alex','Beth','Caroline','Dave','Eleanor','Freddie']

scores = {val:random.randint(1,100) for val in names}
print(scores)

passed_students = {val:scores[val] for val in scores if scores[val] > 50}
print(passed_students)

# another way for same dict
passed_students = {name:score for (name,score) in scores.items() if score > 50}

print(passed_students) """

#############################################################
#exercise1

""" sentence = "What is the Airspeed Velocity of an Unladen Swallow?"

dict_22 = {word:len(word) for word in sentence.split()}
print(dict_22) 

#exercise2
# to change from celsius to feherinet temp_f = (temp_c * 9/5) + 32
weather_c = {
    'Monday':12,
    'Tuesday':14,
    'Wednesday':15,
    'Thursday':14,
    'Friday':21,
    'Saturday':22,
    'Sunday':24,
}

weather_f = {day:(temp_c * 9/5) + 32 for (day,temp_c) in weather_c.items() }
print(weather_f)

# or other way

weather_f = {day:(weather_c[day] * 9/5) + 32 for day in weather_c}
print(weather_f)"""

########################################
#looping on a dataframe
import pandas as pd

student_dict = {
    "Studnet":["Yousef","Ahmed","Hani"],
    "score":[56,76,98],
}

df = pd.DataFrame(student_dict)

# looping through a DataFrame is like looping in dictionary
""" for (key,value) in df.items():
    print(value) """


# pandas has its iterate way as built in function, iterate over index of row and the row itself
for (index,row) in df.iterrows():
    print(row.score)# could choose speific coulmn name