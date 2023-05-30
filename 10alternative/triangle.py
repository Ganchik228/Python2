import math

class Triangle:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def area(self):
        p = (self.a + self.b + self.c) / 2
        return math.sqrt(p * (p - self.a) * (p - self.b) * (p - self.c))

    def perimeter(self):
        return self.a + self.b + self.c

    def circumradius(self):
        return (self.a * self.b * self.c) / (4 * self.area())

    def inradius(self):
        return 2 * self.area() / self.perimeter()