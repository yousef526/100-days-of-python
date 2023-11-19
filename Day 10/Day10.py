# convert string to title case in python use str.title()

"""print("hello world".title())

#Mulitple return values

def format_name(f_name,l_name):
    if f_name == "" or l_name =='':
        return 'you didnt enter input'
    formated_fname = f_name.title()
    formated_lname = l_name.title()
    #return f_name,l_name
    return formated_fname+" "+formated_lname

print(format_name('AHMed','aBBas'))"""

##########################################
# exercise
"""def is_leap(year):
    if year % 4 == 0:
        if year % 400 == 0:
            return True
        elif year % 100 == 0 and year % 400 != 0:
            return False 
        else:
            return True
    else:
        return False
    
def days_in_month(year,month):
    #return number of days of given month
    month_days = [31,28,31,30,31,30,31,31,30,31,30,31]
    if is_leap(year) and month == 2:
        var = month_days[month-1]+1
        return var
    else:
        return month_days[month-1]


year = int(input("Enter the year: "))
month = int(input("Enter the month: "))
print(days_in_month(year,month))"""
###############################
# the calculator
from logo import art

def add(number1,number2):
    return number1+number2
def mult(number1,number2):
    return number1*number2
def subtract(number1,number2):
    return number1-number2
def divide(number1,number2):
    return number1/number2

operations_dict = {
    '+':add,
    '-':subtract,
    '*':mult,
    '/':divide,
}


print(art)
res = 0
first_number = float(input("Enter first Number:"))
operation = input("+\n*\n-\n/\nEnter operation sign: ")
second_number = float(input("Enter second Number:"))
operation_lis = ['+','/','-','*']
choice = 0
while True:
    function = operations_dict[operation]
    res = function(first_number,second_number)
    print(f"{first_number} {operation} {second_number} = {res}")
    choice = input(f"Want to contiune with {res} press 'y' to contiune or 'n' to start new calculation or x to exit ")
    if choice.lower() == 'n':
        first_number = int(input("Enter first Number:"))
        operation = input("+\n*\n-\n/\nEnter operation sign: ")
        second_number = int(input("Enter second Number:"))
    elif choice.lower() == 'y':
        first_number = res
        operation = input("+\n*\n-\n/\nEnter operation sign: ")
        second_number = int(input("Enter second Number:"))
    else:
        print("Goodbye!")
        break