import math

class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def show(self):
        print("(", self.x, ",", self.y, ")")

    def move(self, dx, dy):
        self.x += dx
        self.y += dy

    def dist(self, other):
        return math.sqrt((self.x - other.x) ** 2 + (self.y - other.y) ** 2)

x1 = int(input("x1 engiz: "))
y1 = int(input("y1 engiz: "))
point1 = Point(x1, y1)

x2 = int(input("x2 engiz: "))
y2 = int(input("y2 engiz: "))
point2 = Point(x2, y2)

point1.show()
point2.show()

distance = point1.dist(point2)
print("distance:", distance)

dx = int(input("x ozgertu: "))
dy = int(input("y ozgertu: "))
point1.move(dx, dy)

point1.show()
