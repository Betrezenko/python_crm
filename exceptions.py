class ReachedGroupLimitError(Exception):
    def __init__(self, group_name):
        self.group_name = group_name
        super().__init__(f"{self.group_name} is full, try another group.")

class StudentAlreadyInGroupError(Exception):
    def __init__(self, group_name, student):
        self.group_name = group_name
        self.student = student
        super().__init__(f"{self.student} already in {self.group_name}")