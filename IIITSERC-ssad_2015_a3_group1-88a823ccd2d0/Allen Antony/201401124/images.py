import pygame
from colors import *
pygame.init()
"""class for images """
class Images(pygame.sprite.Sprite):
    def __init__(self, image_file, location,height,width):
        pygame.sprite.Sprite.__init__(self)  #call Sprite initializer
        self.image = pygame.image.load(image_file)
        self.image = pygame.transform.scale(self.image,[width,height])
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = location

"""class for the door """
class Door(pygame.sprite.Sprite) :
    def __init__(self) :
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("door.png")
        self.image = pygame.transform.scale(self.image,[50,50])
        self.rect = self.image.get_rect()
        self.rect.left = 450
        self.rect.bottom = 785
    
    def remove_fireballs(self,all_fireball_list) :
        hit_list = pygame.sprite.spritecollide(self,all_fireball_list,True)

