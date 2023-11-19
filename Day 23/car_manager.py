COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10

from turtle import Turtle
import random

movingSpeed = STARTING_MOVE_DISTANCE

class CarManager():
    def __init__(self):
        self.cars = []

    def createcar(self):
        tim = Turtle()
        tim.shape('square')
        tim.penup()
        tim.shapesize(stretch_wid=1,stretch_len=2)
        tim.color(random.choice(COLORS))
        y_cor = random.randint(-250,250)
        x_cor = random.randint(330,340)
        tim.goto(x_cor,y_cor)
        self.cars.append(tim)

    def move(self):
        global movingSpeed
        for car in self.cars:
            car.backward(movingSpeed)

    def inc_speed(self):
        global movingSpeed
        movingSpeed += MOVE_INCREMENT

    


        

    
