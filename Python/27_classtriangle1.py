import math

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distance(self, other):
        dx = self.x - other.x
        dy = self.y - other.y
        return math.sqrt(dx**2 + dy**2)

class Triangle:
    def __init__(self, p1, p2, p3):
        self.p1 = p1
        self.p2 = p2
        self.p3 = p3

    def is_valid(self):
        a = self.p1.distance(self.p2)
        b = self.p2.distance(self.p3)
        c = self.p3.distance(self.p1)
        return a + b > c and b + c > a and c + a > b

    def perimeter(self):
        if not self.is_valid():
            return "INVALID"
        a = self.p1.distance(self.p2)
        b = self.p2.distance(self.p3)
        c = self.p3.distance(self.p1)
        return round(a + b + c, 3)

# Đọc input và xử lý
num_tests = int(input())
for _ in range(num_tests):
    x1, y1, x2, y2, x3, y3 = map(float, input().split())
    p1 = Point(x1, y1)
    p2 = Point(x2, y2)
    p3 = Point(x3, y3)
    triangle = Triangle(p1, p2, p3)
    print(triangle.perimeter())