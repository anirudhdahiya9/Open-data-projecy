#!/usr/bin/python
import player 
from board import Board
import donkey
import sys
import random
from random import randint
length = 80
width = 30
print "!!Level 1!!"
mod = 50
class _GetchUnix:
	    def __init__(self):
		    import tty, sys
    	    def __call__(self):
		import sys, tty, termios
		fd = sys.stdin.fileno()	
		old_settings = termios.tcgetattr(fd)
		try:
			tty.setraw(sys.stdin.fileno())
			ch = sys.stdin.read(1)
		finally:
			termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
		return ch
getch = _GetchUnix()

#dr = Donkey()
pl = player.Player()
dr = donkey.Donkey()
fr = donkey.FireBall()
#fr = FireBall()
curry = 0
temp = " "
while pl.life!=0 :
	key = getch()
	if (key=="q"):
	 	break 
	elif (key==" "):
	 	steps=0
 	 	while(steps<=3):
			flag = getch()
	 		pl.jump(flag,steps)
			dr.move(curry,temp)
			fr.move()
			steps+=1
			for n in range(width):
				for m in range(length):
					sys.stdout.write(Board.board[n][m])
				print
			print "Score: " ,pl.score
			for i in range(8):
				print
			if Board.board[pl.posx-1][pl.posy]=="H":
			 	break
	if Board.board[dr.posx][dr.posy-1]!=" ":
	 	curry=dr.posy-1
	 	temp=Board.board[dr.posx][dr.posy-1]
	elif Board.board[dr.posx][dr.posy+1]!=" ":
	 	curry=dr.posy+1
	 	temp=Board.board[dr.posx][dr.posy+1]
	dr.move(curry,temp)
	ball = random.randint(1,100)
	if ball%mod==0:
	   	fr.throw()
	fr.move()
	pl.move(key)
	for i in range(len(fr.ball)-1):
		if fr.ball[i][2]==0 and fr.ball[i][0]==pl.posx and fr.ball[i][1]==pl.posy-1:
			pl.score-=25
			Board.board[pl.posx][pl.posy]=" "
			fr.ball.remove(fr.ball[i])
			pl.posx=28
			pl.posy=2
			pl.life-=1
		elif fr.ball[i][2]==1 and fr.ball[i][0]==pl.posx and fr.ball[i][1]==pl.posy+1:
			pl.score-=25
			Board.board[pl.posx][pl.posy]=" "
			fr.ball.remove(fr.ball[i])
			pl.posx=28
			pl.posy=2
			pl.life-=1
		elif fr.ball[i][1]==pl.posy and fr.ball[i][0]==pl.posx-1 and pl.posy==" ":	
			pl.score-=25
			Board.board[pl.posx][pl.posy]=" "
			fr.ball.remove(fr.ball[i])
			pl.posx=28
			pl.posy=2
			pl.life-=1
		elif fr.ball[i][1]==pl.posy and fr.ball[i][0]==pl.posx+1 and pl.posy==" ":	
			pl.score-=25
			Board.board[pl.posx][pl.posy]=" "
			fr.ball.remove(fr.ball[i])
			pl.posx=28
			pl.posy=2
			pl.life-=1
		elif fr.ball[i][1]==pl.posy and fr.ball[i][0]==pl.posx:	
			pl.score-=25
			Board.board[pl.posx][pl.posy]=" "
			fr.ball.remove(fr.ball[i])
			pl.posx=28
			pl.posy=2
			pl.life-=1
	for n in range(width):
		for m in range(length):
			sys.stdout.write(Board.board[n][m])
		print
	print "Score: " ,pl.score
	if pl.posx==2 and pl.posy==18:
	 	print "!! You Won !!"
		if mod==20:
		 	break
		mod=20
		pl.score+=50
		pl.posx=28
		pl.posy=3
		Board.board[2][18]="Q"
#		for i in range(len(fr.ball)-1):
#	fr.ball.remove(fr.ball[i])
		print "!! Level 2 !!"
		for i in range(8):
			print
	if dr.mv==1 and pl.posx==dr.posx and pl.posy-1==dr.posy:
	 	print "!!Game Over!!"
	 	break
	elif dr.mv==0 and pl.posx==dr.posx and pl.posy+1==dr.posy:
	 	print "!!Game Over!!"
	 	break
	elif dr.posx==pl.posx and pl.posy==dr.posy:
	  	print "!!Game Over!!"
	  	break
	for i in range(8):
		print " " 
	flag = key
if pl.life==0:
	print "!!Game Over!!"
