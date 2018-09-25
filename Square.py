import math
from Rectangle import Rectangle
from interface import implements, Interface
from Shape import Shape

class Square(Rectangle, implements(Shape)):

    def __init__(self, length: float):
        super().__init__(length, length)