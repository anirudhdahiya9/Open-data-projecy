import sys
import tty
from Body import Body


class Player(Body):

    """Class for the Player."""

    def __init__(self, lev, score=0):
        Body.__init__(self, lev)
        self.__lives = 3
        self.__score = score
        self.__visited = [0] * 1001
        self.__jflag = 0

    def retLives(self):
        return self.__lives

    def getPlayerPosition(self):
        self.__playerPos = self.getPosition("P")

    def retPlayerPosition(self):
        return self.__playerPos

    def setjFlag(self):
        """Sets the jump flag.

        This is the flag responsible for disabling gravity for
        3 steps"""

        self.__jflag = 1

    def unsetjFlag(self):
        """Unsets the jump flag."""

        self.__jflag = 0

    def motionController(self, key):
        """Responsible for Player motion by handling keypresses.

        Translates the ASCII value of various keypresses into
        motion."""

        self.__key = key
        if (self.__jflag == 0 and self.inAir()):
            self.__playerPos = [self.__playerPos[0]+1, self.__playerPos[1]]
            return self.gravity([self.__playerPos[0]-1, self.__playerPos[1]])
        if self.__key == 65 or self.__key == 97:
            return self.moveLeft()
        if self.__key == 68 or self.__key == 100:
            return self.moveRight()
        if self.__key == 87 or self.__key == 119:
            return self.moveUp()
        if self.__key == 83 or self.__key == 115:
            return self.moveDown()
        else:
            return self.dontMove()

    def dontMove(self):
        """Returns current position which is used to restrict motion"""

        return [self.__playerPos[0], self.__playerPos[1]]

    def inAir(self):
        if (self.levelB[self.__playerPos[0]+1][self.__playerPos[1]] in
                [" ", "O", "C"]):
            return True
        return False

    def checkWall(self, dir):
        """Used to check for collision with walls.(Xs)"""

        if dir == 1:
            if self.levelB[self.__playerPos[0]][self.__playerPos[1]-1] == "X":
                return False
        if dir == 2:
            if self.levelB[self.__playerPos[0]][self.__playerPos[1]+1] == "X":
                return False
        if dir == 3:
            if self.levelB[self.__playerPos[0]-1][self.__playerPos[1]] == "X":
                return False
        return True

    def moveLeft(self):
        if self.checkWall(1) is True:
            self.__playerPos = [self.__playerPos[0], self.__playerPos[1]-1]
            return self.__playerPos
        return self.dontMove()

    def moveRight(self):
        if self.checkWall(2) is True:
            self.__playerPos = [self.__playerPos[0], self.__playerPos[1]+1]
            return self.__playerPos
        return self.dontMove()

    def moveUp(self):
        if self.__playerPos in self.ladderCoordinates or self.__jflag == 1:
            if self.checkWall(3) is True:
                self.__playerPos = [self.__playerPos[0]-1, self.__playerPos[1]]
                return self.__playerPos
        return self.dontMove()

    def moveDown(self):
        onedown = [self.__playerPos[0]+1, self.__playerPos[1]]
        if onedown in self.ladderCoordinates:
            self.__playerPos = onedown
            return onedown
        return self.dontMove()

    def collectCoin(self):
        """Whenever the Player is on the co-ordinates of a coin,
        the coin collected and score is increased."""

        if (self.__playerPos in self.coinCoordinates and
            self.__visited
                [self.coinCoordinates.index(self.__playerPos)] == 0):
            self.__score += 5
            self.__visited[self.coinCoordinates.index(self.__playerPos)] = 1
        return self.__visited

    def fireDeath(self):
        """Checks for fireball collision and returns player back to
        the spawn location."""

        if self.__playerPos in self._fireCoordinates:
            self.__lives -= 1
            self.__score -= 25
            self.__playerPos = [24, 2]
            return True
        return False

    def retScore(self):
        return self.__score

    def victory(self):
        """Checks for victory condition."""

        if self.__playerPos == self.prinPoint:
            return True
        return False
