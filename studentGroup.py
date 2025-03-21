from exceptions import ReachedGroupLimitError
from exceptions import StudentAlreadyInGroupError

class StudentGroup:
    def __init__(self, group_name, limit=10):
        self.group_name = group_name
        self.limit = limit
        self.students_set = set()

    def __str__(self):
        return self.group_name

    # Выглядит топорно, но я не придумал как сделать две проверки иначе
    # Видос из задания как-будто не совсем сюда подходит, либо я не понял как его использовать в этом случае
    def add_student(self, student):
        if len(self.students_set) < self.limit:
            if student not in self.students_set:
                self.students_set.add(student)
                student.add_to_group(self.group_name)
            else:
                raise StudentAlreadyInGroupError(self.group_name, student)
        else:
            raise ReachedGroupLimitError(self.group_name)

    def rm_student(self, student):
        if student in self.students_set:
            self.students_set.discard(student)
            print(f"{student.name} was removed from {self.group_name}.")
        else:
            print(f"There's no such student in {self.group_name}.")

    def show_students(self):
        for student in self.students_set:
            print(student)

    def change_group_limit(self, limit):
        self.limit = limit
        return f"{self.group_name} limit was changed to {self.limit}"