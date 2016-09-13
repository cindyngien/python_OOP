from animal import Animal

class Dragon(Animal):
    def __init__(self, name):
        super(Dragon, self).__init__(self)
        self.name = name
        self.health = 170
        print "This is a dragon!"

    def fly(self):
        self.health -= 10
        return self


dragon1 = Dragon("Draaaaagon")
dragon1.walk().walk().walk().run().run().fly().fly().displayHealth()
