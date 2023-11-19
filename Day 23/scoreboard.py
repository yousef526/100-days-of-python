FONT = ("Courier", 24, "normal")

from turtle import Turtle

class Scoreboard(Turtle):
    
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.goto(-260,260)
        self.level = 1
        self.write(f"Level: {self.level}", move=False, align='left', font=FONT)

    def inc_level(self):
        self.clear()
        self.level += 1
        self.write(f"Level: {self.level}", move=False, align='left', font=FONT)

    def game_Over(self):
        tim = Turtle()
        tim.hideturtle()
        tim.penup()
        tim.goto(0,0)
        tim.write("Game over", move=False, align='left', font=FONT)
