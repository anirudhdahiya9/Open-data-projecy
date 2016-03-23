import pygame
from pygame.locals import *

class Gorilla(pygame.sprite.Sprite):
	def __init__(self):
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.image.load('gorilla.gif')
		self.rect = self.image.get_rect()
		self.rect.x = 20
		self.rect.y = 57
		self.dirt = 1
	def move(self,x1,x2) :
		if self.dirt == 1 :
			self.rect.x += 10
			if self.rect.x == x1 :
				self.dirt = 2
		elif self.dirt == 2 :
			self.rect.x -= 10
			if self.rect.x == x2 :
				self.dirt = 1
	

