class Point :
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def distance(self, k) :
        x0 = self.x - k.x
        y0 = self.y - k.y
        return (x0 * x0 + y0 * y0) ** 0.5

class Triangle :
    def __init__(self, p1, p2, p3):
        self.p1 = p1
        self.p2 = p2
        self.p3 = p3
    def area(self) :
        a = self.p1.distance(self.p2)
        b = self.p2.distance(self.p3)
        c = self.p1.distance(self.p3)
        if a + b <= c or a + c <= b or b + c <= a :
            return 'INVALID'
        else :
            S = ((a + b + c) * (a + b - c) * (a - b + c) * (-a + b + c)) ** 0.5 / 4
            return format(S, '.2f')

a = []
t = int(input())
for x in range(t):
    a += [float(i) for i in input().split()]
i = 0
for index in range(t):
    triagle = Triangle(Point(a[i], a[i+1]), Point(a[i+2], a[i+3]), Point(a[i+4], a[i+5]))
    print(triagle.area())
    i += 6