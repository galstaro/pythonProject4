# Ex-7.1
dic1={1:10,2:20}
dic2={3:30,4:40}
dic3={5:50,6:60}
dic1.update(dic2)
dic1.update(dic3)
dic=dic1.copy()
print(dic)

# Ex-7.2
x=int(input("Enter key: "))
print(x in dic)

#Ex-7.3
print(dic.items())
my_dict = dict((y,x) for x,y in dic.items())
print(my_dict)