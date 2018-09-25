from interface import implements, Interface

class Shape(Interface):

    def get_area(self):
        pass
    def get_perimeter(self):
        pass
    def resize(self, scaling_factor: float):
        pass
