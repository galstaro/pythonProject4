class Student:
    def __init__(self, name, adress, age, grades):
        self.name = name
        self.adress = adress
        self.age = age
        self.grades = grades

    def details(self):
        print("Student name: " + self.name)
        print("Student adress: " + self.adress)
        print("Student age: ", self.age)
        print("Student grades: ", self.grades)

    def updateage(self, age):
        self.age = age

    def getage(self):
        return self.age

    def addGrade(self, grade):
        if (len(self.grades) < 5):
            self.grades.append(grade)
            return True
        else:
            return False

    def average(self):
        return self.grades.sum() / len(self.grades)

    def Scores(self):
        return self.grades


student = Student("Gal", "Geva Carmel", 0, [])
student.updateage(21)
for i in range(5):
    student.addGrade(int(input("Enter grade: ")))

student.details()
if student.getage() < 20:
    print("Very young")
elif student.getage() > 30:
    print("Mature")
else:
    print("Young")

for s in student.Scores():
    if (s < 70):
        print("Fail", s)
    else:
        print("Pass", s)
