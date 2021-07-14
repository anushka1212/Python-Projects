class QuizBrain:
    def __init__(self, q_list):
        self.quiz_number = 0
        self.question_list = q_list
        self.score = 0

    def still_has_questions(self):
        return len(self.question_list) > self.quiz_number

    def next_question(self):
        question = self.question_list[self.quiz_number]
        self.quiz_number += 1
        user_answer = input(f"Q.{self.quiz_number}: {question.text} (True/False): ")
        self.check_answer(user_answer, question.answer)

    def check_answer(self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            print("You got it right.")
            self.score += 1
        else:
            print("That's wrong.")
        print(f"The correct answer is {correct_answer}.")
        print(f"Your current score is {self.score}/{self.quiz_number}\n")
