import pygame
import random
pygame.init()
#colors
black = (0,0,0)
white= (255,255,255)
red = (255,0,0)

class fireball(pygame.sprite.Sprite):
	def __init__(self,x,y,width,height):
		pygame.sprite.Sprite.__init__(self)
		self.image=pygame.image.load("images/fire.gif").convert()
		self.image=pygame.transform.scale(self.image,[width,height])

		self.rect=self.image.get_rect()

		self.hit_count=0
		
		self.rect.y=y
		self.rect.x=x+60
		self.rand=1
		self.rcount=0
		self.lcount=0

		self.plat_hit=0
		self.flag=0
		self.mult=1
		self.change=1.36

		self.ladder_hit_list=0


		self.grav=0
		self.count=0



	

	def move(self,walls,plats):

		self.mult+=1
		self.count+=1
		
		self.hit_count=pygame.sprite.spritecollide(self,walls,False)
		self.plat_hit=pygame.sprite.spritecollide(self,plats,False)
		
		if len(self.plat_hit) >0: 
			self.flag=0
			self.mult=1
			self.change=1.36

		if self.change>6:
		  self.rand=random.randrange(2)

		if self.grav==0:
			self.gravity()

		for wall in self.plat_hit:
			if self.rect.y>0:
				self.rect.bottom=wall.rect.top
			
			else:
				self.rect.top=wall.rect.bottom
				

		
		
		
		if len(self.hit_count) >0 :

			self.rand=(self.rand+1)%2
			self.rcount=0
			self.lcount=0

		
		if self.rand==1:
			self.rect.x+=2
			self.rcount+=1

		elif self.rand==0:
			self.rect.x-=2
			self.lcount+=1



	def gravity(self):

		# effet of gravity
		if len(self.plat_hit) ==0 and self.flag==0:
			self.rect.y+=1
			self.flag=1
		else:
			self.change=self.change+(self.mult * 0.36)
			self.rect.y+=self.change

	def collide(self,player_list,ball_list):

		collide_hit_list=pygame.sprite.spritecollide(player_list,ball_list,False)

		for hit in collide_hit_list:
			
			return 1

		return 0
