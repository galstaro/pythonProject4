from ex12_classes import *

shapes=[Point(3,1),Circle(3,1,5),Cylinder(3,1,5,10)]

print(shapes[1].centercircle())
for i in shapes:
    print(i.__str__())

