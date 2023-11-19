from turtle import Turtle,Screen
FONT = ('Courier', 24, 'normal')

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.highestScore = 0
        with open('data.txt') as f:
            data = f.read()
            self.highestScore = int(data)
        self.hideturtle()
        self.penup()
        self.color('white')
        self.goto(0,270)
        self.write(f"Score: {self.score} Highest Score: {self.highestScore}",move=False,align='center', font=FONT)
        

    def on_score(self):
        self.clear()
        self.score+=1
        self.write(f"Score: {self.score} Highest Score: {self.highestScore}",move=False,align='center', font=FONT)

    """ def gameOver(self):
        self.goto(0,0)
        self.color('red')
        self.write(f"Game Over",move=False,align='center', font=('Courier', 24, 'normal')) """
    
    def reset_score(self):
        if self.highestScore < self.score:
            self.highestScore = self.score
            with open('data.txt',mode='w') as f:
                f.write(f"{self.highestScore}")
        
        self.score = 0
        self.clear()
        self.write(f"Score: {self.score} Highest Score: {self.highestScore}",move=False,align='center', font=FONT)
