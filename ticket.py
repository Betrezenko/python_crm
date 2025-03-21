import random

class Ticket:
    def __init__(self, subject, text):
        self.subject = subject
        self.text = text

    def to_question(self):
        difficulty = random.randint(1, 5)
        question = {'Subject' : self.subject.title, 'Question' : self.text, 'Difficulty' : difficulty}
        return question