import math

class Vector:
    def __init__(self, x_component, y_component):
        self.x = x_component
        self.y = y_component
    def get_magnitude(self):
        magnitude = math.sqrt(self.x ** 2 + self.y ** 2)
        return magnitude
    def __str__(self):
        vector = f"<{self.x},{self.y}>"
        return vector

vector1 = Vector(3,4)
print(vector1)

vector2 = Vector(4,5)
print(vector2)

class Vector_Manipulation:
    def __init__(self, vector1, vector2):
        self.one = vector1
        self.two = vector2
    def dot_product(self):
        dot = self.one.x * self.two.x + self.one.y * self.two.y
        return dot
    def cross_product(self):
        cross = self.one.x * self.two.y - self.one.y * self.two.x
        return cross

vector_set = Vector_Manipulation(vector1, vector2)
print(vector_set.cross_product())
print(vector_set.dot_product())