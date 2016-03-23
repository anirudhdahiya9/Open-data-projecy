import sys
import os
import tty
import pygame
import time
from Level import Level
from Donkey import Donkey
from Player import Player
from Body import Body
from Fireball import Fireball


class DKMain:

    """Main class of the game."""

    def __init__(self):
        pass        

    def reload(self, score=0, level=1):
        self.__level = level
        self.__Lev = Level()
        self.__Lev.findLadderCoordinates()
        self.__Lev.coinsGen()
        self.__Lev.findCoinCoordinates()
        self.__Lev.paintLadder()
        self.__Lev.levelLoad(self.__level)
        self.__win = False
        self.__Kong = Donkey(self.__Lev)
        self.__play = Player(self.__Lev, score)
        self.__firas = [Fireball(self.__Lev) for i in range(1000)]
        for fira in self.__firas:
            fira.getLevelProperties()

        self.__Kong.getLevelProperties()
        self.__play.getLevelProperties()
        self.__Kong.getDonkeyPosition()
        self.__play.getPlayerPosition()


    def gameLoop(self):
        """This is  the main game loop."""
        self.reload()
        self.steps = 0
        self.firaNo = 0
        pygame.mixer.init()
        pygame.mixer.music.load("music/route2.mp3")
        pygame.mixer.music.play()
        while True:
            self.__play.getLevelProperties()
            if self.__play.retLives() <= 0:
                break
            tty.setcbreak(sys.stdin)
            key = ord(sys.stdin.read(1))
            if key == 113 or key == 81:
                break
            if key == 32 and not self.__play.inAir():
                self.gameJumpLoop()
            else:
                self.updateEverything(key)
            self.__win = self.__play.victory()
            if self.__win:
                os.system("clear")
                self.reload(self.__play.retScore(), 2)
            if pygame.mixer.music.get_busy() != True:
                pygame.mixer.music.play()
        print "GAME OVER"

    def updateEverything(self, key):
        """Responsible for updating all instance variables.

        This includes things like positions of the Player,
        Donkey, fireballs etc. Also, responsible for information
        transfer between class objects."""

        if self.steps % 30 == 0 and self.firaNo < 1000:
            l, m = self.__firas[self.firaNo].spawn()
            self.__Lev.updateFBall(l, m)
            self.firaNo += 1
        self.__Kong.getLevelProperties()
        self.__play.getLevelProperties()
        for fira in self.__firas:
            fira.getLevelProperties()

        move = self.__play.motionController(key)
        self.__Lev.updatePlayer(move)
        self.firaList = []
        for i in range(self.firaNo):
            self.__firas[i].destroy()
            self.k, self.j = self.__firas[i].motionFire()
            self.__Lev.updateFBall(self.k, self.j)
            self.firaList.append(self.__firas[i].retFPos())
        self.__Lev.getFireCoordinates(self.firaList)
        if self.__play.fireDeath():
            self.__Lev.updatePlayer()
        pos = self.__Kong.randMove()
        # print move
        os.system('clear')
        #print self.__firas[0].pSpawnPoint, self.__firas[0].retFPos()
        # print self.__play.playerPs, self.__play.fireCoordinates
        self.firaList = []
        for i in range(self.firaNo):
            self.firaList.append(self.__firas[i].retFPos())
        self.__play.fireCoordinatesUpdate(self.firaList)
        # print self.__play.playerPos, self.__play.fireCoordinates
        if self.__play.fireDeath():
            self.__Lev.updatePlayer()
        self.firaList = []
        for i in range(self.firaNo):
            self.firaList.append(self.__firas[i].retFPos())
        self.__play.fireCoordinatesUpdate(self.firaList)
        if pos[1] != -1:
            self.__Lev.updateDonkey(pos[0], pos[1])
        self.__Lev.paintLadder()
        self.__Lev.coinPaint(self.__play.collectCoin())
        self.__Lev.levelLoad(self.__play.retScore(), self.__play.retLives(), self.__level)
        self.steps += 1

    def gameJumpLoop(self):
        """Handles the jump.

        Basically, one step is moved up and gravity is disabled
        for 3 more keypresses."""

        self.__play.setjFlag()
        self.updateEverything(87)
        for i in range(3):
            tty.setcbreak(sys.stdin)
            key = ord(sys.stdin.read(1))
            if key == 32:
                key = 87
            self.updateEverything(key)
        self.__play.unsetjFlag()


if __name__ == "__main__":
    Kong = DKMain()
    Kong.gameLoop()
