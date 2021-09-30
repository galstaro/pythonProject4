print("Hello user you need to Choose a number in your mind that we will guess. The number need to be between 0-100")
i=1
num=50;
high=100
low=0
print("")
while i>0:
  print("The number you think of is",num)
  answer=input("Enter Y if true H if your number is higher and L if your number is lower: ")
  if (answer=="Y"):
      print("Yes we did it after",i,"rounds!!")
      break
  elif answer=="H":
      low = num
      num = round((high + num) / 2)
  elif answer=="L":
      high = num
      num =round( (low + num) / 2)

  i+=1


