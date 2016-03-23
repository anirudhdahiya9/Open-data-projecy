import pygame
from pygame.locals import *
from random import randint
class Coin(pygame.sprite.Sprite):
    def __init__(self,ypos,lb,ub):
        pygame.sprite.Sprite.__init__(self)
        self.image=pygame.image.load('coin.png')
        self.image=pygame.transform.scale(self.image,(20,20))
        self.rect=self.image.get_rect()
        self.rect.x=randint(lb,ub)
        self.rect.y=ypos 

class Fireball(pygame.sprite.Sprite):
    def __init__(self,do_x,do_y,s):
        pygame.sprite.Sprite.__init__(self)
        self.image=pygame.image.load(s)
        self.image=pygame.transform.scale(self.image,(20,20))
        self.rect=self.image.get_rect()
        self.rect.x=do_x
        self.rect.y=do_y
        self._l1=0
        self._l2=0
        self._l3=0

    def movethefireball(self,y,x):
        if self.rect.y<=170:
            if self.rect.x>25:
                self.rect.x-=x
            else:
                self.rect.y+=y
        elif self.rect.y<=270:
            if self.rect.y<270:
                self.rect.y+=y
            else:
                if self.rect.x < 470:
                    self.rect.x+=x
                else: 
                    self.rect.y+=y
        elif self.rect.y<=370:
            if self.rect.y<370:
                self.rect.y+=y
                self._l1=0
            elif self._l1==0:
                if self.rect.x<=590:
                    self.rect.x+=x
                else:
                    self._l1=1
            else:
                if self.rect.x >170:
                    self.rect.x-=x
                else:
                    self.rect.y+=y
        elif self.rect.y<=470:
            if self.rect.y<470:
                self.rect.y+=y
                self._l2=0
            elif self._l2==0:
                if self.rect.x>=10:
                    self.rect.x-=x
                else:
                    self._l2=1
            else:
                if self.rect.x < 440:
                    self.rect.x+=x
                else:
                    self.rect.y+=y 
        elif self.rect.y<=700:
            if self.rect.y < 570:
                self.rect.y+=y
                self._l3=0
            elif self._l3==0:
                if self.rect.x<=590:
                    self.rect.x+=x
                else:
                    self._l3=1
            elif self.rect.x>=270:
                self.rect.x-=x
            else:
                self.rect.y+=y
