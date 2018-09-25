import math
from Parallelogram import Parallelogram
from interface import implements, Interface
from Shape import Shape

class Rectangle(Parallelogram,implements(Shape)):

    def __init__(self, length: float, width: float):
        super().__init__(length, width, width)

    def resize(self, scaling_factor: float):
        super().resize(scaling_factor)
        return self.base, self.height
            