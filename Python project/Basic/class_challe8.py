class Horse:
    def __init__(self,name,weight,rider):
        self.name = name
        self.weight = weight
        self.rider = rider

class Rider:
    def __init__(self,person):
        self.person = person

person = Rider("Tom")

uma = Horse("uma",500,person)

print(uma.rider.person)
