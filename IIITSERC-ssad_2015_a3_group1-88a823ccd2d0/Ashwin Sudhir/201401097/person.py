import pygame
import random
pygame.init()

#colors
black = (0,0,0)
white= (255,255,255)
red = (255,0,0)

class person(pygame.sprite.Sprite):

	def __init__(self,x,y,width,height,name):
		
		self.change_x=0
		self.change_y=0
		pygame.sprite.Sprite.__init__(self)
		self.image=pygame.image.load(name).convert()
		self.image=pygame.transform.scale(self.image,[width,height])
		self.rect=self.image.get_rect()
		self.rect.x=x
		self.rect.y=y

	def movlr(self,x,y,fx,fy):

		if fx==1:
			self.change_x=x
		if fy==1:
			self.change_y=y

	def checkCollision(self, collidion, grav):
		
		if grav == 0:
			self.gravity()
		
			
		#moving left/right

		self.rect.x+=self.change_x

		collide_hit_list=pygame.sprite.spritecollide(self,collidion,False)
		
		
		for wall in collide_hit_list:
			if self.change_x>0:
				self.rect.right=wall.rect.left
			else:
				self.rect.left=wall.rect.right

		#moving up/down
		self.rect.y+=self.change_y

		collide_hit_list=pygame.sprite.spritecollide(self,collidion,False)
		#print wall_hit_list
		for wall in collide_hit_list:
			if self.change_y>0:
				self.rect.bottom=wall.rect.top
				self.change_y=0
			else:
				self.rect.top=wall.rect.bottom
				self.change_y=0

	def gravity(self):

		# effet of gravity
		if self.change_y==0:
			self.change_y+=1
		else:
			self.change_y+=.36





class players(person):
	
	


	def jump(self,collidion):

		self.rect.y+=1
		platform_hit_list=pygame.sprite.spritecollide(self,collidion,False)
		self.rect.y-=1


		if len(platform_hit_list) > 0 :
			self.change_y=-7
			return 1
		return 0

	def collectCoin(self,coins):


		
		self.hit_list=pygame.sprite.spritecollide(self,coins,True)

		if len(self.hit_list) >0:
			return 5
		else:
			return 0


		


class donkey(person):

	def __init__(self,x,y,width,height,name):
		person.__init__(self,x,y,width,height,name)
		self.rand=random.randrange(2)
		self.rcount=0
		self.lcount=0
		self.hit_count=0
		
		

	def rand_move(self,walls):

		
		self.rect.x-=3
		self.hit_count=pygame.sprite.spritecollide(self,walls,False)
		self.rect.x+=3

		
		if len(self.hit_count) >0 or self.rect.x >700:

			self.rand=(self.rand+1)%2
			self.rcount=0
			self.lcount=0

		
		if self.rcount <= 100 and self.rand==1:
			self.movlr(2,0,1,0)
			self.rcount+=1

		elif self.lcount <= 100 and self.rand==0:
			self.movlr(-2,0,1,0)
			self.lcount+=1


		if self.lcount >=100 :
			self.movlr(0,0,1,0)
			self.lcount=0
			self.rand=random.randrange(2)

		if self.rcount >=100 :
			self.movlr(0,0,1,0)
			self.rcount=0
			self.rand=random.randrange(2)

	def checkplayer(self,player):

		self.hit_count=pygame.sprite.spritecollide(self,player,False)

		if len(self.hit_count) >0:
			return 1
		else:
			return 0