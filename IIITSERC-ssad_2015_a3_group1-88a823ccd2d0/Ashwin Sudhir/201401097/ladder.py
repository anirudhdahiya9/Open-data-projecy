import pygame
import random
pygame.init()

#colors
black = (0,0,0)
white= (255,255,255)
red = (255,0,0)

class ladders(pygame.sprite.Sprite):

	def __init__(self,x,y,width,height):
		
		pygame.sprite.Sprite.__init__(self)
		self.image=pygame.image.load("images/ladder.jpg").convert()
		self.image=pygame.transform.scale(self.image,[width,height])

		
		self.rect=self.image.get_rect()

		
		self.rect.x=x
		self.rect.y=y

	def touch_check(self,player,ladder_list):

		ladder_hit_list=pygame.sprite.spritecollide(player,ladder_list,False)
		#print ladder_hit_list

		leg=len(ladder_hit_list)

		return leg
