import pygame
from pygame.locals import *
import random
import time
FPS=18                                                                                                                                    
clock=pygame.time.Clock()


#for player and donkey
class Person:
        def __init__(self,lead_x,lead_y,lead_x_change,lead_y_change):
                self.lead_x=lead_x
                self.lead_y=lead_y
                self.lead_x_change=lead_x_change
                self.lead_y_change=lead_y_change

