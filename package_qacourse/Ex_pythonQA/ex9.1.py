from datetime import datetime

#ex9.1
name=input("Enter your name: ")
age=int(input("Enter your age: "))
now = datetime.now()
print(now)
year=int(now.strftime("%Y"))
print(year)
age100=100-age
age100+=year
print(age100)

#ex9.2
now = datetime.now()
year=now.strftime("%Y")
month=now.strftime("%m")
day=now.strftime("%d")

print(f"American format date: {month}/{day}/{year}")
print(f"European format date: {day}/{month}/{year}")