import pygame
from pygame.locals import *
import time
import random
from Person import *
FPS=18                                                                                                                                    
clock=pygame.time.Clock()


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

