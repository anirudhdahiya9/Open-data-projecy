import pygame
from person import *
from objects import *
import random
#Required variables
def function(x,y):
	global size
	white=(255,255,255)
	size=pygame.display.get_surface().get_width()/80
	# size-=x/1250
	#size=25


#Inital required loading.

x_offset=0
y_offset=50




#Board class- contains the functions related to board and setting up of grid form.
class board:
	def __init__(self,displayWidth,displayHeight,levelr,initScore):
		self.displayWidth=displayWidth
		self.displayHeight=displayHeight
		self.initScore=initScore
		#Creating a wall surface object
		self.wallList=pygame.sprite.Group()
		self.ladderList=pygame.sprite.Group()
		self.coinList=pygame.sprite.Group()
		self.playerList=pygame.sprite.Group()
		self.fireballsList=pygame.sprite.Group()
		self.topladderList=pygame.sprite.Group()
		self.allladderposition=[]
		self.AllList=pygame.sprite.Group()
		self.ladderposition=[]	
		currentlevel='levels/level_'+str(levelr)+'.txt'
		print levelr
		self.f=open(currentlevel,'r') 
		self.input_file=self.f.readlines()
		
	#Includes players,coins,wall and ladders
	def drawgrid(self,mainobject,initPos):

		self.gap_y=y_offset
		self.temprange=-1
		self.check=False
		temp='A'
		numcoins=0
		inp=self.input_file
		coinpos=[]
		for i in range(1,len(self.input_file)):
			self.input_file[i]=list(self.input_file[i].strip())
			for j in range(1,79):
				if inp[i][j]=='X' and inp[i-1][j]==' ':
					coinpos.append((i-1,j))
		while numcoins<25:
			i=random.randint(0,len(coinpos)-1)
			inp[coinpos[i][0]][coinpos[i][1]]='C'
			numcoins+=1
			coinpos.pop(i)
		for i in self.input_file:
			self.gap_x=x_offset
			if self.temprange>=0:
				self.check=True
			iteration=0			
			for j in i:
				#print j
				if j=='X':	
					wall=Wall(self.gap_x,self.gap_y,size)
					self.wallList.add(wall)
					self.AllList.add(wall)				

				elif j=='H':
					ladder=Ladder(self.gap_x,self.gap_y,size)
					self.ladderList.add(ladder)
					self.AllList.add(ladder)
					self.allladderposition.append([self.gap_x,self.gap_y])
					if temp=='X' or i[iteration+1]=='X':
						self.ladderposition.append([self.gap_x,self.gap_y])
						self.topladderList.add(ladder)

				elif j=="C":
					coin=Coin(self.gap_x,self.gap_y,size)
					self.coinList.add(coin)
					self.AllList.add(coin)

				elif j=="P":
					self.initPos=[self.gap_x,self.gap_y]
					self.create_actor('mario')
					self.playerList.add(self.mario)
					self.AllList.add(self.mario)

				elif j=="D":
					self.temprange=0
					self.initPos=[self.gap_x,self.gap_y]
					self.create_actor('donkey')
					self.playerList.add(self.donkey)
					self.AllList.add(self.donkey)
				elif j=="Q":
					princess=Princess(self.gap_x,self.gap_y,size )
					self.AllList.add(princess)
					self.finPos=[self.gap_x,self.gap_y]
				elif j == " " and self.check==True:
					self.donkey.maximum=self.gap_x-size
					self.temprange=-1
					self.check=False					
				temp=j	
				self.gap_x+=size
			self.gap_y+=size
		self.f.close()
	def showgrid(self):
		print  self.coinList
		print "\n\n\n"
		print self.wallList

	def create_actor(self,name):
		if name=="mario":
			self.mario=player(name,self.initPos[0],self.initPos[1],self.finPos[0],self.finPos[1])
			self.mario.score=self.initScore

		elif name=="donkey":
			self.donkey=donkey(name,self.initPos[0],self.initPos[1])
