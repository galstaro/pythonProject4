from Student import *

class Course:
    def __init__(self,course_number:int,course_name:str,students_max:int):
        if type(course_number)==int or type(course_name)==str or type(students_max)==int:
            self.course_number=abs(course_number)
            self.course_name=course_name
            self.students_max=abs(students_max)
            self.student_list=[]
            self.subject_teacher=dict({})
        else:
            raise TypeError("wrong arguments")

    def __repr__(self):
        return f"Course details\nCourse number:{self.course_number}\nCourse name:{self.course_name}\nMax students in course:{self.students_max}\nStudent list:{self.student_list}\nSubjects and who is taught each one:{self.subject_teacher}"

    def add_student(self,student:Student):
        if type(student) is Student :
            if student not in self.student_list:
                if len(self.student_list)<self.students_max:
                    self.student_list.append(student)
                    return True
                else:
                    return False
            else:
                print("Student with this id is already in the course.")
        else:
            print("Student need to be type of Student class")
            return False

    def add_factor(self,sub:str,factor:int):
        if (type(sub) is str and type(factor) is int):
            if sub in self.subject_teacher.keys():
                for i in self.student_list:
                    i.calc_factor(sub,factor)
            else:
                raise TypeError("Subject is not in this course.")
        else:
            raise TypeError("Subject need to be a string and factor percent need to be an integer")

    def del_student(self,id:int):
       if type(id) is int:
            for i in self.student_list:
                if i.id==id:
                    self.student_list.remove(i)
       else:
           print("ID need to be a number")
           return False




