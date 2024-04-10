class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def distance(self, other):
        return ((self.x - other.x) ** 2 + (self.y - other.y) ** 2) ** 0.5

class Triangle:
    def __init__(self, p1, p2, p3):
        self.p1 = p1
        self.p2 = p2
        self.p3 = p3

    def area(self):
        a = self.p1.distance(self.p2)
        b = self.p2.distance(self.p3)
        c = self.p3.distance(self.p1)
        if a + b <= c or b + c <= a or c + a <= b:
            return -1
        return (((a + b + c) * (a + b - c) * (b + c - a) * (c + a - b)) ** 0.5) / 4
        

def input_triangle(tess):
    points = []
    for _ in range(tess):
        points.append(input().split())
    triangles = []
    for point in points:
        p1 = Point(float(point[0]), float(point[1]))
        p2 = Point(float(point[2]), float(point[3]))
        p3 = Point(float(point[4]), float(point[5]))
        triangles.append(Triangle(p1, p2, p3))
            
    return triangles
    
def main():
    tess = int(input())
    triangles = input_triangle(tess)

    for triangle in triangles:
        if triangle.area() == -1:
            print('INVALID')
        else:
            print(f'{triangle.area():.2f}')

main()