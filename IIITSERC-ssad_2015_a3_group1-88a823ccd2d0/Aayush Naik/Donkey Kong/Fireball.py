import random
from Body import Body


class Fireball(Body):

    def __init__(self, lev):
        Body.__init__(self, lev)
        self.__dir = random.randrange(0, 2)  # 0=l 1=r
        self.__speed = 1
        self.__destroyed = 0
        self.__fPos = [1, 79]

    def retFPos(self):
        """Returns co-ordinates of the fireball."""

        return self.__fPos

    def spawn(self):
        """Spawns the fireball either to the left or right of Donkey."""

        dPos = self.getPosition("D")
        rno = random.randrange(1, 4)
        if rno in [1, 2] and self.levelB[dPos[0]][dPos[1] + 1] != "X":
            self.__fPos = [dPos[0], dPos[1] + 1]
            return self.__fPos, 3
        elif rno == 3 and self.levelB[dPos[0]][dPos[1] - 1] != "X":
            self.__fPos = [dPos[0], dPos[1] - 1]
            return self.__fPos, 3
        else:
            return [4, 4], 3

    def motionFire(self):
        """Resposible for the updation of the fireball's position."""

        if self.__destroyed == 0:
            if (self.levelB[self.__fPos[0]+1][self.__fPos[1]] == "X" and
                    self.levelB[self.__fPos[0]][self.__fPos[1]] == "H"):
                self.__dir = -self.__dir
            if self.levelB[self.__fPos[0]+1][self.__fPos[1]] in\
               [" ", "P", "H", "C"]:
                self.__fPos = [self.__fPos[0] + 1, self.__fPos[1]]
                return self.gravity([self.__fPos[0] - 1, self.__fPos[1]]), 2
            elif self.__dir == 0:
                if self.levelB[self.__fPos[0]][self.__fPos[1] - 1] == "X":
                    self.__fPos = [self.__fPos[0], self.__fPos[1] + self.__speed]
                    self.__dir = 1
                else:
                    self.__fPos = [self.__fPos[0], self.__fPos[1] - self.__speed]
                return self.__fPos, self.__dir
            else:
                if self.levelB[self.__fPos[0]][self.__fPos[1] + 1] == "X":
                    self.__fPos = [self.__fPos[0], self.__fPos[1] - self.__speed]
                    self.__dir = 0
                else:
                    self.__fPos = [self.__fPos[0], self.__fPos[1] + self.__speed]
                return self.__fPos, self.__dir
        else:
            return [1, 79], 3

    def destroy(self):
        """Sets the flag that the fireball is ready to be destroyed."""

        if self.__fPos == self.pSpawnPoint:
            self.__destroyed = 1
