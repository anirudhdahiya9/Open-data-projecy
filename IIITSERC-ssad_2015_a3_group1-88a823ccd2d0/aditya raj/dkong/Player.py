import pygame
from pygame.locals import *
import time
import random
from Person import *
from functions import *
FPS=18                                                                                                                                    
clock=pygame.time.Clock()
red=(255,0,0)


class Player(Person):
        #fall left
	def falll(self,dk,frame,coins,fireballs,queen,score,lives,level):
		i=0
		while i<5:
			if i<2:
			        self.lead_x-=frame.block_size
			self.lead_y+=frame.h/5
			frame.drawgrid()
			coins.gen(frame)
		        for elem in fireballs:
		                if elem.lead_x==0 and elem.lead_y==0:
		                        fireballs.remove(elem)

		                elem.move(frame)
		                frame.gameDisplay.blit(frame.fireimg, (elem.lead_x,elem.lead_y))
		        
		        for t in dk:
			        t.move(frame)
		                frame.gameDisplay.blit(frame.donkeyimg, (t.lead_x,t.lead_y))

		        frame.gameDisplay.blit(frame.queenimg, (queen.lead_x,queen.lead_y))
		        frame.gameDisplay.blit(frame.playimg, (self.lead_x,self.lead_y))
		        s="Lives: "+str(lives)
		        show_lives(s,red,frame)
		        s2="Score: "+str(score)
		        show_score(s2,red,frame)
		        s3="Level: "+str(level)
		        show_level(s3,red,frame)
			pygame.display.update()
			clock.tick(FPS)
			i+=1

	
        #fall right
        def fallr(self,dk,frame,coins,fireballs,queen,score,lives,level):
		i=0
		while i<5:
			if i<2:
			        self.lead_x+=frame.block_size
			self.lead_y+=frame.h/5
			frame.drawgrid()
			coins.gen(frame)
		        for elem in fireballs:
		                if elem.lead_x==0 and elem.lead_y==0:
		                        fireballs.remove(elem)
		                

		                elem.move(frame)
		                frame.gameDisplay.blit(frame.fireimg, (elem.lead_x,elem.lead_y))
		                
		        for t in dk:
			        t.move(frame)
		                frame.gameDisplay.blit(frame.donkeyimg, (t.lead_x,t.lead_y))
		        
		        frame.gameDisplay.blit(frame.queenimg, (queen.lead_x,queen.lead_y))
		        frame.gameDisplay.blit(frame.playimg, (self.lead_x,self.lead_y))
		        s="Lives: "+str(lives)
		        show_lives(s,red,frame)
		        s2="Score: "+str(score)
		        show_score(s2,red,frame)
		        s3="Level: "+str(level)
		        show_level(s3,red,frame)
			pygame.display.update()
			clock.tick(FPS)
			i+=1

        
        #jump left
	def jumpl(self,dk,frame,coins,fireballs,queen,score,lives,level):
		i=0
		while i<4:
			self.lead_x-=2*frame.block_size
			if i<2:
			        self.lead_y-=2*frame.block_size
			else:
			        self.lead_y+=2*frame.block_size
			frame.drawgrid()
			coins.gen(frame)
		        for elem in fireballs:
		                if elem.lead_x==0 and elem.lead_y==0:
		                        fireballs.remove(elem)
		                

		                elem.move(frame)
		                frame.gameDisplay.blit(frame.fireimg, (elem.lead_x,elem.lead_y))
		        
		        for t in dk:
		                t.move(frame)
		                frame.gameDisplay.blit(frame.donkeyimg, (t.lead_x,t.lead_y))
		        
		        frame.gameDisplay.blit(frame.queenimg, (queen.lead_x,queen.lead_y))
		        frame.gameDisplay.blit(frame.playimg, (self.lead_x,self.lead_y))
		        s="Lives: "+str(lives)
		        show_lives(s,red,frame)
		        s2="Score: "+str(score)
		        show_score(s2,red,frame)
		        s3="Level: "+str(level)
		        show_level(s3,red,frame)
			pygame.display.update()
			clock.tick(FPS)
			i+=1


        #jump right
	def jumpr(self,dk,frame,coins,fireballs,queen,score,lives,level):
		i=0
		while i<4:
			self.lead_x+=2*frame.block_size
			if i<2:
			        self.lead_y-=2*frame.block_size
			else:
			        self.lead_y+=2*frame.block_size
			frame.drawgrid()
			coins.gen(frame)
		        for elem in fireballs:
		                if elem.lead_x==0 and elem.lead_y==0:
		                        fireballs.remove(elem)
		                

		                elem.move(frame)
		                frame.gameDisplay.blit(frame.fireimg, (elem.lead_x,elem.lead_y))
		                
		        for t in dk:
			        t.move(frame)
		                frame.gameDisplay.blit(frame.donkeyimg, (t.lead_x,t.lead_y))
		        
		        frame.gameDisplay.blit(frame.queenimg, (queen.lead_x,queen.lead_y))
		        frame.gameDisplay.blit(frame.playimg, (self.lead_x,self.lead_y))
		        s="Lives: "+str(lives)
		        show_lives(s,red,frame)
		        s2="Score: "+str(score)
		        show_score(s2,red,frame)
		        s3="Level: "+str(level)
		        show_level(s3,red,frame)
			pygame.display.update()
			clock.tick(FPS)
			i+=1

        
        #jump up
	def jump(self,dk,frame,coins,fireballs,queen,score,lives,level):
		i=0
		while i<4:
			if i<2:
			        self.lead_y-=2*frame.block_size
			else:
			        self.lead_y+=2*frame.block_size
			frame.drawgrid()
			coins.gen(frame)
		        for elem in fireballs:
		                if elem.lead_x==0 and elem.lead_y==0:
		                        fireballs.remove(elem)
		                

		                elem.move(frame)
		                frame.gameDisplay.blit(frame.fireimg, (elem.lead_x,elem.lead_y))
		        
		        for t in dk:
		                t.move(frame)
		                frame.gameDisplay.blit(frame.donkeyimg, (t.lead_x,t.lead_y))
		        
		        frame.gameDisplay.blit(frame.queenimg, (queen.lead_x,queen.lead_y))
		        frame.gameDisplay.blit(frame.playimg, (self.lead_x,self.lead_y))
		        s="Lives: "+str(lives)
		        show_lives(s,red,frame)
		        s2="Score: "+str(score)
		        show_score(s2,red,frame)
		        s3="Level: "+str(level)
		        show_level(s3,red,frame)
			pygame.display.update()
			clock.tick(FPS)
			i+=1

