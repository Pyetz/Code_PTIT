import math

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def distance(self, other) :
        x0 = self.x - other.x
        y0 = self.y - other.y
        return (x0 ** 2 + y0 ** 2) ** 0.5

class Triangle:
    def __init__(self, p1, p2, p3):
        self.p1 = p1
        self.p2 = p2
        self.p3 = p3
    def perimeter(self):
        a = self.p1.distance(self.p2)
        b = self.p2.distance(self.p3)
        c = self.p1.distance(self.p3)

        if a + b <= c or b + c <= a or c + a <= b:
            return 'INVALID'
        else :
            P = a + b + c
            return format(P, '.3f')

points = []
tess = int(input())
for _ in range(tess):
    points += [float(i) for i in input().split()]
i = 0
for _ in range(tess):
    triagle = Triangle(Point(points[i], points[i+1]), Point(points[i+2], points[i+3]), Point(points[i+4], points[i+5]))
    print(triagle.perimeter())
    i += 6