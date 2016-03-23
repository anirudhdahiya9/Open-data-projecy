import sys
import random
import time
import os
import signal
import tty
import time

class Level:

    """Class for the Level board."""

    def __init__(self):
        """Initializes the Level board and other variables.

        The self.__levelBp list of lists crosses the standard of 80
        characters per line of the PEP 8 standard, but it is only
        so, for more clarity. This way the Level board can be easily
        edited by the user."""

        self.__levelBp = [
            list("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"),
            list("XX           X    Q   X                                                         XX"),
            list("XX           XXXXXXXHXX                                                         XX"),
            list("XX                  H                                                           XX"),
            list("XX  D               H                                                           XX"),
            list("XXXXXXXXXXXHXXXXXXXXXXXX  XXXXXXXXX  XXXXXXXXXXXXXHXXXXX                        XX"),
            list("XX         H                                      H                             XX"),
            list("XX                                                H                             XX"),
            list("XX         H                                      H                             XX"),
            list("XX       XXXXXXXXXXHXXXXXXXXXX  XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"),
            list("XX                 H                                                            XX"),
            list("XX                 H                                                            XX"),
            list("XX                 H                                                            XX"),
            list("XXXXXXXXXXXXXXXXXXXXXXXHXXXXXXXHXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX        XX"),
            list("XX                     H       H                                                XX"),
            list("XX                     H                                                        XX"),
            list("XX                     H       H                                                XX"),
            list("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX  HXXXXXX                                       XX"),
            list("XX                                H                                             XX"),
            list("XX                                H                                             XX"),
            list("xX                                H                                             XX"),
            list("XX                        XXXXXXXXXXXXX  XXXXXXXXXXXHXXXXXXXXXXX  XXXXXXXXXXXXXXXX"),
            list("XX                                                  H                           XX"),
            list("XX                                                  H                           XX"),
            list("XX                                        H         H                           XX"),
            list("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")]

        self.__playSpawnPoint = [24, 2]
        self.__princessPoint = [1, 18]
        self.__grave = [1, 79]
        self.__donkeyPos = [4, 2]
        self.__playerPos = [24, 2]
        self.__levelBp[24][2] = "P"
        self.__fireC = []    
        for line in self.__levelBp:
            temp = list(line)

    def retBlueP(self):
        """Returns the Level board."""

        return self.__levelBp

    def retSpawnPoint(self):
        """Returns the Player Spawn Point."""

        return self.__playSpawnPoint

    def retPrincessPoint(self):
        return self.__princessPoint

    def findLadderCoordinates(self):
        self.ladderC = []
        for i, x in enumerate(self.__levelBp):
            indices = [j for j, a in enumerate(x) if a == "H"]
            for k in indices:
                ladderPos = [i, k]
                self.ladderC.append(ladderPos)

    def findCoinCoordinates(self):
        self.coinC = []
        for i, x in enumerate(self.__levelBp):
            indices = [j for j, a in enumerate(x) if a == "C"]
            for k in indices:
                coinPos = [i, k]
                self.coinC.append(coinPos)

    def getFireCoordinates(self, lis):
        self.__fireC = []
        self.__fireC.extend(lis)

    def retLadderCoordinates(self):
        return self.ladderC

    def retCoinProperties(self):
        return self.coinC, self.totCoins

    def paintLadder(self):
        for x in self.ladderC:
            # print x, self.__donkeyPos, self.__playerPos
            if self.__donkeyPos == x or self.__playerPos == x or x in self.__fireC:
                pass
            else:
                self.__levelBp[x[0]][x[1]] = "H"

    def coinPaint(self, cVisited):
        for i, x in enumerate(self.coinC):
            if self.__donkeyPos == x or self.__playerPos == x or cVisited[i] == 1:
                pass
            else:
                self.__levelBp[x[0]][x[1]] = "C"

    def donkeyPaint(self):
        self.__levelBp[self.__donkeyPos[0]][self.__donkeyPos[1]] = "D"    

    def coinsGen(self):
        coinCount = 0
        self.totCoins = random.randrange(25, 30)
        while coinCount != self.totCoins:

            x = random.randrange(2, 25)
            y = random.randrange(2, 78)
            if self.__levelBp[x][y] == " " and self.__levelBp[x+1][y] == "X":
                    self.__levelBp[x][y] = "C"
                    coinCount += 1


    def updateDonkey(self, lis, LorR):
        self.__donkeyPos = lis
        if LorR == 0:
            self.__levelBp[lis[0]][lis[1]+1] = ' '
        elif LorR == 1:
            self.__levelBp[lis[0]][lis[1]-1] = ' '
        self.__levelBp[lis[0]][lis[1]] = 'D'

    def updatePlayer(self, lis=[24, 2]):
        self.__levelBp[self.__playerPos[0]][self.__playerPos[1]] = " "
        self.__playerPos = lis
        self.__levelBp[self.__playerPos[0]][self.__playerPos[1]] = "P"

    def updateFBall(self, posF, flag):
        #print posF, flag
        if flag == 0:
            self.__levelBp[posF[0]][posF[1] + 1] = " "
        elif flag == 1:
            self.__levelBp[posF[0]][posF[1] - 1] = " "
        elif flag == 2:
            self.__levelBp[posF[0] - 1][posF[1]] = " "
        elif flag == 3:
            self.__levelBp[self.__playSpawnPoint[0]][self.__playSpawnPoint[1]] = " "
        self.__levelBp[posF[0]][posF[1]] = "O"
        self.__levelBp[self.__grave[0]][self.__grave[1]] = "X"

    def levelLoad(self, score=0, lives=0, level=1):
        self.score = score
        self.lives = lives
        print "\t\t\t\tLevel %d" % level
        if level == 2: 
            print "\t\t\t\tFIRESTREAM"
        for line in self.__levelBp:
            strline = ''.join(line)
            print strline
        print "You score is %d" % (self.score)
        print "Lives left : %d" % (self.lives)
