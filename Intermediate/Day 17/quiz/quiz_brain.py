class QuizBrain:

    def __init__(self, q_list):
        self.question_number = 0
        self.score = 0
        self.question_list = q_list
        q_len = len(self.question_list)
        while self.question_number < q_len:
            self.next_question(self.question_number, q_len)
            self.question_number += 1
        if self.question_number == self.q_len:
            print("Congratulations! You have completed the quiz.")
            print(f"Your final score is: {self.score}/{self.q_len}")
        
    def next_question(self, question_number, q_len):
        self.question_number = question_number
        self.q_len = q_len 
        user_answer = input(f"[{question_number+1}/{self.q_len}] {self.question_list[question_number].text} True/False: ")

        user_answer = user_answer[0].capitalize() + user_answer[1:].lower()
   
        if user_answer in ["True", "False"]:
            if user_answer == self.question_list[question_number].answer:
                self.score += 1
                print("You got it right!")
            else:
                print("That's wrong.")
            print(f"The correct answer was: {self.question_list[question_number].answer}")
            print(f"Your current score is: {self.score}/{self.q_len}")

        else:
            print("Please enter a valid answer.")
            self.next_question(question_number, q_len)  