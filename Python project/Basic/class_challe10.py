class Square:

    square_list = []
    
    def __init__(self,s1,s2,s3,s4):
        self.s1 = s1
        self.s2 = s2
        self.s3 = s3
        self.s4 = s4
        self.square_list.append((self.s1,self.s2,self.s3,self.s4))

    def __repr__(self):
        return "{} by {} by {} by {}".format(self.s1,self.s2,self.s3,self.s4)

square = Square(2,6,9,1)

print(square)
