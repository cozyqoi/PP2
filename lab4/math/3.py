import math

s = int(input("количество углов: "))
a = int(input("длина сторон: "))
area = (s * a ** 2) / (4 * math.tan(math.pi / s))
print(round(area, 4))