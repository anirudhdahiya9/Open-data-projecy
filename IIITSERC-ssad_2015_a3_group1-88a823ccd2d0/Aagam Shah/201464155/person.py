import pygame
import settings
import objects
settings.init()
class Person(pygame.sprite.Sprite):
	    def __init__(self,height,width,s,posx,posy):
		super(Person,self).__init__()
		self.height=height
		self.width=width
		self.image=pygame.image.load(s).convert()
		self.rect=self.image.get_rect()
		self.rect.x=posx
		self.rect.y=posy
	    

class Player(Person):        
    def hero(self,x,y):
	settings.gamedisplay.blit(settings.heroimg,(x,y))
    def imgchange(self,sourc):
	
	settings.heroimg=pygame.image.load(sourc)

    def jump(self,x,y):
	self.rect.x=x
	self.rect.y=y
	b=5
	while b!=0:
	     self.rect.y+=5
	     draw.blitndraw()
	     b-=1
	while self.rect.y!=y:
	     self.rect.y-=5
	     draw.blitndraw()
    def falling(self):
	
	self.rect.y+=3
	if ((self.rect.y>=objects.D.height+80-73 and self.rect.y<=objects.D.height+80-70) or (self.rect.y>=settings.dheight*0.4-73 and 		self.rect.y<=settings.dheight*0.4-70) or (self.rect.y>=settings.dheight*0.6-73 and self.rect.y<=settings.dheight*0.6-70) or (self.rect.y>=settings.dheight*0.8-73 and self.rect.y<=settings.dheight*0.8-70) or (self.rect.y>=settings.dheight-73 and self.rect.y<=settings.dheight-70)):
		settings.fall=0
		settings.jump=0

class Donkey(Person):
    def villain(self,i,j):
	settings.gamedisplay.blit(settings.villainimg,(i,j))

    def move(self):

	if self.rect.x<=600 and settings.flag2==0 and settings.win!=1:	
		self.rect.x+=1
	else:
		if settings.win!=1:		
			settings.flag2=1
			self.rect.x-=1
			if self.rect.x<=20:
				settings.flag2=0
    def imgchange(self,sourc):
	
	settings.villainimg=pygame.image.load(sourc)
