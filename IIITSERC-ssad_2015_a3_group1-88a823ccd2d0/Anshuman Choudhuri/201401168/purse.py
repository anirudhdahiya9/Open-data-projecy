import pygame
from pygame.locals import *
class Person(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)

    def makechar(self,char,l,b,x,y):
        self.image=pygame.image.load(char)
        self.image=pygame.transform.scale(self.image,(l,b))
        self.rect=self.image.get_rect()
        self.rect.x=x
        self.rect.y=y
        
    def getPosition():
        print self.rect.x, self.rect.y

class Player(Person):
    
    def __init__(self):
        Person.__init__(self)
        self.makechar('kaneki2.png',50,50,30,535)
        self.__score=0
        self.__v=5
        self.__lives=3
        
    def get_life(self):
        return self.__lives

    def change_life(self,newl):
        self.__lives=newl

    def get_score(self):
        return self.__score

    def change_score(self,newl):\
        self.__score=newl
        
    def jump(self,stand,flag):
        if self.__v==5 and flag==1:
            self.__v=0
        if self.__v>0:
           self.energy=(0.7* self.__v *self.__v)
        else:
            self.energy=-(0.7* self.__v *self.__v)
        self.__v=self.__v-1
        self.rect.y=self.rect.y-self.energy
        if self.rect.y>=stand:
            self.rect.y=stand
            self.__v=5

    def ladder(self):
        if 360<=self.rect.x<=370:
            if 545>=self.rect.y>=445:
                if self.rect.y==445:
                    return 2
                elif self.rect.y<=545:
                    return 1
        if 260<=self.rect.x<=270:
            if 445>=self.rect.y>=345:
                if self.rect.y==345:
                    return 2
                elif self.rect.y<=445:
                    return 1
        if 410<=self.rect.x<=420:
            if 345>=self.rect.y>=245:
                if self.rect.y==245:
                    return 2
                elif self.rect.y<=345:
                    return 1
        if 0<=self.rect.x<=10:
            if 245>=self.rect.y>=145:
                if self.rect.y==145:
                    return 2
                elif self.rect.y<=245:
                    return 1
        if 180<=self.rect.x<=190:
            if 145>=self.rect.y>=45:
                if self.rect.y==45:
                    return 2
                elif self.rect.y<=145:
                    return 1
        if 400<=self.rect.x<=410:
            if 145>=self.rect.y>=45:
                if self.rect.y==45:
                    return 2
                elif self.rect.y<=145:
                    return 1
        return 0 
