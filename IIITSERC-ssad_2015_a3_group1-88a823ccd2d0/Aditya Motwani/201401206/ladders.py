import pygame
from pygame.locals import *

class Ladders(pygame.sprite.Sprite) :
	def __init__(self,ix,iy) :
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.image.load('Ladders.png')
		self.rect = self.image.get_rect()
		self.rect.x = ix
		self.rect.y = iy
	def move(self,mario) :
		 keys=pygame.key.get_pressed()
		 if keys[K_DOWN] or keys[K_s] :
		 	if mario.rect.y + 50 < self.rect.y + self.rect.height  :
		        	mario.rect.y += 10
		 if keys[K_UP] or keys[K_w] :
		        mario.rect.y -= 10
		 elif keys[K_LEFT] or keys[K_a] :
		        mario.rect.x -= 10
		 elif keys[K_RIGHT] or keys[K_d] :
		        mario.rect.x +=10

