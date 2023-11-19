#black jack 
import os
import random

cards = ['ace',2,3,4,5,6,7,8,9,10,10,10,10]
user_cards = []
comupter_cards = []

def ace_check(lis_cards,choice):
    if choice == 'ace':
        if 11+sum(lis_cards) <= 21:
            lis_cards.append(11)
        else:
            lis_cards.append(1)
    else:
        lis_cards.append(choice)

def initie_lists(user_cards,comupter_cards):
    user_cards = []
    comupter_cards = []
    for i in range(2):
        ace_check(user_cards,random.choice(cards))
        ace_check(comupter_cards,random.choice(cards))
    return user_cards,comupter_cards

def earlyStop(user_cards,comupter_cards):
    if sum(user_cards) > 21:
        print(f"Your final cards are: {user_cards}, final score: {sum(user_cards)}")
        print(f"computer final cards are: {comupter_cards}, final score: {sum(comupter_cards)}")
        print("You Went over. you lose")
        return True
    elif sum(user_cards) == 21 and sum(comupter_cards) == 21:
        print(f"Your final cards are: {user_cards}, final score: {sum(user_cards)}")
        print(f"computer final cards are: {comupter_cards}, final score: {sum(comupter_cards)}")
        print("it`s Draw")
    elif sum(user_cards) == 21:
        print(f"Your final cards are: {user_cards}, final score: {sum(user_cards)}")
        print(f"computer final cards are: {comupter_cards}, final score: {sum(comupter_cards)}")
        print("You Won")
        return True
    else:
        return False

def winner_check(user_cards,comupter_cards):
    while True:
        if sum(comupter_cards) >= 17 and sum(comupter_cards) <= 21:
            if sum(comupter_cards) > sum(user_cards):
                print(f"Your final cards are: {user_cards}, final score: {sum(user_cards)}")
                print(f"computer final cards are: {comupter_cards}, final score: {sum(comupter_cards)}")
                print("You lose")
                return 2 # return True means computer wins
            elif sum(comupter_cards) == sum(user_cards):
                print(f"Your final cards are: {user_cards}, final score: {sum(user_cards)}")
                print(f"computer final cards are: {comupter_cards}, final score: {sum(comupter_cards)}")
                print("It is a draw")
                return 0 # means draw
            elif sum(comupter_cards) < sum(user_cards):
                print(f"Your final cards are: {user_cards}, final score: {sum(user_cards)}")
                print(f"computer final cards are: {comupter_cards}, final score: {sum(comupter_cards)}")
                print("You Wins")
                return 1 #means user wins
        elif sum(comupter_cards) > 21:
            print(f"Your final cards are: {user_cards}, final score: {sum(user_cards)}")
            print(f"computer final cards are: {comupter_cards}, final score: {sum(comupter_cards)}")
            print("You Wins")
            return 1 # means user wins
        else:
            ace_check(comupter_cards,random.choice(cards))
            continue 
        
while True:
    user_cards,comupter_cards = initie_lists(user_cards,comupter_cards)
    play_choice = input("Do you want to play Blackjack? Type 'y' or 'n': ")
    if play_choice == 'y':
        os.system('cls')
        while True:
            print(f"Your cards are: {user_cards}, Current score: {sum(user_cards)}")
            print(f"Computer first card: {comupter_cards[0]}")
            if earlyStop(user_cards,comupter_cards):# used to check early stop if has more than 21 
                break
            choice_to_play = input("Type 'y' to get another card, type 'n' to pass: ")
            if choice_to_play == 'y':
                ace_check(user_cards,random.choice(cards))
                continue
            elif choice_to_play == 'n':
                winner_check(user_cards,comupter_cards)
                break
    else:
        break
