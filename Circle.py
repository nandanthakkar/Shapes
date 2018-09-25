import math
from interface import implements, Interface
from Shape import Shape

class Circle(implements(Shape)):

    def __init__(self, radius :float):
        self.radius = radius   

    def get_area(self):
        return math.pi *(self.radius ** 2)

    def get_perimeter(self):
        return 2 * math.pi * self.radius

    def resize(self,scaling_factor: float):

        if scaling_factor >= 0 :
            self.radius = self.radius * scaling_factor
        else : 
            raise ValueError("Scaling Factor cannot be negative")
        return self.radius