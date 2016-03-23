from random import *
import os
from Person import *
from Player import *
class Screen:
	"""Class to create Screen and Other Stuff"""
	def __init__(self):
		#print "Aman"
		self.__score=0
		self.__flag1=0
		self._a=[['X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X'],

['X',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','X'],

['X',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','X',' ',' ','Q',' ',' ',' ','X',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','X'],

['X',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','X','X','X','X','X','H','X','X',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','X'],	
	
['X',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','H',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','X'],

['X',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','H',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','X'],

['X','X','X','X','X','X','X','X','X','X','X','X','H','X','X','X','X','X','X','X','X','X','X','X','X','X','H','X','X','X','X','X','X','X','X',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','X'],

['X',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','H',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','H',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','X'],

['X',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','H',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','X'],

['X',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','H',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','H',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','X'],
	
['X',' ',' ',' ',' ',' ',' ',' ',' ',' ','X','X','X','X','X','X','X','X','X','X','H','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X'],

['X',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','H',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','X'],

['X',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','H',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','X'],

['X',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','H',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','X'],

['X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','H','X','X','X','X','X','H','X','X','X','X','X','X','X',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','X'],

['X',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','H',' ',' ',' ',' ',' ','H',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','X'],

['X',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','H',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','X'],

['X',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','H',' ',' ',' ',' ',' ','H',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','X'],

['X',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','X','X','X','X','X','X','X','H','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X'],

['X',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','H',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','X'],

['X',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','H',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','X'],

['X',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','H',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','X'],

['X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','H','X','X','X','X','X','X',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','X'],

['X',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','H',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','X'],

['X',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','H',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','X'],

['X',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','H',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','X'],

['X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X']]
    
	"""Prints the Screen"""	
	def printScreen(self):
 		#print "Aman"

		for i in range(0,27):
 			for j in range(0,55):
				if(self._a[i][j]=='G'):
					print ('\033[1m'+'\033[91m' + 'G' + '\033[0m'),
				elif(self._a[i][j]=='P'):
					print ('\033[1m'+'\033[92m' + 'P' + '\033[0m'),
				elif(self._a[i][j]=='X'):
					print ('\033[1m'+'\033[95m' + 'X' + '\033[0m'),
				elif(self._a[i][j]=='C'):
					print ('\033[1m'+'\033[93m' + 'C' + '\033[0m'),
				else:	
					print self._a[i][j],
			print ""


	"""Places P on Screen"""
	def printpm(self,x,y,ch):
		if(self._a[x][y]=='C'):
			self.collectCoin(x,y)

		self._a[x][y]=ch
	""" check of H """
	def ladder(self, x,y,ch):
		global flag
		global count






	"""Collection of  Coin"""
	def collectCoin(self,x,y):
		self.__score+=1

	"""Check player can move or not"""
	def checkWall(self,x,y):
		global flag

		flag1=0
		if (self._a[x][y]=='H'):
			flag=1
		if((x==8 and y==12) or (x==16 and y==29)):
			return False
		elif (self._a[x][y]=='Q'):
			self.__flag1=1
		elif(self._a[x][y]=='X'):
			return False
		elif((self._a[x+1][y]!='X' ) and self._a[x+1][y]!='H'):
			return False
		else:
			return True



	"""Generate Coins randomly """
	def genCoins(self):
		count=10
		i=0
		j=0

		while(count!=0):
			while (self._a[i][j]!=' '):
				i=5
				j=randint(1,34)
				if(j==18):
					j=17
			if(self._a[i][j]!='C'):
				self._a[i][j]='C'
				count-=1

			while (self._a[i][j]!=' '):
				i=9
				j=randint(10,53)
				if(j==26):
					j=15
			if(self._a[i][j]!='C'):
				self._a[i][j]='C'
				count-=1

		count=10
		i=0
		j=0
		while(count!=0):
			while (self._a[i][j]!=' '):
				i=13
				j=randint(1,42)
				if(j==20):
					j=25
			if(self._a[i][j]!='C'):
				self._a[i][j]='C'
				count-=1

			while (self._a[i][j]!=' '):
				i=17
				j=randint(16,53)
				if(j==35):
					j=19
			if(self._a[i][j]!='C'):
				self._a[i][j]='C'
				count-=1
		count=10
		i=0
		j=0
		while(count!=0):
			while (self._a[i][j]!=' '):
				i=21
				j=randint(1,39)
				if(j==23):
					j=26
			if(self._a[i][j]!='C'):
				self._a[i][j]='C'
				count-=1

			while (self._a[i][j]!=' '):
				i=25
				j=randint(2,53)
				if(j==33):
					j=15
			if(self._a[i][j]!='C'):
				self._a[i][j]='C'
				count-=1


	"""Get Score"""
	def getScore(self):
		return (self.__score)

	""" Flag of Q""" 
	def getflag1(self):
		return self.__flag1
