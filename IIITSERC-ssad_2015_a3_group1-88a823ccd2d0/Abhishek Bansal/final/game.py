#!/usr/bin/python
import pygame,sys,time
from pygame.locals import *
from constants import *
from board import *
from characters import *
pygame.mixer.init()
pygame.time.set_timer(USEREVENT,FIREBALL_TIME*1000)
def main(sc):
	pygame.init()
	FPS = 30
	fpsClock = pygame.time.Clock()
	mygame=board(1100,750,20,18)
	for i in range (0,MIN_COINS):
		mygame.genCoin()
	mygame.createGame()
	DISPLAY=mygame.DISP
	myplayer=Player(100,710,sc)
	mydonkey=Donkey(100,45,50,70)
	princess=Princess(350,30,25,25)
	myfireball=fireball(150,90,20,30,'R')
	mydonkey.create(mygame)
	myplayer.create(mygame)
	princess.create(mygame)
	for b in mygame.balls:
		b.create(mygame)
	while mygame.gameend(myplayer)==False:
		if myplayer.gameWon(princess):
			pygame.mixer.music.load('win.wav')
			pygame.mixer.music.play()
			pygame.time.wait(100)
			main(myplayer.score+50)
		for b in mygame.balls:
			if myplayer.checkCollision(b):
				myplayer.Collide(mygame)
                if myplayer.checkCollision(mydonkey):
                                myplayer.Collide(mygame)
		for event in pygame.event.get():
			if event.type == QUIT:
				pygame.quit()
				sys.exit()
			if event.type == pygame.USEREVENT:
				mygame.genFireball()
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_RIGHT:
					myplayer.move(mygame,'R',1)
				elif event.key == pygame.K_LEFT:
					myplayer.move(mygame,'L',1)
				elif event.key == pygame.K_UP:
					myplayer.move(mygame,'U',1)
				elif event.key == pygame.K_DOWN:
					myplayer.move(mygame,'D',1)
				elif event.key ==pygame.K_SPACE:
					if myplayer.canjump(mygame):
						myplayer.jump_new(15)
		keys_pressed = pygame.key.get_pressed()
		if keys_pressed[K_RIGHT]:
			myplayer.move(mygame,'R',PLAYER_SPEED)
		elif keys_pressed[K_LEFT]:
			myplayer.move(mygame,'L',PLAYER_SPEED)
		elif keys_pressed[K_UP]:
			myplayer.move(mygame,'U',PLAYER_SPEED_UP)
		elif keys_pressed[K_DOWN]:
			myplayer.move(mygame,'D',PLAYER_SPEED_UP)
		myplayer.gravity_new()
		myplayer.fall()
		myplayer.Collectcoin(mygame)
		mydonkey.move(mygame,300)
		for b in mygame.balls:
			b.move(mygame)
			b.fall()
		mygame.createGame()
		myplayer.create(mygame)
		mydonkey.create(mygame)
		princess.create(mygame)
		for b in mygame.balls:
			b.create(mygame)
		pygame.display.update()
		fpsClock.tick(FPS)
	mygame.DISP.fill(BLACK)
	fontobj = pygame.font.Font('freesansbold.ttf',32)
	score = fontobj.render("Score: " + str(myplayer.score),True,GREEN,BLUE)
	score_rect = score.get_rect()
	score_rect.left,score_rect.top=0,0
	mygame.DISP.blit(score,score_rect)
	sobj = fontobj.render('Game Over',True,GREEN,BLUE)
	robj = sobj.get_rect()
	robj.center = (200,150)
	mygame.DISP.blit(sobj,robj)
	pygame.display.flip()
	pygame.mixer.music.load('gameover.mp3')
	pygame.mixer.music.play()
	time.sleep(3)
	pygame.quit()
	sys.exit()
if __name__ == "__main__":
	main(0)
