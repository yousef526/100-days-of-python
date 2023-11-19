from flask import Flask
import flask
app = Flask(__name__)

def makeBold(func):
    def bold():
        return f"<b>{func()}</b>"
    return bold

def makeEmp(func):
    def EMP():
        return f"<em>{func()}</em>"
    return EMP

def Underlined(func):
    def lined():
        return f"<u>{func()}</u>"
    return lined
    

@app.route('/')
def hello():
    return "<h1>hello</h1>"\
    "<p>this is paragraph</p>"\
    "<img src='https://media.giphy.com/media/K1tgb1IUeBOgw/giphy.gif'>"

@app.route('/bye')
@makeBold
@Underlined
@makeEmp
def bye():
    return "bye"

#creating a path with normal input from user
@app.route('/<username>')
def greet(username):
    return f"greet sdaa {username}"


#creating a path with normal input as path and with specified datatype
@app.route('/user/<path:username>')
def greet22(username):
    return f"greet sdaa {username}"

app.run(debug=True)