STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280

from turtle import Turtle
class Player(Turtle):

    def __init__(self) :
        super().__init__()
        self.shape('turtle')
        self.penup()
        self.goto(STARTING_POSITION)
        self.left(90)

    def moveUp(self):
        y_cor = self.ycor() + MOVE_DISTANCE
        self.goto(0,y_cor)

    def moveDown(self):
        y_cor = self.ycor() - MOVE_DISTANCE
        self.goto(0,y_cor)

    def go_start_state(self):
        self.goto(STARTING_POSITION)

