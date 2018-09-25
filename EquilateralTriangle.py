import math
from interface import implements, Interface
from Shape import Shape


class EquilateralTriangle(implements(Shape)):

    def __init__(self, length: float):
        self.length = length      

    def get_area(self):
        return (math.sqrt(3)/4) * (self.length ** 2)

    def get_perimeter(self):
        return self.length * 3

    def resize(self, scaling_factor: float):
        if scaling_factor >= 0 :
            self.length = self.length * scaling_factor
        else:
            raise ValueError("Scaling Factor cannot be negative")
        return self.length