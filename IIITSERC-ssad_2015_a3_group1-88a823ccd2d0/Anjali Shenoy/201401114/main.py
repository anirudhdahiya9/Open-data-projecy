from random import *
from screen import *
from mario import *
from donkey import *
from fireball import *	
import os
import time


""" Get character from keyboard """
def getchar():
	"""Returns a single character from standard input""" 
	"""Function taken from Github : https://gist.github.com/jasonrdsouza/1901709"""
	import tty, termios, sys
	fd = sys.stdin.fileno()
	old_settings = termios.tcgetattr(fd)
	try:
		tty.setraw(sys.stdin.fileno())
		ch = sys.stdin.read(1)
	finally:
		termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
	return ch


""" Main """
def main():

	os.system("clear")
	sc = Screen()
	sc.genCoins()
	
	mar = Mario()
	donkey=Donkey()
	prevChar=' '
	prevChar2=' '
	
	count=0
	sc.printScreen()
	fb=[]
	k=0
	ans=0
	level=1

	while(1):
		score=sc.getScore()
		print "Level:"+str(level)
		print "No of lives:"+str(mar.getLives())
		print "Current score: "+str(score)
		print "Enter your move (W/S/A/D/Q):",
		ch=getchar()

		count=count+1  										#To count no. of moves
		

		if ch == 'q' or ch == 'Q':							#if player wants to quit
			os.system("")
			os.system("clear")
			print "\nGame over!"
			print "Your final score is "+str(sc.getScore())+"\n"
			break

		if ch==' ' and mar.getX()>=5:					#If mario wants to Jump

			print "\nLeft or right jump(a/s):",
			ch2=getchar()									#gets character for direction of jump
			
			check=mar.mjump(ch2,sc,fb)
			if(check==1 or ans == 1):			#While jumping, check=1 if it collides with 'O'
				temp=mar.die(sc)				#temp =1 when no. of lives=0 and player wants to replay (resets game)
				if temp=='1':
					sc.reset(fb)
					del(fb)
					fb=[]
					ans=0
					sc.genCoins()
					mar.reposition(30,1)
					mar.resetlives()
					donkey.reposition(5,1)
					sc.resetScore()
					print ""
					os.system("clear")
					sc.printScreen()

				elif temp=='2':							#temp =2 implies quits the game after loss of 3 lives
					os.system("clear")
					print "Thanks for playing!"
					break

		
		elif mar.getX() != 1:								#If player isnt on the floor of queen, it still can move

				prevChar2=donkey.printDonkey(sc,prevChar2)		#Move donkey
				prevChar=mar.move(ch,sc,'P',prevChar)			#Move Mario

				dx=donkey.getX()
				dy=donkey.getY()
				x=mar.getX()
				y=mar.getY()

				check=sc.checkCollision(prevChar,fb,mar)			#checks collision with O (1st possibility) returns 1 if true
				if check==1:
					mar.die(sc)
				
				if(count%30==0):									#Generates fireball at intervals of 30 moves
					f=Fireball(dx,dy,' ')
					fb.append(f)
					fb[len(fb)-1].generate(sc)
				
				for i in range(0,len(fb)):							#Movement of fireballs in the grid
					ans=fb[i].fmove(sc)
					if ans==1:										#ans=1 if fireball moves into standing P
						break

				
				print""
				os.system("clear")
				sc.printScreen()
								
				check=sc.checkCollision(prevChar,fb,mar)			#Collision of P and O after O has moved (2nd possibility) 
				if(check==1 or ans == 1):
					temp=mar.die(sc)
					if temp=='1':
						sc.reset(fb)
						del(fb)
						fb=[]
						ans=0
						sc.genCoins()
						mar.reposition(30,1)
						donkey.reposition(5,1)
						mar.resetlives()
						sc.resetScore()
						print ""
						os.system("clear")
						sc.printScreen()

					elif temp=='2':
						os.system("clear")
						print "Thanks for playing!"
						break
				if donkey.donCollision(mar)==True:
					os.system("clear")
					print"You crashed into the donkey!! Game over!!"
					print "Your final score is "+str(sc.getScore())
					break

		else:															#Mario is on queen's level
			level+=1
			os.system("clear")
			print "Congratulations! You saved the queen! Taking you to level"+str(level)+"..."
			time.sleep(3)
			sc.reset(fb)
			del(fb)													#reset fireball, generate coins, reposition all
			fb=[]
			ans=0
			sc.genCoins()
			sc.winscore()
			mar.reposition(30,1)
			donkey.reposition(5,1)
			mar.resetlives()
			print ""
			os.system("clear")
			sc.printScreen()



if __name__ == "__main__":
	main()



