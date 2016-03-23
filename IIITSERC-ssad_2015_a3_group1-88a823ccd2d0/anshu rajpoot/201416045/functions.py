#/bin/bash
from random import*
import sys
def my_print(text,colour):
#sequence = "\x1b[1;%dm" % (30+colour) + text + "\x1b[0m"
	p = sys.stdout                
	p.write(sequence)
#m=[[]]
#m1=",".join(m)
def getchar():

	import tty, termios, sys

	try:
		tty.setraw(sys.stdin.fileno())
		ch = sys.stdin.read(1)
	finally:
		termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
	return ch

class Person():
	def __init__(self):
		self.newposition=(m[23][4])
	def move(self,b):
		pass
	def update_newposition(self,b,inp):
		pass
	def chekwall(self,b):
		if b.getvalueatboard(self.newposition)=='x':
			return True
		else:
			return False
	def coin(self,b):
		if b.getvalueatboard(self.newposition)=='C':
			return True
		else:
			return False
	def donkey(self,b):
		if b.getvalueatboard(self.newposition)=='P':
			return True
		else:
			return False
class donkey(Person):

	def __init__(self,b):
		self.__score=0
		self.__position=(m[23][4])
		self.__reloadcount=0
		self.setdonkeyPosition(b)


	def getScore(self):
		return self.__score
	def getdonkeyPosition(self):
		return self.__position
	def updateScore(self):
		self.__score+=1


	def new_newdposition(self,b,inp):
		if inp=='w':
			self.newposition = ((self.__position[0]-1)%b.getrow(),self.__position[1]%b.getcol())

		elif inp=='a':
			self.newposition = (self.__position[0]%b.getrow(),(self.__position[1]-1)%b.getcol())

		elif inp=='s':
			self.newposition = ((self.__position[0]+1)%b.getrow(),self.__position[1]%b.getcol())

		elif inp=='d':
			self.newposition = (self.__position[0]%b.getrow(),(self.__position[1]+1)%b.getcol())
		else:
			pass

	def move(self,b,inp):

		self.new_newposition(b,inp)
		if self.chekwall(b)==True:
			print "sorry can't go"
		else:
			b.setvalueatboard(self.__position,' ')
			b.setvalueatboard(self.newposition,'P')					
			self.__position = self.newposition
	def setdonkeyPosition(self,b):
		x = randint(0,b.getrow()-1)
		y = randint(0,b.getcol()-1)
		while(b.getvalueatboard((x,y))!=' '):
			x = randint(0,b.getrow()-1)
			y = randint(0,b.getcol()-1)
		self.__position = (x,y)
		b.setvalueatboard((x,y),'P')


class Board():
	def __init__(self,r,c):
		self.__row = r
		self.__column = c
		self.__gameboard = []
	def set_board(self):
		for i in range(0,self.__row):
			self.__gameboard.append([])
			for j in range(0,self.__column):
				self.__gameboard[i].append(' ')
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
					my_print("C ",)
				elif self.__gameboard[i][j]=='x':				
					my_print("x ",)

				elif self.__gameboard[i][j]=='P':				
					my_print("P ",)
				else:
					my_print(" ",)
				print ""

	def __setWalls(self):
		self. __gameboard =[
	['x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x'],
	['x',' ',' ',' ',' ',' ',' ',' ','x',' ','Q',' ',' ',' ','x',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','x'],
	['x',' ',' ',' ',' ',' ',' ',' ','x','x','x','x','x','H','x','x',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','x'],
	['x',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','H',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','x'],
	['x',' ','D',' ',' ',' ',' ','O',' ',' ',' ',' ',' ','H',' ','C',' ',' ','C',' ',' ',' ','C',' ',' ',' ',' ',' ',' ',' ',' ','C',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','x'],
	['x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','H','x','x','x','x','x','x','x','x','x','x','x','x',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','x'],
	['x',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','H',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','x'],
	['x',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','H',' ',' ','C',' ','C',' ',' ',' ',' ',' ',' ',' ','C',' ','C',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','C',' ',' ',' ',' ',' ',' ','x'],
	['x',' ',' ',' ',' ',' ',' ',' ',' ',' ','x','x','x','x','x','H','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x'],
	['x',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','H',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','x'],
	['x',' ','C',' ','O',' ','C',' ',' ',' ',' ',' ',' ',' ',' ','H',' ',' ',' ',' ','C','O',' ',' ',' ','C',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','C',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','x'],
	['x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','H','x','x','x','x','x','x','x','x','x','x','x','x','x',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','x'],
	['x',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','H',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','H',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','x'],
	['x',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','H',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','x'],
	['x',' ',' ','C',' ',' ','O',' ','C',' ',' ',' ',' ','H',' ',' ',' ',' ',' ',' ',' ',' ','C',' ',' ',' ','C',' ',' ',' ',' ',' ',' ','H',' ',' ',' ',' ',' ',' ',' ','C',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','x'],
	['x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','H','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','x'],
	['x',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','H',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','x'],
	['x',' ','C',' ','C',' ',' ',' ',' ',' ',' ',' ','C',' ',' ',' ',' ','H',' ',' ',' ',' ',' ','C',' ',' ','C',' ',' ',' ',' ',' ',' ',' ',' ','C',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','x'],
	['x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','H','x',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','x'],
	['x',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','H',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','x'],
	['x',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','C',' ',' ',' ',' ','C',' ',' ',' ',' ',' ','C',' ',' ',' ',' ',' ',' ',' ',' ',' ','C',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','H',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','x'],
	['x',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','x','x','x','x','x','x','x','x','x','x','x','x','x','x','H','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','H','x','x','x','x','x','x','x','x','x','x','x','x'],
	['x',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','H',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','x'],
	['x',' ',' ','P',' ',' ',' ',' ',' ',' ',' ','C',' ',' ','C',' ',' ',' ','C',' ',' ',' ',' ',' ',' ','H',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','x'],
	['x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x']]
#for i in range(0,25):
#		for j in range (0,60):
#			print m[i][j],
print ""
def main():
	enter=(int)(raw_input("Enter (1) to start the game:\n"))
	if enter==1:

		y=getchar()
		y=y.lower()
		while y!='q':
			monkey = p.move(b,y)
	  		if(monkey==-1):
				b.printlist()
				print "score %d"%(p.getscore())
				print "end\n"
				break
if __name__ == "__main__":
	        main()


		
