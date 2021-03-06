import os, sys
from time import sleep
from random import randint
import donk
import firecoin
import purse
import pygame
from pygame.locals import *

class Board(purse.Person):
    def __init__(self, width=640,height=600):
        pygame.init()
        purse.Person.__init__(self)
        self.queen=self.makechar('princess.png',30,40,460,54)
        self.screen = pygame.display.set_mode((width,height))
        self.screen.fill((255,255,255))
        self.fpsClock=pygame.time.Clock()
        self.fps=20
        self.xMove=0
        self.yMove=0

        self.flag=0
        self.second=0
        self.font = pygame.font.Font('freesansbold.ttf',30)
        self.hit_list=[]
        self.p_list=pygame.sprite.Group()
        self.d_list=pygame.sprite.Group()
        self.f_list=pygame.sprite.Group()
        self.c_list=pygame.sprite.Group()
        self.q_list=pygame.sprite.Group()
        self.img_list=['Platform2.png','ladder.jpg','background.jpg']
        self.hit_list.append(self.img_list[2])
        for i in range(7):
            self.hit_list.append(self.img_list[0])
        for i in range(8):
            self.hit_list.append(self.img_list[1])
        self.img_list=self.hit_list
        self.hit_list=[]

        self.value_list=[(800,800),(350,20),(400,20),(450,20),(510,20)
                         ,(480,20),(650,20),(300,20),(20,50),(20,30),(20,95),(20,105),
                         (20,105),(20,105),(20,105),(20,105)]
        self.coord=[(0,0),(-4,580),(265,580),(-4,490),(190,390),
                    (-4,290),(-4,190),(180,90),(350,245),(350,200),(380,495),(280,395),
                   (430,295),(20,195),(200,95),(420,95)]
 
    def run(self):
        self.loadimg()
        self.j=0
        self.jumprest=True
        self.downrest=True
        while 1:
#Checking for events
            if self.second!=2:
                for event in pygame.event.get():

                    if event.type == pygame.QUIT:
                        sys.exit()

                    elif event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_d: 
                            self.xMove=10
                        elif event.key == pygame.K_a:
                            self.xMove=-10
                        elif event.key == pygame.K_w or event.key == pygame.K_SPACE:
                            self.yMove=-10
                            if self.jumprest==True:
                                self.j=1
                                self.player.rect.y==self.stand
                        elif event.key == pygame.K_s:
                            self.yMove=+10
                        elif event.key == pygame.K_q:
                            sys.exit()

                    elif event.type == pygame.KEYUP:
                        if event.key == pygame.K_d or event.key == pygame.K_a:
                            self.xMove=0
                        if event.key == pygame.K_w or event.key == pygame.K_s or event.key == pygame.K_SPACE:
                            self.yMove=0
#END Checking for events

            self.stand=535
            self.leftbound=0
            self.rightbound=595
            self.is_lad=0
            self.is_lad=self.player.ladder()

            self.stand=self.check()

            if self.is_lad==1:
                self.j=0
                self.jumprest=False
                self.downrest=True
            elif self.is_lad==0:
                self.jumprest=True
                self.downrest=True
            elif self.is_lad==2:
                if self.yMove==-10:
                    self.j=1
                else:
                    self.j=0
                self.jumprest=True
                self.downrest=False
            if self.second==1:
                self.f_list=self.dragon.moveslikejagger(self.f_list,'ballfire1.png',370)
            self.f_list=self.donkey.moveslikejagger(self.f_list,'fireball.png',170)
            self.i=0

# Switching between 3 speeds randomly for every fireball

            for agni in self.f_list:
                self.troy=self.i%(randint(2,5))
                if self.troy<=1:
                    agni.movethefireball(10,10)
                elif self.troy<=3:
                    agni.movethefireball(10,15)
                else:
                    agni.movethefireball(10,20)                
                self.i=self.i+1
                
            self.player.rect.x += self.xMove

            if ((self.jumprest==False and self.yMove > 0 and self.player.rect.y +10 <= self.stand) or (self.downrest==False and self.yMove>0) or (self.jumprest==False and self.yMove<0)):

                self.player.rect.y += self.yMove

            self.stand=self.check()

            if self.player.rect.y < self.stand and self.j==0 and self.jumprest==True and self.downrest==True:
                self.player.rect.y=self.stand

            if self.player.rect.x < self.leftbound:
                if 175>self.leftbound>30:
                    self.flag=1
                    self.j=1
                    self.stand=self.stand+100
                else:
                    self.player.rect.x = self.leftbound 

            elif self.player.rect.y < 0:
                self.player.rect.y =0

            elif self.player.rect.x > self.rightbound:
                if 550>self.rightbound>419:
                    self.flag=1
                    self.j=1
                    self.stand=self.stand+100
                else:
                    self.player.rect.x = self.rightbound

            if self.j==1:
                if self.flag==0:
                    self.player.jump(self.stand,self.flag)
                else:
                    self.player.jump(self.stand,self.flag)
                if self.player.rect.y==self.stand:
                    self.j=0
                    self.flag=0
            self.collision()

            if self.second==2:

                self.screen.fill((255,255,255))
                self.text1 = self.font.render("Your Score: "+str(self.player.get_score()+50)+ " :)" , True,(0,0,0),(255,255,255))
                self.text3 = self.font.render("Press Q to Quit,  R to Retry", True,(0,0,0),(255,255,255))

                self.screen.blit(self.text1,(150,100))
                self.screen.blit(self.text3,(150,200))
                pygame.display.update()
                for event in pygame.event.get():
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_q: 
                            sys.exit()
                        elif event.key == pygame.K_r:
                            self.second=0
                            self.player.rect.y=535
                            self.player.rect.x=30
                            self.d_list=pygame.sprite.Group()
                            self.f_list=pygame.sprite.Group()
                            self.c_list=pygame.sprite.Group()
                            self.p_list=pygame.sprite.Group()
                            self.q_list=pygame.sprite.Group()
                            self.player.change_life(3)
                            self.player.change_score(0)
                            self.loadimg()
                            self.xMove=0

            if self.second!=2:
                self.showall()

            self.fpsClock.tick(self.fps)

    def showall(self):
            self.i=0
            for self.i in range(15):
                self.screen.blit(self.final_list[self.i],self.coord[self.i])

            self.text = self.font.render("Score: "+str(self.player.get_score())+ " Level: "+str(self.second+1), True,(0,0,0),(255,255,255))
            self.screen.blit(self.text,(10,5))


            if self.player.get_life() >= 1:
                self.screen.blit(self.heart,(540,10))
                if self.player.get_life()>=2:
                    self.screen.blit(self.heart1,(565,10))
                    if self.player.get_life()>=3:
                        self.screen.blit(self.heart2,(590,10))
            
            if self.player.get_life()<1:
                sys.exit()
#                self.player.rect.y=535
#                self.player.rect.x=30
#                self.player.lives=3
#                self.player.score-=25
#                self.f_list=pygame.sprite.Group()
#                self.c_list=pygame.sprite.Group()
#                self.load_coins()

            self.p_list.draw(self.screen)
            self.d_list.draw(self.screen)
            if len(self.f_list)>0:
                self.f_list.draw(self.screen)
                self.f_list.update()
            self.c_list.draw(self.screen)
            self.q_list.draw(self.screen)
            
            self.q_list.update()
            self.c_list.update()
            self.p_list.update()
            self.d_list.update()
            pygame.display.update()

# this is the checkCollision() function, coins are collected in this
# for which self.player.change_score() {<---- collectCoin()} is called
    def collision(self):
        self.hit_list=pygame.sprite.spritecollide(self.player,self.d_list,False)
        if len(self.hit_list)>0:
            self.player.change_life(0)
        self.hit_list=[]
        self.hit_list=pygame.sprite.spritecollide(self.player,self.f_list,True)
        if len(self.hit_list)>0:
            if self.player.get_life()>0:
                self.player.change_life(self.player.get_life()-1)
            if self.player.get_score()>0:
                self.player.change_score(self.player.get_score()-25)
            self.player.rect.x=30
            self.player.rect.y=535
        self.hit_list=[]
        self.hit_list=pygame.sprite.spritecollide(self.player,self.c_list,True)
        if len(self.hit_list)>0:
            self.player.change_score(self.player.get_score()+5)
        self.hit_list=pygame.sprite.spritecollide(self.player,self.q_list,False)

        if len(self.hit_list)>0:
            if self.second==1:
                self.second=2

            if self.second==0:
                self.second=1
                self.player.rect.y=535
                self.player.rect.x=30
                self.player.change_score(self.player.get_score()+50)
                self.dragon=donk.Donkey('demon5.png',40,60,300,335)
                self.d_list.add(self.dragon)
                self.f_list=pygame.sprite.Group()
                self.c_list=pygame.sprite.Group()
                self.load_coins()
                self.player.change_life(3)

# This is the checkWall() function
    def check(self):
        m=535
        if self.player.rect.y >= 450:
            m=545
        elif self.player.rect.y >= 350:
            m=445
            self.rightbound=420
        elif self.player.rect.y >= 250:
            m=345
            self.leftbound=170
        elif self.player.rect.y >= 150:
            m=245
            self.rightbound=440
        elif self.player.rect.y >= 50:
            m=145
        elif self.player.rect.y >=0:
            m=45
            self.rightbound=460
            self.leftbound=160
        return m

    def loadimg(self):
        self.player=purse.Player()
        self.donkey=donk.Donkey('regi.png',60,100,200,95)
        self.load_coins()

        self.p_list.add(self.player)
        self.d_list.add(self.donkey)
        self.q_list.add(self)
        self.final_list=[]
        self.i=0
        for self.i in range(15):
            self.final_list.append(pygame.image.load(self.img_list[self.i]))
            self.i=self.i+1

        self.heart=pygame.image.load('heart.png')
        self.heart1=pygame.image.load('heart.png')
        self.heart2=pygame.image.load('heart.png')

        self.i=0

        for self.i in range(15):
            self.final_list[self.i]=pygame.transform.scale(self.final_list[self.i],self.value_list[self.i])            
            self.i=self.i+1

        self.heart=pygame.transform.scale(self.heart,(20,20))
        self.heart1=pygame.transform.scale(self.heart1,(20,20))
        self.heart2=pygame.transform.scale(self.heart2,(20,20))

# Distributes coins randomly
    def load_coins(self):
        self.i=0
        for self.i in range(6):
            self.c_list.add(firecoin.Coin(545,5,588))
        self.i=0
        for self.i in range(4):
            self.c_list.add(firecoin.Coin(445,5,405))
        self.i=0
        for self.i in range(3):
            self.c_list.add(firecoin.Coin(345,90,588))
        self.i=0
        for self.i in range(4):
            self.c_list.add(firecoin.Coin(245,5,510))
        self.i=0
        for self.i in range(3):
            self.c_list.add(firecoin.Coin(145,90,588))        

if __name__ == "__main__":
    Main = Board()
    Main.run()
