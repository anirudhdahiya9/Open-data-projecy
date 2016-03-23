import pygame
import random
import baseSprites

#basic fireball class to characterize fireballs
class Fireballs(baseSprites.Sprite):

    def __init__(self, center, image):
        baseSprites.Sprite.__init__(self, center, image)
        
        #default speed of the fireballs
        self._vspeed = 0
        self._hspeed = 5

        self.image = image
        self.direction = random.randint(0,1)
        self.moves = random.randint(100, 200)
        self.moveCount = 0

    #update method to determine the position and the movement of the fireballs
    def update(self, block):
        self.gravity()

        self.rect.x += self._hspeed
        collision = pygame.sprite.spritecollide(self, block, False)
        for collided in collision:
            if self._hspeed > 0:
                self.rect.right = collided.rect.left
                self._hspeed = -self._hspeed
                self.rect.x += self._hspeed
            elif self._hspeed < 0:
                self.rect.left = collided.rect.right
                temp = self._hspeed
                self._hspeed = -self._hspeed
                self.rect.x += self._hspeed

        self.rect.y += self._vspeed
        collision = pygame.sprite.spritecollide(self, block, False)
        for collided in collision:
            if self._vspeed > 0:
                self.rect.bottom = collided.rect.top
                self._vspeed = 0
            elif self._vspeed < 0:
                self.rect.top = collided.rect.bottom
                self._vspeed = 0

    #basic method to implement gravity
    def gravity(self, gravity=0.35):
        if self._vspeed == 0:
            self._vspeed = 1 
        else:
            self._vspeed += gravity


