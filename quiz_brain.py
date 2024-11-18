
#asking the questions
#checking if the answer is correct
#checking if we are at the end of the quiz



class QuizBrain:
    def __init__(self, quiz_list):
        self.question_number = 0
        self.question_list = quiz_list

    def still_jas_questions(self):

    def next_question(self):
        current_q = self.question_list[self.question_number]
        self.question_number += 1
        user_input = input(f"Q{self.question_number} {current_q.text} True or False?\n")