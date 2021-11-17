class Animal:
    def __init__(self, name):
        self.name = name
        self.hunger = 5.0
        self.energy = 5.0

    def __str__(self):
        return f"animal name: {self.name} \nhunger level: {self.hunger} \nenergy level: {self.energy}"

    def eat(self, gram):
        g = 1.0
        self.hunger-=gram/50
        if(self.hunger<0):
            g =self.hunger
            self.hunger =0
            print("The animal is full and does not finish to eal")
        self.energy += (gram+g*50) / 100
        if(self.energy>10):
            self.energy=10

    def play(self,time):
        g = 1.0
        self.energy -= time /5
        if (self.energy < 0):
            g = self.energy
            self.energy = 0
            print("The animal is too tired to play")
        self.hunger+=(time+g*5)/5
        if self.hunger>10:
            self.hunger=10

    def rest(self,minutes):
        g = 1.0
        self.energy += minutes / 20
        if (self.energy>10):
            g = self.energy
            self.energy = 10
            print("The animal wake up and want to play")
            self.hunger += (minutes + g * 20) / 30
        elif self.hunger > 10:
            g = self.hunger
            self.hunger = 0
            print("The animal wake up and want to eat")
            self.energy += (minutes + g * 30) / 20


dog=Animal("dog")
while 2>1:
    x=int(input("1-eat 2-play 3-rest 0-finish: "))
    if x==1:
        dog.eat(int(input("food weight in grams: ")))
    if x==2:
        dog.play(int(input("play time in minutes: ")))
    if x==3:
        dog.rest(int(input("rest time in minutes: ")))
    if x==0:
        print(dog.__str__())
        break
    print(dog.__str__())

