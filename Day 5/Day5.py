import random

"""Symbols = ["{","}","(",")","[","]",'.',',',':',';','+','-',"*","/","&","|","<",">","="]
alphbet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
            'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

numbers_list = [0,1,2,3,4,5,6,7,8,9]

chars = int(input("Enter number of letters in your password: "))

symbols = int(input("Enter number of symbols in your password: "))

numbers = int(input("Enter number of numbers in your password: "))

random_choices = []
password = ""

for i in range(0,chars):
    choice = random.randint(0,1)
    if choice == 0:
        random_choices.append(random.choice(alphbet).lower())
    else:
       random_choices.append(random.choice(alphbet).upper())

for i in range(0,symbols):
    random_choices.append(random.choice(Symbols))

for i in range(0,numbers):
    random_choices.append(random.choice(numbers_list))


random.shuffle(random_choices)

for i in random_choices:
    password+=str(i)

print("Here is your password: %s"%password)"""
############################################

#exercise cal averge height

"""studnets = input("Enter studnets heights separated by space: ").split()
total = 0
for i in studnets:
    total+=int(i)
total = total/len(studnets)

#other way to get sum use sum for list
print("Avg height is %.1f"%total)"""

############################################
#exercise highest height

"""studnets = input("Enter studnets heights separated by space: ").split()
for i in range(0,len(studnets)):
    studnets[i] = int(studnets[i])
heighest = studnets[0]

for i in range(1,len(studnets)):
    if heighest < studnets[i]:
        heighest = studnets[i]


#other way to get sum use sum for list
print("Tallest height is %d"%heighest)"""
################################
#range(start,end,step) step means how many can we increase

# calculate even number from 0 to 100
"""sum_ = 0
for i in range(0,101,2):
    sum_+=i

print(sum_)


#exercise fizzbuzz


for i in range(1,101):
    if i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    elif i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    else:
        print(i)"""

#################################