s=input("Enter a long text plz: ")
x=""
i= len(s)-1

while i>=0:
    x+=s[i]
    i-=1
print(x)