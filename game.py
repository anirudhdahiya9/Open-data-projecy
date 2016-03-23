"""Donkeykong game"""
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
		sc.prplayer(self.__x,self.__y,' ')
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
                            flag=checkStairs(self.__x,self.__y+1)
                            if(flag==True):
                               # self.__y+=1
                                sc.prplayer(self.__x,self.__y,' ')
                                sc.prplayer(self.__x,self.__y-1,'H')
                            else:
                                self.__y+=1
		sc.prplayer(self.__x,self.__y,'P')
class Player(Person):
	"""Player Class"""
    
	def __init__(self,x,y):
		self.__x=x
		self.__y=y


	def move(self,ch,sc):
		sc.prplayer(self.__x,self.__y,' ')
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
		sc.prplayer(self.__x,self.__y,'P')

	def getX(self):
		return self.__x

	def getY(self):
		return self.__y
class Screen:
    """Screen to show the board"""
    def __init__(self):
        self.__score=0
        self._a=[
       #  0   1   2   3   4   5   6   7   8   9  10  11  12  13  14  15  16  17  18  19  20  21  22  23  24  25  26  27  28  29  30  31  32  33  34  35  36  37  38  39  y <<<
        ['X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X'],#0
        ['X',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','X',' ','Q',' ',' ',' ','X',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','X'],#1
        ['X',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','X','X','X','H','X','X','X',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','X'],#2
        ['X',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','H',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','X'],#3
        ['X',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','H',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','X'],#4
        ['X',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','H',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','X'],#5
        ['X','X','X','X','X','X','X','X','X','X','X','H','X','X','X','X','X','X','X','X','X','X','X','X','X','X','H','X','X',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','X'],#6
        ['X',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','H',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','X'],#7
        ['X',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','H',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','X'],#8
        ['X',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','H',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','H',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','X'],#9
        ['X',' ',' ',' ',' ',' ',' ',' ',' ','X','X','X','X','X','X','H','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X'],#10
        ['X',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','H',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','X'],#11
        ['X',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','H',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','X'],#12
        ['X',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','H',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','X'],#13
        ['X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','H','X','X','X','X','X','X','X','H','X','X',' ',' ',' ',' ',' ',' ',' ',' ',' ','X'],#14
        ['X',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','H',' ',' ',' ',' ',' ',' ',' ','H',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','X'],#15
        ['X',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','H',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','X'],#16
        ['X',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','H',' ',' ',' ',' ',' ',' ',' ','H',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','X'],#17
        ['X',' ',' ',' ',' ',' ',' ','X','X','X','H','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X'],#18
        ['X',' ',' ',' ',' ',' ',' ',' ',' ',' ','H',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','X'],#19
        ['X',' ',' ',' ',' ',' ',' ',' ',' ',' ','H',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','X'],#20
        ['X',' ',' ',' ',' ',' ',' ',' ',' ',' ','H',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','X'],#21
        ['X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','H','X','X','X','X','X',' ',' ',' ',' ',' ',' ',' ',' ','X'],#22
        ['X',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','H',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','X'],#23
        ['X',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','H',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','X'],#24
        ['X',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','H',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','X'],#25
        ['X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X']]#26
    """Prints the screen after every move"""                                                                                                                              #x ^^^ 
    def printScreen(self):
		for i in range(0,27):
 			for j in range(0,40):
				if(self._a[i][j]=='D'):
					print ('\033[1m'+'\033[97m' + 'G' + '\033[0m'),
				elif(self._a[i][j]=='P'):
					print ('\033[1m'+'\033[97m' + 'P' + '\033[0m'),
				elif(self._a[i][j]=='X'):
					print ('\033[1m'+'\033[97m' + 'X' + '\033[0m'),
				elif(self._a[i][j]=='C'):
					print ('\033[1m'+'\033[97m' + 'C' + '\033[0m'),
                                elif(self._a[i][j]=='H'):
                                        print ('\033[1m'+'\033[97m' + 'H' + '\033[0m'),
                                         
				else:	
					print self._a[i][j],
			print "" 
    """Places Player on its right position after every move"""
    def prplayer(self,x,y,ch):
	    if(self._a[x][y]=='C'):
		    self.collectCoin(x,y)
            self._a[x][y]=ch
            
    """Function to check the stairs"""                
    def checkStairs(self,x,y):
            if(self._a[x][y]=='H'):
                return True
            else:
                return False
    """Increments Score everytime Player gets a Coin"""
    def collectCoin(self,x,y):
        if(self._a[x][y]=='C'):
            self.__score+=1
            if(self.__score!=0 and (self.__score%30)==0):
                self.genCoins()
             #self.__score+=1
             #if(self.__score!=0 and (self.__score%30)==0):
               #  self.genCoins()
    """Checks if the move made by Player or Ghost collides with a wall"""
    def checkWall(self,x,y):
        if(self._a[x][y]=='X'):
            return False
        else:
            return True
    """Generate Coins randomly on the board once they are collected by the Player"""
    def genCoins(self):
	    count=5
	    j=0
	    while(count!=0):
		    while(self._a[5][j]!=' '):
			    j=randint(0,28)
	 	    self._a[5][j]='C'
                    count-=1           
            count1=5
            while(count1!=0):
                    while(self._a[9][j]!=' '):
                            j=randint(15,36)
                    self._a[9][j]='C'  
                    count1-=1    
            count2=4
            while(count2!=0):
                    while(self._a[13][j]!=' '):
                            j=randint(3,25)
 		    self._a[13][j]='C'
                    count2-=1
            count3=6
            while(count3!=0):
                    while(self._a[17][j]!=' '):
                            j=randint(16,32)
                    self._a[17][j]='C'
                    count3-=1
            count4=4
            while(count4!=0):
                    while(self._a[21][j]!=' '):
                            j=randint(6,21)
                    self._a[21][j]='C'
                    count4-=1
            count5=6
            while(count5!=0):
                    while(self._a[25][j]!=' '):
                            j=randint(0,25)
                    self._a[25][j]='C'
                    count5-=1
    """Get Score"""
    def getScore(self):
       return (self.__score)
"""Main Function"""
def main():
	screen=Screen()
	pr=Player(25,3)
	screen.prplayer(25,3,'P')
	screen.genCoins()
	screen.printScreen()
        while(1):
            print "Enter Move: ",
            ch=getchar()
            if(ch=='q'):
                break
            pr.move(ch,screen)
            print ""
            os.system("clear")
            screen.printScreen()
            print "Score",
            print screen.getScore()
            if(ch=='q'):
                break

#        while(screen._a[i][j]!=' '):
#		i=randint(0,26)
#		j=randint(0,40)
#	g1=Ghost(5,25)
#	screen.printg(i,j,'G',g1)

if __name__ == "__main__":
	main()

