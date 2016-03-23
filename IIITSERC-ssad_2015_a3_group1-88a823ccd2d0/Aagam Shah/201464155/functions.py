import pygame
import draw
import settings
import objects
import classes
import groups
import random
import time

def generate():
		E=[settings.dheight-60,510,370,220,90]		
		l=0
		p=-1
		for j in range(5):
	    		for i in range(8):
	 	
				p+=1       
				block=classes.Coin('coin.png',random.randrange(66,settings.dwidth,50),E[l])
				blockhits=pygame.sprite.spritecollide(block,groups.all_sprites,False)
				if len(blockhits)==0:
		    			groups.block_list.add(block)
		    			groups.all_sprites.add(block)
	    		l+=1 

def checkWall():
	if objects.A.rect.x>settings.dwidth-objects.A.width:
		objects.A.rect.x=settings.dwidth-objects.A.width
	if objects.A.rect.x<=0:
		objects.A.rect.x=0
	if objects.A.rect.y>settings.dheight-objects.A.height:
		objects.A.rect.y=settings.dheight-objects.A.height
	if objects.A.rect.y<=0:
	       objects.A.rect.y=0

def checkCollision(object,bool):
	variable=pygame.sprite.spritecollide(objects.A,object,bool)
	return variable

def death():
	

	settings.lives-=1
	objects.A.rect.x=0
	objects.A.rect.y=settings.dheight-72
	settings.score-=25
	if settings.lives==0:
		settings.gamedisplay.fill(settings.white)
		myfont = pygame.font.SysFont("monospace",80,True)
		label = myfont.render("Game Over", True, (0,0,0))
		settings.gamedisplay.blit(label, (settings.dwidth/2-200,settings.dheight/2-50))
		myfont2 = pygame.font.SysFont("monospace",60,True)
		label2 = myfont2.render("Score: "+ str(settings.score), True, (0,0,0))
		settings.gamedisplay.blit(label2, (settings.dwidth/2-150,settings.dheight/2+50))
		pygame.display.update()
		time.sleep(3)
		quit()

def checkWin():
	
	if objects.A.rect.x>1.2*objects.B.w and objects.A.rect.x<1.2*objects.B.w+100 and objects.A.rect.y<90 and objects.A.rect.y>0:
		settings.gamedisplay.fill(settings.white)
		settings.win=1
		settings.level+=1
		settings.score+=50
		objects.D.imgchange('donkey1.png')
		while settings.cage!=-100:
			settings.cage-=1
			settings.princess-=1
			settings.gamedisplay.fill(settings.white)
			draw.blitndraw()

		settings.gamedisplay.fill(settings.white)
		myfont = pygame.font.SysFont("monospace",100,True)
		label = myfont.render("Level "+ str(settings.level), True, (0,0,0))
		settings.gamedisplay.blit(label, (settings.dwidth/2-150,settings.dheight/2-50))
		pygame.display.update()
		time.sleep(3)	
		settings.win=settings.jump=settings.left=settings.right=settings.count=0
		generate()
		if settings.level%2==0 or settings.timings==500:
			settings.fast+=0.5
		else:
			settings.timings-=500
		objects.A.rect.x=0
		objects.A.rect.y=settings.dheight-72
		objects.D.imgchange('donkey2.png')
		draw.blitndraw()
		while settings.cage!=0:
			settings.cage+=1
			settings.princess+=1
			draw.blitndraw()

def changeimg(source):		
	settings.princessimg=pygame.image.load(source)

