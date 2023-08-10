class Square:

    square_list = []
    
    def __init__(self,w,l):
        self.width = w
        self.len = l
        self.square_list.append((self.width,self.len))

square1 = Square(2,3)
square2 = Square(4,1)
square3 = Square(5,5)

print(Square.square_list)
