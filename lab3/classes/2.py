import math

class Shape:
    def area(self):
        return 0

class Square(Shape):
    def __init__(self, len):
        self.len = len

    def area(self):
        return self.len ** 2

class Rectangle(Shape):
    def __init__(self, len, wid):
        self.len = len
        self.wid = wid

    def area(self):
        return self.len * self.wid 

a = input("square or rectangle :")

if(a == "square"):
    length = int(input("engiz: ")) 
    square = Square(length)
    print("square area:", square.area())

elif(a == "rectangle"):
    length = int(input("engiz: "))
    width = int(input("engiz: "))
    rectangle = Rectangle(length, width)
    print("rectangle area: ", rectangle.area())

else:
    print("ERROR\nonly square or rectangle")   