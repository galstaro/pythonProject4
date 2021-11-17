
#Hang Man game
import random

footballers=["MESSI","RONALDO","NEYMAR","HALLAND","RAMOS","OBLAK","NEUR","RAUL","BENAYOUN","ZEHAVI","KATAN","SANCHO","MBAPPE","ROBBEN","MEMPHIS"]

ind=random.randint(0,14)
word=footballers[ind]
print(word)
print("Hang Man game!! Guess the word within 8 tries")
str="_"*len(word)
print(str)
list=list(str)

for x in range(8):
    digit=input("Enter digit: ")
    t=0
    for i in word:
        if i==digit.upper():
            list[t]=i
        t+=1
    print("".join(list))
    if list.count("_")==0:
        print("Well Done!!")
        break
else:
    print("Fail")


