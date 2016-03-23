import pygame

def init():
	global score
	global lives
	global cage
	global princess
	global gamequit
	global fall
	global jump
	global win
	global flag2
	global Allowed
	global ball
	global level
	global dwidth
	global dheight
	global gamedisplay
	global fireimg
	global brickimg
	global heroimg
	global ladderimg
	global villainimg
	global coinimg
	global princessimg
	global cageimg
	global white
	global clock
	global fast
	global timings

	white=(255,255,255)
    	score=0
	lives=3
	cage=0
	princess=25
	gamequit=False
	fall=0
	jump=0
	win=0
	flag2=0
	dwidth=1000
	dheight=700
	Allowed=[dwidth*0.7,dheight-110,dwidth*0.8,170,dwidth*0.5,310,dwidth*0.2,440]
	ball=[]
	level=1
	gamedisplay=pygame.display.set_mode((dwidth,dheight))
	fireimg=pygame.image.load('firen.png')
	brickimg=pygame.image.load('brickn.jpg')
	heroimg=pygame.image.load('mariowalk.png')
	ladderimg=pygame.image.load('laddern.png')
	villainimg=pygame.image.load('donkey2.png')
	coinimg=pygame.image.load('coin.png')
	princessimg=pygame.image.load('princess.png')
	cageimg=pygame.image.load('cage2.png')
	clock=pygame.time.Clock()
	fast=1
	timings=4000
