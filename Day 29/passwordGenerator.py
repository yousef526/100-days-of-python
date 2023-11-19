import random
SYMBOLS = ["(",")",'#','+','$',"*","&"]
ALPHBET = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
            'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
NUMBERS = [0,1,2,3,4,5,6,7,8,9]

CHARS_NUMBER = 8

SYMBOLS_NUMBER = 4

NUMBERS_COUNT = 4

class PasswordGenerate():

    def __init__(self):
        self.random_choices = []
        self.password = ""
        pass

    def generatePass(self):

        for i in range(0,CHARS_NUMBER):
            choice = random.randint(0,1)
            if choice == 0:
                self.random_choices.append(random.choice(ALPHBET).lower())
            else:
                self.random_choices.append(random.choice(ALPHBET).upper())

        #adding symbols
        [self.random_choices.append(random.choice(SYMBOLS)) for _ in range(SYMBOLS_NUMBER)] 

        #adding numbers
        [self.random_choices.append(str(random.choice(NUMBERS))) for _ in range(NUMBERS_COUNT)]

        random.shuffle(self.random_choices)

        password = ''.join(self.random_choices)
        return password







