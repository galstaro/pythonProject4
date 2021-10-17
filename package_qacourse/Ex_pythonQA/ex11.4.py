class Person:
    def __init__(self, name, id, age, kids):
        self.name = name
        self.id = id
        self.age = age
        self.kids = kids

    def __init__(self, name, id):
        self.name = name
        self.id = id
        self.age =0
        self.kids =[]


    def details(self):
        print("Name: " + self.name)
        print("ID number: " + self.id)
        print("Age: ", self.age)
        print("Kids names: ", self.kids)

    def updateage(self, age):
        self.age = age

    def getage(self):
        return self.age

    def addkid(self, kid):
        if len(self.kids) < 5:
            self.kids.append(kid)
            return True
        else:
            return False

person =Person("Gal", "314949520")
person.updateage(21)
for i in range(5):
    person.addkid(input("Enter kid name: "))
person.details()