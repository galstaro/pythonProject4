class Shape:
    def area(self):
        return 0
    def volume(self):
        return 0

class Point(Shape):
    def __init__(self,x,y):
        self.x=float(x)
        self.y=float(y)
    def __str__(self):
        return f"Class name: Point \n Attributes are:({self.x},{self.y}) \n Area is:{super().area()} \n Volume is:{super().volume()}"

class Circle(Point):
    def __init__(self,x,y,radios):
        Point.__init__(self,x,y)
        self.radios=float(radios)
    def area(self):
        return self.radios*self.radios*3.14
    def circumference(self):
        return 2*3.14*self.radios
    def centercircle(self):
        return f"({self.x},{self.y})"
    def __str__(self):
        return f"Class name: Circle \n Attributes are:({self.x},{self.y}) radios: {self.radios} \n Area is:{self.area()} \n Circumference is:{self.circumference()} \n Volume is:{super().volume()}"

class Cylinder(Circle):
    def __init__(self,x,y,radios,height):
        Circle.__init__(self,x,y,radios)
        self.height=float(height)
    def volume(self):
        return self.radios*self.radios*3.14*self.height
    def area(self):
        return super().circumference()*(self.radios+self.height)
    def __str__(self):
        return f"Class name: Cylinder \n Attributes are:({self.x},{self.y}) radios: {self.radios} height: {self.height} \n Area is:{self.area()} \n Volume is:{self.volume()}"
