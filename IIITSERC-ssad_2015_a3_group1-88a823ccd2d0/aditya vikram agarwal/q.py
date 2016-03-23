#!/usr/bin/python
from __future__ import print_function
import sys
import os
import random
import time
import tty
import termios
def getchar():
   fd = sys.stdin.fileno()
   old_settings = termios.tcgetattr(fd)
   try:
      tty.setraw(sys.stdin.fileno())
      ch = sys.stdin.read(1)
   finally:
      termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
   return ch
class person(object):
	def __init__(self,char,row,column):
		self.char=char
		self.row=row
		self.column=column
	def __update(self,row,column):
		self.row=row
		self.column=column
		raise NotImplementedError
	def __gorights(self,board,coinlist,newcoinlist,fireballlist):
		raise NotImplementedError
	def __golefts(self,board,coinlist,newcoinlist,fireballlist):
		raise NotImplementedError
class player(person):
	def __init__(self,char,row,column):
		super(player,self).__init__(char,row,column)
		self.score=0
		self.lives=3
	def __newlife(self,board,coinlist,newcoinlist,fireballlist):
		del coinlist[:]
		for i in newcoinlist:
			coinlist.append(i)
		del fireballlist[:]
		self.row=24
		self.column=4
		self.lives=boy.lives-1
		self.score=boy.score-25
	def __update(self,row,column):
		self.row=row
		self.column=column
	def __updatePosition(self,row,column):
		self.__update(row,column)
	def __goups(self,board,coinlist,newcoinlist,fireballlist):
		x=getPosition(self,0)
		j=0
		for i in range(x[0]-(x[0]-1)%4,x[0]-(x[0]-1)%4+4):
			if(board[i][x[1]]=='H' or board[i][x[1]]=='P'):
				j=j+1
		if(j==4 or board[x[0]-1][x[1]]=='Q'):
			self.__updatePosition(x[0]-1,x[1])
		elif(x[0]==4  and board[x[0]-1][x[1]]=='H' or x[0]==3 and board[x[0]+1][x[1]]=='H'):
			self.__updatePosition(x[0]-1,x[1])
		collision=checkCollision(board,self,fireballlist)
		if(collision==1):
			self.__newlife(board,coinlist,newcoinlist,fireballlist)
		if(self.row==queen.row):
			return 1
		else:
			return 0
	def __godowns(self,board,coinlist,newcoinlist,fireballlist):
		x=getPosition(self,0)
		j=0;
		for i in range(x[0]-(x[0]-1)%4,x[0]-(x[0]-1)%4+4):
			if(board[i][x[1]]=='H' or board[i][x[1]]=='P'):
				j=j+1
		if(j==4 and board[self.row+1][self.column]!='X' or x[0]!=24 and x[0]%4==0 and board[x[0]+1][x[1]]=='H' and board[x[0]+2][x[1]]=='H' and board[x[0]+3][x[1]]=='H' and board[x[0]+4][x[1]]=='H'):
			self.__updatePosition(x[0]+1,x[1])
		elif(x[0]==3 and board[x[0]+1][x[1]]=='H' or x[0]==2 and board[x[0]+1][x[1]]=='H' and board[x[0]+2][x[1]]=='H'):
			self.__updatePosition(x[0]+1,x[1])
		collision=checkCollision(board,self,fireballlist)
		if(collision==1):
			self.__newlife(board,coinlist,newcoinlist,fireballlist)
			return
	def __golefts(self,board,coinlist,newcoinlist,fireballlist):
		x=getPosition(self,0)
		wall=checkWall(board,x[0],x[1]-1)
		collision=checkCollision(board,self,fireballlist)
		if(collision==1):
			self.__newlife(board,coinlist,newcoinlist,fireballlist)
			return
		elif (wall==1 or (board[x[0]+1][x[1]+1]!='X' and board[x[0]+1][x[1]]!='X')):
			return
		elif(board[x[0]][x[1]-1]==' ' or board[x[0]][x[1]-1]=='H'):
			self.__updatePosition(x[0],x[1]-1)
		elif(board[x[0]][x[1]-1]=='C'):
			self.__updatePosition(x[0],x[1]-1)
			collectCoin(self,coinlist)
		x=getPosition(self,0)
		if(board[x[0]+1][x[1]]==' '):
			while(board[x[0]+1][x[1]]!='X'):
				self.__updatePosition(x[0]+1,x[1])
				board=[['X' for i in range(0,81)] for j in range(0,26)]
				initialize(board,coinlist,fireballlist)
				printboard(board,1)
				time.sleep(0.1)
				x=getPosition(self,0)
		collision=checkCollision(board,self,fireballlist)
		if(collision==1):
			self.__newlife(board,coinlist,newcoinlist,fireballlist)
			return
	def __gorights(self,board,coinlist,newcoinlist,fireballlist):
		x=getPosition(self,0)
		wall=checkWall(board,x[0],x[1]+1)
		collision=checkCollision(board,self,fireballlist)
		if(collision==1):
			self.__newlife(board,coinlist,newcoinlist,fireballlist)
			return
		elif (wall==1 or (board[x[0]+1][x[1]-1]!='X' and board[x[0]+1][x[1]]!='X')):
			return
		elif(board[x[0]][x[1]+1]==' ' or board[x[0]][x[1]+1]=='H'):
			self.__updatePosition(x[0],x[1]+1)
		elif(board[x[0]][x[1]+1]=='C'):
			self.__updatePosition(x[0],x[1]+1)
			collectCoin(self,coinlist)
		x=getPosition(self,0)
		if(board[x[0]+1][x[1]]==' '):
			while(board[x[0]+1][x[1]]!='X'):
				self.__updatePosition(x[0]+1,x[1])
				board=[['X' for i in range(0,81)] for j in range(0,26)]
				initialize(board,coinlist,fireballlist)
				fireballupdate(board,fireballlist)
				printboard(board,1)
				time.sleep(0.1)
				x=getPosition(self,0)
		collision=checkCollision(board,self,fireballlist)
		if(collision==1):
			self.__newlife(board,coinlist,newcoinlist,fireballlist)
			return
	def __jumps(self,board,coinlist,newcoinlist,fireballlist):
		k=0
		l=4
		while(k<l):
			x=getPosition(self,0)
			wall=checkWall(board,x[0],x[1]+1)
			if(k==3):
				if(wall==0 and board[x[0]+1][x[1]+1]=='C'):
					self.__updatePosition(x[0]+1,x[1]+1)
					collectCoin(self,coinlist)
				elif(wall==1 and board[x[0]+1][x[1]]!='C'):
					self.__updatePosition(x[0]+1,x[1])
				elif(wall==0 and board[x[0]+1][x[1]]=='C'):
					self.__updatePosition(x[0]+1,x[1])
					collectCoin(self,coinlist)
				else:
					self.__updatePosition(x[0]+1,x[1]+1)
				collision=checkCollision(board,self,fireballlist)
				if(collision==1):
					self.__newlife(board,coinlist,newcoinlist,fireballlist)
					return
					break	
				elif(board[self.row+1][self.column]==' '):
					k=k-1
			elif(k==0 or k==1):
				if((x[0]==4 or x[0]==2) and x[1]>=15 and x[1]<=25):
					return
				elif((x[0]==4 or x[0]==3) and x[1]==14):
					self.__updatePosition(x[0]-1,x[1])
				elif(wall==0):
					self.__updatePosition(x[0]-1,x[1]+1)
				else:
					self.__updatePosition(x[0]-1,x[1])
			else:
				if(wall==0):
					self.__updatePosition(x[0]+1,x[1]+1)
				else:
					self.__updatePosition(x[0]+1,x[1])
			board=[['X' for i in range(0,81)] for j in range(0,26)]
			initialize(board,coinlist,fireballlist)
			fireballupdate(board,fireballlist)
			collision=checkCollision(board,self,fireballlist)
			if(collision==1):
				self.__newlife(board,coinlist,newcoinlist,fireballlist)
				return
				break
			printboard(board,1)
			time.sleep(0.1)
			k=k+1
	def __jumplefts(self,board,coinlist,newcoinlist,fireballlist):
		k=0
		l=4
		while(k<l):
			x=getPosition(self,0)
			wall=checkWall(board,x[0],x[1]-1)
			if(k==3):
				if(wall==0 and board[x[0]+1][x[1]-1]=='C'):
					self.__updatePosition(x[0]+1,x[1]-1)
					collectCoin(self,coinlist)
				elif(wall==1 and board[x[0]+1][x[1]]!='C'):
					self.__updatePosition(x[0]+1,x[1])
				elif(wall==1 and board[x[0]+1][x[1]]=='C'):
					self.__updatePosition(x[0]+1,x[1])
					collectCoin(self,coinlist)
				else:
					self.__updatePosition(x[0]+1,x[1]-1)
				collision=checkCollision(board,self,fireballlist)
				if(collision==1):
					self.__newlife(board,coinlist,newcoinlist,fireballlist)
					return
					break
				elif(board[self.row+1][self.column]==' '):
					k=k-1
			elif(k==0 or k==1):
				if((x[0]==4 or x[0]==2) and x[1]>=15 and x[1]<=25):
					return
				elif((x[0]==4 or x[0]==3) and x[1]==26):
					self.__updatePosition(x[0]-1,x[1])
				elif(wall==0):
					self.__updatePosition(x[0]-1,x[1]-1)
				else:
					self.__updatePosition(x[0]-1,x[1])
			else:
				if(wall==0):
					self.__updatePosition(x[0]+1,x[1]-1)
				else:
					self.__updatePosition(x[0]+1,x[1])
			board=[['X' for i in range(0,81)] for j in range(0,26)]
			initialize(board,coinlist,fireballlist)
			fireballupdate(board,fireballlist)
			collision=checkCollision(board,self,fireballlist)
			if(collision==1):
				self.__newlife(board,coinlist,newcoinlist,fireballlist)
				return
				break
			printboard(board,1)
			time.sleep(0.1)
			k=k+1
	def goup(self,board,coinlist,newcoinlist,fireballlist):
		boy.__goups(board,coinlist,newcoinlist,fireballlist)
	def godown(self,board,coinlist,newcoinlist,fireballlist):
		boy.__godowns(board,coinlist,newcoinlist,fireballlist)
	def goleft(self,board,coinlist,newcoinlist,fireballlist):
		boy.__golefts(board,coinlist,newcoinlist,fireballlist)
	def goright(self,board,coinlist,newcoinlist,fireballlist):
		boy.__gorights(board,coinlist,newcoinlist,fireballlist)
	def jump(self,board,coinlist,newcoinlist,fireballlist):
		boy.__jumps(board,coinlist,newcoinlist,fireballlist)
	def jumpleft(self,board,coinlist,newcoinlist,fireballlist):
		boy.__jumplefts(board,coinlist,newcoinlist,fireballlist)
class donkey(person):
	def __update(self,row,column):
		self.row=row
		self.column=column
	def __gorights(self,board,coinlist,newcoinlist,fireballlist):
		self.__update(self.row,self.column+1)
	def __golefts(self,board,coinlist,newcoinlist,fireballlist):
		self.__update(self.row,self.column-1)
	def __updatePosition(self,board,coinlist,newcoinlist,fireballlist):
		i=random.randint(0,1)
		if(board[self.row][self.column+1]!='H' and i==0):
			self.__gorights(board,coinlist,newcoinlist,fireballlist)
		elif(board[self.row][self.column-1]!='X'):
			self.__golefts(board,coinlist,newcoinlist,fireballlist)
	def dragonupdate(self,board,coinlist,newcoinlist,fireballlist):
		self.__updatePosition(board,coinlist,newcoinlist,fireballlist)
class queen(person):
	def __update(self,row,column):
		self.row=row
		self.column=column
	def __gorights(self,board,coinlist,newcoinlist,fireballlist):
		self.__update(self.row,self.column+1)
	def __golefts(self,board,coinlist,newcoinlist,fireballlist):
		self.__update(self.row,self.column-1)
	def __updatePosition(self,board,coinlist,newcoinlist,fireballlist):
		i=random.randint(0,1)
		if(board[self.row][self.column+1]==' ' and i==0):
			self.__gorights(board,coinlist,newcoinlist,fireballlist)
		elif(board[self.row][self.column-1]==' '):
			self.__golefts(board,coinlist,newcoinlist,fireballlist)
	def queenupdate(self,board,coinlist,newcoinlist,fireballlist):
		self.__updatePosition(board,coinlist,newcoinlist,fireballlist)
class board(object):
	def __init__(self,char,row,column):
		self.char=char
		self.row=row
		self.column=column
class fireball(board):
	def __init__(self,char,row,column):
		super(fireball,self).__init__(char,row,column)
		self.movedirection=1
	def __del__(self):
		pass
	def __updatePosition(self,board):
		self.row=self.row
		if(self.movedirection==1):
			self.column=self.column+1
		else:
			self.column=self.column-1
	def __falldown(self,board,k):
		self.movedirection=k
		self.row=self.row+4
		self.column=self.column+1
	def __rebound(self,board):
		if(self.movedirection==0):
			self.movedirection=1
		else:
			self.movedirection=0
	def fireupdate(self,board,fireballlist):
		j=random.randrange(0,2)
		if(self.row==24 and self.column==2):
			fireballlist.remove(self)
		elif(board[self.row+1][self.column]=='H' and j==0 or board[self.row+1][self.column]==' '):
			k=random.randrange(0,2)
			self.__falldown(board,k)
		elif(board[self.row][self.column+1]!='X' and self.movedirection==1):
			self.__updatePosition(board)
		elif(board[self.row][self.column-1]!='X' and self.movedirection==0):
			self.__updatePosition(board)
		else:
			self.__rebound(board)
class coins(board):
	def __init__(self,char,row,column):
		super(coins,self).__init__(char,row,column)
		coins.value=5
def printboard(board,duration):
	global l
	if(duration==1):
		board[boy.row][boy.column]=' '
	#board[queen.row][queen.column]=queen.char
	#board[dragon.row][dragon.column]=dragon.char
	print("\033c")
	for i in range(1,26):
		for j in range(1,81):
			print(board[i][j],end='')
		print('\n',end='')
	print("LIVES:",boy.lives,"SCORE:",boy.score,"LEVEL:",l)
	if(duration==1):
		time.sleep(0.1)
		board[boy.row][boy.column]=boy.char
		printboard(board,0)
l=1
queen=queen('Q',2,17)
boy=player('P',24,4)
dragon=donkey('D',4,4)
dragonbrother=donkey('D',12,4)
dragonbrotherb=donkey('D',20,2)
def initialize(board,coinlist,fireballlist):	
	for i  in range(2,25):
		for j in range(2,80):
			if i%4==1:
				break
			board[i][j]=' '
	for i in range(5,25,4):
		for j in range(2,13):
			if i%8==1:
				board[i][j]=' '
			elif i%4==1:
				board[i][80-j+1]=' '
	board[2][15]='X'
	for i in range(15,26):
		board[3][i]='X'
	board[2][25]='X'
	for j in range (1,81):
		for i in range(1,25):
			if j==65 and i>=21 and i<=24 or j==30 and i>=17 and i<=20 or j==60 and i>=13 and i<=16 or j==25 and i>=9 and i<=12 or j==55 and i>=5 and i<=8 or j==56 and i>=23 and i<=24 or j==56 and i==21 or j==35 and i>=17 and i<=18 or j==44 and i>=13 and i<=14 or j==57 and i>=9 and i<=10 or j==57 and i==13 or j==23 and i>=3 and i<=4:
				board[i][j]='H'
	for i in coinlist:
		board[i.row][i.column]=i.char
	for i in fireballlist:
		board[i.row][i.column]=i.char
	board[queen.row][queen.column]=queen.char
	board[boy.row][boy.column]=boy.char
	board[dragon.row][dragon.column]=dragon.char
	if(l>=2):
		board[dragonbrother.row][dragonbrother.column]=dragonbrother.char
	if(l>=3):
		board[dragonbrotherb.row][dragonbrotherb.column]=dragonbrotherb.char
def initializecoins(board,coinlist,newcoinlist):
	i=0;
	while i<21:
		coinrow=random.randrange(4,25,2)
		coincolumn=random.randrange(2,79,2)
		if (board[coinrow][coincolumn]==' ' and board[coinrow+1][coincolumn]=='X' and board[coinrow][coincolumn+1]!='C' and board[coinrow][coincolumn-1]!='C'):
			newcoin=coins('C',coinrow,coincolumn)
			coinlist.append(newcoin)
			newcoinlist.append(newcoin)
			board[newcoin.row][newcoin.column]=newcoin.char
			i=i+1
def fireballupdate(board,fireballlist):
	for i in fireballlist:
		i.fireupdate(board,fireballlist)
def makefireball(board,fireballlist,l):
	i=random.randint(0,1)
	if(i==0):
		fireballnew=fireball('O',dragon.row,dragon.column+1)
	elif(i==1):
		fireballnew=fireball('O',dragon.row,dragon.column+1)
		if(board[fireballnew.row][fireballnew.column+1]!='O'):
			fireballlist.append(fireballnew)
		if(l>=2):
			fireballnew=fireball('O',dragonbrother.row,dragonbrother.column+1)
			if(board[fireballnew.row][fireballnew.column+1]!='O'):
				fireballlist.append(fireballnew)
		if(l>=3):
			fireballnew=fireball('O',dragonbrotherb.row,dragonbrotherb.column+1)
	if(board[fireballnew.row][fireballnew.column+1]!='O'):
		fireballlist.append(fireballnew)
def getPosition(object,i):
	if i==0:
		rowcolumn=[boy.row,boy.column]
		return rowcolumn
	elif i==1:
		#return rowcolumn
		pass
def checkWall(board,row,column):
	if(board[row][column]=='X'):
		return 1
	else:
		return 0
def checkCollision(board,boy,fireballlist):
	global l
	for i in fireballlist:
		if(boy.row==i.row and boy.column==i.column):
			return 1
	if(boy.row==dragon.row and boy.column==dragon.column):
		return 1
	if(l>=2 and boy.row==dragonbrother.row and boy.column==dragonbrother.column):
		return 1
	if(l>=3 and boy.row==dragonbrotherb.row and boy.column==dragonbrotherb.column):
		return 1
	return 0
def collectCoin(boy,coinlist):
	for i in coinlist:
		if(i.row==boy.row and i.column==boy.column):
			coinlist.remove(i)
			break
	boy.score=boy.score+5
def quit(board,coinlist):
	sys.exit()
def winlose(board,coinlist,newcoinlist,fireballlist,i,name):
	os.system('clear')
	print("\033c")
	global l
	if(i==0):
		l=1
		print(name,"YOU LOSE")
		print("YOUR SCORE:",boy.score)
		boy.score=0
		ask=input("play again? press 1 for yes or 2 for no and press enter: \n")
		if(ask==2):
			quit(board,coinlist)
		boy.lives=3
		i=1
		while(i<=4):
			j=1
			while(j<=10000):
				print("Loading New Game .\r", end="")
				j=j+1
			j=1
			while(j<=10000):
				print("Loading New Game ..\r", end="")
				j=j+1
			j=1
			while(j<=10000):
				print("Loading New Game ...\r", end="")
				j=j+1
			j=1
			while(j<=10000):
				print("Loading New Game    \r",end="")
				j=j+1
			i=i+1
	#os.system('clear')
	elif l<=9:
		boy.score=boy.score+50
		l=l+1
		print("Level ",l)
		i=1
		while(i<=4):
			j=1
			while(j<=10000):
				print("Loading Next Level .\r", end="")
				j=j+1
			j=1
			while(j<=10000):
				print("Loading Next Level ..\r", end="")
				j=j+1
			j=1
			while(j<=10000):
				print("Loading Next Level ...\r", end="")
				j=j+1
			j=1
			while(j<=10000):
				print("Loading Next Level    \r",end="")
				j=j+1
			i=i+1
	elif l==10:
		boy.score=boy.score+50
		print(name,"YOU WIN")
		print("CONGRATULATIONS")
		print("YOUR SCORE:",boy.score)
		l=1
		print("Controls:\n\tleft=a\n\tright=d\n\tup=w\n\tdown=s\n\tjumpright=' '\n\tjumpleft=l\n\tquit=q")
		i=1
		while(i<=4):
			j=1
			while(j<=10000):
				print("Loading New Game .\r", end="")
				j=j+1
			j=1
			while(j<=10000):
				print("Loading New Game ..\r", end="")
				j=j+1
			j=1
			while(j<=10000):
				print("Loading New Game ...\r", end="")
				j=j+1
			j=1
			while(j<=10000):
				print("Loading New Game    \r",end="")
				j=j+1
			i=i+1
	#os.system('clear')
	print("\033c")
	boy.row=24
	boy.column=4
	dragon.row=4
	dragon.column=5
	if(l>=2):
		dragonbrother.row=12
		dragonbrother.column=5
	if(l>=3):
		dragonbrotherb.row=20
		dragonbrotherb.column=2
	del coinlist[:]
	del newcoinlist[:]
	del fireballlist[:]
	initialize(board,coinlist,fireballlist)
	initializecoins(board,coinlist,newcoinlist)
def main():
	os.system('clear')
	print("\033c")
	name=raw_input("Enter your name: ")
	print(name,"GoodLuck!!!!!")
	print("Controls:\n\tleft=a\n\tright=d\n\tup=w\n\tdown=s\n\tjumpright=' '\n\tjumpleft=l\n\tquit=q")
	board=[['X' for i in range(0,81)] for j in range(0,26)]
	coinlist=[]
	newcoinlist=[]
	fireballlist=[]
	initialize(board,coinlist,fireballlist)
	initializecoins(board,coinlist,newcoinlist)
	starttime=time.time()
	i=1
	while(i<=4):
		j=1
		while(j<=10000):
			print("Loading .\r", end="")
			j=j+1
		j=1
		while(j<=10000):
			print("Loading ..\r", end="")
			j=j+1
		j=1
		while(j<=10000):
			print("Loading ...\r", end="")
			j=j+1
		j=1
		while(j<=10000):
			print("Loading    \r",end="")
			j=j+1
		i=i+1
	print("\033c")
	speed=5
	k=1
	while(1):
		board=[['X' for i in range(0,81)] for j in range(0,26)]
		initialize(board,coinlist,fireballlist)
		if(k%2==0):
			dragon.dragonupdate(board,coinlist,newcoinlist,fireballlist)
			queen.queenupdate(board,coinlist,newcoinlist,fireballlist)
		if(time.time()-starttime>=k):
			makefireball(board,fireballlist,l)
			k=k+speed
			dragon.dragonupdate(board,coinlist,newcoinlist,fireballlist)
			if(l>=2):
				dragonbrother.dragonupdate(board,coinlist,newcoinlist,fireballlist)
			if(l>=3):
				dragonbrotherb.dragonupdate(board,coinlist,newcoinlist,fireballlist)
			queen.queenupdate(board,coinlist,newcoinlist,fireballlist)
		fireballupdate(board,fireballlist)
		printboard(board,0)
#		initializecoins(board)
		movement=getchar()
		if movement=="a":
			boy.goleft(board,coinlist,newcoinlist,fireballlist)
		elif movement=="d":
			boy.goright(board,coinlist,newcoinlist,fireballlist)
		elif movement=="w":
			chose=boy.goup(board,coinlist,newcoinlist,fireballlist)
		elif movement=="s":
			boy.godown(board,coinlist,newcoinlist,fireballlist)
		elif movement==" ":
			boy.jump(board,coinlist,newcoinlist,fireballlist)
		elif movement=="l":
			boy.jumpleft(board,coinlist,newcoinlist,fireballlist)
		elif movement=="q":
			quit(board,coinlist)
			if(l>=3):
				speed=speed+1
		if (boy.row==queen.row):
			winlose(board,coinlist,newcoinlist,fireballlist,1,name)
			if(l>=3):
				speed=speed+1
		elif(boy.lives==0):
			winlose(board,coinlist,newcoinlist,fireballlist,0,name)
			if(l>=3):
				speed=speed+1
main()
