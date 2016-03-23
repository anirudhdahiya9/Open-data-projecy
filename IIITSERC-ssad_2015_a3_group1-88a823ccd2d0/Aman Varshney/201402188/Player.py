from random import *
import os
from Person import *
from Screen import *

flag=0
left=0

class Player(Person):
	"""Player Class"""
    
	def __init__(self,x,y):
		self.__x=x
		self.__y=y
	def move(self,ch,sc):
		from time import sleep
		global flag
		global left
		if(flag==1):
			sc.printpm(self.__x,self.__y,'H')
			flag=0
			#count=count-1
			#if(count<=0):
			#flag=0
		else:
			sc.printpm(self.__x,self.__y,' ')

		#if count<=0:
		#	flag=0

		if(ch=='w' or ch=='W'):
			if(sc.checkWall(self.__x-1,self.__y)):
				self.__x-=1
			if(sc._a[self.__x][self.__y]=='H'):
				flag=1
				#count+=1
		elif(ch=='s' or ch=='S'):
			if(sc.checkWall(self.__x+1,self.__y)):
				self.__x+=1
			if(sc._a[self.__x][self.__y]=='H'):
				flag=1
				#count+=1

		elif(ch=='a' or ch=='A'):
			left=1
			if(sc.checkWall(self.__x,self.__y-1)):
				self.__y-=1
			if(sc._a[self.__x][self.__y]=='H'):
				flag=1
				#count+=1

		elif(ch=='d' or ch=='D'):
			left=0

			if(sc.checkWall(self.__x,self.__y+1)):
				self.__y+=1
			if(sc._a[self.__x][self.__y]=='H'):
				flag=1
				#count+=1
		elif (ch==' '):
			if(left==0):
				os.system("clear")
				w1=sc._a[self.__x][self.__y]
				w2=sc._a[self.__x-1][self.__y+1]
				w3=	sc._a[self.__x-2][self.__y+2]
				w4=sc._a[self.__x-1][self.__y+3]
				w5=sc._a[self.__x][self.__y+4]
				if(w5=='H'):
					flag=1

				sc.printpm(self.__x-1,self.__y+1,'P')
				sc.printpm(self.__x,self.__y,w1)
				
				sc.printScreen()
				sleep(0.1)
				sc.printpm(self.__x-1,self.__y+1,' ')
				os.system("clear")


				sc.printpm(self.__x-2,self.__y+2,'P')
				sc.printpm(self.__x-1,self.__y+1,w2)
				sc.printScreen()
				sleep(0.1)
				sc.printpm(self.__x-2,self.__y+2,' ')
				os.system("clear")



				sc.printpm(self.__x-1,self.__y+3,'P')
				sc.printpm(self.__x-2,self.__y+2,w3)
		
				sc.printScreen()
				sleep(0.1)
				sc.printpm(self.__x-1,self.__y+3,' ')
				os.system("clear")



				sc.printpm(self.__x,self.__y+4,'P')
				sc.printpm(self.__x-1,self.__y+3,w4)


				sc.printScreen()
				sleep(0.1)
				self.__y=self.__y+4



			if(left==1):
				os.system("clear")
				w1=sc._a[self.__x][self.__y]
				w2=sc._a[self.__x-1][self.__y-1]
				w3=	sc._a[self.__x-2][self.__y-2]
				w4=sc._a[self.__x-1][self.__y-3]
				w5=sc._a[self.__x][self.__y-4]
				if(w5=='H'):
					flag=1

				sc.printpm(self.__x-1,self.__y-1,'P')
				sc.printpm(self.__x,self.__y,w1)
				
				sc.printScreen()
				sleep(0.1)
				sc.printpm(self.__x-1,self.__y-1,' ')
				os.system("clear")


				sc.printpm(self.__x-2,self.__y-2,'P')
				sc.printpm(self.__x-1,self.__y-1,w2)
				sc.printScreen()
				sleep(0.1)
				sc.printpm(self.__x-2,self.__y-2,' ')
				os.system("clear")



				sc.printpm(self.__x-1,self.__y-3,'P')
				sc.printpm(self.__x-2,self.__y-2,w3)
		
				sc.printScreen()
				sleep(0.1)
				sc.printpm(self.__x-1,self.__y-3,' ')
				os.system("clear")



				sc.printpm(self.__x,self.__y-4,'P')
				sc.printpm(self.__x-1,self.__y-3,w4)


				sc.printScreen()
				sleep(0.1)
				self.__y=self.__y-4



		sc.printpm(self.__x,self.__y,'P')

	def getX(self):
		return self.__x

	def getY(self):
		return self.__y
