"""Pacman Game"""

from random import *
import os

def getchar():
	"""Returns a single character from standard input""" """Function taken from Github : https://gist.github.com/jasonrdsouza/1901709"""
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
	"""Person Class"""
    
	def __init__(self,x=0,y=0):
		self.__x=x
		self.__y=y

	def move(self,ch,sc):
		sc.printpm(self.__x,self.__y,'.')
		if(ch=='w' or ch=='W'):
			if(sc.checkWall(self.__x-1,self.__y)):
				self.__x-=1
		elif(ch=='s' or ch=='S'):
			if(sc.checkWall(self.__x+1,self.__y)):
				self.__x+=1
		elif((ch=='a' or ch=='A') and (self.__x==7 and self.__y==0)):
			self.__y=34;
		elif(ch=='a' or ch=='A'):
			if(sc.checkWall(self.__x,self.__y-1)):
				self.__y-=1
		elif((ch=='d' or ch=='D') and (self.__x==7 and self.__y==34)):
			self.__y=0;
		elif(ch=='d' or ch=='D'):
			if(sc.checkWall(self.__x,self.__y+1)):
				self.__y+=1
		sc.printpm(self.__x,self.__y,'P')

class Pacman(Person):
	"""Pacman Class"""
    
	def __init__(self,x,y):
		self.__x=x
		self.__y=y


	def move(self,ch,sc):
		sc.printpm(self.__x,self.__y,'.')
		if(ch=='w' or ch=='W'):
			if(sc.checkWall(self.__x-1,self.__y)):
				self.__x-=1
		elif(ch=='s' or ch=='S'):
			if(sc.checkWall(self.__x+1,self.__y)):
				self.__x+=1
		elif((ch=='a' or ch=='A') and (self.__x==7 and self.__y==0)):
			self.__y=34;
		elif(ch=='a' or ch=='A'):
			if(sc.checkWall(self.__x,self.__y-1)):
				self.__y-=1
		elif((ch=='d' or ch=='D') and (self.__x==7 and self.__y==34)):
			self.__y=0;
		elif(ch=='d' or ch=='D'):
			if(sc.checkWall(self.__x,self.__y+1)):
				self.__y+=1
		sc.printpm(self.__x,self.__y,'P')

	def getX(self):
		return self.__x

	def getY(self):
		return self.__y


class Ghost(Person):
	"""Ghost Class"""
	def __init__(self,x,y):
		self.__x=x
		self.__y=y
		self.__flag=0

	def move(self,rand,sc,g):
		if(rand==1):
			if(sc.checkWall(self.__x-1,self.__y) and sc.ghostPosition(self.__x-1,self.__y)):
				sc.printg(self.__x,self.__y,'.',g)
				self.__x-=1
		elif(rand==2):
			if(sc.checkWall(self.__x+1,self.__y) and sc.ghostPosition(self.__x+1,self.__y)):
				sc.printg(self.__x,self.__y,'.',g)
				self.__x+=1
		elif(rand==3 and (self.__x==7 and self.__y==0)):
			sc.printg(self.__x,self.__y,'.',g)
			self.__y=34;
		elif(rand==3):
			if(sc.checkWall(self.__x,self.__y-1) and sc.ghostPosition(self.__x-1,self.__y-1)):
				sc.printg(self.__x,self.__y,'.',g)
				self.__y-=1
		elif(rand==4 and (self.__x==7 and self.__y==34)):
			sc.printg(self.__x,self.__y,'.',g)
			self.__y=0;
		elif(rand==4):
			if(sc.checkWall(self.__x,self.__y+1) and sc.ghostPosition(self.__x,self.__y+1)):
				sc.printg(self.__x,self.__y,'.',g)
				self.__y+=1

		sc.printg(self.__x,self.__y,'G',g)

	def getX(self):
		return self.__x

	def getY(self):
		return self.__y
	
	def getFlag(self):
		return self.__flag
	
	def setFlag(self,a):
		self.__flag=a

class Screen:
	"""Screen Class to create Board and Board Functions"""
	def __init__(self):
		self.__score=0
		self._a=[
		['X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X'],
                ['X','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','X'],
                ['X','.','X','X','X','X','.','.','X','X','X','X','X','.','.','.','.','.','.','.','.','.','X','X','X','X','X','.','.','X','X','X','X','.','X'],
                ['X','.','X','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','X','.','X'],
                ['X','.','X','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','X','.','X'],
                ['X','.','X','.','.','.','.','X','.','X','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','X','.','X','.','.','.','.','X','.','X'],
                ['X','.','.','.','.','.','X','X','.','X','X','.','.','.','.','X','.','.','.','X','.','.','.','.','X','X','.','X','X','.','.','.','.','.','X'],
                ['.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','X','.','.','.','X','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.'],
                ['X','.','.','.','.','.','X','X','.','X','X','.','.','.','.','X','X','X','X','X','.','.','.','.','X','X','.','X','X','.','.','.','.','.','X'],
                ['X','.','X','.','.','.','.','X','.','X','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','X','.','X','.','.','.','.','X','.','X'],
                ['X','.','X','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','X','.','X'],
                ['X','.','X','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','X','.','X'],
                ['X','.','X','X','X','X','.','.','X','X','X','X','X','.','.','.','.','.','.','.','.','.','X','X','X','X','X','.','.','X','X','X','X','.','X'],
                ['X','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','X'],
                ['X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X']]
    
	"""Prints the Game Board after every Move"""	
	def printScreen(self):
		for i in range(0,15):
 			for j in range(0,35):
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
			print 

	"""Places Pacman on its right position after every move"""
	def printpm(self,x,y,ch):
		if(self._a[x][y]=='C'):
			self.collectCoin(x,y)
		self._a[x][y]=ch

	"""Places Ghost on its right position after every move"""
	def printg(self,x,y,ch,g):
		if(ch!='.' or self._a[x][y]!='P'):
			if(ch=='G' and self._a[x][y]=='C'):
				g.setFlag(1)
			self._a[x][y]=ch
		if(g.getFlag()==1 and ch=='.'):
			if(self._a[x][y]=='P'):
				self.collectCoin(x,y)
			else:
				self._a[x][y]='C'
			g.setFlag(0)

	"""Increments Score everytime Pacman gets a Coin"""
	def collectCoin(self,x,y):
		self.__score+=1
		if(self.__score!=0 and (self.__score%30)==0):
			self.genCoins()

	"""Checks if the move made by Pacman or Ghost collides with a wall"""
	def checkWall(self,x,y):
		if(self._a[x][y]=='X'):
			return False
		else:
			return True

	"""Checks that 2 Ghosts don't overlap"""
	def ghostPosition(self,x,y):
		if(self._a[x][y]=='G'):
			return False

		else:
			return True

	"""Generate Coins randomly on the board once they are collected by the pacman"""
	def genCoins(self):
		count=30
		i=0
		j=0
		while(count!=0):
			while(self._a[i][j]!='.'):
				i=randint(0,14)
				j=randint(0,34)
			self._a[i][j]='C'
			count-=1

	"""Get Score"""
	def getScore(self):
		return (self.__score)

	"""Checks if the Ghost catches the Pacman or not"""
	def checkGhost(self,p,g,ch,rand):
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


"""Main Function"""
def main():
	screen=Screen()
	i=0
	j=0
	while(screen._a[i][j]!='.'):
		i=randint(0,14)
		j=randint(0,34)
	pm=Pacman(i,j)
	screen.printpm(i,j,'P')
	while(screen._a[i][j]!='.'):
		i=randint(0,14)
		j=randint(0,34)
	g1=Ghost(i,j)
	screen.printg(i,j,'G',g1)
	while(screen._a[i][j]!='.'):
		i=randint(0,14)
		j=randint(0,34)
	g2=Ghost(i,j)
	screen.printg(i,j,'G',g2)
	os.system("clear")
	screen.genCoins()
	screen.printScreen()
	while(1):
		print "Enter Move  :",
		ch=getchar()
		if(ch=='q'):
			break
		pm.move(ch,screen)
		rand1=randint(1,4)
		prevX=g1.getX()
		prevY=g1.getY()
		g1.move(rand1,screen,g1)
		nextX=g1.getX()
		nextY=g1.getY()
		while(prevX==nextX and prevY==nextY):
			rand1=randint(1,4)
			g1.move(rand1,screen,g1)
			nextX=g1.getX()
			nextY=g1.getY()
		rand2=randint(1,4)
		prevX=g2.getX()
		prevY=g2.getY()
		g2.move(rand2,screen,g2)
		nextX=g2.getX()
		nextY=g2.getY()
		while(prevX==nextX and prevY==nextY):
			rand2=randint(1,4)
			g2.move(rand2,screen,g2)
			nextX=g2.getX()
			nextY=g2.getY()
		print ""
		os.system("clear")
		screen.printScreen()
		print "Score :",
		print screen.getScore()
		check=screen.checkGhost(pm,g1,ch,rand1)
		if(check=='q'):
			break
		check=screen.checkGhost(pm,g2,ch,rand2)
		if(check=='q'):
			break
	print ""
	print "Game Over!!! Your Final Score is:",
	print screen.getScore()

if __name__ == "__main__":
	main()
