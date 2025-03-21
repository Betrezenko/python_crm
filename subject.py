class Subject:
    def __init__(self, title, teacher=None):
        self.title = title
        self.teacher = teacher

    def __str__(self):
        return self.title

    def change_teacher(self, teacher):
        self.teacher = teacher
        print(f"{teacher.name} is a teacher for {self.title}")

    def show_teacher(self):
        print(f"{self.title} teacher is {self.teacher}")