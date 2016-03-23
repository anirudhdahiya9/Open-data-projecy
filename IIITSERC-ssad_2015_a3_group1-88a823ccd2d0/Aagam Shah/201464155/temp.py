import pygame
import time
import random
import os
import draw
import settings
import objects
import classes
import groups
import functions

if __name__=="__main__":
	
	#initializing pygame	
	pygame.init()
	settings.init()
	pygame.font.init()
	
	pygame.display.set_caption('Donkey Kong')

	settings.gamequit=False

	#adding objects to Sprite groups to detect collision
	objectslist=[objects.L1,objects.L2,objects.L3,objects.L4,objects.D,objects.A]
	for i in objectslist:
		groups.character.add(i)
		groups.all_sprites.add(i)

	#defining a user event every four seconds
	pygame.time.set_timer(pygame.USEREVENT,settings.timings)	
	pygame.mixer.music.load('02-the-superstar-saga.mp3')
	pygame.mixer.music.play(100)
	def game_loop():
	    functions.generate()
	 
	    # initializing local variables
	    changex=0
	    changey=0
	    speedx=3
	    man=40
	    k=-1
	    count=0
	    m=0
	    velocity=3
	  
	    while not settings.gamequit:
		
		keys = pygame.key.get_pressed()
	    	if keys[pygame.K_a] and ((objects.A.rect.y>=objects.D.height+80-90 and objects.A.rect.y<=objects.D.height+80-70) or (objects.A.rect.y>=settings.dheight*0.4-90 and objects.A.rect.y<=settings.dheight*0.4-70) or (objects.A.rect.y>=settings.dheight*0.6-90 and objects.A.rect.y<=settings.dheight*0.6-70) or (objects.A.rect.y>=settings.dheight*0.8-90 and objects.A.rect.y<=settings.dheight*0.8-70) or (objects.A.rect.y>=settings.dheight-90 and objects.A.rect.y<=settings.dheight-72)):
			objects.A.rect.x -= 2
			if settings.jump==1:
				settings.left=1
			objects.A.imgchange('mariowalk2.png')
	
		if keys[pygame.K_d] and ((objects.A.rect.y>=objects.D.height+80-90 and objects.A.rect.y<=objects.D.height+80-70) or (objects.A.rect.y>=settings.dheight*0.4-90 and objects.A.rect.y<=settings.dheight*0.4-70) or (objects.A.rect.y>=settings.dheight*0.6-90 and objects.A.rect.y<=settings.dheight*0.6-70) or (objects.A.rect.y>=settings.dheight*0.8-90 and objects.A.rect.y<=settings.dheight*0.8-70) or (objects.A.rect.y>=settings.dheight-90 and objects.A.rect.y<=settings.dheight-72)):
			objects.A.rect.x += 2
			objects.A.imgchange('mariowalk.png')
			if settings.jump==1:
				settings.right=1

		if keys[pygame.K_w] and ((objects.A.rect.x>settings.Allowed[0]-30 and objects.A.rect.x<settings.Allowed[0]+50 and objects.A.rect.y>settings.Allowed[1]-objects.A.height-30 and objects.A.rect.y<settings.Allowed[1]+50) or (objects.A.rect.x>settings.Allowed[2]-30 and objects.A.rect.x<settings.Allowed[2]+50 and objects.A.rect.y>settings.Allowed[3]-objects.A.height-30 and objects.A.rect.y<settings.Allowed[3]+50) or (objects.A.rect.x>settings.Allowed[4]-30 and objects.A.rect.x<settings.Allowed[4]+50 and objects.A.rect.y>settings.Allowed[5]-objects.A.height-30 and objects.A.rect.y<settings.Allowed[5]+50) or (objects.A.rect.x>settings.Allowed[6]-30 and objects.A.rect.x<settings.Allowed[6]+50 and objects.A.rect.y>settings.Allowed[7]-objects.A.height-20 and objects.A.rect.y<settings.Allowed[7]+50)):
			objects.A.rect.y-=1
			#A.imgchange('marioback.png')

		if keys[pygame.K_s] and ((objects.A.rect.x>settings.Allowed[0]-30 and objects.A.rect.x<settings.Allowed[0]+50 and objects.A.rect.y>settings.Allowed[1]-objects.A.height-50 and objects.A.rect.y<settings.Allowed[1]+40) or (objects.A.rect.x>settings.Allowed[2]-30 and objects.A.rect.x<settings.Allowed[2]+50 and objects.A.rect.y>settings.Allowed[3]-objects.A.height-50 and objects.A.rect.y<settings.Allowed[3]+40) or (objects.A.rect.x>settings.Allowed[4]-30 and objects.A.rect.x<settings.Allowed[4]+50 and objects.A.rect.y>settings.Allowed[5]-objects.A.height-50 and objects.A.rect.y<settings.Allowed[5]+40) or (objects.A.rect.x>settings.Allowed[6]-30 and objects.A.rect.x<settings.Allowed[6]+50 and objects.A.rect.y>settings.Allowed[7]-objects.A.height-50 and objects.A.rect.y<settings.Allowed[7]+46)) :
			objects.A.rect.y+=1
			#A.imgchange('marioback.png')

		for event in pygame.event.get():
			man+=30
			if event.type==pygame.QUIT:
				settings.gamequit=True
			if event.type==pygame.KEYDOWN:
			   
				if event.key==pygame.K_SPACE and settings.jump!=1 and ((objects.A.rect.y>=objects.D.height+80-90 and objects.A.rect.y<=objects.D.height+80-70) or (objects.A.rect.y>=settings.dheight*0.4-90 and objects.A.rect.y<=settings.dheight*0.4-70) or (objects.A.rect.y>=settings.dheight*0.6-90 and objects.A.rect.y<=settings.dheight*0.6-70) or (objects.A.rect.y>=settings.dheight*0.8-90 and objects.A.rect.y<=settings.dheight*0.8-70) or (objects.A.rect.y>=settings.dheight-90 and objects.A.rect.y<=settings.dheight-70)):
				    changey=-5
				    changex=0
				    save=objects.A.rect.y
				    settings.jump=1
				if event.key==pygame.K_q:
					settings.gamequit=True
	
			if event.type==pygame.USEREVENT:
	 		 	k+=1               
			 	settings.ball.append('0')
			 	settings.ball[k]=classes.Fireball('firen.png',objects.D.rect.x,110)
				settings.ball[k].start(settings.fast,0,0)
			 	groups.fireball.add(settings.ball[k])
		m=0	
		while m<=k:
			settings.ball[m].movement()
			m+=1

		if ((objects.A.rect.y>=objects.D.height+80-90 and objects.A.rect.y<=objects.D.height+80-70 and objects.A.rect.x>3*296) or (objects.A.rect.y>=settings.dheight*0.4-90 and objects.A.rect.y<=settings.dheight*0.4-70 and objects.A.rect.x>2*296 and objects.A.rect.x<3*296-195) or (objects.A.rect.y>=settings.dheight*0.6-90 and objects.A.rect.y<=settings.dheight*0.6-70 and ((objects.A.rect.x>296 and objects.A.rect.x<2*296-230) or (objects.A.rect.x>3*296+40 and objects.A.rect.x<settings.dwidth)))):
			settings.fall=1

		if settings.fall==1:
			objects.A.falling()

		if objects.A.rect.x>1.2*296+40:
			functions.changeimg('princess2.png')
		else:
			functions.changeimg('princess.png')

		if settings.jump==1 and velocity>0 and settings.count==0:
			objects.A.rect.y-=velocity
			if settings.right==1:
				objects.A.rect.x+=2
			elif settings.left==1:
				objects.A.rect.x-=2
			else:
				objects.A.rect.x+=0
			velocity-=0.1
	
		elif settings.jump==1 and objects.A.rect.y<save:
			velocity+=0.1			
			settings.count=1		
			objects.A.rect.y+=velocity
			settings.count+=1
			if settings.left==1:
				objects.A.rect.x-=2
			elif settings.right==1:
				objects.A.rect.x+=2
			else:
				objects.A.rect.x+=0
			
		else:
			if objects.A.rect.y==71:
				objects.A.rect.y=68
			settings.count=settings.jump=settings.left=settings.right=0
			velocity=3
	   

		functions.checkWall()

		blockhit=functions.checkCollision(groups.block_list,True)

		for blocks in blockhit:
		     settings.score+=5

		firehit=functions.checkCollision(groups.fireball,False)
		donkeyhit=functions.checkCollision(groups.donkey,False)

		if len(firehit)!=0 or len(donkeyhit)!=0:
			settings.jump=settings.right=settings.count=settings.left=settings.fall=0		
			functions.death()

		objects.D.move()
		functions.checkWin()
		changex=0
		changey=0
		draw.blitndraw()



	game_loop()

