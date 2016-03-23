from bard import *
from player import *
from boarditems import *
from donkey import *

class ball(boarditems):
	def __init__(self,don):
		if don.direction==0:
			self.x=don.x+1
		else:
			self.x=don.x-1
		self.y=don.y
		self.direction=don.direction
		self.mode=0
	
	def __fall(self):
		self.mode=1
		self.y+=1

	def generateball(self,don):
		from random import randint
		return b1


	def move(self,brd):
		if brd.checkfloor(self) and brd.getitem(self.x,self.y+1)!='H' and self.mode==0:
			if self.direction==0:
				if brd.getitem(self.x+1,self.y)=='X':
					self.direction=1
				else:
					self.x+=1
			else:
				if brd.getitem(self.x-1,self.y)=='X':
					self.direction=0
				else:
					self.x-=1
		elif brd.checkfloor(self) and brd.getitem(self.x,self.y+1)!='H' and self.mode==1:
			import random
			self.direction=random.randint(0,1)
			self.mode=0
			if self.direction==0:
				if brd.getitem(self.x+1,self.y)=='X':
					self.direction=1
				else:
					self.x+=1
			else:
				if brd.getitem(self.x-1,self.y)=='X':
					self.direction=0
				else:
					self.x-=1
			
		elif brd.getitem(self.x,self.y+1)!='X':
			self.__fall()
		return self
