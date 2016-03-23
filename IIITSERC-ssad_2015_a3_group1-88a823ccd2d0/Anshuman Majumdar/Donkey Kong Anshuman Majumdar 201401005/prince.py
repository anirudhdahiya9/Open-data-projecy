import math
import pygame
import baseSprites
from helpers import *

#prince class describing the methods of the prince
class Prince(baseSprites.Sprite):

    def __init__(self, center, image):
        baseSprites.Sprite.__init__(self, center, image)

        self.coins = 0

        self.originx = self.rect.centerx
        self.originy = self.rect.centery

        self.hspeed = 0
        self.vspeed = 0

    #method to move the prince when pressed keyboard buttons
    def moveKeyDown(self, key, stair):
        if key == K_RIGHT:
            self.changeSpeed(5,0)
        elif key == K_LEFT:
            self.changeSpeed(-5,0)
        elif key == K_UP:
            if pygame.sprite.spritecollide(self, stair, False):
                self.changeSpeed(0,-5)
        elif key == K_DOWN:
            self.changeSpeed(0,5)
        elif key == K_SPACE:
            self.changeSpeed(0,-5)

    #method to stop moving the player when released keyboard buttons
    def moveKeyUp(self, key):
        if key == K_RIGHT:
            if self.hspeed != 0:
                self.hspeed = 0
        elif key == K_LEFT:
            if self.hspeed != 0:
                self.hspeed = 0
        elif key == K_UP:
            if self.vspeed != 0:
                self.vspeed = 0
        elif key == K_DOWN:
            if self.vspeed != 0:
                self.vspeed = 0
        elif key == K_SPACE:
            if self.vspeed != 0:
                self.vspeed = 0
    
    #this method is used as a Check Wall Function
    def update(self, block, stair):

        climbing = pygame.sprite.spritecollide(self, stair, False)
        if climbing:
            self.rect.y += self.vspeed
        else:
            self.gravity()

        self.rect.x += self.hspeed
        collision = self.checkCollision(self, block)
        for collided in collision:
            if self.hspeed > 0:
                self.rect.right = collided.rect.left
                self.hspeed = 0
            elif self.hspeed < 0:
                self.rect.left = collided.rect.right
                self.hspeed = 0

        self.rect.y += self.vspeed
        collision = self.checkCollision(self, block)
        for collided in collision:
            if self.vspeed > 0:
                self.rect.bottom = collided.rect.top
                self.vspeed = 0
            elif self.vspeed < 0:
                self.rect.top = collided.rect.bottom
                self.vspeed = 0
    
    #method to change the speed of the player
    def changeSpeed(self, hspeed, vspeed):
        self.hspeed += hspeed
        self.vspeed += vspeed

    #method to get the position of the player
    def getPosition(self):
        xcoor = self.rect.x
        ycoor = self.rect.y
        return [xccor,ycoor]

    #method to check the collision of the player with other objects
    def checkCollision(self, prince, block):
        collisions = pygame.sprite.spritecollide(prince, block, False)
        return collisions

    #method to check the collision of the player with the walls
    def checkWall(self, prince, block):
        collisions = pygame.sprite.spritecollide(prince, block, False)
        return collisions

    #main gravity defining method
    def gravity(self, gravity=0.35):
        if self.vspeed == 0:
            self.vspeed = 1
        else:
            self.vspeed += gravity


