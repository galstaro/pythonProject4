import datetime
#from datetime import datetime
# #ex9.1
# name=input("Enter your name: ")
# age=int(input("Enter your age: "))
# now = datetime.now()
# print(now)
# year=int(now.strftime("%Y"))
# print(year)
# age100=100-age
# age100+=year
# print(age100)
#
# #ex9.2
# now = datetime.now()
# year=now.strftime("%Y")
# month=now.strftime("%m")
# day=now.strftime("%d")
#
# print(f"American format date: {month}/{day}/{year}")
# print(f"European format date: {day}/{month}/{year}")
#
# #ex9.3
# #s=datetime.strptime(input("Enter date: "),'%b %d %Y')
# #print(s)
#
# #ex9.4
d_number=int(input("Enter number: "))
date = datetime.datetime.now()
day=int(date.strftime("%w"))+1

if 0<d_number<8:
    if d_number>day:
        date+=datetime.timedelta(days=d_number-day)
    elif day>d_number:
        date-=datetime.timedelta(days=day-d_number)
else:
    print("Enter number between 1-7")
print(date)


