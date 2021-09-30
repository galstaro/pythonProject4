import statistics

i=0
x=[]
biggest=0
smallest=0
while(i<6):
    x.append(int(input("Enter number to array: ")))
    if i==0:
        smallest=x[i]
        i += 1
        continue
    if x[i]>biggest:
        biggest=x[i]
    if x[i]<smallest:
        smallest=x[i]
    i+=1

print("The array is ",x)
print("The biggest number is",biggest)
print("The smallest number is",smallest)
print("The average of the numbers in this array is",statistics.mean(x))