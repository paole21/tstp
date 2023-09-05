
import math

class Circle:
    
    def __init__(self,x):
        """変数xを半径とする"""
        self.radius = x

    def area(self):
        """半径Xを基に円の面積を求めます"""
        return self.radius ** 2 * math.pi

circle = Circle(4)

print(circle.area())
