from turtle import Turtle, Screen
import random


screen = Screen()
screen.setup(width=500,height=400)
screen.title("Welcome to turtles race")
colors = ['red','orange','yellow','green','blue','purple']
turtles = []
user_input = screen.textinput("Make your bet", "Which turtle will win? Enter turtle name: ")


y_pos = -150
for color in colors:
    tim = Turtle(shape="turtle")
    tim.color(color)
    tim.penup()
    tim.goto(x=-230,y=y_pos)
    turtles.append(tim)
    y_pos+=50


no_winning_turtle = True
color_winning_turtle = ''
while no_winning_turtle:
    for turtle in turtles:
        turtle.fd(random.randint(0,10))
        if turtle.xcor() >= 230:
            color_winning_turtle = turtle.pencolor()
            no_winning_turtle = False

win_check = "lose" if user_input.lower() != color_winning_turtle else "win"
print(f"You {win_check}. The {color_winning_turtle} turtle is the winner")

screen.exitonclick()