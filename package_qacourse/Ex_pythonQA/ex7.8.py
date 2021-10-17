names=["Ronaldo","Messi","Neymar","Mbappe","Suarez"]
grades=[100,70,45,78,89]
my_dict = dict((names[x],grades[x]) for x in range(len(names)))
print(my_dict)
sum=0
for i in range(len(grades)):
    sum+=grades[i]
    average=sum/5
print("The average grade is:",average)
best=[]
grades1=list(my_dict.values())
names1=list(my_dict.keys())
for i in range(len(my_dict)):
    if grades1[i]>average:
      best.append(names1[i])
print("The best students are:",best)