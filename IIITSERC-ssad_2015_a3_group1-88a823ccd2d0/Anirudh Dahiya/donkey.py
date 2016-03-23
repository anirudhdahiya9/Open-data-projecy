from bard import *
from player import *
from boarditems import *
from ball import *
class donkey(boarditems):
	def __init__(self):
		boarditems.__init__(self,4,4)
		self.flip=0

	def __revertback(self):
		if self.x==64:
			self.direction=1
		if self.x==4:
			self.direction=0
		return self
	
	def __singlemove(self):
		if self.direction==0:
			self.x+=1
		else:
			self.x-=1
		return self
			
	def move(self,brd):
		import random
		self=self.__revertback()
		if not self.flip==6:
			self=self.__singlemove()
			self.flip+=1
		else:
			self=self.__singlemove()
			self.flip=0
			self.direction=random.randint(0,1)
		return self
