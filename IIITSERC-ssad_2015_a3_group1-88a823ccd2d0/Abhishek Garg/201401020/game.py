import os
import random 
import copy
import time
from player import player
from screen import set_screen
from donkey import donkey
from fireball import fireball
from coins import coins
from key import key
from constants import *
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

		
class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    

#surface[29][2]='P'
def print_surface(surface,score,lives,level):
	
	for i in range (height):
		for j in range(width):
			if surface[i][j]=='O':
				print ('\033[1m'+'\033[91m' + 'O' + '\033[0m' + ' '),
			elif surface[i][j]=='D':
				print ('\033[1m'+'\033[91m' + 'D' + '\033[0m' + ' '),
			elif surface[i][j]=='H':
				print ('\033[1m'+'\033[95m' + 'H' + bcolors.BOLD + ' '),
			elif surface[i][j]=='Q':
				print ('\033[1m'+'\033[95m' + 'Q' + bcolors.BOLD + ' '),
			elif surface[i][j]=='x':
				print (bcolors.FAIL + 'x' + '\033[0m' + ' '),
			elif surface[i][j]=='P':
				print (bcolors.BOLD + 'P' + bcolors.OKGREEN + ' '),
			elif surface[i][j]=='C':
				print ('\033[1m'+'\033[93m' + 'C' + '\033[0m' + ' '),
			else:
				print surface[i][j]+' ',
		print
	print 'SCORE : ' + str(score)
	print 'LIVES : ' + str(lives)
	print 'LEVEL : ' + str(level)		
	print "\n"


def main():
#	from constants import *
	surface=[[' ' for x in range(width)]for y in range(height)]
	screen=set_screen(surface,width,height)                     #setting the basic screen
	surface_copy=copy.deepcopy(surface)
	surface[queen_x][queen_y]='Q'

	# creating instances
	Fire=fireball(surface,surface_copy,width,height)
	prince=player(surface,29,2)
	donk1=donkey(surface,9,2,-1)
	Donkey=[donk1]
	Coins=coins(width,height)
	Key=key(width,height,key_x,key_y)

	Coins.generate_coins()
	Coins.place_coins(surface)
	level=1
	lives=3
	score=0
	queen_captured=False
	key_captured=False
	running=True
	print '\n\n'
	print_surface(surface,score,lives,level)


	while running:
		surface=copy.deepcopy(surface_copy)
		x='s'
		if queen_captured==False:
			x=getchar()
		#	time.sleep(0.04)
			if x=='q':
				print 'You have decided to exit the game.'
				break
		else:
			queen_captured=False
			surface=Coins.place_coins(surface)
			
		if ord(x)==32:
			player_pos=prince.get_pos()
			surface[player_pos[0]-1][player_pos[1]]='P'
			surface[queen_x][queen_y]='Q'
			for i in range(len(Donkey)):
				surface=Donkey[i].donk_move(Fire,surface,Fire.flag%3)	
			surface=Fire.update_balls_location(surface)
			surface=Coins.place_coins(surface)
			print_surface(surface,score,lives,level)
			time.sleep(0.3)
			
			surface=copy.deepcopy(surface_copy)
			surface[player_pos[0]][player_pos[1]]='P'
			surface[queen_x][queen_y]='Q'
			for i in range(len(Donkey)):
				surface=Donkey[i].donk_move(Fire,surface,Fire.flag%3)	
			surface=Fire.update_balls_location(surface)
			surface=Coins.place_coins(surface)

			if Fire.fireball_hits_player(surface)==-1 :
				surface[player_pos[0]][player_pos[1]]='+'
				lives-=1
				score-=25
				running=False
				print_surface(surface,score,lives,level)
				
			for i in range(len(Donkey)):
				if  Donkey[i].donk_hits_player(surface)==-1:
					surface[player_pos[0]][player_pos[1]]='+'
					lives-=1
					score-=25
					running=False
					print_surface(surface,score,lives,level)


			if running==False:
				if lives>0:
					print 'You lost a life.'
					time.sleep(1.5)
					surface=copy.deepcopy(surface_copy)
					surface=prince.reset_player_pos(surface)
					surface[queen_x][queen_y]='Q'
					for i in range(len(Donkey)):
						surface=Donkey[i].donk_move(Fire,surface,Fire.flag%3)	
					surface=Coins.place_coins(surface)
					Fire.remove_fireballs()
					print_surface(surface,score,lives,level)
					running=True
				else:
					print 'You lost a life.'
					print "Game Over!! "

			else:
				print_surface(surface,score,lives,level)
				time.sleep(0.3)

			continue
			
		surface=prince.move(surface,x)
	#	surface=make_surface_move(surface)
		surface[queen_x][queen_y]='Q'
		for i in range(len(Donkey)):
			surface=Donkey[i].donk_move(Fire,surface,Fire.flag%3)	
		surface=Fire.update_balls_location(surface)
		surface=Coins.place_coins(surface)
		if prince.queen_captured(queen_x,queen_y):
			surface[queen_x][queen_y]='*'
			print_surface(surface,score,lives,level)
			queen_captured=True
			time.sleep(1.5)
		
		if queen_captured==True:
			print 'You have successfully completed level : ' +str(level)
			
			if level<3:
				level+=1
				if level==3:
					donk2=donkey(surface,8,7,1)
					Donkey.append(donk2)
				print 'proceeding to level : ' + str(level)
				surface_copy=Key.change_level(surface_copy,level)
				surface=prince.reset_player_pos(surface)
				Coins.generate_coins()
				Fire.remove_fireballs()
				continue
				
			else :
				print 'You have won the game.'
				break
			

		if Key.player_gets_key(surface)==True:
			surface_copy=Key.restore_surface_copy(surface_copy)
			surface=Key.restore_surface_copy(surface)
			surface[key_x][key_y]='P'
			time.sleep(1)
			print 'You got the key.'
			print 'Now the queen is free.'
			print_surface(surface,score,lives,level)
			continue
			
			
		player_pos=prince.get_pos()
		
		if Fire.fireball_hits_player(surface)==-1  or Fire.check_for_swap(surface,prince.cur_dir)==-1:
			surface[player_pos[0]][player_pos[1]]='+'
			lives-=1
			score-=25
			running=False
			
		for i in range(len(Donkey)):
			if running==True:
				if Donkey[i].donk_hits_player==-1:
					surface[player_pos[0]][player_pos[1]]='+'
					lives-=1
					score-=25
					running=False
				
			
		if Coins.player_gets_a_coin(player_pos[0],player_pos[1])==1:
			score+=5

		print_surface(surface,score,lives,level)
		if running==False:
			if lives>0:
				print 'You lost a life.'
				time.sleep(1.5)
				surface=copy.deepcopy(surface_copy)
				surface=prince.reset_player_pos(surface)
				surface[queen_x][queen_y]='Q'
				for i in range(len(Donkey)):
					surface=Donkey[i].donk_move(Fire,surface,Fire.flag%3)	
				surface=Coins.place_coins(surface)
				Fire.remove_fireballs()
				print_surface(surface,score,lives,level)
				running=True
			else:
				print 'You lost a life.'
				print "Game Over!! "

if __name__ == "__main__":
	main()		
# colours,jump,fireballs movement	
