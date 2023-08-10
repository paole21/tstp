
class Triangle:
    def __init__(self,u,h):
        self.under = u
        self.high = h

    def area(self):
        return self.under * self.high / 2
    
triangle = Triangle(6,7)

print(triangle.area())
