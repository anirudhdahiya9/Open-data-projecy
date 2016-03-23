import pygame
import random


def getdestruction(x,y):
	global a,b
	a=x
	b=y
class Fireball(pygame.sprite.Sprite):
	""" Player will die"""
	def __init__(self, x, y, size):

    # Calling sprite's constructor
	    pygame.sprite.Sprite.__init__(self)

	    self.fireball=pygame.image.load('../images/fireball.png').convert_alpha()
	    self.fireball=pygame.transform.scale(self.fireball,(size,size))

	    self.image=self.fireball

	    self.rect = self.image.get_rect()
	    self.rect.y = y
	    self.rect.x = x
	    self.wallList=None
	    self.topladderList=None
	    self.deltaX=4
	    self.deltaY=4
	    x=random.randint(0,1)
	    self.moveright=x
		
	def destroy(self):

		if a-5<=self.rect.x <=a+5 and b-5<=self.rect.y<=b+5:
			self.kill()
	def update(self):		

		self.destroy()
		if self.deltaY == 0:
			self.deltaY = 1
		else:
			self.deltaY += 0.2
			xx=random.randint(0,1)
 			if xx==0:
 				self.deltaX=-self.deltaX
		self.rect.x+=self.deltaX
		if self.wallList != None:
			WallCollsionlist= pygame.sprite.spritecollide(self, self.wallList, False)
			
			#print WallHitlist
			for wall in WallCollsionlist:

				if self.deltaX > 0:
					self.rect.right = wall.rect.left
				elif self.deltaX < 0:
					self.rect.left = wall.rect.right

				self.deltaX=-self.deltaX
  #       Move up/down
 	
		self.rect.y+=1
 
  #       Checking vertical hits

  		if self.topladderList!=None:
  			ladders=pygame.sprite.spritecollide(self, self.topladderList, False)
  			yy=random.randint(0,1)
			for ladder in ladders:
	 			if self.deltaY > 0:
	 				if yy==0:
	 					self.rect.y+=2
	 				else:
	 					pass		  				
  		
  		self.rect.y+=self.deltaY
  		if self.wallList != None:
			WallCollisionlist= pygame.sprite.spritecollide(self, self.wallList, False)

			for wall in WallCollisionlist:
		 		if self.deltaY > 0:
		 			self.rect.bottom = wall.rect.top
 				self.deltaY = 0	

 									
