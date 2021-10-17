class StudentInClass:
    def __init__(self,id,name,adress,grade):
        self.id=id
        self.name=name
        self.adress=adress
        self.grade=grade
    def failOrPass(self):
        if(self.grade>=70):
            return "Pass"
        else:
            return "Fail"

student1=StudentInClass(34322,"Gal","barcelona",92)
print(student1.failOrPass())