import pygame
import time
import random

pygame.init()

#show message after completion of a level
def message_to_screen(msg,color,frame):
         screen_text=font.render(msg, True, color)
         frame.gameDisplay.blit(screen_text, [frame.display_width/3,frame.display_height/2])


#show the current score of player
def show_score(msg,color,frame):
         screen_text=font.render(msg, True, color)
         frame.gameDisplay.blit(screen_text, [3*frame.display_width/4,5*frame.block_size])


#show the number of lives of player
def show_lives(msg,color,frame):
         screen_text=font.render(msg, True, color)
         frame.gameDisplay.blit(screen_text, [5*frame.block_size,5*frame.block_size])

#show the current level
def show_level(msg,color,frame):
         screen_text=font.render(msg, True, color)
         frame.gameDisplay.blit(screen_text, [frame.display_width/2-4*frame.block_size,4*frame.block_size])


#show the score after completion of mission
def level_score(msg,color,frame):
         screen_text=font.render(msg, True, color)
         frame.gameDisplay.blit(screen_text, [frame.display_width/2-4*frame.block_size,frame.display_height/2+2*frame.block_size])


#for player and donkey
class Person:
        def __init__(self,lead_x,lead_y,lead_x_change,lead_y_change):
                self.lead_x=lead_x
                self.lead_y=lead_y
                self.lead_x_change=lead_x_change
                self.lead_y_change=lead_y_change


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
		                
		                if checkcollision(self.lead_x,self.lead_y,elem.lead_x,elem.lead_y,frame)==1:
		                        lives-=1
		                        if lives<=0:
		                                gameover=True
		                        else:
		                                gameloop(lives,0,level)
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
		                
		                if checkcollision(self.lead_x,self.lead_y,elem.lead_x,elem.lead_y,frame)==1:
		                        lives-=1
		                        if lives<=0:
		                                gameover=True
		                        else:
		                                gameloop(lives,0,level)
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
		                
		                if checkcollision(self.lead_x,self.lead_y,elem.lead_x,elem.lead_y,frame)==1:
		                        lives-=1
		                        if lives<=0:
		                                gameover=True
		                        else:
		                                gameloop(lives,0,level)
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
		                
		                if checkcollision(self.lead_x,self.lead_y,elem.lead_x,elem.lead_y,frame)==1:
		                        lives-=1
		                        if lives<=0:
		                                gameover=True
		                        else:
		                                gameloop(lives,0,level)
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
		                
		                if checkcollision(self.lead_x,self.lead_y,elem.lead_x,elem.lead_y,frame)==1:
		                        lives-=1
		                        if lives<=0:
		                                gameover=True
		                        else:
		                                gameloop(lives,0,level)
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


class Donkey(Person):
        #controls donkey movement
        def move(self,frame):
                if self.lead_x>4*frame.w-5*frame.block_size:
                        self.lead_x-=self.lead_x_change
                        self.lead_x_change=-frame.block_size/2

                if self.lead_x<6*frame.block_size:
                        self.lead_x-=self.lead_x_change
                        self.lead_x_change=frame.block_size/2
                self.lead_x+=self.lead_x_change



class Fireball:
        
        def __init__(self,lead_x,lead_y,lead_x_change,lead_y_change):
                self.lead_x=lead_x
                self.lead_y=lead_y
                self.lead_x_change=lead_x_change
                self.lead_y_change=lead_y_change
        
        #controls fireball movement
        def move(self,frame):
                if self.lead_x==frame.block_size:
                        if self.lead_y==frame.display_height-2*frame.block_size: #for respawning
                                lead_x=0
                                lead_y=0
                                lead_x_change=0
                                lead_y_change=0

                        else:
                                self.lead_x_change=-self.lead_x_change #for checking left wall

                if self.lead_x==frame.display_width-2*frame.block_size:  #for checking right wall
                        self.lead_x_change=-self.lead_x_change

                if frame.checkfloor(self.lead_x,self.lead_y)==1:  #for  checking floor
                        if self.lead_y_change!=0:
                                self.lead_y_change=0
                                x=random.randrange(0,2)
                                if x==0:
                                        self.lead_x_change=frame.block_size/2
                                else:
                                        self.lead_x_change=-frame.block_size/2
                        
                        self.lead_x+=self.lead_x_change
                        self.lead_y+=self.lead_y_change
                
                elif frame.checkfloor(self.lead_x,self.lead_y)==0:  #for checking fall
                        if frame.checkdown(self.lead_x,self.lead_y)==1:
                                x=random.randrange(0,3)
                                if x==0:
                                        self.lead_x_change=0
                                        self.lead_y_change=frame.block_size
                                        self.lead_y+=self.lead_y_change
                                else:
                                        self.lead_x+=self.lead_x_change
                                        self.lead_y+=self.lead_y_change
                                        
                        else:
                                if self.lead_y_change!=0:
                                        self.lead_y_change=0
                                        x=random.randrange(0,2)
                                        if x==0:
                                                self.lead_x_change=frame.block_size/2
                                        else:
                                                self.lead_x_change=-frame.block_size/2

                                self.lead_x+=self.lead_x_change
                                self.lead_y+=self.lead_y_change

                elif frame.checkfloor(self.lead_x,self.lead_y)==2: #floor movement
                        self.lead_x+=self.lead_x_change
                        self.lead_y_change=frame.h/5
                        self.lead_y+=self.lead_y_change

                elif frame.checklad(self.lead_x,self.lead_y)==1:  #ladder movement
                        self.lead_x+=self.lead_x_change
                        self.lead_y+=self.lead_y_change

                else:                                     #falling
                        self_lead_x_change=0
                        self.lead_x+=self.lead_x_change
                        self.lead_y+=self.lead_y_change
                
                if self.lead_y>frame.floorg:
                        self.lead_y=frame.floorg
                        self.lead_y_change=0
                        self.lead_x_change=frame.block_size/2






class Board:
	def __init__(self):
		self.block_size=20

		self.display_width=1600
		self.display_height=1000
		
		self.gameDisplay=pygame.display.set_mode((self.display_width, self.display_height))
		pygame.display.set_caption('DonkeyKong')
		
		self.h=round(self.display_height/140)*20
		self.w=round(self.display_width/100)*20
		
		self.floorg=self.display_height-2*self.block_size
		self.floors1=[self.display_height-self.h-self.block_size,self.display_height-3*self.h-self.block_size,self.display_height-5*self.h-self.block_size]
		self.floors2=[self.display_height-2*self.h-self.block_size,self.display_height-4*self.h-self.block_size]
		self.floort=self.display_height-6*self.h-self.block_size
                
                #images
                self.fireimg=pygame.image.load('fireballnn.jpeg')
                self.donkeyimg=pygame.image.load('donkeyn.jpeg')
                self.coinimg=pygame.image.load('coinn.jpeg')
                self.queenimg=pygame.image.load('queenn.jpeg')
                self.playimg=pygame.image.load('hulk.jpeg')
        
        #drawing whole grid
	def drawgrid(self):
                self.gameDisplay.fill(black)
                ladimg=pygame.image.load('lader.jpeg')

                #ladders
                self.gameDisplay.blit(ladimg, (3*self.w,self.display_height-self.h))
                self.gameDisplay.blit(ladimg, (3*self.w,self.display_height-3*self.h))
                self.gameDisplay.blit(ladimg, (3*self.w,self.display_height-5*self.h))
                self.gameDisplay.blit(ladimg, (2*self.w,self.display_height-2*self.h))
                self.gameDisplay.blit(ladimg, (2*self.w,self.display_height-4*self.h))
                self.gameDisplay.blit(ladimg, (2*self.w,self.display_height-6*self.h))

               
                floorimg=pygame.image.load('floor.jpeg')
                floor2img=pygame.image.load('floor2.jpeg')
               #floors
                self.gameDisplay.blit(floorimg, (0,self.display_height-self.h))
                self.gameDisplay.blit(floorimg, (0,self.display_height-3*self.h))
                self.gameDisplay.blit(floorimg, (0,self.display_height-5*self.h))
                self.gameDisplay.blit(floorimg, (self.w,self.display_height-2*self.h))
                self.gameDisplay.blit(floorimg, (self.w,self.display_height-4*self.h))
                self.gameDisplay.blit(floor2img, (self.w,self.display_height-6*self.h))

                #boundaries
                pygame.draw.rect(self.gameDisplay,brown,[0,0,self.display_width,self.block_size])
                pygame.draw.rect(self.gameDisplay,brown,[0,0,self.block_size,self.display_height])
                pygame.draw.rect(self.gameDisplay,brown,[self.display_width-self.block_size,0,self.block_size,self.display_height])
                pygame.draw.rect(self.gameDisplay,brown,[0,self.display_height-self.block_size,self.display_width,self.block_size])
                
                #cage
                cageimg=pygame.image.load('cage.jpeg')
                self.gameDisplay.blit(cageimg, (self.w,self.block_size))
                self.gameDisplay.blit(cageimg, (3*self.w-self.block_size,self.block_size))
        
        #checking floor contact
	def checkfloor(self,lead_x,lead_y):
		if lead_y in self.floors1:
		        if lead_x!=2*self.w and lead_x!=2*self.w+self.block_size and lead_x!=3*self.w and lead_x!=3*self.w+self.block_size:
		                if lead_x<=4*self.w:
		                        return 1
		                else:
		                        return 2
		        else:
		                return 0
		
		elif lead_y in self.floors2:
		        if lead_x!=2*self.w and lead_x!=2*self.w+self.block_size and lead_x!=3*self.w and lead_x!=3*self.w+self.block_size:
		                if lead_x>=self.w:
		                        return 1
		                else:
		                        return 2
		        else:
		                return 0

		elif lead_y==self.floorg:
		        if lead_x!=3*self.w and lead_x!=3*self.w+self.block_size:
		                return 1
		        else:
		                return 0
		
		elif lead_y==self.floort:
		        if lead_x!=2*self.w and lead_x!=2*self.w+self.block_size:
		                if lead_x>self.w and lead_x<3*self.w-self.block_size:
		                        return 1
		                elif lead_x<=self.w:
		                        return 2
		                else:
		                        return 3
		        else:
		                return 0

        
        #checking ladder base
	def checkup(self,lead_x,lead_y):
		if lead_y in self.floors1:
		        if lead_x==2*self.w or lead_x==2*self.w+self.block_size:
		                return 1
		        else:
		                return 0
		elif lead_y==self.floorg or lead_y in self.floors2:
		        if lead_x==3*self.w or lead_x==3*self.w+self.block_size:
		                return 1
		        else:
		                return 0
		return 0

        
        #checking ladder top
	def checkdown(self,lead_x,lead_y):
		if lead_y in self.floors2 or lead_y==self.floort:
		        if lead_x==2*self.w or lead_x==2*self.w+self.block_size:
		                return 1
		        else:
		                return 0
		elif lead_y in self.floors1:
		        if lead_x==3*self.w or lead_x==3*self.w+self.block_size:
		                return 1
		        else:
		                return 0
		return 0
        
        #checking ladder
	def checklad(self,lead_x,lead_y):
		if lead_y not in self.floors1 or lead_y!=self.floort and lead_y!=self.floorg and lead_y not in self.floors2:
		        return 1
		return 0






class coinframe:
        def __init__(self,display_width,display_height,w,h,block_size):
                x=0
                athick=20
                self.coin=[]
                while x<25:  #random coin generation on floors
                        randax=round(random.randrange(athick,display_width-2*athick)/20.0)*20.0
                        randay=random.randrange(0,6)
                        if randax<w:
                                 if randay==2 or randay==4 or randay==6:
                                        randay-=1
                        elif randax>3*w:
                                if randax<4*w:
                                        if randay==6:
                                                randay-=1
                                else:
                                        if randay==1 or randay==3 or randay==5:
                                                randay-=1
                
                        new=[]
                        new.append(randax)
                        if randay==0:
                                new.append(display_height-2*block_size)
                        else:
                                new.append(display_height-randay*h-block_size)
                        self.coin.append(new)
                        x+=1
        
        #drawing randomly generated coins on grid
        def gen(self,frame): 
                for elem in self.coin:
                        frame.gameDisplay.blit(frame.coinimg, (elem[0],elem[1]))



#check collision of 2 objects
def checkcollision(x,y,a,b,frame):
        if abs(x-a)<=frame.block_size and abs(y-b)<frame.block_size:
                return 1
        else:
                return 0


#check coin collision
def collectcoin(x,y,a,b,frame):
        if abs(x-a)<frame.block_size and abs(y-b)<frame.block_size:
                return 1
        else:
                return 0


#check wall collision
def checkwall(x,y,frame):
        if x>frame.display_width-2*frame.block_size:
                return 1
        if x<frame.block_size:
                return 2
        return 0


#check airspace contact above ladders
def checkair(x,y,frame):
        if x==3*frame.w or x==3*frame.w+frame.block_size:
                if (y < frame.display_height-frame.h-frame.block_size and y > frame.display_height-2*frame.h-frame.block_size ) or (y < frame.display_height-3*frame.h-frame.block_size  and y > frame.display_height-4*frame.h-frame.block_size ) or (y < frame.display_height-5*frame.h-frame.block_size ):
                        return 1
                
        if x==2*frame.w or x==2*frame.w+frame.block_size:
                if (y > frame.display_height-frame.h-frame.block_size ) or (y < frame.display_height-2*frame.h-frame.block_size  and y > frame.display_height-3*frame.h-frame.block_size ) or (y < frame.display_height-4*frame.h-frame.block_size  and y > frame.display_height-5*frame.h-frame.block_size ) or y < frame.display_height-6*frame.h-frame.block_size :
                        return 1
        return 0



#the game
def gameloop(lives,score,level):

        dk=[]
        frame=Board()

        i=0
        while i<level: #donkey
                if i==0:
                        dead_x=8*frame.block_size
                if i==1:
                        dead_x=40*frame.block_size
                if i==2:
                        dead_x=20*frame.block_size

                dead_y=frame.display_height-5*frame.h-frame.block_size
                dead_x_change=frame.block_size/2
                dk.append(Donkey(dead_x,dead_y,dead_x_change,0))
                i+=1

        
        lead_x=frame.block_size
        lead_x_change=0
        lead_y=frame.display_height-2*frame.block_size
        lead_y_change=0
        player=Player(lead_x,lead_y,lead_x_change,lead_y_change)  #the player
        
        queen=Player(2*frame.w+frame.w/2,frame.floort,0,0)  #the queen

	fireballs=[]   #first fireball
        fire=Fireball(dead_x,dead_y,-dead_x_change,0)
        fireballs.append(fire)
        
        #coins
        coins=coinframe(frame.display_width,frame.display_height,frame.w,frame.h,frame.block_size)

        gameexit=False
        gameover=False
        gamewon=False

        pre=0
        count=0
        while not gameexit:
                #when lives=0
                while gameover == True:                                                                                                   
                        frame.gameDisplay.fill(white)
                        message_to_screen("Game over, press C to play again or Q to quit",red,frame)
                        s="Your Final Score: " + str(score)
                        level_score(s,blue,frame)
                        pygame.display.update()
                        for event2 in pygame.event.get():
                                if event2.type==pygame.QUIT:
                                        gameover=False
                                        gameexit=True
                                if event2.type==pygame.KEYDOWN:
                                        if event2.key==pygame.K_q:
                                                gameexit=True
                                                gameover=False
                                        elif event2.key==pygame.K_c:
                                                gameloop(3,0,1)
                
                #when winning a level
                while gamewon == True:                                                                                                   
                        frame.gameDisplay.fill(white)
                        if level<3:
                                message_to_screen("You Won!!!, press C to play next level or Q to quit",green,frame)
                                s="Your Score this level: " + str(score)
                                level_score(s,blue,frame)
                                pygame.display.update()
                                for event2 in pygame.event.get():
                                        if event2.type==pygame.QUIT:
                                                gamewon=False
                                                gameexit=True
                                        
                                        if event2.type==pygame.KEYDOWN:
                                                if event2.key==pygame.K_q:
                                                        gameexit=True
                                                        gamewon=False
                                                elif event2.key==pygame.K_c:
                                                        gameloop(3,score+50,level+1)

                        else:  #when winning all levels
                                message_to_screen("You Won the game!!!!!, press C to play again or Q to quit",green,frame)
                                s="Your Final Score: " + str(score)
                                level_score(s,blue,frame)
                                pygame.display.update()
                                for event2 in pygame.event.get():
                                        if event2.type==pygame.QUIT:
                                                gamewon=False
                                                gameexit=True
                                        
                                        if event2.type==pygame.KEYDOWN:
                                                if event2.key==pygame.K_q:
                                                        gameexit=True
                                                        gamewon=False
                                                elif event2.key==pygame.K_c:
                                                        gameloop(3,0,1)


                if level==1:
                        div=300
                if level==2:
                        div=200
                if level==3:
                        div=150
                if count%150==0: #generate fireballs
                        for t in dk:
                                fire=Fireball(t.lead_x,t.lead_y,-t.lead_x_change,0)
                                fireballs.append(fire)
                
                for event in pygame.event.get(): #input control movement
                        if frame.checkfloor(player.lead_x,player.lead_y)==1:
                                state=0
                        elif frame.checkup(player.lead_x,player.lead_y)==1:
                                state=1
                        elif frame.checkdown(player.lead_x,player.lead_y)==1:
                                state=2
                        elif frame.checklad(player.lead_x,player.lead_y)==1:
                                state=3
                        
                        if event.type == pygame.QUIT:
                                gameexit = True
                        if event.type == pygame.KEYDOWN:
                                if event.key == pygame.K_q:
                                        gameexit=True
                                elif event.key == pygame.K_a:  #move left
                                        pre=-1
                                        if state!=3:
                                                player.lead_x_change=-frame.block_size
                                                player.lead_y_change=0
                                                pre=-1
                                
                                elif event.key == pygame.K_d:   #move right
                                        pre=1
                                        if state!=3:
                                                player.lead_x_change=frame.block_size
                                                player.lead_y_change=0
                                
                                elif event.key == pygame.K_w:   #move up
                                        if state==1 or state==3:
                                                player.lead_y_change=-frame.block_size
                                                player.lead_x_change=0
                                
                                elif event.key == pygame.K_s:  #move down
                                        if state==2 or state==3:
                                                player.lead_y_change=frame.block_size
                                                player.lead_x_change=0

                                elif event.key==pygame.K_SPACE and state!=3:   #jump movements
                                        if pre==-1:
                                                player.jumpl(dk,frame,coins,fireballs,queen,score,lives,level)
                                                
                                        elif pre==1:
                                                player.jumpr(dk,frame,coins,fireballs,queen,score,lives,level)
                                        
                                        else:
                                                player.jump(dk,frame,coins,fireballs,queen,score,lives,level)

                        if event.type == pygame.KEYUP:  #when key is released
                                if event.key == pygame.K_a or event.key == pygame.K_d:
                                        player.lead_x_change=0
#                                        pre=0
                                elif event.key == pygame.K_s or event.key == pygame.K_w:
                                        player.lead_y_change=0
 #                                       pre=0
                

                pygame.display.update()
                player.lead_x=player.lead_x+player.lead_x_change
                if checkwall(player.lead_x,player.lead_y,frame)==1:   #check right wall
                        player.lead_x=frame.display_width-2*frame.block_size
                
                if checkwall(player.lead_x,player.lead_y,frame)==2:  #check left wall
                        player.lead_x=frame.block_size
                

                if player.lead_y in frame.floors1:  #checks falling
                        if frame.checkfloor(player.lead_x,player.lead_y)==2: #left fall
                                player.fallr(dk,frame,coins,fireballs,queen,score,lives,level)
                        
                elif player.lead_y in frame.floors2:
                        if frame.checkfloor(player.lead_x,player.lead_y)==2: #right fall
                                player.falll(dk,frame,coins,fireballs,queen,score,lives,level)
                
                elif player.lead_y==frame.floort: #check cage collision
                        if frame.checkfloor(player.lead_x,player.lead_y)==2:
                                player.lead_x=player.lead_x-player.lead_x_change
                        
                        elif frame.checkfloor(player.lead_x,player.lead_y)==3:
                                player.lead_x=player.lead_x-player.lead_x_change
                
                player.lead_y=player.lead_y+player.lead_y_change
                
                
                if checkair(player.lead_x,player.lead_y,frame)==1: #check airspace above ladders
                                player.lead_y=player.lead_y-player.lead_y_change 
                
                if player.lead_y>=frame.display_height-2*frame.block_size:  #check ground
                        player.lead_y=frame.display_height-2*frame.block_size
                
                
                frame.drawgrid()
                coins.gen(frame)
                for elem in coins.coin: #coin collection
                        if collectcoin(player.lead_x,player.lead_y,elem[0],elem[1],frame)==1:
                                score+=5
                                coins.coin.remove(elem)
                        
                
                for t in dk: #donkey movement
                        t.move(frame)

                for elem in fireballs: #fireballs movements
                        if elem.lead_x==0 and elem.lead_y==0:
                                fireballs.remove(elem)
                        
                        if checkcollision(player.lead_x,player.lead_y,elem.lead_x,elem.lead_y,frame)==1:  #fireball collision
                                lives-=1
                                if lives<=0:
                                        gameover=True
                                else:
                                        gameloop(lives,score-25,level)

                        elem.move(frame)
                        frame.gameDisplay.blit(frame.fireimg, (elem.lead_x,elem.lead_y))
                        
                if player.lead_x==queen.lead_x and player.lead_y==queen.lead_y:  #rescuing queen
                        gamewon=True
                
                for t in dk:
                        frame.gameDisplay.blit(frame.donkeyimg, (t.lead_x,t.lead_y))
                
                for t in dk: #donkey collision
                        if checkcollision(player.lead_x,player.lead_y,t.lead_x,t.lead_y,frame)==1:
                                lives-=1
                                if lives==0:
                                        gameover=True
                                else:
                                        gameloop(lives,0,level)

                
                frame.gameDisplay.blit(frame.queenimg, (queen.lead_x,queen.lead_y))
                
                frame.gameDisplay.blit(frame.playimg, (player.lead_x,player.lead_y))
                s="Lives: "+str(lives)  #show lives
                show_lives(s,red,frame)
                s2="Score: "+str(score) #show score
                show_score(s2,red,frame)
                s3="Level: "+str(level)  #show level
                show_level(s3,red,frame)
                pygame.display.update()
                clock.tick(FPS)
                count+=1

        pygame.quit()
        quit()



black=(0,0,0)
white=(255,255,255)
red=(255,0,0)
dred=(155,0,0)
green=(0,155,0)
blue=(0,0,255)  
brown=(120,67,33)      


FPS=18                                                                                                                   
clock=pygame.time.Clock()
font=pygame.font.SysFont(None,30)

gameloop(3,0,1)
