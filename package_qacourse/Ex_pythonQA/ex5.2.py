str=input("Enter a long text plz: ")
x=""
i= len(str)-1

while i>=0:
    x+=str[i]
    i-=1
print(x)