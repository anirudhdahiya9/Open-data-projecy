import pygame,random
from constants import *
class Person():
	def __init__(self,x,y):
		self.x=x
		self.y=y
	def getPosition(self):
		return (self.x,self.y)
	def canfall(self):
		if GROUND_NEW.has_key(self.man.bottom):
			if self.man.left > GROUND_NEW[self.man.bottom][1][0] or self.man.right < GROUND_NEW[self.man.bottom][0][0]:
				return True
		return False
	def makefall(self,speed):
		self.falling = True
		self.vel=speed
		if GROUND_NEW.has_key(self.man.bottom + 120):
			self.ground = self.man.bottom + 120
		else:
			if self.man.bottom == 60:
				self.ground = 120
			else:
				self.ground = 740
	def fall(self):
		if self.falling:
			self.vel+=GRAVITY
			self.man.bottom+=self.vel
			if self.man.bottom > self.ground:
				self.man.bottom = self.ground
				self.vel = 0
				self.falling = False
class fireball(Person):
	def __init__(self,x,y,w,h,d):
		self.x=x
		self.y=y
		self.w=w
		self.h=h
		self.man=pygame.Rect(self.x,self.y,self.w,self.h)
		self.d=d
		self.falling = False
	def create(self,gameinst):
		pygame.draw.rect(gameinst.DISP,FIREBALL_COLOUR,self.man)
	def move(self,gameinst):
		l = gameinst.checkLadder(self.man.left,self.man.bottom,'X')
		if l!=None and self.man.bottom == l[1][1]:
			r = random.randrange(0,3)
			if r == 0:
				self.d = 'D'
		if self.d == 'R':
			if gameinst.checkWall(self.man.right,self.man.bottom):
				self.d = 'L'
			else:
				self.man.right+=BALL_SPEED
				if self.canfall():
					self.makefall(0)
					self.d = DIR[random.randrange(0,2)]
		elif self.d == 'L':
			if self.man.left <=21 and self.man.bottom == 740:
				gameinst.balls.remove(self)
				return
			if gameinst.checkWall(self.man.left,self.man.bottom):
				self.d = 'R'
			else:
				self.man.left-=BALL_SPEED
				if self.canfall():
					self.makefall(0)
					self.d = DIR[random.randrange(0,2)]
		elif self.d =='D':
			if GROUND_NEW.has_key(self.man.bottom+120):
				self.man.bottom+=120
			else:
				self.man.bottom+=140
			self.d = DIR[random.randrange(0,2)]
class Player(Person):
	def __init__(self,x,y,sc):
		Person.__init__(self,x,y)
		self.lives=3
		self.score=sc
		self.jumping = False
		self.ground = 740
		self.man=pygame.Rect(self.x,self.y,20,30)
		self.falling = False
	def create(self,gameinst):
		pygame.draw.rect(gameinst.DISP,PLAYER_COLOUR,self.man)
	def onladder(self,gameinst):
		lad1 = gameinst.checkLadder(self.man.left,self.man.bottom,'X')
		if lad1 == None:
			lad1 = gameinst.checkLadder(self.man.right,self.man.bottom,'X')
		if (lad1!=None) and (lad1[0][1] - lad1[1][1] == 40) and self.man.bottom==lad1[1][1] and GROUND_NEW.has_key(lad1[1][1])==False:
			return True
		lad = gameinst.checkLadder(self.man.left,self.man.bottom,'U')
		if lad == None:
			lad = gameinst.checkLadder(self.man.right,self.man.bottom,'U')
		if lad == None:
			return False
		else:
			if self.jumping == True:
				return False
			else:
				if lad[0][1]==self.man.bottom and GROUND_NEW.has_key(lad[0][1]):
					return False
				else:
					return True
	def canjump(self,gameinst):
		x = gameinst.checkLadder(self.man.left,self.man.bottom,'U')
		if x!=None and self.jumping == False:
			return False
		return True
	def move(self,gameinst,d,v):
		if d=='L':
			if gameinst.checkWall(self.man.left,self.man.top) or self.onladder(gameinst):
				return
			if GROUND_NEW.has_key(self.man.bottom) and self.man.right < GROUND_NEW[self.man.bottom][0][0]:
				self.makefall(0)
			else:
				self.man.left-=v
				return
		elif d=='R':
			if gameinst.checkWall(self.man.right,self.man.top) or self.onladder(gameinst):
				return
			if GROUND_NEW.has_key(self.man.bottom) and self.man.left > GROUND_NEW[self.man.bottom][1][0]:
				self.makefall(0)
			else:
				self.man.left+=v
				return
		elif d=='U':
			c = gameinst.checkLadder(self.man.left,self.man.bottom,'U')
			if c == None:
				c = gameinst.checkLadder(self.man.right,self.man.bottom,'U')
			if c!=None:
				if self.man.bottom - v >= c[1][1]:
					self.man.top-=v
				else:
					self.man.bottom = c[1][1]
			return
		elif d=='D':
			c = gameinst.checkLadder(self.man.left,self.man.bottom,'D')
			if c == None:
				c = gameinst.checkLadder(self.man.right,self.man.bottom,'D')
			if c!=None:
				if self.man.bottom + v < c[0][1]:
					self.man.top+=v
				else:
					self.man.bottom = c[0][1]
			return
	def jump_new(self,speed):
		if self.jumping == False:
			pygame.mixer.music.load('jump.mp3')
			pygame.mixer.music.play()
			self.vel=-speed
			self.ground = self.man.bottom
			self.jumping = True
	def gravity_new(self):
		if self.jumping:
			self.vel+=GRAVITY
			self.man.bottom+=self.vel
			if self.man.bottom > self.ground:
				self.man.bottom = self.ground
				self.vel = 0
				self.jumping = False
				if self.canfall():
					self.makefall(5)
	def Collectcoin(self,gameinst):
		c = self.man.collidelist(gameinst.coins)
		if c!=-1:
			pygame.mixer.music.load('coin.mp3')
			pygame.mixer.music.play()
			self.score+=COIN_VAL
			gameinst.coins.remove(gameinst.coins[c])
		return
	def checkCollision(self,obj):
		return self.man.colliderect(obj.man)
	def gameWon(self,princess):
		return self.checkCollision(princess)
	def Collide(self,gameinst):
		self.lives-=1
		self.score-=25
		pygame.mixer.music.load('respawn.mp3')
		pygame.mixer.music.play()
		self.jumping = False
		self.man.left=100
		self.man.top=710
		pygame.time.wait(105)
class Donkey(Person):
	def __init__(self,x,y,w,h):
		Person.__init__(self,x,y)
		self.w=w
		self.h=h
		self.d='R'
		self.man=pygame.Rect(self.x,self.y,self.w,self.h)
	def create(self,gameinst):
		pygame.draw.rect(gameinst.DISP,DONKEY_COLOUR,self.man)	
	def move(self,gameinst,max):
		if self.d=='R':
			if self.man.right==max:
				self.d='L'
			else:
				self.man.left+=DONKEY_SPEED
		else:
			if gameinst.checkWall(self.man.left,self.man.bottom):
				self.d='R'
			else:
				self.man.left-=DONKEY_SPEED
class Princess(Person):
	def __init__(self,x,y,w,h):
		Person.__init__(self,x,y)
		self.w=w
		self.h=h
		self.man=pygame.Rect(self.x,self.y,self.w,self.h)
	def create(self,gameinst):
		pygame.draw.rect(gameinst.DISP,PRINCESS_COLOUR,self.man)
		fontobj = pygame.font.Font('freesansbold.ttf',14)
		save = fontobj.render("Save Me",True,WHITE,BLACK)
		save_rect = save.get_rect()
		save_rect.left,save_rect.top=380,30
		gameinst.DISP.blit(save,save_rect)
