import random

ranNumber=random.randint(1, 9)

print("Hello user you need to guess the number I chose.")


i=0
while i<100:
    num = int(input("Enter number: "))
    if(num==ranNumber):
        print("CONGRATULATIONS YOU CHOSE THE CORRECT NUMBER!")
        break
    if (num > ranNumber):
        print("you chose higher number")

    if (num < ranNumber):
        print("you chose lower number")
    i+=1