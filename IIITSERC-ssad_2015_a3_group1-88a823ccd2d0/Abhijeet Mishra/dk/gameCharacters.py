from control import *
class Person():
	"""Class for defining in-game characters"""
	
	def getPosition(self, Board):
		idChar = self.idChar
		layout = Board.layout
		rows = Board.rows
		columns = Board.columns
		for i in rows:
			for j in columns:
				if(layout[i][j]==idChar):
					self.position[0]=i
					self.position[1]=j
				return position

class Player(Person):
	def __init__(self,idchar="P"): 
		"""Sets up the building blocks of the layout"""
		self.idChar = "P"
		self.position = [29,1]
		self.coins = 0
		self.score = 0
	def createPlayer(self):
		self.position = [int("29"),int("1")]
	def spawnPlayer(self,Board):
		position = self.position
		Board.layout[position[0]][position[1]] = self.idChar
		print self.idChar
		return 	
	
	def movePlayer(self,direction,Board):
		prevPosition = self.position
		position = self.position
		layout = Board.layout
		if(direction=="d"):
			if((layout[position[0]][position[1]+1]==" " or layout[position[0]][position[1]+1]=="C")and layout[position[0]+1][position[1]+1]=="X"):
				if(layout[position[0]][position[1]+1]=="C"):
					self.coins += 1
					self.score += 5
				self.position[1] +=1
				position = self.position
				Board.layout[position[0]][position[1]-1]=" "
				Board.addStairs()
			elif(layout[position[0]][position[1]+1]=="H"):
				Board =	ladderPlacePrev(self,Board,encounterLadderRight(self,Board))
		elif(direction=="a"):
			if((layout[position[0]][position[1]-1]==" " or layout[position[0]][position[1]-1]=="C")and layout[position[0]+1][position[1]-1]=="X"):
				if(layout[position[0]][position[1]-1]=="C"):
					self.coins += 1
					self.score += 5
				self.position[1] -=1
				position = self.position
				Board.layout[position[0]][position[1]+1]=" "
				Board.addStairs()
			elif(layout[position[0]][position[1]-1]=="H"):
				Board =	ladderPlacePrev(self,Board,encounterLadderLeft(self,Board))
		elif(direction=="w"):
			if(layout[position[0]-1][position[1]]=="H"):
				self.position[0] -=1
				position = self.position
				encounterLadderUp(self,Board)
				Board.addStairs()
			elif(layout[position[0]-1][position[1]]=="X"):
				self.position[0] -=2
				position = self.position
				encounterLadderUp(self,Board)
				Board.addStairs()
		elif(direction=="s"):
			if(layout[position[0]+1][position[1]]=="H"):
				self.position[0] +=1
				position = self.position
				encounterLadderUp(self,Board)
				Board.addStairs()
			elif(position[0] != 29 and layout[position[0]+2][position[1]]=="H"):
				prevPosition = self.position
				Board.layout[prevPosition[0]][prevPosition[1]]=" "
				self.position[0] +=2
				position = self.position
				encounterLadderUp(self,Board)
				Board.addStairs()

			
		
		return Board

def encounterLadderRight(Player,Board):
	prevPosition = Player.position
	Player.position[1] +=1
	position =Player.position
	Board.layout[position[0]][position[1]-1]=" "
	Board.layout[prevPosition[0]][prevPosition[1]]=" "
	Player.spawnPlayer(Board)
	ladderPlace=Player.position
	return ladderPlace

def encounterLadderLeft(Player,Board):
	prevPosition = Player.position
	Player.position[1] -=1
	position =Player.position
	Board.layout[position[0]][position[1]+1]=" "
	Board.layout[prevPosition[0]][prevPosition[1]]=" "
	Player.spawnPlayer(Board)
	ladderPlace=Player.position
	return ladderPlace

def encounterLadderUp(Player,Board):
	prevPosition = Player.position
	position =Player.position
	Board.layout[position[0]][position[1]-1]=" "
	Board.layout[prevPosition[0]][prevPosition[1]]="H"
	Player.spawnPlayer(Board)
	ladderPlace=Player.position
	Board.addStairs()
	Player.spawnPlayer(Board)
	Board.printBoard(Player)
	return ladderPlace

def encounterLadderUp(Player,Board):
	prevPosition = Player.position
	position =Player.position
	Board.layout[position[0]][position[1]-1]=" "
	Board.layout[prevPosition[0]][prevPosition[1]]="H"
	Player.spawnPlayer(Board)
	ladderPlace=Player.position
	Board.addStairs()
	Player.spawnPlayer(Board)
	Board.printBoard(Player)
	return ladderPlace

def ladderPlacePrev(p1,board,ladderPlace):
	os.system("clear")
	board.printBoard(p1)
	direction = getch()
	if(direction=="q"):
		sys.exit()
	p1.movePlayer(direction,board)
	board.addStairs()
	p1.spawnPlayer(board)
	board.printBoard(p1)
	print ladderPlace
	return board