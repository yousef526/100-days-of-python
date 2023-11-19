"""
So to catch an expection we have main four words
try: try smth that can cause error 
excpet: Do this if there was an exception
else: Do this if there were no excpetions (means that there were no errors)
finally: Do this no matter what happens

The most important parts are the try part and the except part and we can ignore the else and finally 
We can make many except statements as to catch different errors type
"""

# example for exception

""" try:
    with open('data.txt') as f:
        print(f.read()+"  The file contents")
except:
    print("Error occured")
 else:
    print('It went perfect with no flows')

finally:
    print("The rest of code that will happen in any case") """


# mutli excoetion for different errors
""" try:
    with open('data.txt') as f:
        print(f.read()+"  The file contents")
        dict2 = {'key':545}
        print(dict2['ke'])
except FileNotFoundError:
    print("File not found error ")

except KeyError:
    print("Key error") """

#######################################################################
# raising our only error meaning raise an error even there is no error from interperter

""" try:
    dict2 = {'key':545}
    print(dict2['key'])

except:
    print(KeyError)
else:
    print("Hello")
finally:
    raise KeyboardInterrupt """ # the error appear even if no error catched by the interpreter


###########################################################3
# another exmaple

""" height = float(input("Enter your height: "))
weight = float(input("Enter your weight: "))

if height > 3:
    raise ValueError("Not normal human height")

print(weight / height**2) """
#######################################################
# exercise1

""" fruits = ["Apple","Pear","Orange"]

def make(index):
    try:
        fruit = fruits[index]
    except IndexError as error:
        print("fruit pie")
    else:
        print(f"{fruit} pie")

make(4) """
#######################################################
# exercise2
""" facebook_posts = [
    {'Likes': 21, 'Comments': 2}, 
    {'Likes': 13, 'Comments': 2, 'Shares': 1}, 
    {'Likes': 33, 'Comments': 8, 'Shares': 3}, 
    {'Comments': 4, 'Shares': 2}, 
    {'Comments': 1, 'Shares': 1}, 
    {'Likes': 19, 'Comments': 3}
]

total_likes = 0

for post in facebook_posts:
    try:
        total_likes = total_likes + post['Likes']
    except KeyError:
        total_likes += 0

print(total_likes) """
#######################################################################################################
# Working with jsons
"""
We have 3 ways 
Write: json.dump()  it means to create new file and write info

Read: json.load()  it means to read a file that is already exist

Update: json.update() it means to update the contents of a file that exist
"""