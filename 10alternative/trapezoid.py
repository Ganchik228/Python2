import math

class Trapezoid:
    def __init__(self, base_a, base_b, height):
        self.base_a = base_a
        self.base_b = base_b
        self.height = height

    def area(self):
        return (self.base_a + self.base_b) / 2 * self.height

    def perimeter(self):
        c = math.sqrt((self.base_b - self.base_a)**2 + self.height**2)
        return self.base_a + self.base_b + 2 * c

    def inscribed_radius(self):
        return self.area() / (0.5 * (self.base_a + self.base_b) * self.height)

    def circumscribed_radius(self):
        return 0.5 * math.sqrt((self.base_b - self.base_a)**2 + 4*self.height**2) + 0.5 * (self.base_a + self.base_b)