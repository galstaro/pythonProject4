dic={1:20,2:99,3:78,4:99,5:130,6:20,7:45,8:78,9:10}
s=list(dic.values())
print(s)
s1 = list(dic.items())
print(s1)

for i in range(len(s1)-1):
    x=i
    while x<len(s1):
        if s[i]==s[x] and x!=i:
            del s[x]
            s1.remove(s1[x])
        x+=1

dic=dict(s1)
print(dic)