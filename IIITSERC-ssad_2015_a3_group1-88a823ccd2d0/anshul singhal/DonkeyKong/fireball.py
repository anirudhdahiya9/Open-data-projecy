import os,sys,time,threading,copy

class Fireballs:
	def __init__(self,x,y,direction):
		self.__x=x
		self.__y=y
		self.__direction=direction
	def move(self,ch,board):
		x=self.__x
		y=self.__y
		if board._a[x][y+1]=='X':
			self.__direction=self.__direction*(-1)
		board._a[x][y]=board._copy[x][y]
		if ch:
			self.__y += 1*(self.__direction)
	def getpositionX(self):
		return self.__x
	def getpositionY(self):
		return self.__y
	def getdirection(self):
		return self.__direction
	def down(self,x,y,board):
		while board._a[x+1][y]==' ' or board._a[x+1][y]=='C' :
			os.system("clear")
			board._a[x][y]=board._copy[x][y]
			board.fireballcordinate(x+1,y)
			board.printscreen()
			x=x+1
		self.__x=x
