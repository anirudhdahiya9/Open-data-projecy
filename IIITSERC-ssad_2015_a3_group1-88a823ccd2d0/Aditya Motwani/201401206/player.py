import pygame
from pygame.locals import *

class Player(pygame.sprite.Sprite) :
	def __init__(self):
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.image.load('mario.jpg')
		self.rect = self.image.get_rect()
		self.rect.x = 210
		self.rect.y = 500
	def move(self) :
		keys=pygame.key.get_pressed()
		#if keys[Ke_DOWN] or keys[K_s] :
		#	se)f.rect.y += 10
		if keys[K_UP] or keys[K_w] :
			self.rect.y -= 10
		elif keys[K_LEFT] or keys[K_a] :
			self.rect.x -= 10
		elif keys[K_RIGHT] or keys[K_d] : 
			self.rect.x += 10
	def checkmove(self,list_obj) :
		h=1000
		for line in list_obj :
			if self.rect.x >= line.rect.x and self.rect.x <= line.rect.x + line.rect.width and line.rect.y - 50 >= self.rect.y and line.rect.y - 50 <= h :
				h = line.rect.y - 50
		if self.rect.x < 10 :
			self.rect.x=10
		elif self.rect.x > 750 :
			self.rect.x =750
		return h
