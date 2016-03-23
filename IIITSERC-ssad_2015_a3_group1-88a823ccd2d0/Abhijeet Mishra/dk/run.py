from layout import *
from gameCharacters import *
import os,sys
board = Board(31,70)
board.addWalls()
board = board.addCracks()
board.addCoins()
board.addStairs()
p1 = Player("P")
p1.createPlayer()
p1.spawnPlayer(board)
board.printBoard(p1)
while(1==1):
	os.system("clear")
	board.printBoard(p1)
	direction = getch()
	if(direction=="q"):
		break
	p1.movePlayer(direction,board)
	p1.spawnPlayer(board)
 	
	