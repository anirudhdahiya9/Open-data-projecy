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


class board:
	def __init__(self):
		self.board=[['X']*80]
		for i in range(1,29):
			self.board=self.board+[['X']+78*[' ']+['X']]
		self.board+=[['X']*80]
		for i in range(65):
			for j in range(5,30,8):
				self.board[j][i]='X'
		for i in range(15,80):
			for j in range(9,30,8):
				self.board[j][i]='X'
		for i in range(25,29):
			self.board[i][60]='H'
		for i in range(13,17):
			self.board[i][65]='H'
		for i in range(5,9):
			self.board[i][55]='H'
		for i in range(21,25):
			self.board[i][20]='H'
		for i in range(9,13):
			self.board[i][16]='H'
		for i in range(0,15):
			self.board[2][i]='X'
		for i in range(2,5):
			self.board[i][2]='H'
		self.board[1][14]='X'
		import random
		for i in range(25):
			while True:
				x=random.randint(15,65)
				y=random.randint(1,28)
				tp=self.board[y][x]
				if tp==' ':
					break
			self.board[y][x]='C'	

			

	def printboard(self,plr,don=0):
		import os
		from time import sleep
		os.system('clear')
		self.board[plr.y][plr.x]='P'
		if type(don)==int:
			pass
		else:
			self.board[don.y][don.x]='D'
		for i in self.board:
			ln=''	
			print ln.join(i)
		print 'Score:',plr.score
		sleep(0.08)
	
		
	def getitem(self,x,y):
		return self.board[y][x]
	
		
	def updateitem(self,y,x,tmp):
		self.board[y][x]=tmp		
		return self

	def checkwall(self,plr,mv):
		if mv.lower()=='d':
			if self.board[plr.y][plr.x+1]=='X':
				return True
			return False
		elif mv.lower()=='a':
			if self.board[plr.y][plr.x-1]=='X':
				return True
			return False
		elif mv.lower()=='s':
			if self.board[plr.y+1][plr.x]=='X':
				return True
			return False

	def checkstair(self,plr,mv):
		if self.board[plr.y][plr.x]=='H':
			return True
		return False

	def checkfloor(self,plr):
		if self.board[plr.y+1][plr.x]==' ' or self.board[plr.y+1][plr.x]=='C':
			return False
		return True

class player:
	def __init__(self,name,x=1,y=28):
		self.x=x
		self.y=y
		self.name=name
		self.score=0

	def getcoin(self,tmp):
		if tmp=='C':
			tmp=' '
			self.score+=5
		return tmp


	def move(self,plr,brd,tmp,mode=0,mv=''):
		if mv=='':
			pass
		elif mv.lower()=='d':
			if brd.checkwall(plr,mv):
				return plr,tmp
			else:
				brd=brd.updateitem(plr.y,plr.x,tmp)
				tmp=brd.getitem(plr.x+1,plr.y)
				tmp=self.getcoin(tmp)
				plr.x+=1
				return plr,tmp
		elif mv.lower()=='a':
			if brd.checkwall(plr,mv):
				return plr,tmp
			else:
				brd=brd.updateitem(plr.y,plr.x,tmp)
				tmp=brd.getitem(plr.x-1,plr.y)
				tmp=self.getcoin(tmp)
				plr.x-=1
				return plr,tmp
		elif mv.lower()=='w':
		 	if mode==0:
				if not tmp=='H':
					return plr,tmp
				if brd.checkwall(plr,mv):
					return plr,tmp
				else:
					brd=brd.updateitem(plr.y,plr.x,tmp)
					tmp=brd.getitem(plr.x,plr.y-1)
					tmp=self.getcoin(tmp)
					plr.y-=1
					return plr,tmp
			elif mode==1:
				brd=brd.updateitem(plr.y,plr.x,tmp)
				tmp=brd.getitem(plr.x,plr.y-1)
				tmp=self.getcoin(tmp)
				plr.y-=1
				return plr,tmp
				
		elif mv.lower()=='s':
			if brd.checkwall(plr,mv):
				return plr,tmp
			else:
				brd=brd.updateitem(plr.y,plr.x,tmp)
				tmp=brd.getitem(plr.x,plr.y+1)
				tmp=self.getcoin(tmp)
				plr.y+=1
				return plr,tmp
		elif mv.lower()=='q':
			exit()
		else:
			return plr,tmp
	
	def checkfall(self,brd,tmp,don):
		from time import sleep
		while not brd.checkfloor(self):
			sleep(0.12)
			self,tmp=self.move(self,brd,tmp,0,'s')
			brd.printboard(self,don)
		return self,tmp
	
	def jump(self,brd,direction,tmp,don):
		if direction==0:
			if brd.getitem(y=self.y-1,x=self.x+1)!='X':
				self,tmp=self.move(self,brd,tmp,0,'d')
				self,tmp=self.move(self,brd,tmp,1,'w')
				brd.printboard(self,don)
			else:
				self,tmp=self.checkfall(brd,tmp,don)
					
			if brd.getitem(y=self.y-1,x=self.x+1)!='X':
				self,tmp=self.move(self,brd,tmp,0,'d')
				self,tmp=self.move(self,brd,tmp,1,'w')
				brd.printboard(self,don)
			else:
				self,tmp=self.checkfall(brd,tmp,don)
			if brd.getitem(y=self.y+1,x=self.x+1)!='X':
				self,tmp=self.move(self,brd,tmp,0,'d')
				self,tmp=self.move(self,brd,tmp,1,'s')
				brd.printboard(self,don)
			else:
				self,tmp=self.checkfall(brd,tmp,don)
		
			if brd.getitem(y=self.y+1,x=self.x+1)!='X':
				self,tmp=self.move(self,brd,tmp,0,'d')
				self,tmp=self.move(self,brd,tmp,1,'s')
				brd.printboard(self)
			else:
				self,tmp=self.checkfall(brd,tmp,don)
		else:
			if brd.getitem(y=self.y-1,x=self.x-1)!='X':
				self,tmp=self.move(self,brd,tmp,0,'a')
				self,tmp=self.move(self,brd,tmp,1,'w')
				brd.printboard(self,don)
			else:
				self,tmp=self.checkfall(brd,tmp,don)
					
			if brd.getitem(y=self.y-1,x=self.x-1)!='X':
				self,tmp=self.move(self,brd,tmp,0,'a')
				self,tmp=self.move(self,brd,tmp,1,'w')
				brd.printboard(self,don)
			else:
				self,tmp=self.checkfall(brd,tmp,don)
			if brd.getitem(y=self.y+1,x=self.x-1)!='X':
				self,tmp=self.move(self,brd,tmp,0,'a')
				self,tmp=self.move(self,brd,tmp,1,'s')
				brd.printboard(self,don)
			else:
				self,tmp=self.checkfall(brd,tmp,don)
		
			if brd.getitem(y=self.y+1,x=self.x-1)!='X':
				self,tmp=self.move(self,brd,tmp,0,'a')
				self,tmp=self.move(self,brd,tmp,1,'s')
				brd.printboard(self,don)
			else:
				self,tmp=self.checkfall(brd,tmp)
		return self,tmp

class donkey:
	def __init__(self):
		self.x=4
		self.y=4
		self.direction=0
		self.flip=0
		self.dtemp=' '
			
	def move(self,brd):
		import random
		if self.x==64:
			self.direction=1
		if self.x==4:
			self.direction=0
		if not self.flip==6:
			if self.direction==0:
				self.dtemp=brd.board[4][self.x+1]
				brd.board[4][self.x]=self.dtemp
				self.x+=1
			else:
				self.dtemp=brd.board[4][self.x-1]
				brd.board[4][self.x]=self.dtemp
				self.x-=1
			self.flip+=1
		else:
			if self.direction==0:
				self.dtemp=brd.board[4][self.x+1]
				brd.board[4][self.x]=self.dtemp
				self.x+=1
			else:
				self.dtemp=brd.board[4][self.x-1]
				brd.board[4][self.x]=self.dtemp
				self.x-=1
			self.flip=0
			self.direction=random.randint(0,1)
		return self
			

		
		
	
def main():
	import os
	from time import sleep
	brd=board()
	plr=player('Dahiya')
	don=donkey()
	brd.printboard(plr,don)
	tmp=' '
	direction=0
	while True:
		plr,tmp=player.checkfall(plr,brd,tmp,don)
		mv=getchar()
		if mv==' ':
			plr,tmp=plr.jump(brd,direction,tmp,don)
		else:
			if mv.lower()=='a':
				direction=1
			elif mv.lower()=='d':
				direction=0
			plr,tmp=plr.move(plr,brd,tmp,0,mv)
			don=don.move(brd)
		brd.printboard(plr,don)



	
if __name__=="__main__":
	main()
