class Student:
    def __init__(self,id:int,name:str,dic:dict):
        if (type(id) is not int or type(name) is not str or type(dic) is not dict):
            raise TypeError("The arguments inserted incorrect")
        else:
            if name.isalpha():
                self.id=abs(id)
                self.name=name
                self.subject_grade=dic
            else:
                raise TypeError("Name have to be contain only words")

    def add_grade(self,subject:str,grade:int):
        if(type(subject) is str and type(grade) is int):
            self.subject_grade.update({subject:abs(grade)})
        else:
            print("Subject need to be a string and grade need to be an integer")
            return False

    def __repr__(self):
        return f"\nStudent details\nID:{self.id}\nName:{self.name}\nGrades:{self.subject_grade}"

    def calc_factor(self,sub:str,factor:int):
        if (type(sub) is str and type(factor) is int):
            if sub in self.subject_grade:
                self.subject_grade[sub]=round(self.subject_grade[sub]+self.subject_grade[sub]*factor/100)
                if self.subject_grade[sub]>100:
                    self.subject_grade[sub]=100
            else:
                print("the student didnt learn this subject")
                return False
        else:
            print("Subject need to be a string and factor percent need to be an integer")
            return False

    def average(self):
        if len(self.subject_grade)>0:
            return sum(self.subject_grade.values())/len(self.subject_grade)
        else:
            print("There are not grades in list")
            return False

    def __eq__(self, other):
        if self.id==other.id:
            return True
        return False
