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
            self.add_tail((x,0))
            x-=20

    def add_tail(self,pos):
        square1 = Turtle(shape='square')
        square1.penup() 
        square1.color('white')
        square1.setpos(pos)
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

    def detect_wall(self):
        if self.head.xcor() > 280 or self.head.ycor() > 280 :
            return True
        elif self.head.xcor() < -280 or self.head.ycor() < -280 :
            return True
        else:
            return False
        
    def extend_tail(self):
        #[len(self.squares) - 1] get last item also [-1]
        self.add_tail(self.squares[-1].pos())

    def reset_snake(self):
        for square in self.squares:
            square.goto(1000,1000)
        self.squares = []
        self.create_snake()
        self.head = self.squares[0]
