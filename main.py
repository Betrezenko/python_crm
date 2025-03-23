import random

from People.student import Student
from subject import Subject
from People.teacher import Teacher
from studentGroup import StudentGroup
from exam import Exam
from faker import Faker

fake_name = Faker()
group_list = []
teachers_list = []
math = Subject("Math")
physics = Subject("Physics")
literature = Subject('Literature')
subjects = [math, physics, literature]

def generate_teacher():
    teacher = Teacher(
        fake_name.first_name(),
        random.randint(18, 30),
        random.choice(['M', 'F'])
    )

    teachers_list.append(teacher)
    teacher.add_subject(random.choice(subjects))

    return teacher

def generate_groups(count):
    if count > 0:
        for i in range(count):
            group = StudentGroup(f'Group {i + 1}')
            group_list.append(group)
    else:
        print('Enter correct counter to generate groups.')

def generate_student():
    student = Student(
        fake_name.first_name(),
        random.randint(18, 30),
        random.choice(['M', 'F'])
    )

    student.add_to_group(random.choice(group_list))

    return student

generate_groups(3)
for _ in range(30):
    generate_student()

print()

for _ in range(3):
    generate_teacher()

print()

group1 = group_list[0]
group1.show_students()

mathTeacher = teachers_list[0]
physicsTeacher = teachers_list[1]
literatureTeacher = teachers_list[2]

mathExam = Exam(group_list[0], subjects[0], mathTeacher)
physicsExam = Exam(group_list[1], subjects[1], physicsTeacher)
literatureExam = Exam(group_list[0], subjects[2], literatureTeacher)

mathExam.start_exam()
physicsExam.start_exam()
literatureExam.start_exam()
