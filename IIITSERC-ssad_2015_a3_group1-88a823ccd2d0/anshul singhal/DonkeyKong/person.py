import os,sys,time,threading,copy

class Person:
	def __init__(self,x,y):                 #constructor of persons
		self.__x=x
		self.__y=y
	
	def move(self,ch,board,player,record):
		x=self.__x
		y=self.__y
		board._a[x][y]=board._copy[x][y]
		if (ch=='W' or ch=='w'):
			if(board.checkWall(x-1,y) and board.checkladder(x-1,y)):
				if board.checkcoin(x-1,y):
					board.collectCoin()
				self.__x -= 1
			elif (not board.checkWall(x,y-1) and not board.checkWall(x,y+1)):
				if board.checkcoin(x-1,y):
					board.collectCoin()
				self.__x -= 1
		elif (ch=='A' or ch=='a'):
			if(board.checkWall(x,y-1) and board.checkfloor(x+1,y)):
				if board.checkcoin(x,y-1):
					board.collectCoin()
				self.__y -= 1
		elif (ch=='S' or ch=='s'):
			if(board.checkWall(x+1,y) and board.checkladder(x+1,y)):
				if board.checkcoin(x+1,y):
					board.collectCoin()
				self.__x += 1	
		elif (ch=='D' or ch=='d'):
			if(board.checkWall(x,y+1) and board.checkfloor(x+1,y) ):
				if board.checkcoin(x,y+1):
					board.collectCoin()
				self.__y += 1
		elif (ch==' '):
				if record == 'd' or record == 'D':
					mul=1
				else:
					mul=-1
				if (board.checkWall(x,y+(1*mul)) and board.checkWall(x,y+(2*mul)) and board.checkWall(x,y+(3*mul)) and board.checkWall(x,y+(4*mul)) and board.checkWall(x-1,y+(1*mul)) and board.checkWall(x-2,y+(2*mul)) ):					
					if board.checkcoin(x-1,y+mul*1):
						board.collectCoin()	
					
					self.__x -=1
					self.__y +=mul*1
					x=player.getpositionX()
					y=player.getpositionY()
					board.playercordinate(x,y)
					board.printscreen()
					
					x=self.__x
					y=self.__y
					board._a[x][y]=board._copy[x][y]
					if board.checkcoin(x-1,y+mul*1):
						board.collectCoin()	
					self.__x -=1
					self.__y +=mul*1
					time.sleep(0.2)
					os.system("clear")

					x=player.getpositionX()
					y=player.getpositionY()
					board.playercordinate(x,y)
					board.printscreen()
					x=self.__x
					y=self.__y
					board._a[x][y]=board._copy[x][y]
					if board.checkcoin(x+1,y+mul*1):
						board.collectCoin()	
					self.__x +=1
					self.__y +=mul*1
					time.sleep(0.2)
					os.system("clear")
					
					x=player.getpositionX()
					y=player.getpositionY()
					board.playercordinate(x,y)
					board.printscreen()
					time.sleep(0.2)
					os.system("clear")
					
					x=self.__x
					y=self.__y
					board._a[x][y]=board._copy[x][y]
					if board.checkcoin(x+1,y+mul*1):
						board.collectCoin()	
					self.__x +=1
					self.__y +=mul*1
				
		
	def down(self,x,y,board):
		while board._a[x+1][y]==' ' or board._a[x+1][y]=='C':
			if board.checkcoin(x,y):
				board.collectCoin()	
			board.playercordinate(x+1,y)
			board._a[x][y]=board._copy[x][y]
			os.system("clear")
			board.printscreen()
			x=x+1
		self.__x=x		
class Player(Person):
	def getpositionX(self):
		return self._Person__x
	def getpositionY(self):
		return self._Person__y
class Donkey(Person):
	def getpositionX(self):
		return self._Person__x
	def getpositionY(self):
		return self._Person__y
	def move(self,ch,board,direction):
		x=self._Person__x
		y=self._Person__y
		if y>7:
			direction=-1
		if y<2:
			direction=1
		board._a[x][y]=board._copy[x][y]
		if ch:
			self._Person__y += 1*direction
		return direction

