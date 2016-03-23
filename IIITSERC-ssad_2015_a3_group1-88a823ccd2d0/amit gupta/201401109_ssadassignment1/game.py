#!/usr/bin/python
from __future__ import print_function
from takeInput import _Getch
import os, random, time
import customFunctions as my
import controller
import sys

#----------------------------------VARIOUS CLASSES AND METHODS DEFINITION------------------------------------------
class person:
	def __init__(self):
		self.score = 0
		self.__life = 5
		self.__level = 1
	def __display(self):
		print("Players name is " + self.name)
	def __reduceLife(self):
		pass
	def __increaseLevel(self):
		pass

class Player(person):
	def __init__(self, nameOfPlayer):
		self.name = nameOfPlayer
		my.clearIt()
		print("Ok", nameOfPlayer + "\n" +  "Let's begin the real showdown..!!")

	def _positionChanger(self,myBoard,playerPosition):
		myBoard[playerPosition.x][playerPosition.y] = 'P'
		pass
	def _takeInput(self):
		key = getch()
		return key
		pass
	def _scoreChanger(self, GameObject, GameSetup):
		GameSetup.displayScore(GameObject.score)
		pass
class fireball(person):
	def gotladder(self, myBoard,ballposition):
		if myBoard[ballposition.x+1][ballposition.y]=='H':
			ballposition.x=ballposition.x+1;
class DonkeyKong(person):
        
	def throwFireBall(self):
		pass

class gameDisplaySetup:
	def __init__(self,myBoard, lengthOfBoard, breadthOfBoard):
		#self.__floorArray = []
		self._lengthOfBoard = lengthOfBoard
		self._breadthOfBoard = breadthOfBoard
		myBoard = self.__boardInitialize(myBoard)
		self.__border(myBoard)
		self.floor(myBoard)
		self.coins(myBoard)
               # self.coins1(myBoard)
	
                self.stairs1(myBoard)
		self.myBoard = myBoard
		
	def __border(self, myBoard):
		#Horizontal Border
		for y in xrange(0,self._lengthOfBoard):
			myBoard[0][y] = 'X'
			myBoard[self._breadthOfBoard-1][y]= 'X'
		
		# #Vertical Border
		for x in xrange(0,self._breadthOfBoard):
			myBoard[x][0] = 'X'
			myBoard[x][self._lengthOfBoard-1] = 'X'
#-----------------------------------------------------------------------------------------------------------	
#------------------------random coin generator------------------------------------------------

      
        def coins(self, myBoard):
		j=0
		l1=[8,12,16,20,24,28]
		l2=[8+j,15+j,16+j,23+j,34+j,45+j,50+j]
		l3=[80-j,72-j,65-j,64-j,53-j,41]
		#self.numberOfCoins=random.randint(20,30)
		for i in l1:
			if j%2==0:
				for k in l2:
					myBoard[i][k+j]='C'
			else:
				for k in l3:
					myBoard[i][k-j]='C'
			j=j+1
				
#----------------------------------FLOOR GENERATOR-------------------------------
	def floor(self, myBoard):
		count=0
                for i in xrange(1,4):
			myBoard[i][10] = 'X'
		for i in xrange(1,4):
			myBoard[i][34] = 'X'
		for y in xrange(10,35):
			myBoard[4][y] = 'X'
		for x in xrange(self._breadthOfBoard-1,0,-4):
			if count==6:
				break
			floorLength = 65
			if count%2==1:
				for y in xrange(1,floorLength):
					myBoard[x][y] = 'X'
	
			else:
				for y in xrange(self._lengthOfBoard-2,self._lengthOfBoard-floorLength-1,-1):
					myBoard[x][y] = 'X'
	
			count+=1
#-----------------------------------HARDCODED STAIRS-----------------------------------------------------------		
        def stairs1(self,myBoard):
                myBoard[28][20]='H'
                myBoard[27][20]='H'
                myBoard[26][20]='H'
                myBoard[25][20]='H'
                myBoard[24][35]='H'
                myBoard[23][35]='H'
                myBoard[22][35]='H'
                myBoard[21][35]='H'
		myBoard[20][48]='H'
		myBoard[19][48]='H'
		myBoard[18][48]='H'
		myBoard[17][48]='H'
		myBoard[16][25]='H'
		myBoard[15][25]='H'
		myBoard[14][25]='H'
		myBoard[13][25]='H'
		myBoard[12][55]='H'
		myBoard[11][55]='H'
		myBoard[10][55]='H'
               	myBoard[9][55]='H'
		myBoard[8][31]='H'
		myBoard[7][31]='H'
		myBoard[6][31]='H'
		myBoard[5][31]='H'
		myBoard[4][31]='H'
               
	def __boardInitialize(self, myBoard):
		myBoard = [' '] * self._breadthOfBoard
		for i in xrange(self._breadthOfBoard):
			myBoard[i] = [' '] * self._lengthOfBoard 
		      
		return myBoard
	def displayScore(self):
		pass
#---------------------------------ACCESING OTHER FILES AND THEIR FUNCTIONS----------------------------
nameOfPlayer = raw_input("Please enter your name :-\n")
GameObject = person()
GamePlayer = Player(nameOfPlayer)
lengthOfBoard = 80
breadthOfBoard = 30
myBoard = []
GameSetup = gameDisplaySetup(myBoard, lengthOfBoard, breadthOfBoard)
myBoard = GameSetup.myBoard
myBoard[3][18]='q'
getch = _Getch()
playerPosition = my.attrDict(x=breadthOfBoard-2,y=2)
myBoard[playerPosition.x][playerPosition.y] = 'P'
myBoard[8][3]='D'
myBoard[8][4]='O'
my.printMyBoard(myBoard)

controllerObject = controller.Controller()

#------------------------------------------VARIABLES INITIALISATION------------------------------------------------------------------

flag=0
f=0
var=1
vary=2
varx=8
flag22=0
life=5
flagd=-1
oldf=0
oldf1=0
key=None
oldf11=0
oldf12=0
var11=0
var12=0
f11=0
f12=0
j=0  
varb=8
oldf11=0
oldf111=0
ct =0
#------------------------------------------------VARIABLE INITIALISATION ENDS---------------------------------------------------------

#----------------------------------------------------------------------MAIN LOOP STARTS-----------------------------------------------------------

while key!='Q':
	
	#if ct%10==0:
	#	myBoard[8][var+1]='O'
	
	ct=ct+1
	my.clearScreen()
	my.printMyBoard(myBoard)
	
	print("Your Lives left are : ",life)	
	print("Your Score is : ",GameObject.score)	
		
	if flag22>0:
		time.sleep(0.04)
	
	if flag22==0:	
		key = GamePlayer._takeInput()
	
	
	if playerPosition.x==3 and playerPosition.y == 18:
		print ("You Won  ",nameOfPlayer)
		print("Final score is : ",GameObject.score+20)
		break 
	elif myBoard[playerPosition.x][playerPosition.y] == 'q':
		print ("You Won")
		break		
	elif flag==1:
		myBoard[playerPosition.x][playerPosition.y] = 'H'
		flag=0
	elif myBoard[playerPosition.x][playerPosition.y] !='H':
		myBoard[playerPosition.x][playerPosition.y] = ' '
	
	if flag22==0:	
		key=key.upper()
	if var<=62 and f==0:
                
		if oldf==1:
			myBoard[8][var]=ch1
			oldf=0
		else:

			myBoard[8][var]=' '
		if oldf==0:
			ch1=myBoard[8][var+1]
		if ch1=='C' or ch1=='H':
			oldf=1
		
        	myBoard[8][var+1]='D'
		
		var=var+1
        else:
		if oldf1==1:
			myBoard[8][var]=ch2
			oldf1=0
		else:

			myBoard[8][var]=' '
		if oldf1==0:
			ch2=myBoard[8][var-1]
		if ch2=='C' or ch2=='H':
			oldf1=1
		f=1
		myBoard[8][var-1]='D'
		
		var=var-1
		

			
		
#-----------------------------Fire Ball-------------------------------------		

	if var11<79 and f11==0:
                #print('if')
		#time.sleep(1)	
		#if oldf11==1:
		#	myBoard[varb][var11]=ch111
		#	oldf11=0
		#else:
 
		if oldf11==1:
			myBoard[varb][var11]=ch111
			oldf11=0
		else:

			myBoard[varb][var11]=' '
		if oldf11==0:
			ch111=myBoard[varb][var11+1]
		if ch111=='C' or ch111=='H':
			oldf11=1
		
        	myBoard[varb][var11+1]='O'

	#	if varb<30 and var11+1<78:
		#	myBoard[varb][var11]=' '
		#if oldf==0:
		#	ch111=myBoard[8][var11+1]
		#if ch1=='C' or ch1=='H':
		#	oldf11=1
		
        	myBoard[varb][var11+1]='O'
		
		var11=var11+1
		if varb<30 and var11<79:
			if myBoard[varb+1][var11]==' ':
				#myBoard[varb+4][var]
				#print (varb,var11)
				myBoard[varb][var11]=' '					
				varb=varb+4
        else:
		#if oldf12==1:
		#	myBoard[8][var11]=ch21
		#	oldf1=0
		#else:
		f11=1
		if var11>=79:
			var11=78
#		print ('esle')
#		print (varb,var11)
		#time.sleep(1)		
		if oldf111==1:
			myBoard[varb][var11]=ch22
			oldf111=0
		else:

			myBoard[varb][var11]=' '
		if oldf111==0:
			ch22=myBoard[varb][var11-1]
		if ch22=='C' or ch22=='H':
			oldf111=1
		f=1
		myBoard[varb][var11-1]='O'
		
        	#myBoard[varb][var11-1]='O'



	       	#if varb<30 and var11-1>1:
	        #	myBoard[varb][var11]=' '
		#if oldf12==0:
		#	ch21=myBoard[8][var11-1]
		#if ch2=='C' or ch2=='H':
		#	oldf12=1
		#f11=1
		myBoard[varb][var11-1]='O'
		var11=var11-1
		if var11==1:
			f11=0
		if varb<30 and var11<78:
			if myBoard[varb+1][var11]==' ':
				#myBoard[varb+4][var]
				#print (varb,var11)					
				myBoard[varb][var11]=' '				
				varb=varb+4
		

#--------------------------------------------------------------	DONKEY AND PLAYER---------------------------------------------
	

	

	if (playerPosition.x==8 and playerPosition.y==var) or(playerPosition.x==8 and playerPosition.y+1==var )or (playerPosition.x==8 and playerPosition.y-1==var):
		life=life-1;
		myBoard[28][2]='P'		
		print ("OOP's You Find The Donkey")
		GameObject.score=GameObject.score-5
		time.sleep(1)
		playerPosition = my.attrDict(x=breadthOfBoard-2,y=2)
		myBoard[playerPosition.x][playerPosition.y] = 'P'
		j=j^1
		l1=[8,12,16,20,24,28]
		l2=[8+j,15+j,16+j,23+j,34+j]
		l3=[80-j,72-j,65-j,41]
		
		for i in l1:
			if j%2==0:
				for k in l2:
					if i<30 and k+j<80:	
						myBoard[i][k+j]='C'
			else:
				for k in l3:
					if i<30 and k+j<80:	
						myBoard[i][k-j]='C'
			j=j+1

			

#--------------------------------------fireball meeting player--------------------

	if (playerPosition.x==varb and playerPosition.y==var11) or(playerPosition.x==varb and playerPosition.y+1==var11 )or (playerPosition.x==varb and playerPosition.y-1==var11):
		life=life-1;
		myBoard[28][2]='P'		
		print ("OOP's You Find The Fireball")
		GameObject.score=GameObject.score-5
		time.sleep(1)
		playerPosition = my.attrDict(x=breadthOfBoard-2,y=2)
		myBoard[playerPosition.x][playerPosition.y] = 'P'	
#---------------------------------ending of fireball---------------------------------
	

#----------------------------------------------------------------------------------------
		#def coins(self, myBoard):
		j=j^1
		l1=[8,12,16,20,24,28]
		l2=[8+j,15+j,16+j,23+j,34+j]
		l3=[80-j,72-j,65-j,41]
		#self.numberOfCoins=random.randint(20,30)
		for i in l1:
			if j%2==0:
				for k in l2:
					if i<30 and k+j<80:	
						myBoard[i][k+j]='C'
			else:
				for k in l3:
					if i<30 and k+j<80:	
						myBoard[i][k-j]='C'
			j=j+1


#-------------------------------------------------------------------------------------------	
		myBoard[24][41]='C'
                myBoard[24][38]='C'
		myBoard[24][15]='C'
		myBoard[24][12]='C'
		myBoard[24][9]='C'
		myBoard[24][30]='C'
		myBoard[24][33]='C'
		myBoard[24][36]='C'
		myBoard[16][10]='C'
		myBoard[16][12]='C'
		myBoard[16][15]='C'    
		myBoard[16][40]='C'	      
		myBoard[16][44]='C'	      
		myBoard[16][47]='C'	      
		myBoard[16][50]='C'	      
		myBoard[12][40]='C'
		myBoard[12][70]='C'
		myBoard[12][68]='C'       
		myBoard[12][67]='C'       
		myBoard[8][25]='C'
		myBoard[8][28]='C'
		myBoard[8][32]='C'
		myBoard[8][34]='C' 
			
	if life==0:
		print ("You Lose...Game Over")
		break
        
	if var<=1:
                f=0
		
		
#-------------------------FLAGD HOLDS THE DIRECTION FOR THE PREVIOUS INPUT----------------------------------------		
	if key=='A':
        	flagd=0
	elif key=='D':
		flagd=1
		
#------------------------------------------------FOR HANDLING JUMP INSTRUCTIONS----------------------------------------------------	

#-----------------------------------------JUMP RESTRICTIONS-------------------------------------------------	

	if key=='J':
		if playerPosition.x==24 or playerPosition.x==28 or playerPosition.x==20 or playerPosition.x==16 or playerPosition.x==12 or playerPosition.x==8 or playerPosition.x==3: 
			if playerPosition.y+4>79:
				if flagd==0:	
					if playerPosition.x+1<30 and playerPosition.y+4<79:	
						if (myBoard[playerPosition.x+1][playerPosition.y+4]=='X' or myBoard[playerPosition.x+1][playerPosition.y+4]=='H') and flagd==1 :
								flag22=4
						elif (myBoard[playerPosition.x+1][playerPosition.y-4]=='X' or myBoard[playerPosition.x+1][playerPosition.y-4]=='H') and flagd==0:
							flag22=4
	
						else:
							pass							
					
					else:
						pass
			elif playerPosition.y-4<0:			
 			    	if flagd==1:
					if myBoard[playerPosition.x+1][playerPosition.y+4]=='X':
						flag22=4
					elif myBoard[playerPosition.x+1][playerPosition.y-4]=='X':
						flag22=4
	
					else:
						pass
					
				else:
					pass
			else:
				if playerPosition.x+1<30 and playerPosition.y+4<79:
  					if myBoard[playerPosition.x+1][playerPosition.y+4]=='X'and flagd==1:
						flag22=4
				if playerPosition.x+1<30 and playerPosition.y-4>0:
					if myBoard[playerPosition.x+1][playerPosition.y-4]=='X' and flagd==0:
						flag22=4		
				else:
					pass	
#-------------------------------------------------------------------------------------------------------------------------	
#---------------------------INSTRUCTING FOR THE RIGHT JUMP-----------------------------------------------------------------		
	if flagd==1:
		if flag22==4:
			key='X'
			flag22=3	
			try:
				playerPosition = getattr(controllerObject,'move' + key)(myBoard,playerPosition,GameSetup,GameObject)
				GamePlayer._scoreChanger(GameObject.score)
			except  Exception, e:
				
				pass
        
			
		elif flag22==3:
			key='Y'
			flag22=2	
			try:
				playerPosition = getattr(controllerObject,'move' + key)(myBoard,playerPosition,GameSetup,GameObject)
				GamePlayer._scoreChanger(GameObject.score)
			except  Exception, e:
				
				pass
        
		elif flag22==2:
			key='T'
			flag22=1	
			try:
				playerPosition = getattr(controllerObject,'move' + key)(myBoard,playerPosition,GameSetup,GameObject)
				GamePlayer._scoreChanger(GameObject.score)
			except  Exception, e:
				
				pass
		
		elif flag22==1:
			key='P'
			flag22=0	
			try:
				playerPosition = getattr(controllerObject,'move' + key)(myBoard,playerPosition,GameSetup,GameObject)
				GamePlayer._scoreChanger(GameObject.score)
			except  Exception, e:
				
				pass
		else:
			try:
				playerPosition = getattr(controllerObject,'move' + key)(myBoard,playerPosition,GameSetup,GameObject)
				GamePlayer._scoreChanger(GameObject.score)
			except  Exception, e:
				
				pass	

#---------------------------------------INSTRUCTION SET FOR THE LEFT JUMP---------------------------------------------------------------------------
	if flagd==0:
		if flag22==4:
			key='M'
			flag22=3	
			try:
				playerPosition = getattr(controllerObject,'move' + key)(myBoard,playerPosition,GameSetup,GameObject)
				GamePlayer._scoreChanger(GameObject.score)
			except  Exception, e:
				
				pass
        
			
		elif flag22==3:
			key='N'
			flag22=2	
			try:
				playerPosition = getattr(controllerObject,'move' + key)(myBoard,playerPosition,GameSetup,GameObject)
				GamePlayer._scoreChanger(GameObject.score)
			except  Exception, e:
				
				pass
        
		elif flag22==2:
			key='B'
			flag22=1	
			try:
				playerPosition = getattr(controllerObject,'move' + key)(myBoard,playerPosition,GameSetup,GameObject)
				GamePlayer._scoreChanger(GameObject.score)
			except  Exception, e:
				
				pass
		
		elif flag22==1:
			key='V'
			flag22=0	
			try:
				playerPosition = getattr(controllerObject,'move' + key)(myBoard,playerPosition,GameSetup,GameObject)
				GamePlayer._scoreChanger(GameObject.score)
			except  Exception, e:
				
				pass
		else:
			try:
				playerPosition = getattr(controllerObject,'move' + key)(myBoard,playerPosition,GameSetup,GameObject)
				GamePlayer._scoreChanger(GameObject.score)
			except  Exception, e:
				
				pass		
#-----------------------------------------------------JUMP CONDITION ENDS----------------------------------------------------------------------------	

	if playerPosition.x<=29 and playerPosition.y<=79:	
		if myBoard[playerPosition.x][playerPosition.y] == 'H':
			flag=1
	GamePlayer._positionChanger(myBoard,playerPosition)



#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------CODE FOR MULTIPLE FIREBALLS THOUGH NOT WORKING---------------------------------


'''

---------------------------Fire Ball-------------------------------------		
	for i in range(1,ctb+1):
	
		if var11[i]<79 and f11[i]==0:
 			if myBoard[varb[i]][var11[i]+1]!=' ':
				pass
			else:
				myBoard[varb[i]][var11[i]+1]='O'
			myBoard[varb[i]][var11[i]]=' '
			
			
			var11[i]=var11[i]+1
			if varb[i]<30 and var11[i]<80:
				if myBoard[varb[i]+1][var11[i]]==' ':
					#myBoard[varb+4][var]
					print (varb[i],var11[i])
					myBoard[varb[i]][var11[i]]=' '					
					varb[i]=varb[i]+4
        	else:
			#if prevf12==1:
			#	myBoard[8][var11]=ch21
			#	prevf1=0
			#else:
			#f11[i]=1
			if var11[i]>=79:
				var11[i]=78
					
			if prevf111[i]==1:
				myBoard[varb[i]][var11[i]]=ch22[i]
				prevf111[i]=0
			else:
	
				myBoard[varb[i]][var11[i]]=' '
			if prevf111[i]==0:
				if varb[i]<30 and var11[i]<80:
					ch22[i]=myBoard[varb[i]][var11[i]-1]
			if ch22[i]=='C' or ch22[i]=='H':
				prevf111[i]=1
			if varb[i]<30 and var11[i]-1<78:				
				myBoard[varb[i]][var11[i]-1]='O'
			f11[i]=1
        		#myBoard[varb][var11-1]='O'
	
	
	
		       	#if varb<30 and var11-1>1:
		        #	myBoard[varb][var11]=' '
			#if prevf12==0:
			#	ch21=myBoard[8][var11-1]
			#if ch2=='C' or ch2=='H':
			#	prevf12=1
			#f11=1
			#yBoard[varb[i]][var11[i]-1]='O'
			var11[i]=var11[i]-1
			#if var11[i]==1:
			#	f11[i]=0
			if varb[i]<30 and var11[i]<78:
				if myBoard[varb[i]+1][var11[i]]==' ':
					#myBoard[varb+4][var]
					print (varb[i],var11[i])					
					myBoard[varb[i]][var11[i]]=' '				
					varb[i]=varb[i]+4
'''
#--------------------------------------------------------------GAME ENDS------------------------------------------------------
		
