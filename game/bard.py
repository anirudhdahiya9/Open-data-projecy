from player import *
from boarditems import *
from donkey import *
from ball import *
class board:
	def __init__(self):
		self.__makeframe()
		self.__board[1][14]='X'
		self.__board[1][13]='Q'
		self.__generatecoins()

	def __makeframe(self):
		self.__board=[['X']*80]
		for i in range(1,25):
			self.__board=self.__board+[['X']+78*[' ']+['X']]
		self.__board+=[['X']*80]
		for i in range(65):
			for j in range(5,26,8):
				self.__board[j][i]='X'
		for i in range(15,80):
			for j in range(9,26,8):
				self.__board[j][i]='X'
		
		for i in range(21,25):
			self.__board[i][60]='H'
		for i in range(13,17):
			self.__board[i][65]='H'
		for i in range(5,9):
			self.__board[i][60]='H'
		for i in range(17,21):
			self.__board[i][20]='H'
		for i in range(9,13):
			self.__board[i][16]='H'
		for i in range(0,15):
			self.__board[2][i]='X'
		for i in range(2,5):
			self.__board[i][2]='H'

	def __generatecoins(self):
		import random
		for i in range(25):
			while True:
				x=random.randint(15,65)
				y=random.randint(1,25)
				tp=self.getitem(x,y)
				if tp==' ':
					break
			self.updateitem(x,y,'C')	

	def __copyboard(self):
		copy=[]		
		for i in range(len(self.__board)):
			copy+=[[]]
			for j in range(len(self.__board[i])):
				if self.getitem(j,i)==' ':
					copy[i]+=[' ']
				elif self.getitem(j,i)=='X':
					copy[i]+='X'
				elif self.getitem(j,i)=='H':
					copy[i]+='H'
				elif self.getitem(j,i)=='C':
					copy[i]+='C'
				elif self.getitem(j,i)=='Q':
					copy[i]+='Q'
				else:
					copy[i]+='X'
		return copy

	def __getbitms(self,copy,plr,b1,don):
		copy[plr.y][plr.x]='P'
		for i in b1:
			copy[i.y][i.x]='O'
		if type(don)==int:
			pass
		else:
			copy[don.y][don.x]='D'
		return copy


	def printboard(self,plr,don,b1):
		import os
		from time import sleep
		os.system('clear')
		copy=self.__copyboard()
		copy=self.__getbitms(copy,plr,b1,don)
		for i in copy:
			ln=''	
			print ln.join(i)
		print 'Score:',plr.score
		print 'Lives:',plr.lives
		sleep(0.08)
	
		
	def getitem(self,x,y):
		return self.__board[y][x]

	def updateitem(self,x,y,c):
		self.__board[y][x]=c
	
		

	def checkwall(self,plr,mv):
		if mv.lower()=='d':
			if self.getitem(plr.x+1,plr.y)=='X':
				return True
			return False
		elif mv.lower()=='a':
			if self.getitem(plr.x-1,plr.y)=='X':
				return True
			return False
		elif mv.lower()=='s':
			if self.getitem(plr.x,plr.y+1)=='X':
				return True
			return False

	def checkstair(self,plr,mv):
		if self.getitem(plr.x,plr.y)=='H':
			return True
		return False

	def checkfloor(self,plr):
		if self.getitem(plr.x,plr.y+1)==' ' or self.getitem(plr.x,plr.y+1)=='C':
			return False
		return True
