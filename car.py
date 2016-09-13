class Car(object):
    def __init__(self, price, speed, fuel, mileage):
        self.price = price
        self.speed = speed
        self.fuel = fuel
        self.mileage = mileage
        self.tax = 0.12
        if self.price >= 10000:
            self.tax = 0.15

    def displayAll(self):
        print self.price, self.speed, self.fuel, self.mileage, self.tax
        return self


car1 = Car(3000, "60 mph", "empty", "20 mpg")
car2 = Car(10000, "80 mph", "full", "30 mpg")
car3 = Car(6000, "20 mph", "half full", "15 mpg")
car4 = Car(8000, "40 mph", "kind of full", "20 mpg")
car5 = Car(20000, "100 mph", "not full", "10 mpg")
car6 = Car(2000, "60 mph", "empty", "20 mpg")

car1.displayAll()
car2.displayAll()
car3.displayAll()
car4.displayAll()
car5.displayAll()
car6.displayAll()
