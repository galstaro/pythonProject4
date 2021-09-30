i=0
passed=0
fail=0
print("Hello teacher!")
while i<10:
    if 60<=int(input("Enter test score: ")):
        passed+=1
    else:
        fail+=1
    i+=1

print("The number of students who passed the test is:",passed)
print("The number of students who failed the test is:",fail)