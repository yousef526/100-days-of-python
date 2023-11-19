import turtle as t
import random
import time
from snake import Snake

screen = t.Screen()
screen.setup(width=600,height=600)
screen.bgcolor('black')
screen.title(titlestring="My snake game")
screen.tracer(0)

snake = Snake()

screen.listen()
screen.onkey(snake.goUp,'Up')
screen.onkey(snake.goDown,'Down')
screen.onkey(snake.leftward,'Left')
screen.onkey(snake.rightward,'Right')
game_is_on = True

def detect_collsion(a,b):
    return abs(a.xcor() - b.xcor()) < 20 and abs(a.ycor() - b.ycor()) < 20

while game_is_on:
    points = t.Turtle(shape='circle')
    points.penup()
    points.color('white')
    points.setpos(random.randint(-200,200),random.randint(-200,200))

    screen.update()
    time.sleep(0.1)
    snake.move()
    no_collide = True
    while no_collide:
        if detect_collsion(snake.head,points):
            points.reset()
            no_collide = False
            snake.add_tail()
            snake.addPostions()
        else:
            screen.update()
            time.sleep(0.1)
            snake.move()
    

screen.exitonclick()