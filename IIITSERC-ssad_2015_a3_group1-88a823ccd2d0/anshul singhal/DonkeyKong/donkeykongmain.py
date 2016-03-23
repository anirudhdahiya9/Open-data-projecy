"""donkey kong"""
import os,sys,time,threading,copy
from person import Donkey,Person,Player
from fireball import Fireballs
from screen import Screen
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
	return ch   #return the pressed character3

def main():
	turn =3
	fireballs=[]
	record='w'
	flag=0
	direction=1
	nuofmoves=0
	board=Screen()
	board.randomcoins()
	player=Player(24,2)
	donkey=Donkey(4,2)
	x2=donkey.getpositionX()
	y2=donkey.getpositionY()
	fireballs.append(Fireballs(x2,y2+1,1))
	board.playercordinate(24,2)
	board.donkeycordinate(4,2)
	board.fireballcordinate(x2,y2+1)
	board.printscreen()
	while 1:
		ch=getchar()
		nuofmoves += 1
		if(nuofmoves%15==0):
			x2=donkey.getpositionX()
			y2=donkey.getpositionY()
			fireballs.append(Fireballs(x2,y2+1,1))
			board.fireballcordinate(x2,y2+1)
		if ch == 'd' or ch == 'D' or ch == 'a' or ch == 'A':
			record=ch
		if ch=='Q' or ch=='q':
			break
		
		os.system("clear")
		player.move(ch,board,player,record)
		direction=donkey.move(ch,board,direction)	
		x=player.getpositionX()
		y=player.getpositionY()
		for i in range(0,len(fireballs)):
			if board.checkCollision(fireballs[i].getpositionX(),fireballs[i].getpositionY(),x,y):
				if turn>0:
					turn -=1
					os.system("clear")
					print "Press any key to user your life or press q to quit"
					ch=getchar()
					if ch=='Q' or ch=='q':
						print "Game over!"
						flag=1
						break
						
				else:
					print "Game over!"
					flag=1
					break
		if flag==1:
			break
		for i in range(0,len(fireballs)):
			fireballs[i].move(ch,board)
			x3=fireballs[i].getpositionX()
			y3=fireballs[i].getpositionY()
			board.fireballcordinate(x3,y3)
			if (board.checkdharti(x3,y3)):
				fireballs[i].down(x3,y3,board)
				os.system("clear")
		for i in range(0,len(fireballs)):
			if board.checkCollision(fireballs[i].getpositionX(),fireballs[i].getpositionY(),x,y):
				if turn>0:
					turn -=1
					board.reducecoin()
					os.system("clear")
					print "Press any key to use your life or press q to quit"
					ch=getchar()
					if ch=='Q' or ch=='q':
						print "Game over!"
						flag=1
						break
				else:
					print "Game over!"
					flag=1
					break	
		x2=donkey.getpositionX()
		y2=donkey.getpositionY()
		board.playercordinate(x,y)
		board.donkeycordinate(x2,y2)
		board.printscreen()
		if (board.checkdharti(x,y)):
			player.down(x,y,board)
		print "Total : %d ,Life-Left: %d"  % (board.getscore(), turn)
		if board.getqueen(player.getpositionX(),player.getpositionY()):
			
			board.reload()
			os.system("clear")
			board.randomcoins()
			board.printscreen()
			player._Person__x=24
			player._Person__y=2
			board.playercordinate(24,2)
			
if __name__=="__main__":
	main()	


