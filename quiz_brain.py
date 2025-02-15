class QuizBrain:

    def __init__(self, question_list):
        self.question_number = 0
        self.question_list = question_list
        self.score = 0

    def next_question(self):
        question = self.question_list[self.question_number]
        self.question_number += 1
        answer = input(f"Q.{self.question_number} {question.text} (True/False)? ")
        self.check_answer(answer, question.answer)

    def still_has_questions(self):
        if self.question_number < len(self.question_list):
            return True
        else:
            return False

    def check_answer(self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            self.score += 1
            print("You got it!!")
            print(f"Your current score is: {self.score}/{self.question_number} \n")
        else:
            print("You got it wrong :(")
            print(f"The correct answer is {correct_answer}. ")
            if self.question_number == 12:
                print(f"\nYour final score is: {self.score}/{self.question_number} \n")
            else:
                print(f"\nYour current score is: {self.score}/{self.question_number} \n")
