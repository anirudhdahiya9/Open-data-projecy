import pygame
from colors import *
""" Class for the coins """

class Coin(pygame.sprite.Sprite) :
    def __init__(self,xpoint,ypoint) :
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("coin.png")
        self.image = pygame.transform.scale(self.image,[30,30])
        self.rect = self.image.get_rect()
        self.rect.x = xpoint
        self.rect.y = ypoint

