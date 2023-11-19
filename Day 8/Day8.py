#exercise 1
import math

"""def greet_with(name,location):
    print(f"Hello {name} from {location} ?")
    print("What is it like in %s"%location)
#greet_with(name='Ahmed',location='Tanta')

def calc_area(height,width,coverage):
    area = math.ceil((height*width)/coverage)
    print(f"You `ll need {area} of paint can")

h = int(input("Enter height of wall: "))
w = int(input("Enter width of wall: "))
calc_area(h,w,5)"""
#############################
#exercise 2
#prime number checker
"""def prime_checker(number):
    check = True
    for i in range(2,number):
        if number % i == 0:
            print("Not prime")
            check = False
            break
    if check:
        print("Prime Number")

x = int(input("Check number: "))
prime_checker(number=x)""" 

################################
#final exercise ceasper
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g',
             'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r',
               's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def cipher2(Msg,shiftNumber,process_type):
    output = ''
    for i in Msg:
        if i not in alphabet:
            output+=i
        elif process_type.lower() == 'encode':
            index = alphabet.index(i)
            index+=shiftNumber
            index %= 25
            output+=alphabet[index]
        else:
            index = alphabet.index(i)
            index-=shiftNumber
            index = (index + 25) if index < 0 else index
            index %= 25
            output+=alphabet[index]
    print(f"The {process_type}d text is {output}")

while True:
    Msg = input("Enter your message: ").lower()
    processType = input("Enter your process type: ")
    shiftNumber = int(input("Enter your shift number: "))

    cipher2(Msg,shiftNumber,processType)
    repeat = input("Do you want to start program agian? Yes or No? ")
    if repeat.lower() == 'no':
        break
#qnuux gxbum