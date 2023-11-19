#Exercsie 1
# conditonal statments
"""print("Welcome to roller coster")
height = int(input("Enter your height in cm: "))
if height >= 120:
    print("You can ride")
else:
    print("You can`t ride")"""

###################################
# exercise 2 even or odd
#num = int(input("Enter no: "))
#str1 = "even" if num%2==0 else "odd"
#print(str1)

################################
#Exercsie 3
# conditonal statments
"""print("Welcome to roller coster")
height = int(input("Enter your height in cm: "))
age = int(input("Enter your age: "))
if height >= 120:
    if age < 12:
        print("You can ride after paying 5$")
    elif age <= 18:
        print("You can ride after paying 7$")
    else:
        print("You can ride after paying 12$")
else:
    print("You can`t ride")"""

#########################################
#exercise 4 BMI calc

"""weight = int(input("Enter your weight in Kg: "))
height = float(input("Enter your height in M: "))

mass = round(weight/height**2)

if mass <= 18.5:
    print("underweight")
elif mass <= 25:
    print("normal weight")
elif mass <= 30:
    print("overweight")
elif mass <= 35:
    print("obese")
elif mass > 35:
    print("clinalliy obese")"""
########################################

#exercise 5 leap year

"""year = int(input("Enter the year: "))

if year % 4 == 0:
    if year % 400 == 0:
        print("Leap year")
    elif year % 100 == 0 and year % 400 != 0:
        print("Not leap year")
    else:
        print("Leap year")
else:
    print("Not leap year")"""
############################################
# exercise with addition
"""print("Welcome to roller coster")
height = int(input("Enter your height in cm: "))
age = int(input("Enter your age: "))
bill = 0
if height >= 120:
    if age < 12:
        print("Your ticket = 5$")
        bill = 5
    elif age <= 18:
        print("Your ticket = 7$")
        bill = 7
    else:
        print("Your ticket = 12$")
        bill = 12
    photo = input("Do you want a photo? Y or N.")
    if photo == 'y' or 'Y':
        bill+=3
        
    print(f"you sholud pay {bill}$")
else:
    print("You can`t ride")"""
#############################################

#exercise pizza system
"""print("Welcome to pizza store")

pizza =  input("Enter size of your size: S, M, L ")
pepporoni = input("Want pepporoni: Y, N? ")
Extra_cheese = input("Want extra cheese: Y, N? ")
bill = 0

if pizza.lower() == 's':
    bill+=15
elif pizza.lower() == 'm':
    bill+=20
elif pizza.lower() == 'l':
    bill+=25

if pepporoni.lower() == 'y':
    if pizza.lower() == 's':
        bill+=2
    else:
        bill+=3

if Extra_cheese.lower() == 'y':
    bill+=1

print(f"You should pay {bill}$")"""

########################
#exercise love quiz
"""print("Welcome to love calculator")
name1 = input("Enter first name: ").lower()
name2 = input("Enter second name: ").lower()

True_word = name1.count('t')+name1.count('r')+name1.count('u')+name1.count('e')+name2.count('t')+name2.count('r')+name2.count('u')+name2.count('e')


love_word = name1.count('l')+name1.count('o')+name1.count('v')+name1.count('e')+name2.count('l')+name2.count('o')+name2.count('v')+name2.count('e')


total_score = int(str(True_word)+str(love_word))

if total_score < 10 or total_score > 90:
    print(f"Your score is {total_score}, you go together like coke and mentos.")

elif total_score <= 50 and total_score >= 40:
    print(f"Your score is {total_score}, you are alright together")
else:
    print("Your score is %d."%total_score)"""
##########################################################
#last exercise

print("Welcome to Treasure Island.")
print("Your mission is to find the treasure")

choice_1 = input("Enter your choice:left or right? ").lower()

if choice_1 == 'left':
    choice_1 = input("Enter your choice:swim or wait? ").lower()
    if choice_1 == 'wait':
        choice_1 = input("Enter your choice:Which door Red, blue or yellow ").lower()
        if choice_1 == "red":
            print("Burned by fire.\nGame Over.")
        elif choice_1 == "blue":
            print("Eaten by beasts.\nGame Over.")
        elif choice_1 == "yellow":
            print("You Win!")
        else:
            print("Game Over.")
    else:
        print("Attacked by trout.\nGame Over.")
        
else:
    print("Fall into a hole. \nGame Over.")