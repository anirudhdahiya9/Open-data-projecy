import pygame
from pygame.locals import *
import random

class Fireball(pygame.sprite.Sprite) :
	def __init__(self,gor,fire_list) :
		pygame.sprite.Sprite.__init__(self)
		self.image=pygame.image.load('fireball.gif')
		self.rect=self.image.get_rect()
		self.rect.x = gor.rect.x
		self.rect.y = gor.rect.y 
		self.dirt = 1
		self.state = 0
		self.h = 0
		fire_list.add(self)
	def move(self,pl_list,list_obj,fire_list) :
		if self.dirt == 1 :
			self.rect.x += 10
			if self.rect.x >= 750 :
				self.dirt = 2
		elif self.dirt == 2 :
			self.rect.x -= 10
			if self.rect.x <= 10 :
				self.dirt = 1
				if self.rect.y == 584 :
					fire_list.remove(self)
		#print self.rect.x
		h=1000
		for line in list_obj :
		 	if self.rect.x >= line.rect.x and self.rect.x <= line.rect.x + line.rect.width :
				if self.rect.y + 16 <= line.rect.y and line.rect.y - 16 <= h:
		 			h = line.rect.y - 16
		self.rect.y = h 
			
		                

