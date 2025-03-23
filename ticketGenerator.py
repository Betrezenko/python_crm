import random

from ticket import Ticket

class TicketGenerator:
    TICKETS_LIMIT = 10
    PATH = './questions.txt'

    def __init__(self, subject):
        self.subject = subject
        self.limit = TicketGenerator.TICKETS_LIMIT
        self.path = TicketGenerator.PATH

    def create_tickets(self):
        with open(f'{self.path}', 'r') as q:
            questions = []
            for line in q:
                questions.append(line.strip())

        for _ in range(self.limit):
            ticket = Ticket(
                self.subject,
                random.sample(questions, k=1)
            )
            yield ticket.to_question()