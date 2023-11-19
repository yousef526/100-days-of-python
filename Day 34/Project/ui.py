from tkinter import *
from quiz_brain import QuizBrain
import time
THEME_COLOR = "#375362"
FONT = ("Arial",20,"italic")


class QuizUI():

    def __init__(self,quiz_brain:QuizBrain):
        self.quiz_brain = quiz_brain

        self.window = Tk()
        self.window.config(padx=50,pady=50,bg=THEME_COLOR)
        self.window.title('Quizzlar')
        self.score = Label(text="Score: 0",bg=THEME_COLOR,fg='white')
        self.score.grid(row=0,column=1)
        

        self.canvas = Canvas(width=300,height=250,highlightthickness=0)
        self.Q_text = self.canvas.create_text(
            150,125,
            width=280,
            text="QUESTIONS",
            fill=THEME_COLOR,
            font=FONT)
        self.canvas.grid(row=1,column=0,columnspan=2,pady=50)


        #Buttons
        self.right_image = PhotoImage(file='images/true.png')
        self.right_btn = Button(image=self.right_image,highlightthickness=0,command=self.check_right_btn)
        self.right_btn.grid(row=2,column=0)

        self.left_image = PhotoImage(file='images/false.png')
        self.wrong_btn = Button(image=self.left_image,highlightthickness=0,command=self.check_wrong_btn)
        self.wrong_btn.grid(row=2,column=1)

        self.next_Q()
        self.window.mainloop()

    def next_Q(self):
        self.canvas.config(bg='white')
        if self.quiz_brain.still_has_questions():
            
            q_text = self.quiz_brain.next_question()
            self.canvas.itemconfig(self.Q_text,text=q_text)
        else:
            self.canvas.itemconfig(self.Q_text,text="You have reached end of quiz")
            self.right_btn.config(state='disabled')
            self.wrong_btn.config(state='disabled')

    def check_right_btn(self):
        answer = self.quiz_brain.check_answer("true")
        self.feeback(answer)



    def check_wrong_btn(self):
        answer = self.quiz_brain.check_answer("false")
        self.feeback(answer)
        

    def feeback(self,param: bool):
        if param:
            self.canvas.config(bg='green')
            self.score['text'] = f"Score: {self.quiz_brain.score}"
        else:
            self.canvas.config(bg='red')
        self.window.after(1000,self.next_Q)

