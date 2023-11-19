"""x = 1

def inc():
    x = 2
    print("inside",x)

inc()
print("outside",x)

def game():
    def drink():
        postion = 2
        print(postion)
    drink()
game()


if 5 > 3:
    aa = 22
print(aa)"""
############################################################################################
# to make a change on outside value from a funtion must declare global 
# variable in the local scope of function

"""x = 1

def inc():
    global x
    x += 2
    print("inside",x)

inc()
print("outside",x)"""
##############################
#naming conevtion in python for const variables is to name it in big cas

"""PI = 3.1415926
print(x+0.3516854968465198)
def calc():
    PI"""
##########################
#final project guess the number
import random
from art import logo
def check_losing(lives):
    if lives == 0 :
        print("You've run out of guesses, you lose.")
        return False
    else:
        print("Guess agian.")
        return True

print(logo)
print('Welcome to the Number Guessing Game!')
print("I'm thinking of a number between 1 and 100.")
diculty = input("Choose a difficulty. Type 'easy' or 'hard': ")
if diculty.lower() == 'easy':
    lives = 10
else:
    lives = 5




computer_guess = random.randint(1,100)
print(computer_guess)
flag = True
while flag:
    print(f"You have {lives} attempts remaining to guess the number.")
    guess = int(input("Make a guess: "))
    if guess > computer_guess:
        print("Too high.")
        lives-=1
        flag = check_losing(lives)
    elif guess < computer_guess:
        print("Too low.")
        lives-=1
        flag = check_losing(lives)
    else:
        print(f"You got it! The answer was {guess}.")
        break