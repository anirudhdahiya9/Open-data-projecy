from random import *
import sys

BLACK = 0
RED = 1
GREEN = 2
YELLOW = 3
BLUE = 4
MAGENTA = 5
CYAN = 6
WHITE = 7

def my_print(text,colour):
                sequence = "\x1b[1;%dm" % (30+colour) + text + "\x1b[0m"
		p = sys.stdout                
		p.write(sequence)

def getchar():

  	import tty, termios, sys
   	fd = sys.stdin.fileno()
  	old_settings = termios.tcgetattr(fd)
   	try:
      		tty.setraw(sys.stdin.fileno())
      		ch = sys.stdin.read(1)
   	finally:
      		termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
   	return ch
   

class Person():

	def __init__(self):
		self.updatedposition=(0,0)

	def move(self,b):
		pass
	

	def update_updatedposition(self,b,inp):
		pass

	def checkWall(self,b):
		if b.getvalueatboard(self.updatedposition)=='X':
			return True
		else:
			return False

	def checkCoin(self,b):
		if b.getvalueatboard(self.updatedposition)=='C':			
			return True
		else:
			return False

	def checkPacman(self,b):
		if b.getvalueatboard(self.updatedposition)=='P':
			return True
		else:
			return False

	def checkGhost(self,b):
		if b.getvalueatboard(self.updatedposition)=='G':
			return True
		else:
			return False

class Pacman(Person):
	
	def __init__(self,b):
		self.__score=0
		self.__position=(0,0)
		self.__reloadcount=0			
		self.setPacmanPosition(b)

		
	def getScore(self):
		return self.__score

	def incrementScore(self):
		self.__score+=1
	
	def setPacmanPosition(self,b):
		x = randint(0,b.getrow()-1)
		y = randint(0,b.getcol()-1)
		while(b.getvalueatboard((x,y))!='.'):
			x = randint(0,b.getrow()-1)
			y = randint(0,b.getcol()-1)
		self.__position = (x,y)
		b.setvalueatboard((x,y),'P')
	
	def getPacmanPosition(self):
		return self.__position
	
	def update_updatedposition(self,b,inp):
		if inp=='w':
			self.updatedposition = ((self.__position[0]-1)%b.getrow(),self.__position[1]%b.getcol())
		
		elif inp=='a':
			self.updatedposition = (self.__position[0]%b.getrow(),(self.__position[1]-1)%b.getcol())
	
		elif inp=='s':
			self.updatedposition = ((self.__position[0]+1)%b.getrow(),self.__position[1]%b.getcol())
	
		elif inp=='d':
			self.updatedposition = (self.__position[0]%b.getrow(),(self.__position[1]+1)%b.getcol())
		else:
			pass

	def move(self,b,inp,gamelevel):

		self.update_updatedposition(b,inp)
		if self.checkGhost(b)==True:
			b.setvalueatboard(self.__position,'.')
			b.setvalueatboard(self.updatedposition,'G')
			self.__position = self.updatedposition
			return -1
		
		elif self.checkWall(b)==True:
			print "You have hit the wall. Can't Go"
		
		elif self.checkCoin(b)==True:
			h = self.collectCoin(gamelevel) 			
			b.setvalueatboard(self.__position,'.')
			b.setvalueatboard(self.updatedposition,'P')
			self.__position = self.updatedposition
			if h==-1:
				return 2	
		else:
			b.setvalueatboard(self.__position,'.')
			b.setvalueatboard(self.updatedposition,'P')
			self.__position = self.updatedposition



	def collectCoin(self,gamelevel):
		self.incrementScore()
		self.__reloadcount+=1
		if self.__reloadcount%(25*(gamelevel))==0:
			return -1

class Ghost(Person):
	
	def __init__(self,b):
		self.__position = (0,0)
		self.setGhostPosition(b)
		
	def setGhostPosition(self,b):
		x = randint(0,b.getrow()-1)
		y = randint(0,b.getcol()-1)
		while(b.getvalueatboard((x,y))!='.'):
			x = randint(0,b.getrow()-1)
			y = randint(0,b.getcol()-1)
		self.__position = (x,y)
		b.setvalueatboard((x,y),'G')
	
	def getGhostPosition(self):
		return self.__position

	def update_updatedposition(self,b):
		mov = randint(1,4)
		if mov==1:
			self.updatedposition = ((self.__position[0]-1)%b.getrow(),self.__position[1]%b.getcol())
		
		elif mov==2:
			self.updatedposition = (self.__position[0]%b.getrow(),(self.__position[1]-1)%b.getcol())
	
		elif mov==3:
			self.updatedposition = ((self.__position[0]+1)%b.getrow(),self.__position[1]%b.getcol())
	
		elif mov==4:
			self.updatedposition = (self.__position[0]%b.getrow(),(self.__position[1]+1)%b.getcol())

	def move(self,b):
		self.update_updatedposition(b)
		if self.checkPacman(b)==True:
			b.setvalueatboard(self.__position,'.')
			b.setvalueatboard(self.updatedposition,'G')
			self.__position = self.updatedposition
			return -1			
		elif self.checkWall(b)==True or self.checkGhost(b)==True:
			pass

		elif self.checkCoin(b)==True and b.getvalueatboard(self.__position)!='C/G':
			b.setvalueatboard(self.__position,'.')
			b.setvalueatboard(self.updatedposition,'C/G')
			self.__position = self.updatedposition

		elif self.checkCoin(b)==True and b.getvalueatboard(self.__position)=='C/G':
			b.setvalueatboard(self.__position,'C')
			b.setvalueatboard(self.updatedposition,'C/G')
			self.__position = self.updatedposition
		
		else:
			if b.getvalueatboard(self.__position)=='C/G':
				b.setvalueatboard(self.__position,'C')
				b.setvalueatboard(self.updatedposition,'G')
				self.__position = self.updatedposition

			else:
				b.setvalueatboard(self.__position,'.')
				b.setvalueatboard(self.updatedposition,'G')
				self.__position = self.updatedposition
		
	
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
				elif self.__gameboard[i][j]=='X':				
					my_print("X ", CYAN)
				elif self.__gameboard[i][j]=='C/G':				
					my_print("G ", RED)
				elif self.__gameboard[i][j]=='P':				
					my_print("P ", GREEN)
				elif self.__gameboard[i][j]=='G':				
					my_print("G ", RED)
				else:
					my_print(". ", WHITE)
			print ""

	def __setWalls(self):
		self.__gameboard = [
['X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X'],
['.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.'],
['X','.','.','X','X','X','X','X','X','.','.','.','.','X','X','X','.','.','.','X','X','X','.','.','.','.','X','X','X','X','X','X','.','.','X'],
['X','.','.','.','.','.','.','.','X','.','.','.','.','X','.','.','.','.','.','.','.','X','.','.','X','.','X','.','.','.','.','.','.','.','X'],
['X','.','.','X','X','X','.','.','X','.','X','.','.','X','.','.','.','X','.','.','.','X','.','.','X','.','X','.','.','X','X','X','.','.','X'],
['X','.','.','.','.','.','.','.','X','.','X','X','X','X','.','.','.','.','.','.','.','X','X','X','X','.','X','.','.','.','.','.','.','.','X'],
['X','X','X','X','.','.','.','.','.','.','.','.','.','.','.','.','X','.','X','.','.','.','.','.','.','.','.','.','.','.','.','X','X','X','X'],
['.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','X','.','X','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.'],
['X','X','X','X','.','.','.','.','.','.','.','.','.','.','.','.','X','.','X','.','.','.','.','.','.','.','.','.','.','.','.','X','X','X','X'],
['X','.','.','.','.','.','.','.','X','.','X','.','X','X','.','.','.','.','.','.','.','X','X','X','X','.','X','.','.','.','.','.','.','.','X'],
['X','.','.','X','X','X','.','.','X','.','X','.','.','X','.','.','.','X','.','.','.','X','.','.','X','.','X','.','.','X','X','X','.','.','X'],
['X','.','.','.','.','.','.','.','X','.','.','.','.','X','.','.','.','.','.','.','.','X','.','.','X','.','X','.','.','.','.','.','.','.','X'],
['X','.','.','X','X','X','X','X','X','.','.','.','.','X','X','X','.','.','.','X','X','X','.','.','.','.','X','X','X','X','X','X','.','.','X'],
['.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.'],
['X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X']]



	def __setCoins(self,count):
		while(count!=0):
			x = randint(0,self.__row-1)
			y = randint(0,self.__column-1)
			while(self.__gameboard[x][y]!='.'):
				x = randint(0,self.__row-1)
				y = randint(0,self.__column-1)
			self.__gameboard[x][y] = 'C'
			count-=1
		
	def initialize_board(self):
		self.__setWalls()
		self.__setCoins(25*(self.__gamelevel))

	def reloadboard(self):
		self.__setCoins(25*(self.__gamelevel))


def main():
	try:
		lev = (int)(raw_input("Enter difficulty level(1/2/3):\n"))	
		b = Board(15,35,lev)
		b.set_board()
	
		p = Pacman(b)
		numofghosts=1
		tobreakloop = False

		g = []		
	
		if lev==1:
			numofghosts = 1
		elif lev==2:
			numofghosts = 3
		elif lev==3:
			numofghosts = 5
		else:
			print "Level Invalid\n"
			return

		for i in range(0,numofghosts):
			gh = Ghost(b)
			g.append(gh)
	
		b.printlist()
		print "Score: %d"%(p.getScore())
		print "To begin game, enter w/s/a/d/q only. Then you can enter anything."	
		y = getchar()
		y = y.lower()	
		while y!='q':
			retforpacman = p.move(b,y,lev) 
			if(retforpacman==-1):
				b.printlist()
				print "Final Score: %d"%(p.getScore())
				print "Game Ends!! Ghost has eaten you.\n"			
				break

			elif(retforpacman==2):
				b.reloadboard()

			for i in range(0,numofghosts):
				if(g[i].move(b)==-1) or p.getPacmanPosition()==g[i].getGhostPosition():
					tobreakloop = True			
					break
	
			b.printlist()
			print "Score: %d"%(p.getScore())
			if tobreakloop == True:
				b.printlist()
				print "Final Score: %d"%(p.getScore())
				print "Game Ends!! Ghost has eaten you.\n"
				break		

			print "Enter your move(Type Character w/a/s/d/q): "
			y = getchar()
			y = y.lower()

			if y=='q':
				break
		if y=='q':
			b.printlist()
			print "Final Score: %d"%(p.getScore())
			print "You have chosen to quit.\n"
	except (AttributeError):
		print "To begin game, enter w/s/a/d/q only. Then you can enter anything."


if __name__ == "__main__":
	main() 


