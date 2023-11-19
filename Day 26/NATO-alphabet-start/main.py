# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

#TODO 1. Create a dictionary in this format:
{"A": "Alfa", "B": "Bravo"}

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.

import pandas as pd

df = pd.read_csv(r'F:\python course practice\Day 26\NATO-alphabet-start\nato_phonetic_alphabet.csv')

dict_22 = {val.letter:val.code for (_,val) in df.iterrows()}
#print(dict_22)

while True:
    try:
        user_input = input("Enter word: ")
        lis22 = [dict_22[letter.upper()] for letter in user_input]
    except KeyError:
        print("Sorry, only letters in the alphabet please.")
    else:
        print(lis22)