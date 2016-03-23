from board import Board
class Player:
	def __init__(self):
		self.posx=28
		self.posy=3
		self.score=0
		self.life=3
	def checkWall(self,var):
		if var=="d":
			if Board.board[self.posx][self.posy+1]=="X":
				return 0
			else: 
				return 1
		elif var=="a":
			if Board.board[self.posx][self.posy-1]=="X":
				return 0
			else:
				return 1
	def move(self,var):
		if var=="d":
			if self.checkWall(var)==1:
				if Board.board[self.posx][self.posy+1]=="C":
					self.score+=5
				Board.board[self.posx][self.posy]=" "
				if Board.board[self.posx-1][self.posy]=="H":
					Board.board[self.posx][self.posy]="H"
				self.posy+=1
				Board.board[self.posx][self.posy]="P"
				if Board.board[self.posx+1][self.posy]==" ":
					Board.board[self.posx][self.posy]=" "
					self.fall()
		elif var=="a":
			if self.checkWall(var)==1:
				if Board.board[self.posx][self.posy-1]=="C":
					self.score+=5
				Board.board[self.posx][self.posy]=" "
				if Board.board[self.posx-1][self.posy]=="H":
					Board.board[self.posx][self.posy]="H"
				self.posy-=1
				Board.board[self.posx][self.posy]="P"
				if Board.board[self.posx+1][self.posy]==" ":
					Board.board[self.posx][self.posy]=" "
					self.fall()
		elif var=="w":
			if Board.board[self.posx-1][self.posy]=="H":
				Board.board[self.posx][self.posy]="H"
				self.posx-=1
				Board.board[self.posx][self.posy]="P"
			elif Board.board[self.posx][self.posy]=="P" and Board.board[self.posx+1][self.posy]=="H" and Board.board[self.posx][self.posy+1]=="X":
				Board.board[self.posx][self.posy]="H"
				self.posx-=1
				Board.board[self.posx][self.posy]="P"
		elif var=="s":
			if Board.board[self.posx+1][self.posy]=="H":
				Board.board[self.posx][self.posy]="H"
				if Board.board[self.posx-1][self.posy]==" " and Board.board[self.posx][self.posy-1]==" ":
					Board.board[self.posx][self.posy]=" "
				self.posx+=1
				Board.board[self.posx][self.posy]="P"
	def fall(self):
		while Board.board[self.posx+1][self.posy]!="X":
			self.posx+=1
			if Board.board[self.posx][self.posy]=="C":
				self.score+=5
		Board.board[self.posx][self.posy]="P"
	def jump(self,var,steps):
		if var=="d":
			
			if steps<2:
				Board.board[self.posx][self.posy]=" " 	
				self.posx-=1
				self.posy+=1
				if Board.board[self.posx][self.posy]=="X":
					self.posx+=1
					self.posy-=1
					self.fall()
				Board.board[self.posx][self.posy]="P"
			elif steps>=2:
				Board.board[self.posx][self.posy]=" "
				self.posx+=1
				self.posy+=1
				if Board.board[self.posx][self.posy]=="X":
					self.posx-=1
					self.posy-=1
					self.fall()
				Board.board[self.posx][self.posy]="P"		
		elif var=="a":
			if steps<2:
				Board.board[self.posx][self.posy]=" "
				self.posx-=1
				self.posy-=1
				if Board.board[self.posx][self.posy]=="X":
					self.posx+=1
					self.posy+=1
					self.fall()
				Board.board[self.posx][self.posy]="P"
			elif steps>=2:
				Board.board[self.posx][self.posy]=" "
				self.posx+=1
				self.posy-=1
				if Board.board[self.posx][self.posy]=="X":
					self.posx-=1
					self.posy+=1
					self.fall()
				Board.board[self.posx][self.posy]="P"
		elif var=="w":
			if steps<2:
				Board.board[self.posx][self.posy]=" "
				self.posx-=1
				Board.board[self.posx][self.posy]="P"
			elif steps>=2:
				Board.board[self.posx][self.posy]=" "
				self.posx+=1
				Board.board[self.posx][self.posy]="P"
