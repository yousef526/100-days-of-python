import random

"""userChoice = int(input("Enter 0 for rock, 1 for paper or 2 for scissors: "))

listChoice = [0,1,2]
listChoice = random.randint(0,2) # better coding
computerChoice = random.choice(listChoice)

if userChoice == computerChoice:
    print("It`s tie")

elif userChoice == 0 and computerChoice == 1:
    print("you lose")

elif userChoice == 1 and computerChoice == 2:
    print("you lose")

elif userChoice == 2 and computerChoice == 0:
    print("you lose")

elif userChoice == 0 and computerChoice == 2:
    print("you win")

elif userChoice == 1 and computerChoice == 0:
    print("you win")

elif userChoice == 2 and computerChoice == 1:
    print("you win")
print(computerChoice)"""

#####################################################
"""randomNumber = random.random()+random.randint(0,6)
print(round(randomNumber,2))

# or solution
randomNumber = random.random()*5
print(round(randomNumber,2))

randomNumber = random.randint(0,1)

if randomNumber == 0:
    print("head")
else:
    print("tail")"""

##############################################

#see list documention of python xaxaxaxaxa
#exercise

#names = input("Enter name: ").split(', ')
#print(names)
#print(f"{random.choice(names)} will buy us the meal today!")
#################################################

#exercise

"""row1 = ["😀","😀","😀"]
row2 = ["😀","😀","😀"]
row3 = ["😀","😀","😀"]

tresure = [row1,row2,row3]
print(f"{tresure[0]}\n{tresure[1]}\n{tresure[2]}\n")

location = input("Enter location: ")
#vertical first then horiztonal second
tresure[int(location[1])-1][int(location[0])-1] = 'x'
print(f"{tresure[0]}\n{tresure[1]}\n{tresure[2]}\n")"""

###################################
# rock paper scsoirss game with modication
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

shpaes = [rock,paper,scissors]

userChoice = int(input("Enter 0 for rock, 1 for paper or 2 for scissors: "))
computerChice = random.randint(0,2)

if userChoice >= 3:
    print("invalid input lose")
else:
    print(shpaes[userChoice])
    if computerChice > userChoice:
        print(shpaes[computerChice])
        print("You lose")
    elif computerChice < userChoice:
        print(shpaes[computerChice])
        print("You Win")
    elif computerChice == userChoice:
        print(shpaes[computerChice])
        print("Tie")

    elif computerChice == 0 and 2 == userChoice:
        print(shpaes[computerChice])
        print("You Lose")

    elif computerChice == 2 and 0 == userChoice:
        print(shpaes[computerChice])
        print("You Win")
