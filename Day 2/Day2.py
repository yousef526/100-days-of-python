print("Welcome to the tip calculator")
bill = float(input("What was the total bill? $"))
no_of_people = int(input("How many people to split the bill? "))
tips = int(input("What perctange of tip you would like to give? 10, 12, or 15? "))/100
total = (bill/no_of_people)+((bill/no_of_people)*tips)
print("Each person should pay: %.2f"%total)

#####################################################
"""print("hellloo"[::-1])
print("hellloo"[1::])
print("hellloo"[0:4])
print("hello"[-1])

# can write here big numbers with underscores
print(123_545_654_841)
print(123545654841)
ins = "angel"
print("you %d chars"%len(ins))
"""

###################################################
#exercise

"""digits = input("Enter your digits: ")
total = int(digits[0])+int(digits[1])
print("The sum is %d"%total)"""

#####################################

# // for integer division
# / for float division
#print(6//3)

# ** for power
#print(6**2)
"""
proirty
()
**
mult
divsion
addation
subtraction
"""
#print(3*3+3/3-3)
#print(3*(3+3/3-3))

###########################

#exercise BMI calculator

"""weight = float(input("Enter your weight in Kg "))
height = float(input("Enter your height in Meter "))
mass = weight / (height**2)
print("Your body mass is %d kg/m2" %mass)"""

#####################################################
"""
print(8/3)
print(8//3)
print(round(8/3,4))
"""
#####################################################

#exercise

"""age = int(input("Enter your age: "))

lefted_years = 90 - age

days = 365 * lefted_years
weeks = 52 * lefted_years  
months = 12 * lefted_years

print(f"You have {days}, {weeks} and {months} months left")"""
