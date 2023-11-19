from turtle import Turtle,Screen
timmy = Turtle()

#timmy.shapesize(3,3)
#timmy.color('blue')
#timmy.shape("turtle")

""" for i in range(13):
    timmy.fd(100)
    timmy.fd(-100)
    timmy.fd(-100)
    timmy.fd(100)
    timmy.right(15) """
##############################################


#draw square
#for i in range(4):
 #   timmy.fd(100)
  #  timmy.right(90)

################################

#draw dashed line
#sol. 
""" for i in range(6):
    timmy.fd(20)
    timmy.color('white')
    timmy.fd(20)
    timmy.color('blue') """

# other sol
""" for i in range(6):
    timmy.fd(20)
    timmy.penup()
    timmy.fd(20)
    timmy.pendown() """
#######################################

# create shapes of from 3 angles to 11 angles with different colors
""" import random
colors = ['blue','DarkOrange','DarkGoldenrod','gold','gray','purple','green','cyan']#,'DarkBlue','red']

for i in range(3,11):
    angle = 360 / i
    #var = 
    for x in range(i):
        timmy.color(random.choice(colors))
        timmy.forward(100)
        timmy.left(angle) """
##################################################

#Random walk
""" import random

angles = [0,90,180,270]
timmy.pensize(10)
timmy.speed('fastest')
timmy.hideturtle()
Screen().colormode(255)

for i in range(200):
    timmy.pencolor((random.randint(0,255),random.randint(0,255),random.randint(0,255)))
    timmy.forward(50)
    timmy.left(random.choice(angles)) """
##########################################

# drawing Spirograph
import random
#timmy.pensize(10)
timmy.speed("fastest")

Screen().colormode(255)

# old sol. not correct
""" for i in range(181):
    timmy.pencolor((random.randint(0,255),random.randint(0,255),random.randint(0,255)))
    timmy.left(i+2)
    timmy.circle(100) """
    
# correct sol.

def draw_Spirograph(gap):
    for _ in range(int(360/gap)): # that is used to make gaps between the circles and dont repeat circles
        timmy.pencolor((random.randint(0,255),random.randint(0,255),random.randint(0,255)))
        timmy.circle(100)
        timmy.setheading(timmy.heading()+gap) # to change place which drawing start from

draw_Spirograph(3)

screen = Screen()
screen.exitonclick()