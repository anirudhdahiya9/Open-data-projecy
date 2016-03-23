from random import *
import os

class Person:
	"""Person Class"""
    
	def __init__(self,x=0,y=0):
		self.__x=x
		self.__y=y

	def move(self,ch,sc):
		sc.printpm(self.__x,self.__y,' ')
		if(ch=='w' or ch=='W'):
			if(sc.checkWall(self.__x-1,self.__y)):
				self.__x-=1
		elif(ch=='s' or ch=='S'):
			if(sc.checkWall(self.__x+1,self.__y)):
				self.__x+=1
		elif(ch=='a' or ch=='A'):
			if(sc.checkWall(self.__x,self.__y-1)):
				self.__y-=1
		elif(ch=='d' or ch=='D'):
			if(sc.checkWall(self.__x,self.__y+1)):
				self.__y+=1

		sc.printpm(self.__x,self.__y,'P')
