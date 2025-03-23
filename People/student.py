from People.human import Human
from studentGroup import StudentGroup
from exceptions import StudentAlreadyInGroupError


class Student(Human):
    STATUS = "student"

    def __init__(self, name, age, sex):
        self.name = name
        self.age = age
        self.sex = sex
        self.subjects = set()
        self.balance = 0.0
        self.group = None

    def __str__(self):
        group_name = self.group.group_name or f"{self.name} not in group"
        return f"{group_name} : {self.name}"

    def add_subject(self, subject):
        self.subjects.add(subject)
        print(f"{subject.title} added to {self.name}'s list.")

    def rm_subject(self, subject):
        self.subjects.discard(subject)
        print(f"{subject.title} removed from {self.name}'s list.")

    def show_subjects(self):
        if not self.subjects:
            print(f"Student {self.name} has no subjects.")
        else:
            print(f"Subjects for {self.name}:")
            for subject in self.subjects:
                print(subject)

    def add_to_group(self, group):
        if not isinstance(group, StudentGroup):
            raise TypeError(f"{group} should be a StudentGroup object.")
        self.group = group
        if len(group) < group.limit:
            if self not in group.students_set:
                group.students_set.add(self)
                print(f"{self.name} was added to {group}.")
            else:
                raise StudentAlreadyInGroupError(group.group_name, self)

    def show_group(self):
        if self.group is not None:
            print(f"{self.name} is in {self.group}.")
        else:
            print(f"{self.name} has no group.")

    def add_money(self, amount: float):
        self.balance += amount
        print(f"{amount} added to {self.name}'s balance: {self.balance} ")

    def rm_money(self, amount: float):
        self.balance -= amount
        print(f"{amount} removed from {self.name}'s balance: {self.balance} ")

    def show_balance(self):
        print(f"{self.name}'s balance is {self.balance}")