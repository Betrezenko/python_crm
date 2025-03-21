from ticketGenerator import TicketGenerator

class Exam:
    def __init__(self, student_group, subject, teacher):
        self.student_group = student_group
        self.subject = subject
        self.teacher = teacher

    def start_exam(self):
        print(f"{self.subject} exam for {self.student_group} started. {self.teacher} is examinator.")
        tickets = TicketGenerator(self.subject)
        questions = list(tickets.create_tickets())
        for q in questions:
            print(q)