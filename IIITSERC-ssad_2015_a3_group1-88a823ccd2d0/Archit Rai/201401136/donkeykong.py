from random import *
import person
import board
import sys
import time

BLACK = 0
RED = 1
GREEN = 2
YELLOW = 3
BLUE = 4
MAGENTA = 5
CYAN = 6
WHITE = 7
prev='_'
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
   
def main():
	try:
		lev = (int)(raw_input("Select Difficulty Level (1,2,3):\n"))	
		b = board.Board(27,40,lev)
		b.set_board()
		cnt=0
		p = person.Pl(b,cnt)
		numofdonkeys=1
		tobreakloop = False

		d = []		
		f = []
		lives=3
		moves=0
		numoffireball=1
		if lev<1 or lev>3:
			print "Level Invalid\n"
			return

		don = person.Donkey(b)
		d.append(don)
		fir = person.Fireball(b)
		f.append(fir)
		b.printlist()
		print "Score: %d"%(p.getScore())
		print "Controls: W/S/A/D/<space>/Q"
		print "Lives: %d" %(lives)
		y = getchar()
		y = y.lower()	
		while y!='q':
			retforpl = p.move(b,y,lev)
			cnt=p.getScore()
			moves=moves+1
			if lev==1:
				if(moves%30==0):
					fir = person.Fireball(b)
					f.append(fir)
					numoffireball=numoffireball+1
			elif lev==2:
				if(moves%20==0):
					fir = person.Fireball(b)
					f.append(fir)
					numoffireball=numoffireball+1
			elif lev==3:
				if(moves%15==0):
					fir = person.Fireball(b)
					f.append(fir)
					numoffireball=numoffireball+1
	
			if(retforpl==-1):
				lives=lives-1
				if(lives==0):
					corner=(25,1)
					b.setvalueatboard(corner,'_')
					b.printlist()
					print "Final Score: %d"%(p.getScore())
					print "Lives: %d" %(lives)					
					print "Game Over.\n"			
					break
				else:
					p=person.Pl(b,cnt-25)
			elif(retforpl==2):
				b.printlist()
				time.sleep(1)				
				b = person.Board(27,40,lev)
				b.set_board()
				p = person.Pl(b,cnt+50)				
				numofdonkeys=1
				numoffireball=1
				moves=0
				d = []		
				f = []
				don = person.Donkey(b)
				d.append(don)
				fir = person.Fireball(b)
				f.append(fir)	
				b.printlist()
			if(d[0].move(b)==-1 or d[0].getDonkeyPosition()==p.getPlPosition()):
				lives=lives-1
				p=person.Pl(b,cnt-25)				
				if(lives==0):				
					tobreakloop=True
			else:
				for i in range(0,numoffireball):
					xcord=f[i].getFireballx()
					if(xcord==-1):
						continue
					if f[i].move(b)==-1 or p.getPlPosition()==f[i].getFireballPosition():
						lives=lives-1
						p=person.Pl(b,cnt-25)
						if(lives==0):							
							tobreakloop = True			
							break
	
			b.printlist()
			print "Score: %d"%(p.getScore())
			if tobreakloop == True:
				corner=(25,1)
				b.setvalueatboard(corner,'_')
				b.printlist()
				print "Final Score: %d"%(p.getScore())
				print "Lives: %d" %(lives)				
				print "Game Over.\n"
				break		

			print "Controls: W/S/A/D/<space>/Q"
			print "Lives: %d" %(lives)
			y = getchar()
			y = y.lower()

			if y=='q':
				break
		if y=='q':
			b.printlist()
			print "Final Score: %d"%(p.getScore())
			print "Game ended.\n"
	except (AttributeError):
		print "Controls: W/S/A/D/<space>/Q"

if __name__ == "__main__":
	main()
