list1=[1,20,45,32,2,56,-9,47,-1]
list2=[12,20,415,32,2,56,-91,48,-1]

set1=set(list1)
set2=set(list2)
print(set1)
print(set2)
set3=set1.copy()
set3.update(set2)
print(set3)
set3.discard(415)
print(set3)
print(len(set3))
list3=list(set3)
max=list3[0]
min=list3[0]
for i in range(len(set3)):
    if(list3[i]>max):
        max=list3[i]
    if(list3[i]<min):
        min=list3[i]
print("max:",max,"min:",min)

set4=set3.copy()
set4.add(14)
set4.add(567)

set1.clear()
set2.clear()

print(set4,set1,set2)