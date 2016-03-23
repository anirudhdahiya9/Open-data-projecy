import random
import time
from Body import Body


class Donkey(Body):

    "Class of the fireball-throwing gorilla, Donkey Kong."

    def __init__(self, lev):
        Body.__init__(self, lev)

    def getDonkeyPosition(self):
        """Gets Donkey's position on the Level board."""

        self.__donkeyPos = self.getPosition("D")

    def randMove(self):
        randVar = random.randrange(0, 2)
        if (randVar == 0 and self.levelB[self.__donkeyPos[0]]
                [self.__donkeyPos[1]-1] != "X"):
            self.__donkeyPos = [self.__donkeyPos[0], self.__donkeyPos[1]-1]
            return self.__donkeyPos, 0
        elif (randVar == 1 and self.levelB[self.__donkeyPos[0]]
              [self.__donkeyPos[1]+1] != "X" and
              self.levelB[self.__donkeyPos[0]+1]
              [self.__donkeyPos[1]+1] == 'X'):
            self.__donkeyPos = [self.__donkeyPos[0], self.__donkeyPos[1]+1]
            return self.__donkeyPos, 1
        else:
            return [-1, -1], -1
