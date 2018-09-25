import math
from interface import implements, Interface
from Shape import Shape

class Parallelogram(implements(Shape)):

    def __init__(self, base: float, slant: float, height: float):
        self.base = base
        self.slant = slant
        self.height = height

        if height > slant:
            raise ValueError("Height cannot be greater than Slant")


    def get_area(self):
        return self.base * self.height

    def get_perimeter(self):
        return 2 * (self.base + self.slant)

    def resize(self, scaling_factor: float):
        if scaling_factor >= 0:
            self.slant, self.base, self.height = self.slant * scaling_factor, self.base * scaling_factor, self.height * scaling_factor
        else :
            raise ValueError("Scaling Factor cannot be negative")
        return self.base, self.slant, self.height