from animal import Animal

class Dog(Animal):
    def __init__(self, name):
        super(Dog, self).__init__(self)
        self.name = name
        self.health = 150

    def pet(self):
        self.health += 5
        return self



dog1 = Dog("Happy")
dog1.walk().walk().walk().run().run().pet().displayHealth()
