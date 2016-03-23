from person import *
from Board import *
from gen import *
import random
import time

class Donkey(Person, Board):
    def __init__(self,x,y):
        Person.__init__(self, "Donkey",4,6)
        Board.__init__(self,30,90)
        self.x=x
        self.y=y
        self.direction = 'left'
        self.backup = ' '

    def locate_donkey(self, Matrix):
        Matrix[self.x][self.y] = 'D'

    def movement(self, Matrix):
        if (self.direction == 'right'):
            if(checkWall(self.x+1, self.y+1,Matrix) or
                Matrix[self.x + 1][self.y+1] == 'H'):

                Matrix[self.x][self.y] = self.backup
                self.y+=1
                self.backup = Matrix[self.x][self.y]
                Matrix[self.x][self.y] = 'D'

            else:
                self.direction = 'left'


        elif self.direction == 'left':
            if checkWall(self.x, self.y-1,Matrix):
                self.direction = 'right'
            else:
                Matrix[self.x][self.y] = self.backup
                self.y-=1
                self.backup = Matrix[self.x][self.y]
                Matrix[self.x][self.y] = 'D'

    def randomize_direction(self):
        t = random.randint(0, 1)
        if t == 1:
            self.direction = "right"
        else:
            self.direction = "left"

    def getPosition(self):
        return self.x,self.y
