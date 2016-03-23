import pygame,random
from constants import *
from ladder import *
from characters import fireball
class board():
	def __init__(self,w,h,b,lw):
		self.w=w
		self.h=h
		self.border=b
		self.lw=lw
		self.gameover = False
		self.balls=[]
		self.ladders=[((700,740),(700,600)),((350,600),(350,480)),((500,600),(500,560)),((500,520),(500,480)),((800,480),(800,360)),((400,360),(400,240)),((350,240),(350,200)),((350,160),(350,120)),((600,240),(600,120)),((450,120),(450,60))]
		self.DISP=pygame.display.set_mode((w,h))
		pygame.display.set_caption('Game')
		self.coins=[]
	def checkWall(self,x,y):
		if x>=0 and x<=self.border:
			return True
		if x<=self.w and x>=(self.w - self.border):
			return True
		return False
	def checkLadder(self,x,y,c):
		flag=0
		for currl in self.ladders:
			p1=currl[1]
			p2=currl[0]
			if y>=p1[1] and y<=p2[1] and x>=p1[0] and x<=p1[0]+self.lw:
				if y==p1[1]:
					if c=='U':
						return None
					else:
						return currl
				else:
					flag=1
					return currl
		if flag==0:
			return None
	def genCoin(self):
		r = random.randrange(1,7)
		l = r*120
		if l == 720:
			l = 740
		g = GROUND_NEW[l]
		flag = 0
		while True:
			if flag == 1:
				return
			x = random.randrange(g[0][0],g[1][0])
			if self.checkLadder(x,g[0][1],'U') == None and self.checkWall(x,g[0][1]) == False:
				flag = 1
				self.coins.append((x,g[0][1]-COIN_RADIUS-5,1,1))
	def createGame(self):
		DISPLAY=self.DISP
		DISPLAY.fill(BLACK)
		pygame.draw.line(DISPLAY,GROUND_COLOUR,(0,0),(1100,0),20)
		pygame.draw.line(DISPLAY,GROUND_COLOUR,(0,0),(0,750),20)
		pygame.draw.line(DISPLAY,GROUND_COLOUR,(1100,0),(1100,750),20)
		pygame.draw.line(DISPLAY,GROUND_COLOUR,(0,750),(1100,750),20)    #0
		pygame.draw.line(DISPLAY,GROUND_COLOUR,(300,60),(500,60),10)      #6
		pygame.draw.line(DISPLAY,GROUND_COLOUR,(0,120),(700,120),10)  #gap=120	#5
		pygame.draw.line(DISPLAY,GROUND_COLOUR,(250,240),(1100,240),10)   #4
		pygame.draw.line(DISPLAY,GROUND_COLOUR,(0,360),(900,360),10)      #3
		pygame.draw.line(DISPLAY,GROUND_COLOUR,(200,480),(1100,480),10)   #2
		pygame.draw.line(DISPLAY,GROUND_COLOUR,(0,600),(850,600),10)      #1
		l = self.ladders
		for x in l:
			ladder(x[0],x[1],19).make_ladder(self)
		for coin in self.coins:
			pygame.draw.rect(self.DISP,COIN_COLOUR,coin)
			pygame.draw.circle(self.DISP,COIN_COLOUR,(coin[0],coin[1]),COIN_RADIUS)
	def genFireball(self):
		self.balls.append(fireball(150,90,20,30,'R'))
	def gameend(self,player):
		return player.lives==0
