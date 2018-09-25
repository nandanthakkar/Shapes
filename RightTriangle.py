import math
from interface import implements, Interface
from Shape import Shape

class RightTriangle(implements(Shape)):

    def __init__(self, base: float, height: float):
        self.base = base
        self.height = height
        self.hypotenus = math.sqrt(base ** 2 + height ** 2)


    def get_area(self):
        return 0.5 * self.base * self.height

    def get_perimeter(self):
        return self.base + self.height + self.hypotenus

    def resize(self, scaling_factor: float):
        if scaling_factor >= 0 :
            self.base, self.height, self.hypotenus = self.base * scaling_factor, self.height * scaling_factor, self.hypotenus * scaling_factor
        else :
            raise ValueError("Scaling Factor cannot be negative")
        return self.base, self.height, self.hypotenus