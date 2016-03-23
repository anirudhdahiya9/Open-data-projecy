def getchar():
	import tty, termios, sys
	fd = sys.stdin.fileno()
	old_settings = termios.tcgetattr(fd)
	try:
		tty.setraw(sys.stdin.fileno())
		ch = sys.stdin.read(1)
	finally:
		termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
		return ch

def start(plr):
	from random import randint
	from time import sleep
	import os
	if plr.lives<0:	
		print 'GAME OVER!!!!!!!!'
		sleep(2)
		exit()
	plr.x=2
	plr.y=24
	brd=board()
	don=donkey()
	b1=[ball(don)]
	brd.printboard(plr,don,b1)
	while True:
		if plr.x==13 and plr.y==1:
			print 'You win!','Wanna play again? (y/n):'
			ans=getchar()
			if ans.lower()=='y':
				main()
			print 'Bye! Have fun with that princess!!'
			sleep(4)
			exit()
		if plr.x==don.x and plr.y==don.y:
			os.system('clear')
			print 'Oops!! That Hurt!'
			plr.lives-=1
			sleep(1)
			plr.score=0
			start(plr)
		if plr.x==don.x+1 and plr.y==don.y:
			if plr.direction==1 and don.direction==0:
				os.system('clear')
				print 'Oops!! That Hurt!'
				plr.lives-=1
				sleep(1)
				plr.score=0
				start(plr)
		if plr.x==don.x-1 and plr.y==don.y:
			if plr.direction==0 and don.direction==1:
				os.system('clear')
				print 'Oops!! That Hurt!'
				plr.lives-=1
				sleep(1)
				plr.score=0
				start(plr)
		for i in b1:
			if i.x==plr.x and i.y==plr.y:
				os.system('clear')
				print 'Oops!! That Hurt!'
				plr.lives-=1
				sleep(1)
				plr.score=0
				start(plr)
			if i.x==plr.x+1 and i.y==plr.y:
				if i.direction==1 and plr.direction==0:
					os.system('clear')
					print 'Oops!! That Hurt!'
					plr.lives-=1
					sleep(1)
					plr.score=0
					start(plr)
			if i.x==plr.x-1 and i.y==plr.y:
				if i.direction==0 and plr.direction==1:
					os.system('clear')
					print 'Oops!! That Hurt!'
					plr.lives-=1
					sleep(1)
					plr.score=0
					start(plr)
		if randint(0,randint(3,6))==1:
			b1+=[ball(don)]
		plr=player.checkfall(plr,brd,don,b1)
		mv=getchar()
		if mv==' ':
			plr=plr.jump(brd,don,b1)
		else:
			if mv.lower()=='a':
				plr.direction=1
			elif mv.lower()=='d':
				plr.direction=0
			plr=plr.move(plr,brd,0,mv)
		for i in b1:
			i=i.move(brd)
		don=don.move(brd)
		brd.printboard(plr,don,b1)

class board:
	def __init__(self):
		self.__makeframe()
		self.__board[1][14]='X'
		self.__board[1][13]='Q'
		self.__generatecoins()

	def __makeframe(self):
		self.__board=[['X']*80]
		for i in range(1,25):
			self.__board=self.__board+[['X']+78*[' ']+['X']]
		self.__board+=[['X']*80]
		for i in range(65):
			for j in range(5,26,8):
				self.__board[j][i]='X'
		for i in range(15,80):
			for j in range(9,26,8):
				self.__board[j][i]='X'
		
		for i in range(21,25):
			self.__board[i][60]='H'
		for i in range(13,17):
			self.__board[i][65]='H'
		for i in range(5,9):
			self.__board[i][60]='H'
		for i in range(17,21):
			self.__board[i][20]='H'
		for i in range(9,13):
			self.__board[i][16]='H'
		for i in range(0,15):
			self.__board[2][i]='X'
		for i in range(2,5):
			self.__board[i][2]='H'

	def __generatecoins(self):
		import random
		for i in range(25):
			while True:
				x=random.randint(15,65)
				y=random.randint(1,25)
				tp=self.getitem(x,y)
				if tp==' ':
					break
			self.updateitem(x,y,'C')	

	def __copyboard(self):
		copy=[]		
		for i in range(len(self.__board)):
			copy+=[[]]
			for j in range(len(self.__board[i])):
				if self.getitem(j,i)==' ':
					copy[i]+=[' ']
				elif self.getitem(j,i)=='X':
					copy[i]+='X'
				elif self.getitem(j,i)=='H':
					copy[i]+='H'
				elif self.getitem(j,i)=='C':
					copy[i]+='C'
				elif self.getitem(j,i)=='Q':
					copy[i]+='Q'
				else:
					copy[i]+='X'
		return copy

	def __getbitms(self,copy,plr,b1,don):
		copy[plr.y][plr.x]='P'
		for i in b1:
			copy[i.y][i.x]='F'
		if type(don)==int:
			pass
		else:
			copy[don.y][don.x]='D'
		return copy


	def printboard(self,plr,don,b1):
		import os
		from time import sleep
		os.system('clear')
		copy=self.__copyboard()
		copy=self.__getbitms(copy,plr,b1,don)
		for i in copy:
			ln=''	
			print ln.join(i)
		print 'Score:',plr.score
		print 'Lives:',plr.lives
		sleep(0.08)
	
		
	def getitem(self,x,y):
		return self.__board[y][x]

	def updateitem(self,x,y,c):
		self.__board[y][x]=c
	
		

	def checkwall(self,plr,mv):
		if mv.lower()=='d':
			if self.getitem(plr.x+1,plr.y)=='X':
				return True
			return False
		elif mv.lower()=='a':
			if self.getitem(plr.x-1,plr.y)=='X':
				return True
			return False
		elif mv.lower()=='s':
			if self.getitem(plr.x,plr.y+1)=='X':
				return True
			return False

	def checkstair(self,plr,mv):
		if self.getitem(plr.x,plr.y)=='H':
			return True
		return False

	def checkfloor(self,plr):
		if self.getitem(plr.x,plr.y+1)==' ' or self.getitem(plr.x,plr.y+1)=='C':
			return False
		return True

class boarditems:
	def __init__(self,x,y):
		self.x=x
		self.y=y
		self.direction=0


class player(boarditems):
	def __init__(self):
		boarditems.__init__(self,1,24)
		self.score=0
		self.lives=3

	def getcoin(self,brd):
		if brd.getitem(self.x,self.y)=='C':
			brd.updateitem(self.x,self.y,' ')
			self.score+=5

# 0 means right direction, 1 means left
	def move(self,plr,brd,mode=0,mv=''):
		if mv=='':
			pass
		elif mv.lower()=='d':
			if brd.checkwall(plr,mv):
				return plr
			else:
				self.getcoin(brd)
				plr.x+=1
				return plr
		elif mv.lower()=='a':
			if brd.checkwall(plr,mv):
				return plr
			else:
				self.getcoin(brd)
				plr.x-=1
				return plr
		elif mv.lower()=='w':
		  	if mode==0:
				if not brd.getitem(self.x,self.y)=='H':
					return plr
				if brd.checkwall(plr,mv):
					return plr
				else:
					self.getcoin(brd)
					plr.y-=1
					return plr
			elif mode==1:
				if brd.checkwall(plr,mv):
					return plr
				else:
					self.getcoin(brd)
					plr.y-=1
					return plr
				
		elif mv.lower()=='s':
			if brd.checkwall(plr,mv):
				return plr
			else:
				self.getcoin(brd)
				plr.y+=1
				return plr
		elif mv.lower()=='q':
			exit()
		else:
			return plr
	
	def checkfall(self,brd,don,b1):
		from time import sleep
		while not brd.checkfloor(self):
			sleep(0.12)
			self=self.move(self,brd,0,'s')
			brd.printboard(self,don,b1)
		return self
	
	def jump(self,brd,don,b1):
		if self.direction==0:
			if brd.getitem(y=self.y-1,x=self.x+1)!='X':
				self=self.move(self,brd,0,'d')
				self=self.move(self,brd,1,'w')
				brd.printboard(self,don,b1)
			else:
				self=self.checkfall(brd,don,b1)
					
			if brd.getitem(y=self.y-1,x=self.x+1)!='X':
				self=self.move(self,brd,0,'d')
				self=self.move(self,brd,1,'w')
				brd.printboard(self,don,b1)
			else:
				self=self.checkfall(brd,don,b1)
			if brd.getitem(y=self.y+1,x=self.x+1)!='X':
				self=self.move(self,brd,0,'d')
				self=self.move(self,brd,1,'s')
				brd.printboard(self,don,b1)
			else:
				self=self.checkfall(brd,don,b1)
		
			if brd.getitem(y=self.y+1,x=self.x+1)!='X':
				self=self.move(self,brd,0,'d')
				self=self.move(self,brd,1,'s')
				brd.printboard(self,don,b1)
			else:
				self=self.checkfall(brd,don,b1)
		elif self.direction==1:
			if brd.getitem(y=self.y-1,x=self.x-1)!='X':
				self=self.move(self,brd,0,'a')
				self=self.move(self,brd,1,'w')
				brd.printboard(self,don,b1)
			else:
				self=self.checkfall(brd,don,b1)
					
			if brd.getitem(y=self.y-1,x=self.x-1)!='X':
				self=self.move(self,brd,0,'a')
				self=self.move(self,brd,1,'w')
				brd.printboard(self,don,b1)
			else:
				self=self.checkfall(brd,don,b1)
			if brd.getitem(y=self.y+1,x=self.x-1)!='X':
				self=self.move(self,brd,0,'a')
				self=self.move(self,brd,1,'s')
				brd.printboard(self,don,b1)
			else:
				self=self.checkfall(brd,don,b1)
		
			if brd.getitem(y=self.y+1,x=self.x-1)!='X':
				self=self.move(self,brd,0,'a')
				self=self.move(self,brd,1,'s')
				brd.printboard(self,don,b1)
			else:
				self=self.checkfall(brd,don,b1)
		return self

class donkey(boarditems):
	def __init__(self):
		boarditems.__init__(self,4,4)
		self.flip=0

	def __revertback(self):
		if self.x==64:
			self.direction=1
		if self.x==4:
			self.direction=0
		return self
	
	def __singlemove(self):
		if self.direction==0:
			self.x+=1
		else:
			self.x-=1
		return self
			
	def move(self,brd):
		import random
		self=self.__revertback()
		if not self.flip==6:
			self=self.__singlemove()
			self.flip+=1
		else:
			self=self.__singlemove()
			self.flip=0
			self.direction=random.randint(0,1)
		return self
			
class ball(boarditems):
	def __init__(self,don):
		if don.direction==0:
			self.x=don.x+1
		else:
			self.x=don.x-1
		self.y=don.y
		self.direction=don.direction
		self.mode=0

	def move(self,brd):
		if brd.checkfloor(self) and brd.getitem(self.x,self.y+1)!='H' and self.mode==0:
			if self.direction==0:
				if brd.getitem(self.x+1,self.y)=='X':
					self.direction=1
				else:
					self.x+=1
			else:
				if brd.getitem(self.x-1,self.y)=='X':
					self.direction=0
				else:
					self.x-=1
		elif brd.checkfloor(self) and brd.getitem(self.x,self.y+1)!='H' and self.mode==1:
			import random
			self.direction=random.randint(0,1)
			self.mode=0
			if self.direction==0:
				if brd.getitem(self.x+1,self.y)=='X':
					self.direction=1
				else:
					self.x+=1
			else:
				if brd.getitem(self.x-1,self.y)=='X':
					self.direction=0
				else:
					self.x-=1
			
		else:
			if brd.getitem(self.x,self.y+1)!='X':
				self.mode=1
				self.y+=1
		return self



				
	
def main():
	import os
	from time import sleep
	from random import randint
	plr=player()
	start(plr)



		
if __name__=="__main__":
	main()
