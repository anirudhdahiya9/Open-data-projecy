import pygame
from pygame.locals import *
import random

class Coins(pygame.sprite.Sprite) :
	def __init__(self) :
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.image.load('coin.gif')
		self.rect = self.image.get_rect()
	
	def cd (self,flag):
		lst = [80+i*100 for i in range(6)]
		self.rect.y = random.choice(lst)
		if flag == 1 :
			self.rect.x = random.randrange(10,580)
			self.rect.y = random.choice([80,280,480,580])
		elif flag == 2 :
			self.rect.x = random.randrange(260,750)
			self.rect.y = random.choice([180,380]) 

