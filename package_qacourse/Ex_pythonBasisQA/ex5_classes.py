class HardDisk:
    def __init__(self):
        self.totalspace = 100
        self.takenspace = 0
        self.numoffiles = 0

    def show(self):
        return f"Total space[GB]: {self.totalspace} \nTaken space[GB]: {self.takenspace} \nNumber of files: {self.numoffiles}"
    def freeSpace(self):
        return self.totalspace-self.takenspace
    def addFile(self,gb):
        if (self.takenspace+gb<=100):
            self.numoffiles+=1
            self.takenspace+=gb
            print("Success. File is added to hard disk.")
        else:
            print("Fail to add file to hard disk.")
    def delFile(self,gb):
        self.takenspace -= gb
        self.numoffiles-=1
        if self.takenspace<0:
            self.takenspace=0


disc=HardDisk()
for i in range(5):
    disc.addFile(int(input("Enter space[gb] your file will take: ")))

disc.delFile(15)
print(disc.show())