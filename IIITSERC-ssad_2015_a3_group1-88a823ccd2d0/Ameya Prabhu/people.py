import time
from random import randint

class person:
	def setvar(self,x,y,isfloor,isstair,iswallright,iswallleft):
		if isstair==True:
			self.allowup=True
		else:
			self.allowup=False

		if not isfloor:
			self.allowdown=True
		else:
			self.allowdown=False

		if iswallright==True:
			self.allowright=False
		else:
			self.allowright=True

		if iswallleft==True:
			self.allowleft=False
		else:
			self.allowleft=True

		if isfloor==False:
			self.floor=False
		else:
			self.floor=True

	def move_right(self):
		if self.allowright==True:
			self.x-=1

	def move_left(self):
		if self.allowleft==True:
			self.x+=1

	def move_up_right(self):
		if self.allowright==True:
			self.x-=1
			self.y+=1
		else:
			self.fall()

	def move_down_right(self):
		if self.allowright==True:
			self.x-=1
			self.y-=1
		else:
			self.fall()

	def move_up_left(self):
		if self.allowleft==True:
			self.x+=1
			self.y+=1
		else:
			self.fall()

	def move_down_left(self):
		if self.allowleft==True:
			self.x+=1
			self.y-=1
		else:
			self.fall()

	def fall(self):
		if self.floor==False:
			self.y-=1

class player(person):
	def __init__(self):
		self.lives=3
		self.points=0
		self.totalpoints=0

	def climb_up(self):
		if self.allowup==True:
			self.y+=1

	def climb_down(self):
		if self.allowdown==True:
			self.y-=1

	def setcondition(self,iscoin,isfireball):
		if iscoin==True:
			self.points+=5

		if isfireball==True:
			self.lives-=1
			self.points-=25

class Fireball(person):
	def __init__(self,x,y):
		if randint(0,10)%2==0:
			self.dir='r'
		else:
			self.dir='l'
		self.x=x+1
		self.y=y
		self.state=0

	def show(self):
		return [self.x,self.y]

	def climb_down(self):
		if self.allowdown==True:
			self.y-=1

	def move(self):
		if self.state==1 or self.state==2 or self.state==3:
			self.climb_down()
			self.state+=1
			self.state%=4
		elif self.allowdown==True and randint(1,100)%2==0 and self.state==0:
			self.climb_down()
			self.state=1
		elif self.dir=='r' and self.allowright==True:
			self.move_right()
		elif self.dir=='l' and self.allowleft==True:
			self.move_left()
		elif self.allowleft==False:
			self.dir='r'
		else:
			self.dir='l'

class donkey(person):
	def __init__(self):
		self.dir='r'
		self.fireballs=[]

	def setvar_donkey(self,allow_left,allow_right):
		if allow_left==True:
			self.allowleft=True
		else:
			self.allowleft=False
		if allow_right==True:
			self.allowright=True
		else:
			self.allowright=False

	def move(self):
		if self.dir=='r' and self.allowright==True:
			if randint(0,100)%10==0:
				self.dir='l'
			else:
				self.move_right()
		elif self.dir=='l' and self.allowleft==True:
			if randint(0,100)%10==0:
				self.dir='r'
			else:
				self.move_left()
		elif self.allowleft==False:
			self.dir='r'
		else:
			self.dir='l'

		for i in self.fireballs:
			i.move()
		self.loc=[]
		for i in self.fireballs:
			self.loc.append(i.show())
		return self.loc[:]

	def emitfireball(self):
		if randint(0,1000)%50==0:
			fireball=Fireball(self.x,self.y)
			print 'Fireball!!!'
			self.fireballs.append(fireball)

	def setvarfireball(self,i,set6,set1,set4,set5):
		i.setvar(i.x,i.y,set6,set1,set4,set5)

