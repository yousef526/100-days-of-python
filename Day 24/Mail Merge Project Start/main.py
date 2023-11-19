#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

letter = ""
with open("./input/Letters/starting_letter.txt") as f:
    letter = f.read()

names = []

with open("./input/Names/invited_names.txt") as f:
    names = f.read().split("\n")

for name in names:
    with open(f"./Output/ReadyToSend/letter_for_{name}.txt",mode='w') as f:
        substring = letter[5:11] # or i can write [name] as may be the place change
                                 #but still same item that i replace
        replaced_letter = letter.replace(substring,name)# = name
        f.write(replaced_letter)
    