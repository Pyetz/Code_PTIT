class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def distance(self, other):
        return ((self.x - other.x) ** 2 + (self.y - other.y) ** 2) ** 0.5
    
def main():
    tess = int(input())
    points = [(input().split()) for _ in range(tess)]

    for point in points:
        p1 = Point(float(point[0]), float(point[1]))
        p2 = Point(float(point[2]), float(point[3]))
        print(f'{p1.distance(p2):.4f}')

main()