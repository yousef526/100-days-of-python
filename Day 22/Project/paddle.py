from turtle import Turtle


class Paddle(Turtle):
    def __init__(self,posx,posy):
        super().__init__()
        self.shape('square')
        self.color('red')
        self.shapesize(stretch_wid=5,stretch_len=1)
        #self.shapesize(stretch_wid=1,stretch_len=5)
        #self.setheading(90)
        self.penup()
        self.goto(posx,posy)
        self.speed('fastest')


    def moveUp(self):
        #self.setheading(90)
        #self.fd(20)
        self.goto(self.xcor(),self.ycor() + 20)


    def moveDown(self):
        #self.setheading(270)
        #self.fd(20)
        self.goto(self.xcor(),self.ycor() - 20)
