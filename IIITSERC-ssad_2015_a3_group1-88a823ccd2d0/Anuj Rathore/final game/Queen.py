from person import *
from gen import *
class Queen(Person):
    def __init__(self):
        Person.__init__(self, "Princess",1,12)
        self.x = 1
        self.y = 12

    def locate_queen(self, Matrix):
        Matrix[1][12] = 'X'
        Matrix[1][15] = 'Q'
        Matrix[1][27] = 'X'
