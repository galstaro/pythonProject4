dic={1:20,2:30,3:78,4:99,5:130}
key=int(input("Enter key: "))
s=list(dic.keys())
print(s)
s1 = list(dic.items())
print(s1)
for i in range(len(s)):
    if s[i]==key:
        s1.remove(s1[i])
        dic=dict(s1)

print(dic)
