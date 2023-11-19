# looping on dictioneries with one value only it loops on only the key

# exercise 1

"""student_scores = {
    'Harry':81,
    'Ron':89,
    'Hermine':99,
    'Draco':74,
    'Nevile':62,
}
print(student_scores)
student_grades = {}
for key in student_scores:
    if student_scores[key] > 90:#student_scores[key] >= 91 and student_scores[key] <= 100 old condition and change the rest
        student_grades[key] = 'Outstanding'
    elif student_scores[key] > 80:
        student_grades[key] = 'Exceeds Expections'
    elif student_scores[key] > 70:
        student_grades[key] = 'Acceptable'
    else:#short it with else instead of elif student_scores[key] <= 70
        student_grades[key] = 'Fail'

print(student_grades)"""

################################


"""def add_new_country(country,visits,cities,travel_log):
    value = {"Country":country,'total_visits':visits,'Cities_visited':cities}
    travel_log.append(value)

travel_log = [
    {"Country":"France",'total_visits':2,'Cities_visited':['paris','monaco']}
]
print(travel_log)
add_new_country('Egypt',4,['Fayuom','Cairo'],travel_log)
add_new_country('Russia',6,['Saint Fatima','Moscow'],travel_log)

print(travel_log)"""

########## 
#exercise
import os
from art import logo

print(logo+'\n')
print("Welcome to auction")
def get_max_bid(bidders):
    name = ''
    max_bid = -1
    for key in bidders:
        if max_bid < bidders[key]:
            max_bid = bidders[key]
            name = key
    print(f"The Winner is {name} with bid = {max_bid}")

dict_bidders = {}

while True:
    name = input("Enter your name: ")
    bid = int(input("Enter your bid:$ "))
    dict_bidders[name] = bid
    choice = input("Do you wish to contiune? Yes or No ")
    if choice.lower() == 'no':
        break
    else:
        os.system('cls')



get_max_bid(dict_bidders)
