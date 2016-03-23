import donkeykong
from donkeykong import *
import person
import sys
from random import *
class Board():

	def __init__(self,r,c,level):
		self.__row = r
		self.__column = c
		self.__gameboard = []
		self.__gamelevel = level

	def set_board(self):
		for i in range(0,self.__row):
			self.__gameboard.append([])
			for j in range(0,self.__column):
				self.__gameboard[i].append('.')
		self.initialize_board()

	def getrow(self):
		return self.__row

	def getcol(self):
		return self.__column

	def getvalueatboard(self,position):
		return self.__gameboard[position[0]][position[1]]

	def setvalueatboard(self,position,val):
		self.__gameboard[position[0]][position[1]] = val

	def printlist(self):
		sys.stderr.write("\x1b[2J\x1b[H")
		for i in range(0,self.__row):
			for j in range(0,self.__column):
				if self.__gameboard[i][j]=='C':				
					my_print("C ", YELLOW)
				elif self.__gameboard[i][j]=='O':
					my_print("O ",RED)
				elif self.__gameboard[i][j]=='Q':
					my_print("Q ",MAGENTA)
				elif self.__gameboard[i][j]=='X':				
					my_print("X ", CYAN)
				elif self.__gameboard[i][j]=='H':				
					my_print("H ", GREEN)
				elif self.__gameboard[i][j]=='D/H':
					my_print("D ", RED)
				elif self.__gameboard[i][j]=='O/H':
					my_print("O ", RED)
				elif self.__gameboard[i][j]=='P/H':
					my_print("P ", GREEN)
				elif self.__gameboard[i][j]=='C/O':				
					my_print("O ", RED)
				elif self.__gameboard[i][j]=='C/D':
					my_print("D ",RED)
				elif self.__gameboard[i][j]=='P':				
					my_print("P ", GREEN)
				elif self.__gameboard[i][j]=='D':				
					my_print("D ", RED)
				elif self.__gameboard[i][j]=='W':				
					my_print("W ", WHITE)
				else:
					my_print("  ", BLACK)
			print ""

	def __setWalls(self):
		self.__gameboard = [
['X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X'],
['X','.','.','.','.','.','.','.','.','.','.','.','X','_','Q','_','_','_','_','X','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','X'],
['X','.','.','.','.','.','.','.','.','.','.','.','X','X','X','X','H','X','X','X','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','X'],
['X','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','H','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','X'],
['X','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','H','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','X'],
['X','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','H','_','_','_','_','_','_','_','_','_','_','_','_','_','.','.','.','.','.','.','.','.','.','X'],
['X','X','X','X','X','X','X','X','X','X','X','X','H','X','X','X','X','X','X','X','X','X','X','X','X','X','H','X','X','X','.','.','.','.','.','.','.','.','.','X'],
['X','.','.','.','.','.','.','.','.','.','.','.','H','.','.','.','.','.','.','.','.','.','.','.','.','.','H','.','.','.','.','.','.','.','.','.','.','.','.','X'],
['X','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','H','.','.','.','.','.','.','.','.','.','.','.','.','X'],
['X','_','_','_','.','.','.','.','.','.','.','_','H','_','_','_','_','_','_','_','_','_','_','_','_','_','H','_','_','_','_','_','_','_','_','_','_','_','_','X'],
['X','.','.','.','.','.','.','.','.','.','.','X','X','X','X','X','X','X','H','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X'],
['X','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','H','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','X'],
['X','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','H','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','X'],
['X','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','H','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','.','.','.','.','.','X'],
['X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','H','X','X','X','X','X','X','H','X','X','X','X','X','.','.','.','.','.','X'],
['X','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','H','.','.','.','.','.','.','H','.','.','.','.','.','.','.','.','.','.','X'],
['X','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','H','.','.','.','.','.','.','.','.','.','.','X'],
['X','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','_','_','_','_','_','H','_','_','_','_','_','_','H','_','_','_','_','_','_','_','_','_','_','X'],
['X','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','X','X','H','X','X','X','X','X','X','H','X','X','X','X','X','X','X','X','X','X','X','X','X','X'],
['X','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','H','.','.','.','.','.','.','H','.','.','.','.','.','.','.','.','.','.','.','.','.','X'],
['X','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','H','.','.','.','.','.','.','.','.','.','.','.','.','.','X'],
['X','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','H','_','_','_','_','_','_','H','_','_','_','_','_','_','_','_','.','.','.','.','.','X'],
['X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','H','X','X','.','.','.','.','.','X'],
['X','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','H','.','.','.','.','.','.','.','X'],
['X','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','H','.','.','.','.','.','.','.','X'],
['X','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','H','_','_','_','_','_','_','_','X'],
['X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X']]



	def __setCoins(self,count):
		while(count!=0):
			x = randint(0,self.__row-1)
			y = randint(0,self.__column-1)
			while(self.__gameboard[x][y]!='_'):
				x = randint(0,self.__row-1)
				y = randint(0,self.__column-1)
			self.__gameboard[x][y] = 'C'
			count-=1
		
	def initialize_board(self):
		self.__setWalls()
		self.__setCoins(30*(self.__gamelevel))

	def reloadboard(self):
		self.__setBoard()
		self.__setCoins(30*(self.__gamelevel))
