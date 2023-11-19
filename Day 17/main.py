from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []

for question in question_data: 
    question_bank.append(Question(question['text'],question['answer']))


#print(question_bank[0].text) 
quiz = QuizBrain(question_bank)
quiz.next()

while quiz.checkEnd():
    quiz.next()
print("You have completed the quiz")
print(f"Your final score was {quiz.questionRight}/{quiz.questionNumber}")