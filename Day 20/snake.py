from turtle import Turtle
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0
MOVE_DIST = 20

class Snake:

    def __init__(self):
        self.squares = []
        self.create_snake()
        self.head = self.squares[0]
        
    def create_snake(self):
        x = 0
        for _ in range(3):
            square1 = Turtle(shape='square')
            square1.penup() 
            square1.color('white')
            square1.setpos(x,0)
            self.squares.append(square1)
            x-=20

    def add_tail(self):
        square1 = Turtle(shape='square')
        square1.penup() 
        square1.color('white')
        square1.setpos(self.squares[len(self.squares) - 1].xcor() - 20,self.squares[len(self.squares) - 1].ycor() - 20)
        self.squares.append(square1)

    def move(self):
        for i in range(len(self.squares)-1,0,-1):
            self.squares[i].goto(self.squares[i-1].pos())
        self.head.forward(MOVE_DIST)

    def goUp(self):
        if self.head.heading() != DOWN:
            self.squares[0].setheading(UP)

    def goDown(self):
        if self.head.heading() != UP:
            self.squares[0].setheading(DOWN)

    def leftward(self):
        if self.head.heading() != RIGHT:
            self.squares[0].setheading(LEFT)

    def rightward(self):
        if self.head.heading() != LEFT:
            self.squares[0].setheading(RIGHT)

    