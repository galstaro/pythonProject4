class Bus:

    def __init__(self,seats_number:int):
        self.seats = ["free" for i in range(seats_number)]
        self.passengers = 0

    def getOn(self,name:str):
        x=self.seats.count("free")
        if x != 0:
            self.passengers+=1
            self.seats[self.seats.index("free")]=name
        else:
            print("the buss is full.",name,"didn't got on bus.")

    def getOff(self,name:str):
        x = self.seats.count(name)
        if x != 0:
            self.passengers-=1
            i=self.seats.index(name)
            self.seats.insert(i,"free")
            self.seats.remove(name)
        else:
            print("the passenger",name,"was not on the buss.")

    def __str__(self):
        return f"The seats list: {self.seats}\nThe number of passengers on the bus: {self.passengers}"


bus=Bus(50)

while 2>1:
    x=int(input("Enter 1 to get up a passenger, 2 to get down passenger , 0 drive: "))
    if x==1:
        bus.getOn(input("Enter the passenger name: "))
    if x==2:
        bus.getOff(input("Enter the passenger name: "))
    if x==0:
        break
print(bus.__str__())

