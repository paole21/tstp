
class Rectangle:
    def __init__(self,w,l):
        self.width = w
        self.len = l

    def calculate_perimeter(self):
        return self.width * 2 + self.len * 2

rectangle = Rectangle(4,8)

print(rectangle.calculate_perimeter())
