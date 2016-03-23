import pygame
import random
from pygame.locals import *
from Board import *
from personsmodule import *

pygame.init()   
gameDisplay=pygame.display.set_mode((800,700))
pygame.display.set_caption('Donkey kong')
pygame.mixer.music.load("abcdonkey.mp3")
pygame.mixer.music.play(-1,0.0)
white = (255,255,255)
black = (0,0,0)
red = (255,0,0)
gold=(255,215,0)
blue =  (0,0,255)
green = (0,255,0)
pink = (255,105,180)
purple=(128,0,128)
silver=(192,192,192)
teal=(0,128,128)
brown=(139,69,19)
orange=(255,140,0)
display_x=800
display_y=600
clock=pygame.time.Clock()

def gameloop():

	gameExit=False
	player=Player(30,550)
	donkey=Donkey(30,85)
	x_change=0
	y_change=0
	
	count=1
	score=0
	
	x3=0
	a1=[]
	a2=[]
	a3=[]
	a4=[]
	a5=[]
	s=0
	s1=250
	s=s+100
	for i in range(4):
		a=random.randrange(s,s+100,20)
		a1.append(a)
		#print a1[i]
	s=0	
	for i in range(4):
		s=s+100
		a=random.randrange(s,s+100,20)
		a2.append(a)
	for i in range(4):
		s1=s1+100
		a=random.randrange(s1,s1+100,20)
		a3.append(a)
	s=0
	for i in range(4):
		s=s+100
		a=random.randrange(s,s+100,20)
		a4.append(a)
	s1=250
	for i in range(4):
		s1=s1+100
		a=random.randrange(s1,s1+100,20)
		a5.append(a)
	
		
	while not gameExit:
		gameDisplay.fill(orange)		
		x,y=player.getPosition()
				
		for event in pygame.event.get(): 
			if event.type==pygame.QUIT:
				gameExit=True
			if event.type==pygame.KEYDOWN:
				if event.key==pygame.K_q:
					return 
				if y==550 or y==460 or y==370 or y==280 or y==190 or y==100:
					if event.key==pygame.K_a:
						x_change=-5
					if event.key==pygame.K_d:
						x_change=5

				if ((x>510 and x<540) or (x>280 and x<310)):
					if event.key==pygame.K_w:
						y_change=-5
					if event.key==pygame.K_s:
						y_change=5
				
			if event.type==pygame.KEYUP:
				if event.key==pygame.K_a or event.key==pygame.K_d:
					x_change=0
				if event.key==pygame.K_w or event.key==pygame.K_s:
					y_change=0

		x=x+x_change
		y=y+y_change
		
		if y>550:
			y=550
		if x<30:
			x=30
		if y>550:
			y=550
		if y<30:
			y=30
		if x>750:
			x=750
		
		if (y>370 and y<460) and (x>510 and x<540):
			y=460
		if (y<280 and y>190) and (x>510 and x<540):
			y=280
		if  y<100 and (x>510 and x<540):
			y=100
		if (y<370 and y>280) and (x<310 and x>280):
			y=370
		if (y<190 and y>100) and (x<310 and x>280):
			y=190
		if (x>560 and y==460):
			y=550
		if (x<240 and y==370):
			y=460
		if (x>560 and y==280):
			y=370
		if (x<240 and y==190):
			y=280
		if (x>560 and y==100):
			y=190
	
		board=Board()
		board.Draw(gameDisplay)
	  	player.Draw(gameDisplay)	  	
	
											
		for i in range(4):
			if x==(a1[i])and y==550:
				a1[i]=-30
				player.collectCoin()		
			if x==(a2[i]) and y==460:
				a2[i]=-30
				player.collectCoin()
				score=score+1
				
			if x==(a3[i]) and y==370:
				a3[i]=-30
				player.collectCoin()
				
			if x==(a4[i]) and y==280:
				a4[i]=-30
				player.collectCoin()
				
			if x==(a5[i]) and y==190:
				a5[i]=-30
				player.collectCoin()
				
			pygame.draw.circle(gameDisplay,teal,(a1[i],560),10,0)
			pygame.draw.circle(gameDisplay,blue,(a2[i],470),10,0)
			pygame.draw.circle(gameDisplay,brown,(a3[i],380),10,0)
			pygame.draw.circle(gameDisplay,gold,(a4[i],290),10,0)
			pygame.draw.circle(gameDisplay,red,(a5[i],200),10,0)
			#scoreboard("")
			
		player.xp=x
		player.yp=y
		player.Draw(gameDisplay)
		
		player.scoredisplay(gameDisplay)
		
		count=donkey.move(count)
		donkey.Draw(gameDisplay)
		pygame.display.update()
		clock.tick(30)
		

gameloop()
pygame.quit()

	 
