import math

class Rectangle:

    def __init__(self, length: float, width: float):
        self.length = length
        self.width = width

    def get_area(self):
        return self.length * self.width

    def get_perimeter(self):
        return 2 * (self.length + self.width)

    def resize(self, scaling_factor: float):
        if scaling_factor >= 0:
            self.length, self.width = self.length * scaling_factor, self.width * scaling_factor
        else :
            raise ValueError("Scaling Factor cannot be negative")
        return self.length, self.width
            