import pygame
import settings
import random

settings.init()
class Block(pygame.sprite.Sprite):
	    def __init__(self,source,posx,posy):
		super(Block,self).__init__()
		self.image=pygame.image.load(source).convert()
		self.rect=self.image.get_rect()
		self.rect.x=posx
		self.rect.y=posy
	    def l(self,x,y):
		settings.gamedisplay.blit(settings.ladderimg,(x,y))
	    

class Coin(pygame.sprite.Sprite):
    def __init__(self,source,posx,posy):
	super(Coin,self).__init__()
	self.image=pygame.image.load(source).convert()
	self.rect=self.image.get_rect()
	self.rect.x=posx
	self.rect.y=posy  

    def lc(self,x,y):
	settings.gamedisplay.blit(settings.coinimg,(x,y)) 

class Fireball(Coin):
	    def start(self,speed,f1,f3):
	    	self.speedx=speed
	    	self.flag=f1	
	    	self.flag3=f3
	    def movement(self):
		if (((self.rect.x>settings.Allowed[0]+15 and self.rect.x<settings.Allowed[0]+50 and self.rect.y>settings.Allowed[1]-50-50 and self.rect.y<settings.Allowed[1]+85) or (self.rect.x>settings.Allowed[2]+15 and self.rect.x<settings.Allowed[2]+50 and self.rect.y>settings.Allowed[3]-50-50 and self.rect.y<settings.Allowed[3]+85) or (self.rect.x>settings.Allowed[4]-15 and self.rect.x<settings.Allowed[4]+10 and self.rect.y>settings.Allowed[5]-50-50 and self.rect.y<settings.Allowed[5]+85) or (self.rect.x>settings.Allowed[6]-15 and self.rect.x<settings.Allowed[6]+10 and self.rect.y>settings.Allowed[7]-50-50 and self.rect.y<settings.Allowed[7]+85))):
			ch=random.randrange(0,2)
			if (ch==1 or self.flag==1) and self.flag!=2:			
		    		self.rect.y+=1
		    		self.rect.x+=0
		    		self.flag=1
			else:
				self.rect.x+=self.speedx
				self.flag=0
		elif ((self.rect.y>=59+80-90 and self.rect.y<=59+80-70 and self.rect.x>3*296) or (self.rect.y>=settings.dheight*0.4-90 and self.rect.y<=settings.dheight*0.4-70 and self.rect.x>2*296 and self.rect.x<3*296-195) or (self.rect.y>=settings.dheight*0.6-90 and self.rect.y<=settings.dheight*0.6-70 and ((self.rect.x>296 and self.rect.x<2*296-230) or (self.rect.x>3*296+40 and self.rect.x<settings.dwidth)))):
			choose=random.randrange(0,2)
			if choose==0 or self.flag3==1:
				self.rect.y+=3
				self.rect.x+=0
				self.flag3=1
			else:
				self.flag3=0				
				self.rect.x+=self.speedx
		else:
		    if self.flag==0:
			self.rect.x+=self.speedx
		    else:
			choice=random.randrange(0,2)
			if choice==0:
			    self.rect.x+=self.speedx
			elif choice==1:
			    self.speedx=-self.speedx
			    self.rect.x+=self.speedx
		    self.flag=0
		    self.flag3=0

	    def fire(self,i,j):
		settings.gamedisplay.blit(settings.fireimg,(i,j))

class Board:
    def __init__(self,h,w):
	self.h=h
	self.w=w
    def brick(self,a,b):
	settings.gamedisplay.blit(settings.brickimg,(a,b))
