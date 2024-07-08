#Question

class Question:
    def __init__(self,text,choices,answer):
        self.text=text
        self.choices = choices
        self.answer = answer
    def checkAnswer(self,answer):
        return self.answer == answer




#Quiz

class Quiz:
    def __init__(self,questions):
        self.questions = questions
        self.score = 0
        self.currentQuestionIndex = 0
    def getQuestion(self):
        return self.questions[self.currentQuestionIndex]
    def displayQuestion(self):
        question = self.getQuestion()
        print(f"Soru {self.currentQuestionIndex+1}: {question.text}")
        for q in question.choices:
            print('-'+q)

        answer = input('cevap: ')
        self.guess(answer)

    def guess(self,answer):
        question = self.getQuestion()
        if question.checkAnswer(answer):
            print('dogru cevap')
            self.score += 1
        else:
            print('yanlis cevap')
        self.currentQuestionIndex += 1
        if self.currentQuestionIndex < len(self.questions):
            self.displayQuestion()
        else:
            print(f'Tebrikler, toplam puaniniz: {self.score}/{len(self.questions)}')        





q1 = Question('en iyi iyi programlama dili hangisidir?',['C#','python','javascript','java'],'python')        
q2 = Question('en popüler programlama dili hangisidir?',['C#','python','javascript','java'],'python')        
q3 = Question('en çok kazandıran programlama dili hangisidir?',['C#','python','javascript','java'],'python')        
questions = [q1,q2,q3]
# print(q1.checkAnswer('python'))
# print(q2.checkAnswer('C#'))

quiz = Quiz(questions)

quiz.displayQuestion()