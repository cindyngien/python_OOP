class Bike(object):
    def __init__(self, price, max_speed):
        self.miles = 0
        self.price = price
        self.max_speed = max_speed

    def displayInfo(self):
        print self.price, self.max_speed, self.miles
        return self

    def ride(self):
        print "riding"
        self.miles = self.miles + 10
        print self.miles
        return self

    def reverse(self):
        print "reversing"
        if self.miles >= 5:
            self.miles = self.miles - 5
        print self.miles
        return self

bike1 = Bike(200,"25mph")
bike2 = Bike(500,"10mph")
bike3 = Bike(300,"15mph")

bike1.ride().ride().ride().reverse().displayInfo()

bike2.ride().reverse().reverse().displayInfo()

bike3.reverse().reverse().reverse().displayInfo()
