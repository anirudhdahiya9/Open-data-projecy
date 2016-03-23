import pygame
from colors import *
"""class for ladders """
class Ladder(pygame.sprite.Sprite) :
    def __init__(self,xpoint,ypoint) :
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("ladder.png")
        self.image = pygame.transform.scale(self.image,[30,100])
        self.rect = self.image.get_rect()
        self.rect.x = xpoint
        self.rect.y = ypoint

