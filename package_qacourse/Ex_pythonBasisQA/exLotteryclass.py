import random

class Lottery:

    def __init__(self):
        self.low = 1
        self.up = 45
        self.numbers = self.draw()
        self.max_prize = self.get_prize()

    def draw(self):
     self.numbers=[]
     self.numbers+=((random.randint(1,45)) for i in range(6))

    def get_prize(self):
        return int(input("Enter max prize: "))

    def print_draw(self):
        print(self.numbers)

    def guess(self,num:int):
        if num>=self.low and num<=self.up and type(num) is int :
            if self.numbers.count(num)>0:
                return True
            else:
                return False
        return

    def your_prize(self,right:int):
        if right<=1:
            return 0
        else:
            return right*self.max_prize/6


print("Welcome to the Lottery!")
loto = Lottery()
loto.draw()
loto.print_draw()
right=0
loyal=True

for i in range(6):
     x=int(input("Enter your guess: "))
     if loto.guess(x)==None:
         loyal=False
         print("your guess is not allowed. you are disqualified from the lottery.")
         break
     elif loto.guess(x):
         right+=1

if loyal== False:
    print("Your prize money is: 0")
else:
    print("Your prize money is:",loto.your_prize(right))
