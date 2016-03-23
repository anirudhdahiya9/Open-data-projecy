import pygame
from gorilla import Gorilla

class Princess(Gorilla):
	def __init__(self) :
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.image.load('princess2.png')
		self.rect = self.image.get_rect()
		self.rect.x = 250
		self.rect.y = 10
		self.dirt = 1
