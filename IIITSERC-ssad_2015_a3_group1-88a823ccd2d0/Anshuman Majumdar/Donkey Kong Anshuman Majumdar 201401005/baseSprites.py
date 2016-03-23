import pygame
from helpers import *

#basic sprite class from which other objects are inherited from
class Sprite(pygame.sprite.Sprite):

    def __init__(self, center, image):
        pygame.sprite.Sprite.__init__(self)
        
        self.image = image
        self.rect = image.get_rect()
        self.rect.center = center

    #since it is inherited from pygame.sprite.Sprite, it already has an update function

