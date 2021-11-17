from Course import *
from Student import *


course=Course(4,"python",15)
z=course.subject_teacher={
    "programing":"moshe",
    "testing":"rafael",
    "backend":"angelina"
}
while 2>1:
    id=int(input("Enter id of student: "))
    if id!=0:
        student=Student(id,input("Enter student name: "),dict({}))
        for i in z:
            student.add_grade(i,int(input(f"Enter grade for {i} subject: ")))
        x=course.add_student(student)
        if x is False:
            break
    else:
        break
course.add_factor("testing",10)
min=course.student_list[0].average()

for i in course.student_list:
    if min>i.average():
        min=i.average()
for i in  course.student_list:
    if min==i.average():
        course.del_student(i.id)
print(course)
