class Exc:
    def __init__(self):
        pass
    def main(self):
        try:
            s
        except:
            print("Something went wrong")
        else:
            print("good")
        finally:
            print("done")

Exc().main()


