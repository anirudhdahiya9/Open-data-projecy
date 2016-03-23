#!/usr/bin/python
import os
class Controller:

	def __init__(self):
		self._levelComplete = False
		self._allCoinsCollected = False
	
	def CoinCollector(self, myBoard, playerPosition, GameSetup, GameObject):
		if myBoard[playerPosition.x][playerPosition.y] == 'C':
			GameObject.score = GameObject.score + 5;
			#self.playSound()
			print(GameObject.score , "Score is this")
		if GameObject.score == GameSetup.numberOfCoins and not self._allCoinsCollected:
		#	self.playBonusSound()
			self._allCoinsCollected = True
		return 
#-------------------------------------VARIOUS KEYS AND THEIR FUNCTIONS--------------------------------------------------------	

#----------------------------------------KEY FOR MOVING LEFT---------------------------------------------------------

	def moveA(self, myBoard, playerPosition, GameSetup, GameObject):
	        futurePoint = myBoard[playerPosition.x][playerPosition.y-1]
		BottomPoint = myBoard[playerPosition.x+1][playerPosition.y-1]
		if futurePoint == 'X':
			return playerPosition
		if BottomPoint != 'X' :
			if BottomPoint =='H':
				playerPosition.y-=1
				self.CoinCollector(myBoard, playerPosition, GameSetup, GameObject)   		
			return playerPosition
		#elif BottomPoint != 'H' :
		#		return playerPosition	
		else:
			playerPosition.y-=1
			self.CoinCollector(myBoard, playerPosition, GameSetup, GameObject)
		return playerPosition

#---------------------------KEY FOR MOVING RIGHT-------------------------------------------

	def moveD(self, myBoard, playerPosition, GameSetup, GameObject):
		#Y will increase
		futurePoint = myBoard[playerPosition.x][playerPosition.y+1]
		BottomPoint = myBoard[playerPosition.x+1][playerPosition.y+1]
		if futurePoint == 'X':
			return playerPosition
		if BottomPoint != 'X' :
			if BottomPoint =='H':
				playerPosition.y+=1
				self.CoinCollector(myBoard, playerPosition, GameSetup, GameObject)
			return playerPosition
		else:
			playerPosition.y+=1			
			self.CoinCollector(myBoard, playerPosition, GameSetup, GameObject)
		return playerPosition

#-------------------------------------KEY FOR MOVING UP------------------------------------------------
	def moveW(self, myBoard, playerPosition, GameSetup, GameObject):
		#X will decrease
		futurePoint = myBoard[playerPosition.x-1][playerPosition.y]
		futurePoint1 = myBoard[playerPosition.x][playerPosition.y]
		if futurePoint != 'H':
			if futurePoint1 =='H' and ( futurePoint==' ' or futurePoint=='C' ) :
				playerPosition.x-=1
				self.CoinCollector(myBoard, playerPosition, GameSetup, GameObject)
			return playerPosition
		else:
			playerPosition.x-=1
			self.CoinCollector(myBoard, playerPosition, GameSetup, GameObject)
		return playerPosition
#--------------------------------------------------SUBSTITUTE KEYS MADE TO EXECUTE JUMP FUNCTIONS-----------------------------------------

#--------------------------------------------FOR RIGHT DIRECTION JUMP-----------------------------------------------------------

        def moveX(self,myBoard,playerPosition,GameSetup,GameObject):	
		playerPosition.x=playerPosition.x-1
		playerPosition.y=playerPosition.y+1
                return playerPosition
	def moveY(self,myBoard,playerPosition,GameSetup,GameObject):	
		playerPosition.x=playerPosition.x-1
		playerPosition.y=playerPosition.y+1	
                return playerPosition
	def moveT(self,myBoard,playerPosition,GameSetup,GameObject):	
		playerPosition.x=playerPosition.x+1
		playerPosition.y=playerPosition.y+1

                return playerPosition
	def moveP(self,myBoard,playerPosition,GameSetup,GameObject):
	
		playerPosition.x=playerPosition.x+1
		playerPosition.y=playerPosition.y+1
                return playerPosition
        def moveJ(self,myBoard,playerPosition,GameSetup,GameObject):
		playerPosition=moveX(myBoard,playerPosition,GameSetup,GameObject)
		#time.sleep(.1)
		playerPosition=moveY(myBoard,playerPosition,GameSetup,GameObject)
		#time.sleep(.1)
		playerPosition=moveT(myBoard,playerPosition,GameSetup,GameObject)
		
		
		playerPosition=moveP(myBoard,playerPosition,GameSetup,GameObject)
			
		
		return playerPosition
#-----------------------------------------------------------------------FOR LEFT DIRECTION OF JUMP------------------------------

        def moveM(self,myBoard,playerPosition,GameSetup,GameObject):	
		playerPosition.x=playerPosition.x-1
		playerPosition.y=playerPosition.y-1
                return playerPosition
	def moveN(self,myBoard,playerPosition,GameSetup,GameObject):	
		playerPosition.x=playerPosition.x-1
		playerPosition.y=playerPosition.y-1	
                return playerPosition
	def moveB(self,myBoard,playerPosition,GameSetup,GameObject):	
		playerPosition.x=playerPosition.x+1
		playerPosition.y=playerPosition.y-1

                return playerPosition
	def moveV(self,myBoard,playerPosition,GameSetup,GameObject):
	
		playerPosition.x=playerPosition.x+1
		playerPosition.y=playerPosition.y-1
                return playerPosition
        def moveJ(self,myBoard,playerPosition,GameSetup,GameObject):
		playerPosition=moveM(myBoard,playerPosition,GameSetup,GameObject)
		#time.sleep(.1)
		playerPosition=moveN(myBoard,playerPosition,GameSetup,GameObject)
		#time.sleep(.1)
		playerPosition=moveB(myBoard,playerPosition,GameSetup,GameObject)		
		
		playerPosition=moveV(myBoard,playerPosition,GameSetup,GameObject)
			
		
		return playerPosition

#--------------------------------------KEY FOR FOR MOVING DOWN------------------------------------------------------------------------


	def moveS(self, myBoard, playerPosition, GameSetup, GameObject):
		#X will increase
		futurePoint =  myBoard[playerPosition.x+1][playerPosition.y]
		if futurePoint == 'X':
			return playerPosition
		else:
			playerPosition.x+=1
			self.CoinCollector(myBoard, playerPosition, GameSetup, GameObject)
		return playerPosition
