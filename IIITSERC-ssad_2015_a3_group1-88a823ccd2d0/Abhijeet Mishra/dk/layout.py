import random


def colourPrint(pixel):
	""" Function for coloured output"""
	if(pixel=="X"):
		print '\033[1;41mX\033[1;m',
	elif(pixel=="H"):
		print '\033[1;47mH\033[1;m',
	elif(pixel=="C"):
		print '\033[1;33mC\033[1;m',
	elif(pixel=="P"):
		print '\033[1;42mP\033[1;m',
	else:
		print pixel,		


class Board(object):
	"""Contains methods for altering the layout and set up of the game"""
	def __init__(self, rows=30,columns=80): 
		"""Sets up the building blocks of the layout"""
		self.rows = rows
		self.columns = columns
		self.layout = [[" " for i in range(columns)] for i in range(rows)]
	
	def addWalls(self):
		"""Adds waals to the game board"""
		layout = self.layout
		rows = self.rows
		columns = self.columns
		for i in range(5):
			for j in range(columns):
				if(i==0 or j==0 or j == (columns-1)):
					layout[i][j]="X"
		for i in range(5,rows):
			for j in range(columns):
				if(i==0 or j==0 or j == (columns-1)):
					layout[i][j]="X"
				if(i%5==0):
					layout[i][j]="X"
				
		return layout

	def addStairs(self):
		layout = self.layout
		rows = self.rows
		columns = self.columns
		upperLevels = [5,10,15,20,25]
		stairPlacement = [13,33,55,27,15]
		for i in range(5):
			# stairPlacement = random.randint(14,34)
			j = upperLevels[i]+1
			for k in range(4):
				layout[j][stairPlacement[i]] = "H"
				j +=1

				
		return layout 	

		

	def addCracks(self):
		"""Adds cracks in floors for the player to fall through"""
		layout = self.layout
		rows = self.rows
		columns = self.columns
		cracks = random.randint(6,10)
		for i in range(5,26):
			if(i%5 == 0 and i%10 == 0):
				for j in range(cracks):
					layout[i][j+1]=" "
			elif(i%5 == 0 and i%10 != 0):
				for j in range(cracks):
					layout[i][columns-j-2]=" "
		self.layout = layout				
		return self

	def addPrincess(self):
		"""Adds cracks in floors for the player to fall through"""
		layout = self.layout
		rows = self.rows
		columns = self.columns
		cracks = random.randint(6,10)
		for i in range(5,26):
			if(i%5 == 0 and i%10 == 0):
				for j in range(cracks):
					layout[i][j+1]=" "
			elif(i%5 == 0 and i%10 != 0):
				for j in range(cracks):
					layout[i][columns-j-2]=" "
		self.layout = layout				
		return self

	def addCoins(self):
		"""Places coins on the game board"""
		layout = self.layout
		rows = self.rows
		columns = self.columns
		coinsCount = 48
		coinRows = [9,14,19,24,29]
		for i in range(coinsCount):
			coinRow = coinRows[i%5]
			if((coinRow+1)%10==0):
				coinColumn = random.randint(12,65)
			else:
				coinColumn = random.randint(1,58)
			layout[coinRows[i%5]][coinColumn] = "C"
		self.layout = layout
		return layout




	
	def printBoard(self,player):
		""" Prints the game board"""
		rows = self.rows
		columns = self.columns
		layout = self.layout
		print "  ",
		for i in range(columns):
			print " ",
		print ""
		for i in range(rows):
			print " " ,
			for j in range(columns):
				colourPrint(layout[i][j])
			print ""
		print "Coins: ",player.coins
		print "Score: ",player.score

