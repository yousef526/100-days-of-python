# TODO asking the questions
# TODO checking if te answer if correct
# TODO checking if we are at the end of the quiz

class QuizBrain():

    def __init__(self,QsList):
        self.questionNumber = 0
        self.QuestionList = QsList
        self.questionRight = 0

    def next(self):
        #for question in self.QuestionList:
        currentQ = self.QuestionList[self.questionNumber]
        choice = input(f"Q.{self.questionNumber+1} {currentQ.text}. (True/False)?: ")
        self.checkAnswer(answer=choice,question=currentQ)
            
    
    def checkAnswer(self,answer,question):
        if answer.lower() == question.answer.lower():
            self.questionRight+=1
            self.questionNumber+=1
            print('you got it right')
        else:
            self.questionNumber+=1
            print('That`s incorrect')

        print(f"Correct answer: {question.answer}")
        print(f"Current Score: {self.questionRight}/{self.questionNumber}")
        print()

    def checkEnd(self):
        return self.questionNumber < len(self.QuestionList)