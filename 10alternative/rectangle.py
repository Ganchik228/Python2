import math

class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2 * (self.length + self.width)

    def diagonal(self):
        return math.sqrt(self.length**2 + self.width**2)

    def inscribed_radius(self):
        return 0.5 * min(self.length, self.width)

    def circumscribed_radius(self):
        return 0.5 * self.diagonal()