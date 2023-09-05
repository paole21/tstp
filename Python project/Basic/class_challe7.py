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

class Shape:
    def what_am_i(self):
        print("I am a shape!!!!!!!")

class Square(Shape):
    def __init__(self,w,l):
        self.width = w
        self.len = l

    def calculate_perimeter(self):
        return self.width * 2 + self.len * 2

    def change_size(self,w,l):
        self.width = self.width + w
        self.len = self.len + l

square = Square(4,7)

square.what_am_i()
