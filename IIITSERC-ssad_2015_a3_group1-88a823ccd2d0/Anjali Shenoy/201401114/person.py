import os

class Person():

	def __init__(self, startX = 30, startY = 1):
		self._x = startX
		self._y = startY

	def printPrev(self,ch,sc):
		"""To print prev character instead of Mario"""
		if sc.checkBrokenStairs(self._x,self._y,ch) == True and ch == 'w':
			sc.printMario(self._x, self._y, 'H')

		elif sc.resVertical(self._x,self._y,ch) == True :
			if sc.checkBrokenStairs(self._x,self._y-1,ch) == True:
				sc.printMario(self._x, self._y, 'H')
			else:
				sc.printMario(self._x, self._y, ' ')

		elif sc.checkBrokenStairs(self._x,self._y,ch) == False and ch == 's' and sc.resVertical(self._x,self._y,'w') == True:
			sc.printMario(self._x,self._y, ' ')

		elif sc.checkBrokenStairs(self._x,self._y, ch) == False:
			sc.printMario(self._x, self._y, 'H')
		
		else:
			sc.printMario(self._x, self._y, ' ')


	def move(self,ch,sc,letter,prevChar):
		"""Movements of Characters"""

		if prevChar=='C' and (letter == 'D' or letter == 'O'):					#D or C shouldnt make C disappear
			sc.printMario(self._x,self._y,'C')
		elif prevChar=='O' and letter=='D':										#D should not eat O
			sc.printMario(self._x,self._y,'O')
		else:
			self.printPrev(ch,sc)	


		if (ch == 'w' and sc.resVertical(self._x, self._y, ch)== False):			#Able to go up, not a wall above you, then move 
			if(sc.checkWall(self._x-1, self._y) == False):
				prevChar=sc.retChar(self._x-1,self._y)
				self._x -= 1
		
		elif (ch == 's' and sc.resVertical(self._x,self._y, ch)== False):			#Able to go down
			if(sc.checkWall(self._x+1, self._y) == False):
				prevChar=sc.retChar(self._x+1,self._y)	
				self._x += 1
		
		elif (ch == 'd') :
			if(sc.checkWall(self._x,self._y+1) == False and sc.resHorizontal(self._x,self._y, ch)== False):  #going right, not a wall, can go horizontal
				prevChar=sc.retChar(self._x,self._y+1)
				self._y += 1
		
		elif(ch == 'a'):
			if(sc.checkWall(self._x,self._y-1) == False and sc.resHorizontal(self._x,self._y, ch)== False): #going left, not a wall there, can move horizontally
				prevChar=sc.retChar(self._x,self._y-1)
				self._y -= 1
		
		sc.printMario(self._x, self._y, letter)
		return prevChar

	"""To get X"""
	def getX(self):
		return self._x

	"""To get Y"""
	def getY(self):
		return self._y








