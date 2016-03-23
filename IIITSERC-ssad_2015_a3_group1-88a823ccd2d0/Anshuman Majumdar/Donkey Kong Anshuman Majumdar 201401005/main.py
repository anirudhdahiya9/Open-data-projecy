import time
import pygame
import level1
import level2
import level3
import os, sys
import fireball
import baseSprites
import pygame.mixer
from pygame.locals import *
from helpers import *
from prince import *


if not pygame.font: print 'Fonts Disabled'
if not pygame.font: print 'Sound Disabled'

BLOCK_SIZE = 24
FIREBALLEVENT = pygame.USEREVENT + 3
RED = (204, 0, 0)
BLUE = (0, 128, 255)
GREEN = (153, 255, 51)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
VIOLET = (51, 0, 102)
YELLOW = (153, 51, 255)

class Main:
    
    def __init__(self, score, level, lives, width=640, height=480):
        pygame.init()
        self.lives = lives
        self.level = level
        self.score = score
        self.width = width
        self.height = height
        self.screen = pygame.display.set_mode((self.width, self.height))

    #main controlling method of the game
    def mainLoop(self, score=0, level=1, lives=3):
        self.loadSprites(level)
        
        #setting up the pygame display
        pygame.display.set_caption('$$$ DoNKeY KonG $$$')
        self.background = pygame.Surface(self.screen.get_size())
        self.background = self.background.convert()
        self.background.fill(BLACK)
        
        #drawing the objects initially on the screen
        self.blockSprites.draw(self.background)
        self.stairSprites.draw(self.background)
        self.queenSprites.draw(self.background)
        self.donkeySprites.draw(self.background)
        self.exitSprites.draw(self.background)
        
        #sound = pygame.mixer.Sound('data/audio/buzzin.wav')
        #sound.play()
        #timer to decide the frame rate
        pygame.time.set_timer(FIREBALLEVENT, 3000)
        clock = pygame.time.Clock()
        fps = 60 
        
        #variables to determine the game state
        GAMEQUIT = False
        GAMEOVER = False
        GAMEWON = False
        
        #main while loop of the game
        while not GAMEQUIT:

            #after collision with fire and no lives left
            while GAMEOVER == True:
                self.background = pygame.Surface(self.screen.get_size())
                self.background = self.background.convert()
                self.screen.fill(VIOLET)
                gameover = "Game Over"
                scoremsg = "Final Score : %d" %(score)
                livesmsg = "Lives Remaining : %d" %(lives)
                optionsmsg1 = "Q - Quit"
                optionsmsg2 = "R - Replay"
                messageDisplay(self.screen, 512, 270, gameover, RED, 45)
                messageDisplay(self.screen, 512, 330, scoremsg, GREEN, 24)
                messageDisplay(self.screen, 512, 350, livesmsg, GREEN, 24)
                messageDisplay(self.screen, 512, 430, optionsmsg1, BLUE, 24)
                messageDisplay(self.screen, 512, 450, optionsmsg2, BLUE, 24)
                
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        sys.exit()
                    elif event.type == KEYDOWN:
                        if event.key == K_q:
                            GAMEQUIT = True
                            GAMEOVER = False
                            sys.exit()
                        elif event.key == K_r:
                            self.mainLoop()
                pygame.display.update()
            
            #final screen after winning the game
            while GAMEWON == True:
                self.background = pygame.Surface(self.screen.get_size())
                self.background = self.background.convert()
                self.screen.fill(VIOLET)
                gamewon = "Hooray! You rescued the Queen"
                scoremsg = "Final Score : %d" %(score+self.score)
                livesmsg = "Lives Remaining : %d" %(lives)
                optionsmsg1 = "Q - Quit"
                optionsmsg2 = "R - Replay"
                messageDisplay(self.screen, 512, 270, gamewon, RED, 45)
                messageDisplay(self.screen, 512, 400, scoremsg, GREEN, 24)
                messageDisplay(self.screen, 512, 430, livesmsg, GREEN, 24)
                messageDisplay(self.screen, 512, 500, optionsmsg1, BLUE, 24)
                messageDisplay(self.screen, 512, 520, optionsmsg2, BLUE, 24)

                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        sys.exit()
                    elif event.type == KEYDOWN:
                        if event.key == K_q:
                            GAMEQUIT = True
                            GAMEWON = False
                            sys.exit()
                        elif event.key == K_r:
                            self.mainLoop()
                pygame.display.update()
            
            self.princeSprites.clear(self.screen, self.background)
            self.fireSprites.clear(self.screen, self.background)
            
            #keyboard event handling
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

                elif event.type == FIREBALLEVENT:
                    self.loadFire(level) 

                elif event.type == KEYDOWN:
                    if event.key == K_q:
                        sys.exit()
                    elif (event.key == K_RIGHT) or (event.key == K_LEFT) or (event.key == K_UP) or (event.key == K_DOWN) or (event.key == K_SPACE):
                        self.prince.moveKeyDown(event.key, self.stairSprites)

                elif event.type == KEYUP:
                        self.prince.moveKeyUp(event.key)
            
            
            #updating the sprites after movement
            self.princeSprites.update(self.blockSprites, self.stairSprites)
            for fire in self.fireSprites.sprites():
                fire.update(self.blockSprites)
            collisions = pygame.sprite.groupcollide(self.exitSprites, self.fireSprites, False, True) 
            
            #determining collisions with other sprites
            self.collectCoin(self.prince, self.coinSprites)
            if pygame.sprite.spritecollide(self.prince, self.fireSprites, False):
                score += self.score
                #sound.stop()
                time.sleep(2)
                if lives == 0:
                    GAMEOVER = True
                else:
                    self.mainLoop(score-25, level, lives-1)
            if pygame.sprite.spritecollide(self.prince, self.queenSprites, False):
                level += 1
                score += self.score
                #sound.stop()
                time.sleep(2)
                if level == 4:
                    GAMEWON = True
                else:
                    self.mainLoop(score, level, lives)

            #refreshing the background and setting up the fonts
            self.screen.blit(self.background, (0, 0))
            if pygame.font:
                scorelivesmsg = "||   SCORE : %d   ||   LIVES : %d   ||" %(score+self.score, lives)
                if level == 1:
                    levelmsg = 'LEVEL I - "Everyone can do this"'
                elif level == 2:
                    levelmsg = 'LEVEL II - "Keep on going"'
                elif level == 3:
                    levelmsg = 'LEVEL III - "Better luck next time"'

                messageDisplay(self.screen, 512, 660, scorelivesmsg, BLUE, 36)
                messageDisplay(self.screen, 512, 65, levelmsg, GREEN, 36)
            
            #drawing the objects finally
            self.coinSprites.draw(self.screen)
            self.princeSprites.draw(self.screen)
            self.fireSprites.draw(self.screen)
        
            #updating the display
            clock.tick(fps)
            pygame.display.flip()

    #method to load all the sprites into objects from other modules
    def loadSprites(self, level):
        xOffset = (BLOCK_SIZE/2)
        yOffset = (BLOCK_SIZE/2)

        #determining the level to load the sprites from
        if level == 1: 
            currentLevel = level1.Level()
        elif level == 2: 
            currentLevel = level2.Level()
        elif level == 3: 
            currentLevel = level3.Level()
        currentLayout = currentLevel.getLayout()
        currentImages = currentLevel.getSprites()

        #creating sprite groups to store the objects
        self.coinSprites = pygame.sprite.Group()
        self.blockSprites = pygame.sprite.Group()
        self.stairSprites = pygame.sprite.Group()
        self.queenSprites = pygame.sprite.Group()
        self.donkeySprites = pygame.sprite.Group()
        self.fireSprites = pygame.sprite.Group()
        self.exitSprites = pygame.sprite.Group()

        #fetching the symbols corresponding to the symbols from level files
        for y in xrange(len(currentLayout)):
            for x in xrange(len(currentLayout[y])):
                center = [(x*BLOCK_SIZE)+xOffset, (y*BLOCK_SIZE)+yOffset]

                if currentLayout[y][x] == currentLevel._BLOCK:
                    block = baseSprites.Sprite(center, currentImages[currentLevel._BLOCK])
                    self.blockSprites.add(block)
                elif currentLayout[y][x] == currentLevel._PRINCE:
                    self.prince = Prince(center, currentImages[currentLevel._PRINCE])
                elif currentLayout[y][x] == currentLevel._COIN:
                    coin = baseSprites.Sprite(center, currentImages[currentLevel._COIN])
                    self.coinSprites.add(coin)
                elif currentLayout[y][x] == currentLevel._STAIR:
                    stair = baseSprites.Sprite(center, currentImages[currentLevel._STAIR])
                    self.stairSprites.add(stair)
                elif currentLayout[y][x] == currentLevel._QUEEN:
                    queen = baseSprites.Sprite(center, currentImages[currentLevel._QUEEN])
                    self.queenSprites.add(queen)
                elif currentLayout[y][x] == currentLevel._DONKEY:
                    donkey = baseSprites.Sprite(center, currentImages[currentLevel._DONKEY])
                    self.donkeySprites.add(donkey)
                elif currentLayout[y][x] == currentLevel._FIRE:
                    fire = fireball.Fireballs(center, currentImages[currentLevel._FIRE])
                    self.fireSprites.add(fire)
                elif currentLayout[y][x] == currentLevel._EXIT:
                    exit = baseSprites.Sprite(center, currentImages[currentLevel._EXIT])
                    self.exitSprites.add(exit)

        self.princeSprites = pygame.sprite.RenderPlain((self.prince))

    #method to load the fireballs into fireball group
    def loadFire(self, level):
        xOffset = (BLOCK_SIZE/2)
        yOffset = (BLOCK_SIZE/2)

        #determining the level to load the sprites from
        if level == 1: 
            currentLevel = level1.Level()
        elif level == 2: 
            currentLevel = level2.Level()
        elif level == 3: 
            currentLevel = level3.Level()
        currentLayout = currentLevel.getLayout()
        currentImages = currentLevel.getSprites()

        #fetching the fireball from the grid in the level files
        for y in xrange(len(currentLayout)):
            for x in xrange(len(currentLayout[y])):
                center = [(x*BLOCK_SIZE)+xOffset, (y*BLOCK_SIZE)+yOffset]
                if currentLayout[y][x] == currentLevel._FIRE:
                    fire = fireball.Fireballs(center, currentImages[currentLevel._FIRE])
                    self.fireSprites.add(fire)

    #method to collect the coins and update the score
    def collectCoin(self, prince, coins):
        collisions = pygame.sprite.spritecollide(prince, coins, True)
        self.prince.coins = self.prince.coins+5*len(collisions)
        self.score = self.prince.coins

    #method to display the score
    def display(self):
        if pygame.font:
            font = pygame.font.Font(None, 36)
            text = font.render("--->   SCORE : %d   <---" % (score+self.score), 1, (255, 0, 0))
            textpos = text.get_rect()
            textpos.centerx = 512
            textpos.centery = 600
            self.screen.blit(text, textpos)

if __name__ == "__main__":
    MainWindow = Main(0, 1, 3, 1024, 720)
    MainWindow.mainLoop(0, 1, 3)


