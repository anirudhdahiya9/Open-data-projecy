import pygame
from pygame.locals import *
import time
import random
from functions import *
FPS=18                                                                                                                                    
clock=pygame.time.Clock()


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
                                if x<1:
                                        self.lead_x_change=frame.block_size/2
                                else:
                                        self.lead_x_change=-frame.block_size/2
                        
                        self.lead_x+=self.lead_x_change
                        self.lead_y+=self.lead_y_change
                
                elif frame.checkfloor(self.lead_x,self.lead_y)==0:  #for checking fall
                        if frame.checkdown(self.lead_x,self.lead_y)==1:
                                x=random.randrange(0,3)
                                if x<2.5:
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

