import pygame
from pygame.locals import *
import random

class Redheart(pygame.sprite.Sprite):
	def __init__(self,ix,iy):
		pygame.sprite.Sprite.__init__(self)
		self.image=pygame.image.load('redheart.gif')
		self.rect=self.image.get_rect()
		self.rect.x = ix
		self.rect.y = iy
class Whiteheart(pygame.sprite.Sprite):
	def __init__(self,ix,iy):
		pygame.sprite.Sprite.__init__(self)
		self.image=pygame.image.load('whiteheart.gif')
		self.rect=self.image.get_rect()
		self.rect.x = ix
		self.rect.y = iy

def life(nlife,heart):
	if nlife == 3 :
		hrt=Redheart(660,50)
		heart.add(hrt)
		hrt=Redheart(690,50)
		heart.add(hrt)
		hrt=Redheart(720,50)
		heart.add(hrt)
	elif nlife == 2:
		hrt=Redheart(660,50)
		heart.add(hrt)
		hrt=Redheart(690,50)
		heart.add(hrt)
		hrt=Whiteheart(720,50)
		heart.add(hrt)
	elif nlife == 1:
		hrt=Redheart(660,50)
		heart.add(hrt)
		hrt=Whiteheart(690,50)
		heart.add(hrt)
		hrt=Whiteheart(720,50)
		heart.add(hrt)
		
