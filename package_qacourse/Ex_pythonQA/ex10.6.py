def lowerUpper(str):
    countU=0
    countL=0
    for i in str:
        if(i.islower()):
            countL+=1
        if(i.isupper()):
            countU+=1
    print("number of lower cases:",countL)
    print("number of upper cases:",countU)
   




str="SUkjkjQWcf"
lowerUpper(str)
