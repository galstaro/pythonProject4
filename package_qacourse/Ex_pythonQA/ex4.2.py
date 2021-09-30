num1 = int(input("Enter number: "))

for i in range(2,num1):
    if num1%i==0:
        print("This is not a prime number",i)
        break;


if (i==num1-1):
    print("This is a prime number")