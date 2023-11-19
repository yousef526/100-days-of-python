import art
from game_data import data
import random
import os
# do the rest of conditions and the writing
user_score = 0

choice_A = random.choice(data)
choice_B = random.choice(data)

correct = True   #will be used for while loop condition
while correct:
    os.system('cls')
    print(art.logo)
    while choice_B == choice_A:
        choice_B = random.choice(data)
    if user_score > 0:
        print(f"You're right! Current score: {user_score}.")# in case guess right and made only after first right guess
    print(f'Compare A: {choice_A["name"]}, a {choice_A["description"]}, from {choice_A["country"]}.')
    print(art.vs)
    print(f'Against B: {choice_B["name"]}, a {choice_B["description"]}, from {choice_B["country"]}.')
    user_choice = input(f"Who has more followers? Type 'A' or 'B': ")
    if user_choice.lower() == 'a':
        if choice_A['follower_count'] > choice_B['follower_count']:
            user_score+=1
            choice_A = choice_B
            choice_B = random.choice(data)
        else:
            correct = False
            
    else:
        if choice_B['follower_count'] > choice_A['follower_count']:
            user_score+=1
            choice_A = choice_B
            choice_B = random.choice(data)
        else:
            correct = False
        

if not correct:
    os.system('cls')
    print(art.logo)
    print(f"Sorry, that's wrong. Final score: {user_score}") # in case losing and exit the game