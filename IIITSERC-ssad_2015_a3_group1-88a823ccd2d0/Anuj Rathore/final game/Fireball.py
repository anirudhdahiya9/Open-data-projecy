from Donkey import *
from gen import *
import random
class FireBalls(Donkey):
    def __init__(self, position, Matrix):
        self.x = position [0]
        self.y = position [1]+3
        Matrix[self.x][self.y] = 'O'
        self.backup = ' '
        self.direction = 'right'
        self.gravity  = 0

    def random_motion(self):
        t = random.randint(0,1)
        return t

    def path (self, Matrix):
        if self.direction == 'left':
            if checkWall (self.x, self.y-1,Matrix) or Matrix [self.x][self.y-1] == 'O' or Matrix [self.x][self.y-1] == 'D' or Matrix [self.x -1][self.y-1] == 'O':
                self.direction = 'right'

            else:
                if Matrix[self.x+1][self.y-1]== ' ':
                    self.gravity = 1


                Matrix[self.x][self.y] = self.backup
                self.backup = Matrix[self.x][self.y -1]
                self.y -= 1
                Matrix[self.x][self.y] = 'O'
        else:
            if (checkWall(self.x,self.y+1,Matrix) or Matrix[self.x][self.y+1] == 'O' or Matrix [self.x][self.y+1] == 'D' or Matrix [self.x -1][self.y+1] == 'D'):
                self.direction = 'left'
            else:
                if Matrix[self.x+1][self.y+1]== ' ':
                    self.gravity = 1


                Matrix[self.x][self.y] = self.backup
                self.backup = Matrix[self.x][self.y + 1]
                self.y += 1
                Matrix[self.x][self.y] = 'O'


    def motion(self, position, Matrix):

        if (self.x == 28 and self.y == 1):
            Matrix[self.x][self.y] = ' '
            self.x = position[0]
            self.y = position[1]+3
            self.direction = 'right'



        elif self.gravity == 1:
            if checkWall (self.x+2,self.y,Matrix):
                self.gravity = 0
                if self.random_motion():
                    self.direction = 'right'
                else:
                    self.direction = 'left'
            if (Matrix[self.x+1][self.y] == 'O'):
                self.backup = ' '
            Matrix[self.x][self.y] = self.backup
            self.backup = Matrix[self.x + 1][self.y]
            Matrix[self.x + 1][self.y] = 'O'
            self.x += 1

        elif (Matrix[self.x+1][self.y] == 'H'):
            if (self.random_motion()):
                Matrix[self.x][self.y] = self.backup
                self.backup = Matrix[self.x + 1][self.y]

                Matrix[self.x + 1][self.y] = 'O'
                self.x += 1
                self.gravity = 1

            else:
                self.path(Matrix)

        else:
            self.path(Matrix)

    def getPosition(self):
        return self.x,self.y
