from random import *
import os

from Person import *
from Player import *
from Screen import *
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



def main():
	global flag
	global count
	screen=Screen()
	i=25
	j=1
	pm=Player(i,j)
	screen.printpm(i,j,'P')
	#flag=0
	#screen.printScreen()

	os.system("clear")
	screen.genCoins()
	screen.printScreen()
	while(1):
		print "Enter Move  :",
		ch=getchar()
		if(ch=='q'):
			break
		pm.move(ch,screen)

		print ""
		os.system("clear")
		screen.printScreen()
		print "Score :",
		print screen.getScore()
		if(screen.getflag1()==1):
			break
	print ""
	print "Game Over!!! Score is:",
	print screen.getScore()




if __name__ == "__main__":
	main()