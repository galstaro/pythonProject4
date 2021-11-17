def newlen(lis):
    """a method that get a list and return the length of list"""
    length = 0
    for i in lis:
        length += 1
    return length
print(newlen.__doc__)

def newcount(lis,num):
    count=0
    for i in lis:
        if(num==i):
            count+=1
    return count

def newfind(lis,num,start):
    for start in range(len(lis)):
        if lis[start]==num:
            return start

def newmax(lis):
    max=lis[0]
    for i in lis:
        if(lis[i]>max):
            max=lis[i]
    return max

def newlist(tipus):
    lis=[]
    if(type(tipus) is (int or float or bool)):
        print("Error")
        return None
    else:
        lis.extend(tipus)
        return lis

print(newlist("str123"))

def newremove(lis,val):
    for i in lis:
        if i==val:
            lis.pop(lis.index(i))
    return lis

lis=[1,2,3,4,5,6]
print(newremove(lis,3))

def newkeys(dic):
    lis=[]
    lis.extend(dic)
    return lis

def newvalues(dic):
    lis=[]
    for i in dic:
        lis.append(dic[i])
    return lis

def newitems(dic):
    lis=[]
    lis+=((i,dic[i]) for i in dic)
    return lis

dic={1:20,2:99,3:78,4:99,5:130,6:20,7:45,8:78,9:10}
print(newkeys(dic))
print(newvalues(dic))
print(newitems(dic))

def newset(lis):
    s={1}
    s.pop()
    for i in lis:
            s.add(i)
    return s

print(newset([1,2,3,2,3,78,45,78]))


