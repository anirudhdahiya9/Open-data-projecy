from random import *
import os
import time
from Person import *
from donkeykong import *
fl=0
class Donkey(Person):
	def __init__(self,x,y):
		self.__x=x
		self.__y=y
		
	def move(self,sc):
		global fl
		sc.printplspace(self.__x,self.__y,' ')
		time.sleep(0.01)

		if(fl==0):
			if(sc.Iscoinpresent(self.__x,self.__y+1)):
				self.__y+=2
			else:
				self.__y+=1
			if(self.__y>50):
				fl=1
		if(fl==1):
			if(sc.Iscoinpresent(self.__x,self.__y-1)):
				self.__y-=2
			else:
				self.__y-=1
			if(self.__y<2):
				fl=0
		sc.printpl(self.__x,self.__y,'D')
		time.sleep(0.01)
	def getx(self):
		return self.__x
	def gety(self):
		return self.__y