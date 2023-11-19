#Hang man
import random
import helpers
import os
#if guess is right replace letters with real one
def right_guess(dashes,usr_input,word): 
    dashes = list(dashes)
    word = list(word)
    counter = word.count(usr_input)
    while counter > 0:
        index = word.index(usr_input)
        dashes[index] = usr_input
        word[index] = '*'
        counter -= 1
    dashes_oustput = ''.join(dashes)
    return dashes_oustput
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g',
             'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r',
               's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

print("Welcome to hangman")
print(helpers.logo)
print("##########################")




random_word = random.choice(helpers.words)
dashes = ''
for char in random_word:
    dashes+='-'

allowed_guesses = 6
while '-' in dashes:
    print("Guessed word until now %s"%dashes)
    print("Number of guesses remaining: %d\n"%allowed_guesses)
    usr_input = input("Enter letter: ").lower()
    os.system('cls')
    if usr_input not in alphabet:
        print("You guessed this letter before\n")
        continue
    elif usr_input in random_word:
        dashes = right_guess(dashes,usr_input,random_word)
        alphabet.remove(usr_input)
    else:
        allowed_guesses-=1
        alphabet.remove(usr_input)
    if allowed_guesses == 0:
        break
    print(helpers.HANGMANPICS[6 - allowed_guesses])

    
if allowed_guesses == 0:
    print(helpers.HANGMANPICS[6 - allowed_guesses])
    print("\nYou LOSE")
    print("Your guess %s"%dashes)
    print("Actual word %s"%random_word)

else:
    print("You WON")