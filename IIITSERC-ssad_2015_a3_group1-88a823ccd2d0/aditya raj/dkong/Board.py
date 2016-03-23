import pygame
from pygame.locals import *
from functions import *
black=(0,0,0)
white=(255,255,255)
red=(255,0,0)
dred=(155,0,0)  
green=(0,155,0)
blue=(0,0,255) 
brown=(120,67,33)
FPS=18                                                                                                                                    
clock=pygame.time.Clock()


#the basic Frame of board
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
                brokladimg=pygame.image.load('broklader.jpeg')

                #broken ladders
                self.gameDisplay.blit(brokladimg, (self.w,self.display_height-self.h))
                self.gameDisplay.blit(brokladimg, (self.w,self.display_height-self.h/3))
                self.gameDisplay.blit(brokladimg, (4*self.w,self.display_height-4*self.h))
                self.gameDisplay.blit(brokladimg, (1.5*self.w,self.display_height-3*self.h))
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

