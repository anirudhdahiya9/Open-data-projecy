import pygame
import random
pygame.init()

#colors
black = (0,0,0)
white= (255,255,255)
red = (255,0,0)

class wall(pygame.sprite.Sprite):

	def __init__(self,x,y,width,height):

		pygame.sprite.Sprite.__init__(self)
		self.image=pygame.Surface([width,height])

		
		self.image.fill(black)
		
		self.rect=self.image.get_rect()
		self.rect.x=x
		self.rect.y=y