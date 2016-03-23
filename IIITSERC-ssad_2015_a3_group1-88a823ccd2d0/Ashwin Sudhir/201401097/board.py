import pygame
import random
pygame.init()
from wall import *
from coin import *
from ladder import *
from platform import *
from person import *

#colors
black = (0,0,0)
white= (255,255,255)
red = (255,0,0)

class board():
	def __init__(self):
		self.screen_width=1600
		self.screen_rheight=1000
		self.screen_height=900
		self.screen=pygame.display.set_mode([self.screen_width,self.screen_rheight])

		# COLLISION LIST
		self.collide_list=pygame.sprite.Group()

		self.wall_list=pygame.sprite.Group()
		self.all_sprite_list=pygame.sprite.Group()
		self.ladder_list=pygame.sprite.Group()
		self.person_list=pygame.sprite.Group()
		self.gamer_list=pygame.sprite.Group()
		self.coin_list=pygame.sprite.Group()

		self.walls=wall(0,0,self.screen_width,20)

		self.wall_list.add(self.walls)
		self.all_sprite_list.add(self.walls )
		self.collide_list.add(self.walls)

		

# WALLS genertae
		self.walls=wall(0,0,20,self.screen_height)

		self.wall_list.add(self.walls)
		self.all_sprite_list.add(self.walls )
		self.collide_list.add(self.walls )


		self.walls=wall(self.screen_width-20,0,20,self.screen_height)

		self.wall_list.add(self.walls)
		self.all_sprite_list.add(self.walls )
		self.collide_list.add(self.walls )



		#self.walls=wall(0,self.screen_height-20,self.screen_width-20,20)

		#self.wall_list.add(self.walls)
		#self.all_sprite_list.add(self.walls )
		#self.collide_list.add(self.walls )


		


		#platforms generate

		self.platform_list=pygame.sprite.Group()


		#ground platform
		self.platform=platforms(0,self.screen_height-20,self.screen_width-20,20)

		self.platform_list.add(self.platform)
		self.all_sprite_list.add(self.platform )
		self.collide_list.add(self.platform )



		# 1st platform
		self.platform=platforms(0,750,self.screen_width-401,10)

		self.platform_list.add(self.platform)
		self.all_sprite_list.add(self.platform )
		self.collide_list.add(self.platform )
       	
		# 2nd platform

		#left half

		self.platform=platforms(200,625,self.screen_width-1300,10)

		self.platform_list.add(self.platform)
		self.all_sprite_list.add(self.platform )
		self.collide_list.add(self.platform )

		#right half
		self.platform=platforms(550,625,self.screen_width-200,10)

		self.platform_list.add(self.platform)
		self.all_sprite_list.add(self.platform )
		self.collide_list.add(self.platform )
		
		# 3rd platform
		# left half
		self.platform=platforms(0,500,self.screen_width-900,10)

		self.platform_list.add(self.platform)
		self.all_sprite_list.add(self.platform )
		self.collide_list.add(self.platform )

		#mid

		self.platform=platforms(750,500,self.screen_width-1400,10)

		self.platform_list.add(self.platform)
		self.all_sprite_list.add(self.platform )
		self.collide_list.add(self.platform )

		#end

		self.platform=platforms(1000,500,self.screen_width-1400,10)

		self.platform_list.add(self.platform)
		self.all_sprite_list.add(self.platform )
		self.collide_list.add(self.platform )

		# 4nd platform

		#left half

		self.platform=platforms(200,375,self.screen_width-1300,10)

		self.platform_list.add(self.platform)
		self.all_sprite_list.add(self.platform )
		self.collide_list.add(self.platform )

		#right half
		self.platform=platforms(550,375,self.screen_width-200,10)

		self.platform_list.add(self.platform)
		self.all_sprite_list.add(self.platform )
		self.collide_list.add(self.platform )

		
		# 5rd platform

		# 3rd platform
		
		# left half
		self.platform=platforms(0,250,self.screen_width-650,10)

		self.platform_list.add(self.platform)
		self.all_sprite_list.add(self.platform )
		self.collide_list.add(self.platform )

		#end

		self.platform=platforms(1000,250,self.screen_width-1400,10)

		self.platform_list.add(self.platform)
		self.all_sprite_list.add(self.platform )
		self.collide_list.add(self.platform )



		#top platform



		self.platform=platforms(345,125,200,10)

		self.platform_list.add(self.platform)
		self.all_sprite_list.add(self.platform )
		self.collide_list.add(self.platform )
		

		self.platform=platforms(595,125,200,10)

		self.platform_list.add(self.platform)
		self.all_sprite_list.add(self.platform )
		self.collide_list.add(self.platform )
		

		
		#		ladders

		#1st
	
		self.ladder=ladders(1200,743,40,130)

		self.ladder_list.add(self.ladder)
		self.all_sprite_list.add(self.ladder)

		#2nd
	
		self.ladder=ladders(504,618,40,130)

		self.ladder_list.add(self.ladder)
		self.all_sprite_list.add(self.ladder)

		#3nd half
	
		self.ladder=ladders(705,500,40,50)

		#self.ladder_list.add(self.ladder)
		self.all_sprite_list.add(self.ladder)
        
        # rd bottom

		self.ladder=ladders(705,580,40,50)

		self.ladder_list.add(self.ladder)
		self.all_sprite_list.add(self.ladder)
		
		#4nd
	
		self.ladder=ladders(955,490,40,130)

		self.ladder_list.add(self.ladder)
		self.all_sprite_list.add(self.ladder)
		
		#5nd
	
		self.ladder=ladders(504,365,40,130)

		self.ladder_list.add(self.ladder)
		self.all_sprite_list.add(self.ladder)

		#6th

		

		self.ladder=ladders(955,240,40,130)

		self.ladder_list.add(self.ladder)
		self.all_sprite_list.add(self.ladder)

		#top ladder

		self.ladder=ladders(554,115,40,130)

		self.ladder_list.add(self.ladder)
		self.all_sprite_list.add(self.ladder)



		
		# PLAYER genertate

		
		self.player=players(100,800,40,40,"images/mario.png")
		self.person_list.add(self.player)
		self.gamer_list.add(self.player)
		

		self.all_sprite_list.add(self.player)
		
		# donkey 

		self.donk=donkey(100,100,60,60,"images/dk6.gif")
		self.person_list.add(self.donk)
		self.all_sprite_list.add(self.donk)


		#queen

		self.queen=players(400,50,35,35,"images/q10.gif")
		self.person_list.add(self.queen)

		self.all_sprite_list.add(self.queen)


		## random coins\
		
		x=random.sample(xrange(75,1550),20)

		y=random.sample(xrange(150,850),20)
		
		for i in range(20):
			self.coin=coins(x[i],y[i],30,30)
			self.coin_list.add(self.coin)



	def display_score(self,score,life):

		font=pygame.font.SysFont("monospace",50)
		scoretext=font.render("Score:"+str(score), 1,black)
		self.screen.blit(scoretext, (200, 950))

		scoretext=font.render("Life:"+str(life), 1,black)
		self.screen.blit(scoretext, (1000, 950))
