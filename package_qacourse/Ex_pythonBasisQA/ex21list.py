
#BoolHIT GAME

import random

def BoolHit(guess, list1):
    bool = 0
    hit = 0
    for i in guess:
        counter=0
        while (counter < 4):
            if (i == list1[counter]):
                if (guess.index(i) == counter):
                    bool += 1
                else:
                    hit += 1
            counter += 1
    print("bools:",bool,"hits:",hit)
    return bool


list1=[]
for i in range(4):
    rand = str(random.randint(0, 9))
    while list1.count(rand)!=0:
            rand=str(random.randint(0,9))
    list1.append(rand)
print(list1)
guess=input("Bool hit game! You have 10 tries .Enter 4 digit number: ")

for i in range(10):
    if BoolHit(guess,list1) == 4:
        print("Winner winner chicken dinner!")
        break
    else:
        guess = input("Enter 4 digit number: ")
else:
    print("Fail")


