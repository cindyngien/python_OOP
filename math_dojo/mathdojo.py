class MathDojo(object):
    def __init__(self):
        self.total = 0

    def add(self, *restOfArg):
        # for i in restOfArg:
        #     if type(i) == int:
        #         self.total += i
        #     elif type(i) == list or type(i) == tuple:
        #         for j in i:
        #             self.total += j
        # return self


        #restOfArg is a list. You have to loop through the list first.
        #J if basically looping through every index in the list and checking
        for i in restOfArg:
            try:
                for j in i:
                    self.total += j
            except TypeError:
                self.total += i
        return self

    def subtract(self, *restOfArg):
        for i in restOfArg:
            try:
                for j in i:
                    self.total -= j
            except TypeError:
                self.total -= i
        return self
    def result(self):
        print self.total
        return self

md = MathDojo()
md.add([1],3,4).add([3, 5, 7, 8], [2, 4.3, 1.25]).subtract(2, [2,3], [1.1, 2.3]).result()
