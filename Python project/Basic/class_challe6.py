
class Rectangle:
    def __init__(self,s1,s2,s3,s4,s5,s6):
        self.s1 = s1
        self.s2 = s2
        self.s3 = s3
        self.s4 = s4
        self.s5 = s5
        self.s6 = s6

    def calculate_perimeter(self):
        return self.s1 + self.s2 + self.s3 + self.s4 + self.s5 + self.s6

class Square:
    def __init__(self,w,l):
        self.width = w
        self.len = l

    def calculate_perimeter(self):
        return self.width * 2 + self.len * 2

    def change_size(self,w,l):
        self.width = self.width + w
        self.len = self.len + l


rectangle = Rectangle(4,7,2,3,9,12)

print(rectangle.calculate_perimeter())

square = Square(16,8)

print(square.calculate_perimeter())

square.change_size(5,-3)

print(square.calculate_perimeter())
