from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.color('red')
        self.penup()
        self.speed('fastest')
        self.y_move = 10
        self.x_move = 10
        



    def moving(self):
        xcor = self.xcor() + self.x_move
        ycor = self.ycor() + self.y_move
        self.goto(xcor,ycor)

    def bounce_y(self):
        self.y_move *= -1
    
    def bounce_x(self):
        self.x_move *= -1
        

    def reset_ball(self):
        self.goto(0,0)
        self.x_move = 10
        self.bounce_x()