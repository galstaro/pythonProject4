def prime(num):
    if (num%2==0 or num%3==0) and (num>3 or num==0):
        return False
    else:
        return True

print(prime(31))