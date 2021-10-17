class Course:
    def __init__(self,courseNumber,courseName,numOfStudents,maxStudents):
        self.courseNumber=courseNumber
        self.courseName=courseName
        self.numOfStudents=numOfStudents
        self.maxStudents=maxStudents
    def details(self):
        return self.courseNumber,self.courseName,self.numOfStudents,self.maxStudents
    def placesLeft(self):
        return self.maxStudents-self.numOfStudents

courseQA=Course(4,"QA",20,30)
print(courseQA.details())
print("The number of palaces which left for the course is:",courseQA.placesLeft())

