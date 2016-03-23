import pygame
import random
pygame.init()

#colors
black = (0,0,0)
white= (255,255,255)
red = (255,0,0)

class coins(pygame.sprite.Sprite):
	def __init__(self,x,y,width,height):
		pygame.sprite.Sprite.__init__(self)
		self.image=pygame.image.load("images/coin2.png").convert()
		self.image=pygame.transform.scale(self.image,[width,height])

		self.rect=self.image.get_rect()

		
		self.rect.x=x
		self.rect.y=y

		self.hit_list=0
		self.plat_hit=0
		self.flag=0
		self.change=1.36
		self.mult=1


	def update(self,plats):
		
		self.gravity(plats)

		
		self.plat_hit=pygame.sprite.spritecollide(self,plats,False)
		
		if len(self.plat_hit) >0: 
			self.flag=0
			self.mult=1
			self.change=1.36
		
			

		for wall in self.plat_hit:
			if self.rect.y>0:
				self.rect.bottom=wall.rect.top
			
			else:
				self.rect.top=wall.rect.bottom
				





	def gravity(self,plat_list):

		self.plat_hit=pygame.sprite.spritecollide(self,plat_list,False)
		if len(self.plat_hit) ==0 and self.flag==0:
			self.rect.y+=1
			self.flag=1
		else:
			self.change=self.change+(self.mult * 0.36)
			self.rect.y+=self.change


