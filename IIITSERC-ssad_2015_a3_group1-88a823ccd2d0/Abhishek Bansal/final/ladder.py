import pygame
from constants import *
class ladder():
	def __init__(self,p1,p2,w):
		self.p1=p1
		self.p2=p2
		self.w=w
	def make_ladder(self,gameinst):
		#c=18
		p1=self.p1
		p2=self.p2
		c=self.w
		l=12
		D=gameinst.DISP
		pygame.draw.line(D,LADDER_COLOUR,p1,p2)
		p3=(p1[0]+c,p1[1])
		p4=(p2[0]+c,p2[1])
		pygame.draw.line(D,LADDER_COLOUR,p3,p4)
		j=p2[1]+l
		pygame.draw.line(D,LADDER_COLOUR,(p1[0],j),(p3[0],j),3)
		while(j<p1[1]):
			pygame.draw.line(D,LADDER_COLOUR,(p1[0],j),(p3[0],j),3)
			j+=l
		return
