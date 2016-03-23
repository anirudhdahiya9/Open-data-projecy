from random import *
import os
import time
from donkeykong import *
firemv=0
firemv=randint(0,1)

class Fireball:
	def __init__(self,x,y):
		self.__x=x
		self.__y=y
	
	def move(self,sc):
		global firemv
		sc.printplspace(self.__x,self.__y,' ')
		time.sleep(0.01)
		# firemv=randint(0,1)
		if(sc.checkdot(self.__x+1,self.__y+1)):
			if(firemv==1):
				if(sc.checkwall(self.__x,self.__y+1)):
					if(sc.Iscoinpresent(self.__x,self.__y+1)):
						self.__y+=2
					else:
						self.__y+=1
				else:
					firemv=0
					self.__y-=1
			else:
				if(sc.checkwall(self.__x,self.__y-1)):
					if(sc.Iscoinpresent(self.__x,self.__y-1)):
						self.__y-=2
					else:
						self.__y-=1
				else:
					firemv=1
					self.__y+=1

		else:
			self.__x+=4
			if(randint(0,1)==1):
				if(sc.Iscoinpresent(self.__x,self.__y+1)):
					self.__y+=2
				else:
					self.__y+=1
				firemv=1
			else:
				if(sc.Iscoinpresent(self.__x,self.__y+1)):
					self.__y-=2
				else:
					self.__y-=1
				firemv=0
		sc.printpl(self.__x,self.__y,'O')
		time.sleep(0.01)
	
	def getx(self):
		return self.__x
	
	def gety(self):
		return self.__y
