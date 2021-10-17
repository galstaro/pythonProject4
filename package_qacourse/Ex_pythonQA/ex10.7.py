def onlyOnce(s):
    set1=set(s)
    return list(set1)

s=[1,5,4,3,7,7,5,4]
print(onlyOnce(s))