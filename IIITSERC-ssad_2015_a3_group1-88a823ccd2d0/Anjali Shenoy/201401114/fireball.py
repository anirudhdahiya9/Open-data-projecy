from donkey import *
from random import *

class Fireball(Donkey):
	def __init__(self,x,y,prevChar):
		self.x=x
		self.y=y
		self.prevChar=' '
		self.level=1

	"""Generate Fireball"""
	def generate(self,sc):
		x=self.x
		y1=self.y+3
		while(sc.retChar(self.x,y1) != ' '):		#generate fireballs away from donkey to make it look like it's shooting it
			y1=y1+3
		sc.printMario(x,y1,'O')
		self.y=y1

	"""Movements of fireballs"""
	def fmove(self,sc):
		i=self.x
		j=self.y
		flag=0
		if self.x!=29 and self.level<7:					#all odd levels move right, even levels move left, except last(7th) level
			if (sc.retChar(i+1,j)=='X'):	
				if self.level%2==0:
					sc.printMario(i,j,self.prevChar) 
					self.prevChar=sc.retChar(i,j-1)
					self.x=i
					self.y=j-1
					sc.printMario(i,j-1,'O')
				else:
					sc.printMario(i,j,self.prevChar)
					self.prevChar=sc.retChar(i,j+1)
					self.x=i
					self.y=j+1
					sc.printMario(i,j+1,'O')

			elif sc.retChar(i+1,j) in [' ', 'C', 'P']:				#If you are standing on space, a coin, or player
				sc.printMario(i,j,self.prevChar)
				self.prevChar=sc.retChar(i+1,j)
				self.x=i+1
				self.y=j
				sc.printMario(i+1,j,'O')
				if (sc.retChar(self.x+2,self.y) =='X'):				#and 2 chars down is space, then increase floor level
							self.level+=1

			elif sc.retChar(i+1,j)=='H':							#if on staircase
				t=0
				t=randint(1,10)										#1- go down 2-continue forward

				if t%2==0 and sc.retChar(self.x,self.y+1) not in ['X',' '] :						#Go forward and you're not in the middle of stairs 
					if self.level%2==0:
						sc.printMario(i,j,self.prevChar)
						self.prevChar=sc.retChar(i,j-1)
						self.x=i
						self.y=j-1
						sc.printMario(i,j-1,'O')
					else:
						sc.printMario(i,j,self.prevChar)
						self.prevChar=sc.retChar(i,j+1)
						self.x=i
						self.y=j+1
						sc.printMario(i,j+1,'O')
				else:										#Go down									
					sc.printMario(i,j,self.prevChar)
					self.prevChar=sc.retChar(i+1,j)
					self.x=i+1
					self.y=j
					sc.printMario(i+1,j,'O')
					if(sc.retChar(self.x+1,self.y)=='X'):
						self.level+=1

			


		elif self.x==29:														#for x=29, x+2 is out of index, so to move down
			sc.printMario(self.x,self.y,self.prevChar)
			self.prevChar=sc.retChar(self.x+1,self.y)
			self.x+=1
			sc.printMario(self.x,self.y,'O')

		elif self.level==7 and self.y!=1:									#On last floor(bottom most) and still not reached left corner, keep going left
			sc.printMario(self.x,self.y,self.prevChar)
			self.prevChar=sc.retChar(self.x,self.y-1) 
			self.y-=1
			sc.printMario(self.x,self.y,'O')

		elif(self.y==1 and self.x==30):									   #O at [30][1] so delete itself (flag=1)
				sc.printMario(self.x,self.y,' ')
				flag=1

		prevChar=self.prevChar

		if flag==1:
			del(self)

		if prevChar == 'P':						#Fireball collided with P
			return 1
		else:
			return 0

	"""return previous char where O is now occupying"""
	def retPrevChar(self):
		return self.prevChar

	"""return row number"""
	def getX(self):
		return self.x
		
	"""return column"""
	def getY(self):
		return self.y



	
