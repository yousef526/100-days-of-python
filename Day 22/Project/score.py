from turtle import Turtle,Screen

class Score(Turtle):
    def __init__(self,posx,posy):
        super().__init__()
        self.score = 0
        self.hideturtle()
        self.penup()
        self.color('white')
        self.goto(posx,posy)
        self.write(f"{self.score}",move=False,align='center', font=('Aerial', 24, 'normal'))

    def inc_score(self):
        self.score+=1
        self.clear()
        self.write(f"{self.score}",move=False,align='center', font=('Aerial', 24, 'normal'))
        