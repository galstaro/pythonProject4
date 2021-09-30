array=[1,2,3,4,5,6,7,8,9,10]
x=array[7:]
print(x)

print(array[::-1])

print(array[::2])


#copy array without using the same id,address
x=array.copy()
x[4]=int(input("Enter number: "))
x[5]=int(input("Enter number: "))
x.append(int(input("Enter number: ")))
print(x)


x=array.copy()
i=0

while i<len(x):
    x[i]=array[i]*2
    i+=1

print(x)

y=[array[-1]]
y+=[array[0]]
print(y)


