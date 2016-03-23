import pygame
from pygame.locals import *
import time
import random          
from functions import *
FPS=18                                                                                                                                    
clock=pygame.time.Clock()


#for coins
class coinframe:
        def __init__(self,display_width,display_height,w,h,block_size):
                self.__x=0   #private variables
                self.__athick=20
                self.coin=[]
                while self.__x<25:  #random coin generation on floors
                        randax=round(random.randrange(self.__athick,display_width-2*self.__athick)/20.0)*20.0
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
                        self.__x+=1
        
        #drawing randomly generated coins on board
        def gen(self,frame): 
                for elem in self.coin:
                        frame.gameDisplay.blit(frame.coinimg, (elem[0],elem[1]))

