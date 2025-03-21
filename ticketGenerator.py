import random

from ticket import Ticket

class TicketGenerator:
    def __init__(self, subject, limit=10):
        self.subject = subject
        self.limit = limit

    def create_tickets(self):
        # можно сделать переменную path с дефолтным значением и ее передавать вместо хардкода файла, но я так оставил
        with open('questions.txt', 'r') as q:
            questions = [l.strip() for l in q.readlines()]

        for _ in range(self.limit):
            ticket = Ticket(
                self.subject,
                random.choice(questions)
            )
            yield ticket.to_question()

        # Сначала было так, потом спросил друга как избавиться от лишних переменных, он подсказал про random.choice
        # lines были в открытии файла через len(questions) для определения лимита
        # for _ in range(self.limit):
        #         line = random.randint(0, lines - 1)
        #         text = questions[line].strip()
        #         ticket = Ticket(self.subject, text)
        #         ticket_res = ticket.to_question()
        #         yield ticket_res
        #         self.tickets.append(ticket_res)

