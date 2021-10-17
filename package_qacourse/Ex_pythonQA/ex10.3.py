def func(s):
    count=1
    for i in s:
        count*=i
    return count

s=[1,5,7,4,8,6]
print(func(s))