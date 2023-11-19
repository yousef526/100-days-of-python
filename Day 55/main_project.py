from flask import Flask
import random
app = Flask(__name__)

@app.route('/')
def hel():
    return "<h1>Guess a number between 0 and 9</h1>"\
    "<img src='https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif'>"

random_no = random.randint(0,9)
print(random_no)

@app.route('/<int:guess>')
def guess_choice(guess):
    if guess == random_no:
        return "<h1 style='color:green'>You found me!</h1>"\
        "<img src='https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif'>"
    elif guess > random_no:
        return "<h1 style='color:red'>Too high try agian</h1>"\
        "<img src='https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif'>"
    else:
        return "<h1 style='color:purple'>Too low try agian</h1>"\
        "<img src='https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif'>"


app.run(debug=True)