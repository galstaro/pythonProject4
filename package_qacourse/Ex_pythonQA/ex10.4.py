def opString(str):
    i=len(str)-1
    s=""
    while i>=0:
        s+=str[i]
        i-=1
    return s

print(opString("starobinetz"))