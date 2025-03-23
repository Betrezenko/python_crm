import random

class Ticket:
    DIFFICULTY_MIN = 1
    DIFFICULTY_MAX = 5
    def __init__(self, subject, text):
        self.subject = subject
        self.text = text

    def to_question(self):
        difficulty = random.randint(Ticket.DIFFICULTY_MIN, Ticket.DIFFICULTY_MAX)
        question = {'Subject' : self.subject.title, 'Question' : self.text[0], 'Difficulty' : difficulty}
        return question