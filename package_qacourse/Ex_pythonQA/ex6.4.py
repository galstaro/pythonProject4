import random
s=[]
# random 10 numbers between 1-100 to create list
for i in range(10):
   s.append(random.randint(1,100))
print(s)
# Convert list to tuple:
t=tuple(s)
print(t)
# add number to tuple:
x=int(input("Hello enter number plz: "))
s=list(t)
s.append(x)
t=tuple(s)
print(t)

# merge two tuples
tt=t[0:4]+t[7:11]
print(tt)
# remove number from tuple:
s=list(tt)
s.remove(s[0])
tt=tuple(s)

print(tt)