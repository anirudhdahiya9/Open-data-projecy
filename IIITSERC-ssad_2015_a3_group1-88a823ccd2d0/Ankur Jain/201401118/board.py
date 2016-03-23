import sys
import random
from random import randint
width=30
length=80
class Board:
	board = [[' ' for i in range(length)] for y in range(width)]
	for i in range(width):	
		board[i][0]="X"
		board[i][79]="X"
	for j in range(length):
		board[0][j]="X"
		board[29][j]="X"
	for j in range(0,60):
		board[24][j]="X"
	for j in range(0,45):
		board[14][j]="X"
	for j in range(15,80):
		board[10][j]="X"
	for j in range(22,80):
		board[19][j]="X"
	for j in range(0,50):
		board[6][j]="X"
	for j in range(15,31):
		board[3][j]="X"
	for i in range(0,3):
		board[i][15]="X"
	for i in range(0,3):
		board[i][30]="X"
	for i in range(24,29):
		board[i][50]="H"
	for i in range(19,24):
		board[i][25]="H"
		board[i][57]="H"
	board[22][57]=" "
	board[23][57]=" "
	for i in range(14,19):
		board[i][42]="H"
	for i in range(10,14):
		board[i][20]="H"
		board[i][35]="H"
	board[12][35]=" "
	board[13][35]=" "
	
	for i in range(6,10):
		board[i][44]="H"
	for i in range(3,6):
		board[i][22]="H"
	board[5][4]="D"
	board[2][18]="Q"
	board[28][3]="P"
	height = [5,18,9,13,23,28]
	for i in range(25):
		y = random.choice(height)
		if(y==5):
			x=random.choice(range(5,50))
		elif(y==18):
			x=random.choice(range(22,79))
		elif(y==9):
		 	x=random.choice(range(15,79))
		elif(y==13):
		 	x=random.choice(range(5,45))
		elif(y==23):
		 	x=random.choice(range(5,60))
		elif(y==28):
		 	x=random.choice(range(5,79))
		board[y][x]="C"
	for i in range(width):
		for j in range(length):
			sys.stdout.write(board[i][j])
		print
