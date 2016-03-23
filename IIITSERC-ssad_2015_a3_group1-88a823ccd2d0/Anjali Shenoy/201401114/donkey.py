from person import *
from random import *

class Donkey(Person):
	def __init__(self,startX=5, startY=1):
		self._x=startX
		self._y=startY


	"""To fix donkey in place"""
	def printDonkey(self,sc,prevChar2):
		i=0
		i=randint(1,3)
		if(i==1 and sc.retChar(self._x,self._y-1) != 'X'):							#To go left till wall
			return self.move('a',sc,'D',prevChar2)
		elif(i==2 and sc.retChar(self._x+1,self._y+1) != ' '):						#To go right till edge of platform
			return self.move('d',sc, 'D',prevChar2)
		else:
			return ' '
			
	"""reposition donkey"""
	def reposition(self,x,y):
		self._x=x
		self._y=y

	"""To check donkey collision with mario"""
	def donCollision(self, mar):
		x=mar.getX()
		y=mar.getY()
		if x==self._x and y==self._y:
			return True
		else:
			return False


