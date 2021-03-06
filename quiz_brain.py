class QuizBrain:

    def __init__(self, q_list):
        """initial method """
        self.question_number = 0
        self.question_list = q_list
        self.score = 0
        self.correct_answer = ""

    def still_have_question(self):
        """check if there are more questions"""
        if len(self.question_list) <= self.question_number:
            return False
        else:
            return True

    def next_question(self):
        """Ask user for question and get the answer"""
        current_question = self.question_list[self.question_number]
        self.correct_answer = current_question.answer
        self.question_number += 1
        return input(f"Q.{self.question_number}: {current_question.text} (True / False):").capitalize()

    def check_answer(self):
        """Check the answer if it is correct or not"""
        if self.next_question() == self.correct_answer:
            self.score += 1
            print("you are right!")
        else:
            print("That's wrong")
        print(f"the correct answer was: {self.question_list[self.question_number-1].answer}")
        print(f"your current score is {self.score}/{self.question_number} ")
        print("\n")