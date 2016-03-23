from random import *
import os
import time
from Person import *
from donkeykong import *

class Player(Person):
	def __init__(self,x,y):
		self.__x=x
		self.__y=y
	def move(self,ch,sc):
		sc.printplspace(self.__x,self.__y,' ')
		time.sleep(0.01)

		
		if(ch=='w' or ch=='W'):
			if(sc.checkstairs(self.__x,self.__y)):
				self.__x-=1
		if(ch=='a' or ch=='A'):
			if(sc.checkdot(self.__x+1,self.__y-1)):

				if(sc.checkwall(self.__x,self.__y-1)):
					self.__y-=1
			else:
				self.__x+=4

				self.__y-=1
		if(ch=='d' or ch=='D'):
			if(sc.checkdot(self.__x+1,self.__y+1)):

				if(sc.checkwall(self.__x,self.__y+1)):
					self.__y+=1
			else:
				self.__x+=4

				self.__y+=1		
		if(ch=='s' or ch=='S'):
			if(sc.checkstairs(self.__x+1,self.__y)):
				self.__x+=1
		if(ord(ch)==32):
			sc.printpl(self.__x-1,self.__y+1,'P')
			sc.printplspace(self.__x,self.__y,' ')
			time.sleep(0.1)
			sc.printpl(self.__x-2,self.__y+2,'P')
			sc.printplspace(self.__x-1,self.__y+1,' ')
			time.sleep(0.1)
			sc.printpl(self.__x-1,self.__y+3,'P')
			sc.printplspace(self.__x-2,self.__y+2,' ')
			time.sleep(0.1)
			sc.printpl(self.__x,self.__y+4,'P')
			sc.printplspace(self.__x-1,self.__y+3,' ')
			self.__y+=4

		sc.printpl(self.__x,self.__y,'P')
		time.sleep(0.01)


	def getx(self):
		return self.__x
	def gety(self):
		return self.__y

