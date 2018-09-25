import math

class Square:

    def __init__(self, length: float):
        self.length = length

    def get_area(self):
        return self.length ** 2

    def get_perimeter(self):
        return 4 * self.length

    def resize(self, scaling_factor: float):
        if scaling_factor >= 0:
            self.length = self.length * scaling_factor
        else :
            raise ValueError("Scaling Factor cannot be negative")
        return self.length