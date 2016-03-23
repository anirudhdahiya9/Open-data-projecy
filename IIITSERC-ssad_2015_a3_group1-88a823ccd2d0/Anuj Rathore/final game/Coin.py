from Board import *
from gen import *
import random
class Coins(Board):
    def __init__(self,num_coins):
        self.num_coins = num_coins

    def create_coins(self,Matrix):
        for i in range (3):
            for j in range (self.num_coins):
                x = random.randint (3,89)
                row = i*5
                if (28-row) == 9 and x == 76:
                    continue
                if (28-row) == 9 and x == 75:
                    continue
                if (28-row) == 9 and x == 74:
                    continue
                if (28-row) == 13 and x == 24:
                    continue
                if (28-row) == 13 and x == 23:
                    continue
                if (28-row) == 13 and x == 25:
                    continue
                if (28-row) == 18 and x == 9:
                    continue
                if (28-row) == 18 and x == 10:
                    continue
                if (28-row) == 18 and x == 8:
                    continue
                if (28-row) == 18 and x == 85:
                    continue
                if (28-row) == 18 and x == 86:
                    continue
                if (28-row) == 18 and x == 87:
                    continue
                if(Matrix[28-row][x] == ' '):
                    Matrix[28-row][x] = 'C'

        for i in range (self.num_coins):
            x = random.randint(3,89)
            if(Matrix[9][x] == ' '):
                Matrix[9][x] = 'C'


        for i in range (self.num_coins):
            x = random.randint(3,89)
            if(Matrix[13][x] == ' '):
                Matrix[13][x] = 'C'
