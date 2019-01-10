class Character(object):
    def __init__(self):
        self.health = 100
        
class Blacksmith(Character):
    def __init__(self):
        super(Blacksmith, self).__init__()

class Hero(Character):
    def __init__(self):
        super(Hero, self).__init__()


bs = Blacksmith()
h = Hero()
print (bs.health)
print (h.health)

