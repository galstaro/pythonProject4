someting=input("type something: ")
note=input("type note you want to find: ")
count=0
for val in someting:
    if val==note:
        count+=1
print("the note found",count,"times.")
