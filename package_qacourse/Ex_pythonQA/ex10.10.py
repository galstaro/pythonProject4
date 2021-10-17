def reverse(str):
    y=len(str)-1
    for i in str:
        if i==str[y]:
            y-=1
        else:
            return False
    else:
        return True

print(reverse("gasdsag"))