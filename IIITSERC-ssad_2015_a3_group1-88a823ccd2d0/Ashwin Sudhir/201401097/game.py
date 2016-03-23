import pygame
import random
pygame.init()
from board import *
from fireball import *
from person import *

#colors
black = (0,0,0)
white= (255,255,255)
red = (255,0,0)

class game(pygame.sprite.Sprite):


	def __init__(self,score,life):
		pygame.sprite.Sprite.__init__(self)
		
		self.done=False

		self.clock=pygame.time.Clock()

		self.score=0

		self.block_size=5

		self.plyboard=board()

		self.grav=0
		self.flag=0

		self.rcount=0
		self.lcount=0
		self.rand=random.randrange(2)
		self.fball=pygame.sprite.Group()
		self.firecount=0
		self.life=life
		self.score=score
		self.end=0
		self.event=0


	def main_loop(self):

		while self.done == False:
			#for event in pygame.event.get():
				
			## DISPLAY SCORE AND LIFE

			




##### FIREBALLS
			
			if self.firecount == 225:
				self.fireballs=fireball(self.plyboard.donk.rect.x,self.plyboard.donk.rect.y,25,25)
				
				self.fball.add(self.fireballs)
				self.firecount=0
			else:
				self.firecount+=1

			for manyballs in self.fball:

				if manyballs.rect.x<200 and manyballs.rect.y >800:
					self.fball.remove(manyballs)

				manyballs.move(self.plyboard.wall_list,self.plyboard.platform_list)
				if manyballs.collide(self.plyboard.player,self.fball) ==1:
					self.end=-1
					break
			if self.end==-1:
				break
				
####### PLAYER MOVEMENT
			for self.event in pygame.event.get():

				if self.event.type == pygame.QUIT :
					self.done= True
				###### REACHING THE QUEEN
				if self.plyboard.queen.rect.bottom >= self.plyboard.player.rect.bottom:
				
					self.score+=50
					self.end=1
					break

				#### donkey player collsion

				if self.plyboard.donk.checkplayer(self.plyboard.gamer_list) == 1:
					self.end=-1
					break


				self.plyboard.screen.fill(white)
				if self.event.type==pygame.KEYDOWN:



					if self.event.key == pygame.K_q:
						self.done= True



					self.grav=0 # to switch gravity on/off
					
					if self.plyboard.ladder.touch_check(self.plyboard.player,self.plyboard.ladder_list) > 0 and self.event.key != pygame.K_w and self.event.key!=pygame.K_SPACE :
						self.plyboard.player.change_y=0
						self.grav=1
							
					if self.event.key==pygame.K_a:
						self.plyboard.player.movlr(-self.block_size,0,1,0)

					elif self.event.key==pygame.K_d:
						self.plyboard.player.movlr(self.block_size,0,1,0)
					
					elif self.event.key==pygame.K_w and self.plyboard.ladder.touch_check(self.plyboard.player,self.plyboard.ladder_list) > 0:
						
						self.plyboard.player.movlr(0,-self.block_size,0,1)
						
						self.grav=1
					elif self.event.key==pygame.K_SPACE :
						if self.plyboard.player.jump(self.plyboard.collide_list) == 0:
							if self.plyboard.ladder.touch_check(self.plyboard.player,self.plyboard.ladder_list) > 0:
								self.grav=1							
								self.plyboard.player.movlr(0,0,0,1)
						

						
					
					elif self.event.key==pygame.K_s:
						self.plyboard.player.movlr(0,self.block_size,0,1)
						if self.plyboard.ladder.touch_check(self.plyboard.player,self.plyboard.ladder_list) > 0:
							self.grav=1
							

				if self.event.type==pygame.KEYUP:

					if self.plyboard.ladder.touch_check(self.plyboard.player,self.plyboard.ladder_list) > 0 :
						
						self.plyboard.player.change_y=0
						self.grav=1


					if self.event.key==pygame.K_a or self.event.key==pygame.K_d : #or 
						self.plyboard.player.movlr(0,0,1,0)

					if self.event.key==pygame.K_w or self.event.key==pygame.K_s:
						self.plyboard.player.movlr(0,0,1,1)


					
			if self.plyboard.ladder.touch_check(self.plyboard.player,self.plyboard.ladder_list) == 0 :
				self.grav=0
				self.flag=0
			elif self.plyboard.ladder.touch_check(self.plyboard.player,self.plyboard.ladder_list) > 0 and self.flag==0 :
				
				self.plyboard.player.change_y=0
				self.grav=1
				self.flag=1

				
			if self.end ==1 or self.end==-1:
				break

			#moving the donkey
			
			self.plyboard.donk.rand_move(self.plyboard.wall_list)

			## Collecting coins
			self.score+=self.plyboard.player.collectCoin(self.plyboard.coin_list)
			

			self.plyboard.player.checkCollision(self.plyboard.collide_list,self.grav)
			self.plyboard.donk.checkCollision(self.plyboard.collide_list,0)
			self.plyboard.queen.checkCollision(self.plyboard.collide_list,0)
			for coin in self.plyboard.coin_list:
				coin.update(self.plyboard.platform_list)
			
			self.plyboard.screen.fill(white)
			self.plyboard.all_sprite_list.draw(self.plyboard.screen)
			self.plyboard.platform_list.draw(self.plyboard.screen)
			self.plyboard.ladder_list.draw(self.plyboard.screen)
			self.plyboard.coin_list.draw(self.plyboard.screen)

			self.fball.draw(self.plyboard.screen)
			self.plyboard.person_list.draw(self.plyboard.screen)
			self.plyboard.wall_list.draw(self.plyboard.screen)
			self.plyboard.display_score(self.score,self.life)
			pygame.display.update()
		  
			

			self.clock.tick(100)

		#Sending score update
		
		if self.end ==- 1:
			return -self.score
		elif self.end ==1:

			return self.score
		
		else :
			return 3.14