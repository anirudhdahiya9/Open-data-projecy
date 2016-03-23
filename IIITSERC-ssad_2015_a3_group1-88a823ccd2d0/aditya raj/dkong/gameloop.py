import pygame
import time
import random
from Person import *
from Player import *
from Donkey import *
from Fireball import *
from coinframe import *
from Board import *
from functions import *


pygame.init()


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
                        div=400
                if level==2:
                        div=250
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

                                elif event.key==pygame.K_SPACE and state!=3 and player.lead_y!=frame.floort:   #jump movements
                                        if pre==-1:
                                                player.jumpl(dk,frame,coins,fireballs,queen,score,lives,level)
                                                
                                        elif pre==1:
                                                player.jumpr(dk,frame,coins,fireballs,queen,score,lives,level)
                                        
                                        else:
                                                player.jump(dk,frame,coins,fireballs,queen,score,lives,level)

                        if event.type == pygame.KEYUP:  #when key is released
                                if event.key == pygame.K_a or event.key == pygame.K_d:
                                        player.lead_x_change=0
                                        pre=0
                                elif event.key == pygame.K_s or event.key == pygame.K_w:
                                        player.lead_y_change=0
                                        pre=0
                

                
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
