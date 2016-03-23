import pygame
from colors import *
"""class for ladders """
class Platform(pygame.sprite.Sprite ) :
     def __init__(self , width , height , x, y, platform_type,image_name):
        self.width = width
        self.height = height
        pygame.sprite.Sprite.__init__(self)
        if platform_type == "line" :
            self.image = pygame.Surface([width,height])
            self.image.fill(white)
            self.rect = self.image.get_rect()
            self.rect.x = x
            self.rect.y = y
        elif platform_type == "platform_picture" :
            self.image = pygame.image.load(image_name)
            self.image = pygame.transform.scale(self.image,[width,height])
            self.rect = self.image.get_rect()
            self.rect.x = x 
            self.rect.y = y

