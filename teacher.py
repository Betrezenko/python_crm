from human import Human


class Teacher(Human):
    STATUS = "teacher"

    def __init__(self, name, age, sex):
        self.name = name
        self.age = age
        self.sex = sex
        self.subj_teacher = None
        self.salary = 1000.0

    def __str__(self):
        return self.name

    def add_subject(self, subject):
        self.subj_teacher = subject
        subject.change_teacher(self)

    def show_salary(self):
        print(f"{self.name}'s salary is {self.salary}")

    def salary_up(self, amount: float):
        self.salary += amount
        print(f"{self.name}'s salary was increased by {amount}")

    def salary_down(self, amount: float):
        self.salary -= amount
        print(f"{self.name}'s salary was decreased by {amount}")