import pygame
import random
from fireball import *


class person(pygame.sprite.Sprite):
	def __init__(self,name,initX,initY):
		pygame.sprite.Sprite.__init__(self)
		self.name=name
		print "Init",initX
		self.rect.y = initY
		self.rect.x = initX
		self.deltaX=0
		self.deltaY=0
		self.ladderstate=0
		self.wallList=None
		self.speed=3#*size*1.0/
		self.ladderList=None
		self.allladerposition=[]
		self.onladder=False
		self.movestate=0
		self.abhi=0

	def getPerson(self):
		return self.name
	
	def getLocation(self):
		return (self.rect.x,self.rect.bottom)

	def update(self):

		self.checkWallcollision()




	#This method checks for collisions and updates the position of player too.	
	def checkWallcollision(self):
		self.rect.x+=self.deltaX
		if self.wallList != None:
			WallCollsionlist= pygame.sprite.spritecollide(self, self.wallList, False)
			
			#print WallHitlist
			for wall in WallCollsionlist:

				if self.deltaX > 0:
					self.rect.right = wall.rect.left
				elif self.deltaX < 0:
					self.rect.left = wall.rect.right
				if self.name == 'donkey':
					self.right=True 	
  #       Move up/down
  		

  		self.rect.y+=self.deltaY

  #       Checking vertical hits
  		if self.wallList != None:
			WallCollisionlist= pygame.sprite.spritecollide(self, self.wallList, False)

			for wall in WallCollisionlist:
		 		if self.deltaY > 0:
		 			self.rect.bottom = wall.rect.top

		 		elif self.deltaY < 0:
		 			self.rect.top = wall.rect.bottom
 				self.deltaY = 0
				

 	def checkLadders(self):
		iterator=0
		#print self.onladder

		if self.ladderList != None:
			LadderTouch=pygame.sprite.spritecollide(self,self.ladderList,False)
			for ladders in LadderTouch:
				if len(LadderTouch) > 0 and ladders.rect.left<=self.rect.left and ladders.rect.right>=self.rect.right:
					#print "up/down allowed"
					self.onladder=True
					self.arrows[2]=1
					self.arrows[3]=1
					if ladders.rect.bottom>self.rect.bottom:
						#print "left/right not allowed"
					#	print ladders.rect.bottom
						self.onladder=True
						self.arrows[0]=0
						self.arrows[1]=0
						self.arrows[4]=0
					else:
						self.onladder=False
						# "left/right allowed"
						self.arrows[0]=1
						self.arrows[1]=1
						self.arrows[4]=1
				iterator+=1	
			if len(LadderTouch)==0:
				#print "up/down disabled"
				self.onladder=False
				self.arrows[2]=0
				self.arrows[3]=0
				

		iterator=0
		for ladder in self.ladderposition:
			#print "Ladderposition",self.ladderposition[iterator][1],self.rect.bottom
			if self.ladderposition[iterator][1]-2<=self.rect.bottom <=self.ladderposition[iterator][1]+1 and self.rect.left >= self.ladderposition[iterator][0] and self.rect.right<=self.ladderposition[iterator][0]+19:
				self.rect.bottom =self.ladderposition[iterator][1]
				self.onladder=True
				self.arrows[0]=1
				self.arrows[1]=1
				self.arrows[2]=0
				self.arrows[3]=1
				self.arrows[4]=1
				#print "Changing permissions"
			iterator+=1 		

	def laddercollision(self):
		
		iterator=0
		#print self.onladder

		for ladders in self.allladerposition:
			if self.deltaY>0:
				print "up/down allowed"
				self.onladder=True
				self.arrows[2]=1
				self.arrows[3]=1
				if ladders.rect.bottom>self.rect.bottom:
					print "left/right not allowed"
				#	print ladders.rect.bottom
					self.onladder=True
					self.arrows[0]=0
					self.arrows[1]=0
					self.arrows[4]=0
				else:
					self.onladder=False
					print "left/right allowed"
					self.arrows[0]=1
					self.arrows[1]=1
					self.arrows[4]=1
			iterator+=1	
		if len(LadderTouch)==0:
			print "up/down disabled"
			self.onladder=False
			self.arrows[2]=0
			self.arrows[3]=0
			

		iterator=0
		for ladder in self.ladderposition:
			#print "Ladderposition",self.ladderposition[iterator][1],self.rect.bottom
			if self.ladderposition[iterator][1]-2<=self.rect.bottom <=self.ladderposition[iterator][1]+1 and self.rect.left >= self.ladderposition[iterator][0] and self.rect.right<=self.ladderposition[iterator][0]+19:
				self.rect.bottom =self.ladderposition[iterator][1]
				self.onladder=True
				self.arrows[0]=1
				self.arrows[1]=1
				self.arrows[2]=0
				self.arrows[3]=1
				self.arrows[4]=1
				print "Changing permissions"
			iterator+=1
			
	def postopladders(self):
		iterator=0
		for i in self.ladderposition:
			#print self.ladderposition[iterator][1],self.rect.bottom
			if self.ladderposition[iterator][1]+1==self.rect.bottom:
				self.rect.bottom-=1
			if self.rect.bottom ==self.ladderposition[iterator][1] and self.rect.left >= self.ladderposition[iterator][0] and self.rect.right<=self.ladderposition[iterator][0]+25:
				return False
			iterator+=1 
		return True

	def checktopLadders(self):
		#print self.topladderList
		#if self.topladderList!=None:
		#self.rect.y+=2
		#self.rect.y+=self.deltaY
		LadderTouch=pygame.sprite.spritecollide(self,self.topladderList,False)
		# #self.rect.y-=1
		# if len(LadderTouch)>0:
		# 	return True
		# return False
		for ladders in LadderTouch:
			print "Yes.Ladder"
			if self.rect.bottom-1<=ladders.rect.top:
				self.rect.bottom=ladders.rect.top
				print "Position",self.rect.bottom
	def moveLeft(self):
		self.movestate=1
		self.ladderstate=0
		self.deltaX = -self.speed
		if self.name=='mario':
			self.image=self.mariowalkleft

	def moveRight(self):
		self.movestate=2
		self.ladderstate=0
		self.deltaX = self.speed
		if self.name=='mario':
			self.image=self.mariowalkright

	def moveUp(self):
		print "Up"
		self.movestate=3
		self.ladderstate=1
		self.deltaY = -self.speed


	def moveDown(self):
		print "Down"	
		self.movestate=4
		self.ladderstate=1
		self.deltaY = self.speed

	def Jump(self):
		self.movestate=5
		print "Jump"
		self.rect.y+=1
		Safeland=pygame.sprite.spritecollide(self,self.wallList,False)
		self.rect.y-=1

		if len(Safeland)>0:
			"inside"
			self.deltaY = -1.3*self.speed
		else:
			self.deltaY=0

	def stopup(self):
		#print "Stop",self.ladderstate
		self.movestate=0
		self.deltaY=0
	def stopside(self):
		self.movestate=0
		self.deltaX=0

def function1(x,y):
	global size
	size=x/80
	size-=5
	#size=22


class player(person):
	def __init__(self,name,initX,initY,finX,finY):
		
		
		self.marioright =pygame.image.load('../images/m1.png').convert_alpha()
		self.marioright=pygame.transform.scale(self.marioright,(size,size))
		self.image=self.marioright

		
		self.mariowalkright=pygame.image.load('../images/m2.png').convert_alpha()
		self.mariowalkright=pygame.transform.scale(self.mariowalkright,(size,size))

		self.mariowalkleft=pygame.transform.scale(self.mariowalkright,(size,size))
		self.mariowalkleft=pygame.transform.flip(self.mariowalkright,1,0)

		self.marioleft=pygame.transform.scale(self.marioright,(size,size))
		self.marioleft=pygame.transform.flip(self.marioleft,1,0)
		self.rect=self.marioright.get_rect()
		person.__init__(self,name,initX,initY)

		self.initX=initX
		self.initY=initY
		self.fireballsList=None
		self.score=0
		self.lives=3
		self.coinList=None
		self.topladderList=None
		self.ladderposition=[]
		self.destination=[finX,finY]
		self.gameover=False
		# Left,Right,Up,Down,Space - permissions
		# 1 - Allowed, 0 - Not allowed
		self.arrows=[1,1,0,0,1]

		getdestruction(self.initX,self.initY)

	def update(self):
		self.freefall()
		if self.movestate!=5:
			self.checkLadders()
		self.collectCoins()
		self.fireballscheck()
		person.update(self)
		if self.destination[0]-size/2<=self.rect.x<=self.destination[0]+size/2 and self.destination[1]-size/2<=self.rect.y<=self.destination[1]+size/2:
			self.gameover=True

		

	def freefall(self):
		#print self.checktopLadders(),"T"
		if self.onladder==False:
			self.deltaY+=0.25

	def checkjumpladders(self):
		iterator=0
		for i in self.ladderposition:
			if self.ladderposition[iterator][1]==self.rect.bottom:
				return True
			iterator+=1 
		return False
	def collectCoins(self):
		if self.coinList != None:
			CoinCollection=pygame.sprite.spritecollide(self,self.coinList,True)
			for coins in CoinCollection:
				self.score+=5
	def ladderscheck(self):
	 	if self.topladderList != None:
 			Topcollision=pygame.sprite.spritecollide(self,self.topladderList,False)

 			# for ladders in Topcollision:
 			# 	print self.deltaY,self.rect.bottom,self.ladderstate
 			# 	if self.deltaY>0:
 			# 		print "BHIBHI"
 			# 		self.rect.bottom=ladders.rect.top
 			# 		if self.checkjumpladders() and self.movestate==4:
 			# 			self.rect.y+=self.deltaY
 			# 			break
				# 	self.deltaY=0
	def fireballscheck(self):
		fireball=pygame.sprite.spritecollide(self,self.fireballsList,False)

		if len(fireball)>0:
			self.lives-=1
			self.arrows=[1,1,0,0,1]
			self.score-=25
			self.rect.x=self.initX
			self.rect.y=self.initY
	


class donkey(person):
	def __init__(self,name,initX,initY):
		
		
		self.donkeyfront =pygame.image.load('../images/donkeyfront.png').convert_alpha()
		self.donkeyfront=pygame.transform.scale(self.donkeyfront,(size,size))
		self.image=self.donkeyfront
		self.rect=self.donkeyfront.get_rect()
		self.rect.y = initY
		self.rect.x = initX
		self.maximum=0
		self.current=0
		self.right=True
		self.topladderList=None
		self.fireballsList=None
		self.currentime=0
		# self.wallList=None
		# self.ladderList=None
		person.__init__(self,name,initX,initY)


	def update(self):

		if self.right == True:
			person.moveRight(self)
			self.checkmyBoundaries()
		else:
			self.current=random.randint(size,self.maximum)
			person.moveLeft(self)
		self.throwfireballs()
		person.update(self)

	def checkmyBoundaries(self):
		if self.rect.x>=self.maximum or self.rect.x>=self.current:
			self.right=False
	def throwfireballs(self):
		#print pygame.time.get_ticks()
		if pygame.time.get_ticks() - self.currentime > 4000:
			self.currentime=pygame.time.get_ticks()
			fireball=Fireball(self.rect.x,self.rect.y,size)
			self.fireballsList.add(fireball)
			fireball.wallList=self.wallList
			fireball.topladderList=self.topladderList