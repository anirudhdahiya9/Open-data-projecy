import pygame
import random
pygame.init()
from game import *

#colors
black = (0,0,0)
white= (255,255,255)
red = (255,0,0)

class commander():
	def __init__(self):
		self.life=3
		self.score=0

	def creator(self):
		while self.life >0:
			gameon=game(self.score,self.life)
			num=gameon.main_loop()
			if num <=0:
				self.life-=1
				self.score=-num
				self.score-=25
				if self.score <0:
					self.score=0

			elif num==3.14:
				print 1
				break
			elif num>=0:
				self.score=num
				
			
		pygame.quit()		