from student import Student
from subject import Subject
from teacher import Teacher
from studentGroup import StudentGroup
from ticket import Ticket
from exam import Exam

math = Subject("Math")
mathTeacher = Teacher('Andrew', 34, 'M')
mathTeacher.add_subject(math)
math.show_teacher()

physics = Subject("Physics")
physicsTeacher = Teacher('Margaret', 54, 'F')
physicsTeacher.add_subject(physics)

literature = Subject('Literature')
literatureTeacher = Teacher('John', 35, 'M')
print()

student1 = Student('Alice',  18, 'F')
student2 = Student('Bob', 20, 'M')
# student1.add_money(10)
# student1.add_money(20)
# student1.rm_money(40)
# student1.show_balance()
# print()
student1.add_subject(math)
student1.add_subject(physics)
student1.add_subject(literature)
student1.show_subjects()
print()

group1 = StudentGroup('Group 1')
group1.add_student(student1)
group1.add_student(student2)
student1.show_group()
group1.show_students()
print()

exam1 = Exam(group1, math, mathTeacher)
exam1.start_exam()


