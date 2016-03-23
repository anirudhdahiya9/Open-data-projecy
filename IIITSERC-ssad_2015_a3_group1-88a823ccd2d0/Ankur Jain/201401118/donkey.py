import random
from random import randint 
from board import Board
from random import randint
class Donkey:
	def __init__(self):
		self.posx=5
		self.posy=4
		self.mv=randint(0,1)
	def move(self,curry,temp):
		if self.mv==0:
			if self.posy!=1:
				if self.posy!=curry:
					Board.board[self.posx][self.posy]=" "
				elif self.posy==curry:
					Board.board[self.posx][self.posy]=temp
				self.posy-=1
				Board.board[self.posx][self.posy]="D"
			elif self.posy==1:
				self.mv=1
		elif self.mv==1:
			if self.posy!=49:
				if self.posy!=curry:
					Board.board[self.posx][self.posy]=" "
				elif self.posy==curry:
					Board.board[self.posx][self.posy]=temp
				self.posy+=1
				Board.board[self.posx][self.posy]="D"
			elif self.posy==49:
				self.mv=0
class FireBall(Donkey):
	def __init__(self):
		Donkey.__init__(self)
		self.ball = []
	def throw(self):
		if self.mv==0:
			self.ball.append([self.posx,self.posy+1,1,Board.board[self.posx][self.posy+1]])
			Board.board[self.posx][self.posy+1]="O"		
		elif self.mv==1:
			self.ball.append([self.posx,self.posy-1,0,Board.board[self.posx][self.posy-1]])
			Board.board[self.posx][self.posy-1]="O"
	def move(self):
		for i in range(len(self.ball)):
			if self.ball[i][2]==0:
				Board.board[self.ball[i][0]][self.ball[i][1]]=self.ball[i][3]
				if self.ball[i][3]=="O" or self.ball[i][3]=="D":
					Board.board[self.ball[i][0]][self.ball[i][1]]=" "
				self.ball[i][1]-=1
				if Board.board[self.ball[i][0]][self.ball[i][1]]=="X":
					self.ball[i][1]+=1
					self.ball[i][2]=1
				self.ball[i][3]=Board.board[self.ball[i][0]][self.ball[i][1]]
				Board.board[self.ball[i][0]][self.ball[i][1]]="O"
				if Board.board[self.ball[i][0]+1][self.ball[i][1]]==" ":
					Board.board[self.ball[i][0]][self.ball[i][1]]=" "
					self.fall(i)
			elif self.ball[i][2]==1:
				Board.board[self.ball[i][0]][self.ball[i][1]]=self.ball[i][3]
				if self.ball[i][3]=="O" or self.ball[i][3]=="D":
					Board.board[self.ball[i][0]][self.ball[i][1]]=" "
				self.ball[i][1]+=1
				if Board.board[self.ball[i][0]][self.ball[i][1]]=="X":
					self.ball[i][1]-=1
					self.ball[i][2]=0
				self.ball[i][3]=Board.board[self.ball[i][0]][self.ball[i][1]]
				Board.board[self.ball[i][0]][self.ball[i][1]]="O"
				if Board.board[self.ball[i][0]+1][self.ball[i][1]]==" ":
					Board.board[self.ball[i][0]][self.ball[i][1]]=" "
					self.fall(i)
		for i in range(len(self.ball)-1):
			if self.ball[i][0]==28 and self.ball[i][1]==3:
				Board.board[28][3]=" "
				self.ball.remove(self.ball[i])
	def fall(self,i):
		while Board.board[self.ball[i][0]+1][self.ball[i][1]]!="X":
			self.ball[i][0]+=1
		self.ball[i][3]=Board.board[self.ball[i][0]][self.ball[i][1]]
		Board.board[self.ball[i][0]][self.ball[i][1]]="O"
		self.ball[i][2]=random.randint(0,1)
