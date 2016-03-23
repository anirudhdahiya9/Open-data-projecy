from bard import *
from player import *
from boarditems import *
from donkey import *
from ball import *
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
def main():
	import os
	from time import sleep
	from random import randint
	plr=player()
	while True:
		fl=0
		plr.checkdeath()
		plr.initpos()
		brd=board()
		don=donkey()
		b1=[ball(don)]
		brd.printboard(plr,don,b1)
		while True:
			plr.checkqueen()
			fl=plr.checkdonkey(don,fl)
			if fl==1:
				break
			fl=plr.checkball(b1,fl)
			if fl==1:
				break
			if randint(0,randint(3,6))==1:
				b1+=[ball(don)]
			plr=player.checkfall(plr,brd,don,b1)
			mv=getchar()
			if mv==' ':
				plr=plr.jump(brd,don,b1)
			else:
				plr=plr.getdir(mv)
				plr=plr.move(plr,brd,0,mv)
			for i in b1:
				i=i.move(brd)
			don=don.move(brd)
			brd.printboard(plr,don,b1)
		if fl==1:
			continue	



		
if __name__=="__main__":
	main()
