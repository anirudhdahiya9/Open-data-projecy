"""Donkey_kong_game"""


from random import *
import os
import threading
import time
from Screen import * 
from Person import *
from Player import *
from Donkey import *
from Fireball import *


def getchar():
	"""Returns a single character from standard input""" """Function taken from Github : https://gist.github.com/jasonrdsouza/1901709"""
	import tty, termios,sys   
	fd = sys.stdin.fileno()
	old_settings = termios.tcgetattr(fd)
	try:
		tty.setraw(sys.stdin.fileno())
		ch = sys.stdin.read(1)
	finally:  
		termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
		return ch

lives=3        
firemv=0  
firemv=randint(0,1)
cnt=0
fl=0  
firefl=0  
score=0

def main():
	# print 
	while(1):
		global lives
		global score
		if(lives==0):
			break
		screen=Screen(score)
		screen.generatecoin()
		screen.printscreen()
		pl=Player(24,1)
		dn=Donkey(4,1)
		# dn.donkeyposition(screen)
		while(1):
			global cnt
			global firefl

			cnt+=1
			ch=getchar()
			if(ch=='q'):
				lives=0
				break
			if(cnt==10):
				fb=Fireball(dn.getx(),dn.gety())
				fb.move(screen)
				firefl=1
				cnt=-10000

			if(firefl==1):	
				fb.move(screen)
				if(fb.getx()==pl.getx() and fb.gety()==pl.gety()):
					lives-=1
					score=screen.getscore()
					score-=25
					os.system("clear")
					break
				if(dn.getx()==pl.getx() and dn.gety()==pl.gety()):
					lives-=1
					os.system("clear")
					score=screen.getscore()
					score-=25
					break
			dn.move(screen)
			if(firefl==1):	
				# fb.move(screen)
				if(fb.getx()==pl.getx() and fb.gety()==pl.gety()):
					lives-=1
					score=screen.getscore()
					score-=25
					os.system("clear")
					break
				if(dn.getx()==pl.getx() and dn.gety()==pl.gety()):
					lives-=1
					os.system("clear")
					score=screen.getscore()
					score-=25
					break
			pl.move(ch,screen)
			if(firefl==1):	
				# fb.move(screen)
				if(fb.getx()==pl.getx() and fb.gety()==pl.gety()):
					lives-=1
					score=screen.getscore()
					score-=25
					os.system("clear")
					break
				if(dn.getx()==pl.getx() and dn.gety()==pl.gety()):
					lives-=1
					os.system("clear")
					score=screen.getscore()
					score-=25
					break
			if(pl.gety()==28 and pl.getx()==1):
				score=screen.getscore()
				score+=50
				os.system("clear")
				print "Bravo!!! You saved your Queen"
				print 'You get 50 bonus points'
				lives=3
				break
			print "Your Score:"
			print screen.getscore()




	print "Ooops!!! Game Over: Your Final Score was:",
	print screen.getscore()
if __name__ == "__main__":
	main()
