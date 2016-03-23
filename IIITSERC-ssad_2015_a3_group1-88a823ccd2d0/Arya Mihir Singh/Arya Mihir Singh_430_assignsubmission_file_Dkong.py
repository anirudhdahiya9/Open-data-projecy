from random import *
import os,time

def getchar():
	"""Returns a single character from standard input"""
	import tty, termios, sys
	fd = sys.stdin.fileno()
	old_settings = termios.tcgetattr(fd)
	try:
		tty.setraw(sys.stdin.fileno())
		ch = sys.stdin.read(1)
	finally:
		termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
	return ch

class Person:
	    
	def __init__(self,x,y):
		self.__x=x
		self.__y=y
	
	def gX(self):
		return self.__x
		
	def gY(self):
		return self.__y

	def move(self,ch,sc):
		sc.printp(self.__x,self.__y,'.')
		#fl=0
		if(ch=='D' or ch=='d' and self._a[x+1][y+1]=='X'):
			if(self.__fl==1):
				self.__fl=0
				sc.printh(self.__x,self.__y-1,'H')
		
			if(sc.checkLadder(self.__x,self.__y+1)):
				self.__fl=1
				
			if(sc.checkWall(self.__x,self.__y+1)):
				self.__y+=1
				sc.printp(self.__x,self.__y,'P')
		elif(ch=='D' or ch=='d' and self._a[x+1][y+1]!='X'):
			sc.printp(self.__x,self.__y,'P')
		if(ch=='A' or ch=='a' and not(sc.checkWall(self.__x+1,self.__y-1))):
			if(self.__fl==1):
				self.__fl=0
				sc.printh(self.__x,self.__y+1,'H')
		
			if(sc.checkLadder(self.__x,self.__y-1)):
				self.__fl=1
				
			if(sc.checkWall(self.__x,self.__y-1)):
				self.__y-=1
				sc.printp(self.__x,self.__y,'P')
		elif(ch=='A' or ch=='a' and not(sc.checkWall(self.__x+1,self.__y-1))):
			sc.printp(self.__x,self.__y,'P')
		
class Player(Person):
	"""Player Class"""
    
	def __init__(self,x,y):
		Person.__init__(self,x,y)
		self.__fl=0
		self.__flr=0

	def move(self,ch,sc):
		if(self.__fl==0):
			sc.printp(self._Person__x,self._Person__y,'.')
		else:
			sc.printh(self._Person__x,self._Person__y,'H')
			self.__fl=0
		#fl=0
		if((ch=='D' or ch=='d') and (not(sc.checkWall(self._Person__x+1,self._Person__y+1)) or sc.checkLadder(self._Person__x+1,self._Person__y+1))):
			self.__flr=1
			if(self.__fl==1):
				self.__fl=0
				sc.printh(self._Person__x,self._Person__y-1,'H')
		
			if(sc.checkLadder(self._Person__x,self._Person__y+1)):
				self.__fl=1
				
			if(sc.checkWall(self._Person__x,self._Person__y+1)):
				self._Person__y+=1
				sc.printp(self._Person__x,self._Person__y,'P')
			elif(not(sc.checkWall(self._Person__x,self._Person__y+1))):
				sc.printp(self._Person__x,self._Person__y,'P')
			
		elif((ch=='D' or ch=='d') and ((sc.checkWall(self._Person__x+1,self._Person__y+1)) or not(sc.checkLadder(self._Person__x+1,self._Person__y+1)))):
			self.__flr=1
			sc.printp(self._Person__x,self._Person__y,'P')
			self.__fl=1
			#if(self.__fl==1):
			#	self.__fl=0
			
			#elif(sc.checkWall(self.__x,self.__y+1)):
			#	self.__y+=1
			#	sc.printp(self.__x,self.__y,'P')
		elif((ch=='A' or ch=='a') and (not(sc.checkWall(self._Person__x+1,self._Person__y-1)) or sc.checkLadder(self._Person__x+1,self._Person__y-1))):
			self.__flr=0
			if(self.__fl==1):
				self.__fl=0
				sc.printh(self._Person__x,self._Person__y+1,'H')
		
			if(sc.checkLadder(self._Person__x,self._Person__y-1)):
				self.__fl=1
				
			if(sc.checkWall(self._Person__x,self._Person__y-1)):
				self._Person__y-=1
				sc.printp(self._Person__x,self._Person__y,'P')
				
			elif(not(sc.checkWall(self._Person__x,self._Person__y-1))):
				sc.printp(self._Person__x,self._Person__y,'P')
				
		elif(ch=='A' or ch=='a' and ((sc.checkWall(self._Person__x+1,self._Person__y-1)) or not(sc.checkLadder(self._Person__x+1,self._Person__y-1)))):
			self.__flr=0
			sc.printp(self._Person__x,self._Person__y,'P')
			self.__fl=1
			
		elif(ch=='w' or ch=='W'):
			if(sc.checkLadder(self._Person__x-1,self._Person__y)):
				self.__fl=1
				self._Person__x-=1
				sc.printp(self._Person__x,self._Person__y,'P')
			elif((not(sc.checkWall(self._Person__x,self._Person__y-1)) and not(sc.checkWall(self._Person__x,self._Person__y+1)))):
				self._Person__x-=1
				sc.printp(self._Person__x,self._Person__y,'P')
			else:
				sc.printp(self._Person__x,self._Person__y,'P')
			#if(sc.checkWall(self.__x-1,self.__y)):
			#	
			#	
		elif(ch=='s' or ch=='S'):
			if(sc.checkLadder(self._Person__x+1,self._Person__y)):
				self.__fl=1
				self._Person__x+=1	
				sc.printp(self._Person__x,self._Person__y,'P')
			else:
				sc.printp(self._Person__x,self._Person__y,'P')
			#if(sc.checkWall(self.__x+1,self.__y)):
			
			#if(self.__):
			#	sc.printp(self.__x,self.__y-1,'H')
			
		#elif((ch=='w' or ch=='W') and (fl==1) and (self.__x-1=='H')):
			#if(sc.checkWall(self.__x-1,self.__y)):
			
			#self.__x-=1
			#self._a[x+1][y]='H'
			#print self._a[x-1][y]
			
		#elif((ch=='s' or ch=='S') and (fl==1) and (self.__x+1=='H')):
			#if(sc.checkWall(self.__x+1,self.__y)):
		#	self.__x+=1
		#	self._a[x-1][y]='H'
			#print self._a[x-1][y]
		elif(ch==' ' and self.__flr==1):
			if(sc.checkWall(self._Person__x,self._Person__y+5) and self._Person__y+5 < 76):
				self._Person__x-=1
				self._Person__y+=1
				sc.printp(self._Person__x,self._Person__y,'P')
				sc.printp(self._Person__x+1,self._Person__y-1,'.')
				time.sleep(0.2)
				os.system("clear")
				self._Person__x-=1
				self._Person__y+=1
				sc.printp(self._Person__x,self._Person__y,'P')
				sc.printp(self._Person__x+1,self._Person__y-1,'.')
				time.sleep(0.2)
				os.system("clear")
				self._Person__x+=1
				self._Person__y+=1
				sc.printp(self._Person__x,self._Person__y,'P')
				sc.printp(self._Person__x-1,self._Person__y-1,'.')
				time.sleep(0.2)
				os.system("clear")
				self._Person__x+=1
				self._Person__y+=1
				sc.printp(self._Person__x,self._Person__y,'P')
				sc.printp(self._Person__x-1,self._Person__y-1,'.')
				time.sleep(0.2)
				os.system("clear")
			elif(sc.checkWall(self._Person__x,self._Person__y+4) and self._Person__y+4 < 76):
				self._Person__x-=1
				self._Person__y+=1
				sc.printp(self._Person__x,self._Person__y,'P')
				sc.printp(self._Person__x+1,self._Person__y-1,'.')
				time.sleep(0.2)
				os.system("clear")
				self._Person__x-=1
				self._Person__y+=1
				sc.printp(self._Person__x,self._Person__y,'P')
				sc.printp(self._Person__x+1,self._Person__y-1,'.')
				time.sleep(0.2)
				os.system("clear")
				self._Person__x+=1
				self._Person__y+=1
				sc.printp(self._Person__x,self._Person__y,'P')
				sc.printp(self._Person__x-1,self._Person__y-1,'.')
				time.sleep(0.2)
				os.system("clear")
				self._Person__x+=1
				sc.printp(self._Person__x,self._Person__y,'P')
				sc.printp(self._Person__x-1,self._Person__y,'.')
				time.sleep(0.2)
				os.system("clear")				
			elif(sc.checkWall(self._Person__x,self._Person__y+3) and self._Person__y+3 < 76):
				self._Person__x-=1
				self._Person__y+=1
				sc.printp(self._Person__x,self._Person__y,'P')
				sc.printp(self._Person__x+1,self._Person__y-1,'.')
				time.sleep(0.2)
				os.system("clear")
				self._Person__x-=1
				self._Person__y+=1
				sc.printp(self._Person__x,self._Person__y,'P')
				sc.printp(self._Person__x+1,self._Person__y-1,'.')	
				time.sleep(0.2)
				os.system("clear")
				self._Person__x+=1
				sc.printp(self._Person__x,self._Person__y,'P')
				sc.printp(self._Person__x-1,self._Person__y,'.')
				time.sleep(0.2)
				os.system("clear")
				self._Person__x+=1
				sc.printp(self._Person__x,self._Person__y,'P')
				sc.printp(self._Person__x-1,self._Person__y,'.')
				time.sleep(0.2)
				os.system("clear")				
			elif(sc.checkWall(self._Person__x,self._Person__y+2) and self._Person__y+2 < 76):
				self._Person__x-=1
				self._Person__y+=1
				sc.printp(self._Person__x,self._Person__y,'P')
				sc.printp(self._Person__x+1,self._Person__y-1,'.')
				time.sleep(0.2)
				os.system("clear")
				self._Person__x+=1
				sc.printp(self._Person__x,self._Person__y,'P')
				sc.printp(self._Person__x-1,self._Person__y,'.')
				time.sleep(0.2)
				os.system("clear")
			elif(sc.checkWall(self._Person__x,self._Person__y+1) and self._Person__y+1 < 76):
				sc.printp(self._Person__x,self._Person__y,'P')	
				
		elif(ch==' ' and self.__flr==0):
			if(sc.checkWall(self._Person__x,self._Person__y-5) and self._Person__y-5 > 0):
				self._Person__x-=1
				self._Person__y-=1
				sc.printp(self._Person__x,self._Person__y,'P')
				sc.printp(self._Person__x+1,self._Person__y+1,'.')
				time.sleep(0.2)
				os.system("clear")
				self._Person__x-=1
				self._Person__y-=1
				sc.printp(self._Person__x,self._Person__y,'P')
				sc.printp(self._Person__x+1,self._Person__y+1,'.')
				time.sleep(0.2)
				os.system("clear")
				self._Person__x+=1
				self._Person__y-=1
				sc.printp(self._Person__x,self._Person__y,'P')
				sc.printp(self._Person__x-1,self._Person__y+1,'.')
				time.sleep(0.2)
				os.system("clear")
				self._Person__x+=1
				self._Person__y-=1
				sc.printp(self._Person__x,self._Person__y,'P')
				sc.printp(self._Person__x-1,self._Person__y+1,'.')
				time.sleep(0.2)
				os.system("clear")
			elif(sc.checkWall(self._Person__x,self._Person__y-4) and self._Person__y-4 < 0):
				self._Person__x-=1
				self._Person__y-=1
				sc.printp(self._Person__x,self._Person__y,'P')
				sc.printp(self._Person__x+1,self._Person__y+1,'.')
				time.sleep(0.2)
				os.system("clear")
				self._Person__x-=1
				self._Person__y-=1
				sc.printp(self._Person__x,self._Person__y,'P')
				sc.printp(self._Person__x+1,self._Person__y+1,'.')
				time.sleep(0.2)
				os.system("clear")
				self._Person__x+=1
				self._Person__y-=1
				sc.printp(self._Person__x,self._Person__y,'P')
				sc.printp(self._Person__x-1,self._Person__y+1,'.')
				time.sleep(0.2)
				os.system("clear")
				self._Person__x+=1
				sc.printp(self._Person__x,self._Person__y,'P')
				sc.printp(self._Person__x-1,self._Person__y,'.')
				time.sleep(0.2)
				os.system("clear")				
			elif(sc.checkWall(self._Person__x,self._Person__y+3) and self._Person__y+3 < 0):
				self._Person__x-=1
				self._Person__y-=1
				sc.printp(self._Person__x,self._Person__y,'P')
				sc.printp(self._Person__x+1,self._Person__y+1,'.')
				time.sleep(0.2)
				os.system("clear")
				self._Person__x-=1
				self._Person__y-=1
				sc.printp(self._Person__x,self._Person__y,'P')
				sc.printp(self._Person__x+1,self._Person__y+1,'.')
				time.sleep(0.2)
				os.system("clear")
				self._Person__x+=1
				sc.printp(self_Person.__x,self._Person__y,'P')
				sc.printp(self._Person__x-1,self._Person__y,'.')
				time.sleep(0.2)
				os.system("clear")
				self.__x+=1
				sc.printp(self._Person__x,self._Person__y,'P')
				sc.printp(self._Person__x-1,self._Person__y,'.')
				time.sleep(0.2)
				os.system("clear")				
			elif(sc.checkWall(self._Person__x,self._Person__y-2) and self._Person__y-2 < 0):
				self._Person__x-=1
				self._Person__y-=1
				sc.printp(self._Person__x,self._Person__y,'P')
				sc.printp(self._Person__x+1,self._Person__y+1,'.')
				time.sleep(0.2)
				os.system("clear")
				self._Person__x+=1
				sc.printp(self._Person__x,self._Person__y,'P')
				sc.printp(self._Person__x-1,self._Person__y,'.')
				time.sleep(0.2)
				os.system("clear")
			elif(sc.checkWall(self._Person__x,self._Person__y-1) and self._Person__y-1 < 0):
				sc.printp(self._Person__x,self._Person__y,'P')
			
			
	def getX(self):
		return self._Person__x

	def getY(self):
		return self._Person__y

		
class Donkey(Person):
	def __init__(self,x,y):
		self.__x=x
		self.__y=y
		self.__counter=1
		self.__right=1
		
	def getRightFlag(self):
		return self.__right
		
	def move(self,ch,sc):
		sc.printp(self.__x,self.__y,'.')
		
		if(ch=='a' or ch=='A' or ch=='w' or ch=='W' or ch=='s' or ch=='S' or ch=='d' or ch=='D' or ch==' '):
			
			if((self.__counter)%14==0 and self.__right==1):
				self.__y-=1
				self.__right=0
				self.__counter+=1
				sc.printd(self.__x,self.__y,'D')
			elif((self.__counter)%14==0 and self.__right==0):
				self.__y+=1
				self.__right=1
				self.__counter+=1
				sc.printd(self.__x,self.__y,'D')
				
			elif((self.__counter)%14!=0 and self.__right==1):
				self.__y+=1
				self.__counter+=1
				sc.printd(self.__x,self.__y,'D')
			elif((self.__counter)%14!=0 and self.__right==0):
				self.__y-=1
				sc.printd(self.__x,self.__y,'D')
				self.__counter+=1
				
	def getX(self):
		return self.__x

	def getY(self):
		return self.__y

class fireBall(Person):
	def __init__(self,x,y):
		self.__x=x
		self.__y=y
		self.__flr=1
		self.__flc=0
#		self.__floor=1	
	def move(self,sc,ch):
		#if(not(sc.checkLadder(self.__x,self.__y)))
		#if(flc==1):
		#	if(flr==1):
		if(self.__flr==1 and self.__flc==1):
			sc.printf(self.__x,self.__y-1,'C')
				
		if(self.__flr==0 and self.__flc==1):
			sc.printf(self.__x,self.__y+1,'C')
			
		sc.printp(self.__x,self.__y-1,'.')
		#flc=0	
		if(ch=='a' or ch=='A' or ch=='w' or ch=='W' or ch=='s' or ch=='S' or ch=='d' or ch=='D' or ch==' '):
			if((not(sc.checkWall(self.__x+1,self.__y+1)) or sc.checkLadder(self.__x+1,self.__y+1)) and self.__flr==1):
				self.__y+=1
				sc.printf(self.__x,self.__y,'O')
			if(sc._a[self.__x][self.__y+1]=='C' and self.__flr==1):
				self__flc=1
				self.__y+=1
				sc.printf(self.__x,self.__y,'O')	
			if((not(sc.checkWall(self.__x+1,self.__y-1)) or sc.checkLadder(self.__x+1,self.__y-1)) and self.__flr==0):
				#self.__flr=0
				self.__y-=1
				sc.printf(self.__x,self.__y,'O')
			if(sc._a[self.__x][self.__y-1]=='C' and self.__flr==0):
				self__flc=1
				#self.__flr=1
				self.__y-=1
				sc.printf(self.__x,self.__y,'O')
				
			
			
			if((sc._a[self.__x+1][self.__y+1]=='.')):
				self.__flr=0
				self.__y+=1
				sc.printf(self.__x,self.__y,'O')
				time.sleep(0.2)
				self.__x+=1
				sc.printf(self.__x,self.__y,'O')
				time.sleep(0.2)
				self.__x+=1
				sc.printf(self.__x,self.__y,'O')
				time.sleep(0.2)
				self.__x+=1
				sc.printf(self.__x,self.__y,'O')
				time.sleep(0.2)
				self.__x+=1
				sc.printf(self.__x,self.__y,'O')
				time.sleep(0.2)	
				
			if(sc._a[self.__x+1][self.__y-1]=='.'):
				self.__flr=1
				self.__y-=1
				sc.printf(self.__x,self.__y,'O')
				time.sleep(0.2)
				self.__x+=1
				sc.printf(self.__x,self.__y,'O')
				time.sleep(0.2)
				self.__x+=1
				sc.printf(self.__x,self.__y,'O')
				time.sleep(0.2)
				self.__x+=1
				sc.printf(self.__x,self.__y,'O')
				time.sleep(0.2)
				self.__x+=1
				sc.printf(self.__x,self.__y,'O')
				time.sleep(0.2)	
			#elif()
			

		
	
				
	
class Screen:
	def __init__(self):
		self.__score=0
		self._a=[['X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X'],
				 ['X','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','X','.','.','.','Q','.','.','.','.','.','X','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','X'],
				 ['X','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','X','X','X','X','X','X','X','X','H','X','X','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','X'],
				 ['X','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','H','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','X'],
				 ['X','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','H','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','X'],
				 ['X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','H','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','H','X','X','X','X','X','X','X','.','.','.','.','.','.','.','.','.','.','.','.','.','.','X'],
				 ['X','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','H','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','H','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','X'],
				 ['X','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','H','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','X'],
				 ['X','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','H','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','H','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','X'],
				 ['X','.','.','.','.','.','.','.','.','.','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','H','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X'],
				 ['X','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','H','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','X'],
				 ['X','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','H','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','X'],
				 ['X','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','H','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','X'],
				 ['X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','H','X','X','X','X','X','X','X','X','X','H','X','X','X','X','X','X','.','.','.','.','.','.','.','X'],
				 ['X','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','H','.','.','.','.','.','.','.','.','.','H','.','.','.','.','.','.','.','.','.','.','.','.','.','X'],
				 ['X','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','H','.','.','.','.','.','.','.','.','.','.','.','.','.','X'],
				 ['X','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','H','.','.','.','.','.','.','.','.','.','H','.','.','.','.','.','.','.','.','.','.','.','.','.','X'],
				 ['X','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','H','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','H','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X'],
				 ['X','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','H','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','H','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','X'],
				 ['X','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','H','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','X'],
				 ['X','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','H','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','H','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','X'],
				 ['X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','H','X','X','X','.','.','.','.','.','.','.','.','.','.','X'],
				 ['X','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','H','.','.','.','.','.','.','.','.','.','.','.','.','.','X'],
				 ['X','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','H','.','.','.','.','.','.','.','.','.','.','.','.','.','X'],
				 ['X','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','H','.','.','.','.','.','.','.','.','.','.','.','.','.','X'],
				 ['X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X']]
				 
	def printScreen(self):
		for i in range(0,26):
			S=""
			for j in range(0,76):
				if(self._a[i][j]=='X'):
					S+=('\033[1m'+'\033[91m' + 'X' + '\033[0m')
				elif(self._a[i][j]=='P'):
					S+=('\033[1m'+'\033[92m' + 'P' + '\033[0m')
				elif(self._a[i][j]=='O'):
					S+=('\033[1m'+'\033[95m' + 'O' + '\033[0m')
				elif(self._a[i][j]=='D'):
					S+=('\033[1m'+'\033[94m' + 'D' + '\033[0m')
				elif(self._a[i][j]=='H'):
					S+=('\033[1m'+'\033[96m' + 'H' + '\033[0m')	
				elif(self._a[i][j]=='C'):
					S+=('\033[1m'+'\033[93m' + 'C' + '\033[0m')
				elif(self._a[i][j]=='Q'):
					S+=('\033[1m'+'\033[97m' + 'Q' + '\033[0m')
				else:	
					S+=self._a[i][j]
			print S

	def printp(self,x,y,ch):
		if(self._a[x][y]=='C'):
			self.collectCoin(x,y)
		#elif(self._a[x][y]=='H'):
		self._a[x][y]=ch
	def printh(self,x,y,ch):
		self._a[x][y]=ch
	def printd(self,x,y,ch):
		self._a[x][y]=ch
	def printf(self,x,y,ch):
		self._a[x][y]=ch
	
	#def printh(self,x,y,ch):
	#	if(self._a[x][y]=='H'):

	"""Increments Score everytime Player gets a Coin"""
	def collectCoin(self,x,y):
		self.__score+=5
		if(self.__score!=0 and (self.__score%180)==0):
			self.genCoins()

	"""Checks if the move made by Player collides with a wall"""
	def checkWall(self,x,y):
		if(self._a[x][y]=='X'):
			return False
		else:
			return True
			
	def checkLadder(self,x,y):
		if(self._a[x][y]=='H'):
			return True
		else:
			return False
			
	def genCoins(self):
		'''Generate Coins randomly on the board'''
		count=6
		i=4
		j=0
		while(count!=0):
			while(self._a[i][j]!='.'):
				'''i=randint(1,25)'''
				j=randint(20,50)
			self._a[i][j]='C'
			count-=1
		count=6
		i=8
		j=0
		while(count!=0):
			while(self._a[i][j]!='.'):
				'''i=randint(1,25)'''
				j=randint(11,70)
			self._a[i][j]='C'
			count-=1
		count=6
		i=12
		j=0
		while(count!=0):
			while(self._a[i][j]!='.'):
				'''i=randint(1,25)'''
				j=randint(1,65)
			self._a[i][j]='C'
			count-=1
		count=6
		i=16
		j=0
		while(count!=0):
			while(self._a[i][j]!='.'):
				'''i=randint(1,25)'''
				j=randint(22,72)
			self._a[i][j]='C'
			count-=1
		count=6
		i=20
		j=0
		while(count!=0):
			while(self._a[i][j]!='.'):
				'''i=randint(1,25)'''
				j=randint(1,60)
			self._a[i][j]='C'
			count-=1
		count=6
		i=24
		j=0
		while(count!=0):
			while(self._a[i][j]!='.'):
				'''i=randint(1,25)'''
				j=randint(7,70)
			self._a[i][j]='C'
			count-=1
	def genFireBall(self):
		return b
		

	"""Get Score"""
	def getScore(self):
		return (self.__score)

	"""Checks if the Donkey catches the Player or not"""
	def checkDonkey(self,p,g,ch,rand):
		if(p.getX()==g.getX() and p.getY()==g.getY()):
			os.system("clear")
			self.printScreen()
			print "Score : ",
			print self.getScore()
			return 'q'
		elif(p.getX()==g.getX()):
			if((p.getY()-1)==g.getY() and (ch=='d'or ch=='D') and rand==3):
				os.system("clear")
				self.printpm(p.getX(),p.getY(),'.')
				self.printScreen()
				print "Score : ",
				print self.getScore()
				return 'q'
			elif((p.getY()+1)==g.getY() and (ch=='a'or ch=='A') and rand==4):
				os.system("clear")
				self.printpm(p.getX(),p.getY(),'.')
				self.printScreen()
				print "Score : ",
				print self.getScore()
				return 'q'
			else:
				return 'a'
		elif(p.getY()==g.getY()):
			if((p.getX()-1)==g.getX() and (ch=='s'or ch=='S') and rand==1):
				os.system("clear")
				self.printpm(p.getX(),p.getY(),'.')
				self.printScreen()
				print "Score : ",
				print self.getScore()
				return 'q'
			elif((p.getX()+1)==g.getX() and (ch=='w'or ch=='W') and rand==2):
				os.system("clear")
				self.printpm(p.getX(),p.getY(),'.')
				self.printScreen()
				print "Score : ",
				print self.getScore()
				return 'q'
			else:
				return 'a'
		else:
			return 'a'

def main():
	screen=Screen()
	i=24
	j=5
	p=Player(i,j)
	screen.printp(i,j,'P')
	
	i=4
	j=2
	d=Donkey(i,j)
	screen.printp(i,j,'D')

	screen.genCoins()
	screen.printScreen()
	flag=0
	#counter=1
	#screen.genCoins()
	#screen.printScreen()
	while(1):
		#counter+=1
		rightf=d.getRightFlag()
		print "Enter Move  :",
		ch=getchar()
		if(ch=='q'):
			break
		p.move(ch,screen)
		d.move(ch,screen)
		DX=d.getX()
		DY=d.getY()
		F=[]
		#c=-1
		#b=fireBall(DX,DY)
		
		if(DY==15 and rightf==1):
			b=fireBall(DX,DY)
			flag=1
			#F.append(fireBall(DX,DY))
			#c+=1
			#begin=1
		#screen.printp(i,j,'O')
		#for l in F:
		
		if flag==1:
			b.move(screen,ch)
			#flag=0

		print ""
		os.system("clear")
		screen.printScreen()
		print "Score :",
		print screen.getScore()
		
	print "Game Over!!! Your Final Score is:",
	print screen.getScore()
	
if __name__ == "__main__":
	main()
