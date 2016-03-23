from board import *
import sys
from random import *
class Person():

	def __init__(self):
		self.updatedposition=(0,0)

	def move(self,b):
		pass
	

	def update_updatedposition(self,b,inp):
		pass

	def checkWall(self,b):
		if b.getvalueatboard(self.updatedposition)=='X':
			return True
		else:
			return False

	def checkCoin(self,b):
		if b.getvalueatboard(self.updatedposition)=='C':			
			return True
		else:
			return False

	def checkPl(self,b):
		if b.getvalueatboard(self.updatedposition)=='P':
			return True
		else:
			return False

	def checkDonkey(self,b):
		if b.getvalueatboard(self.updatedposition)=='D':
			return True
		else:
			return False
	def checkQueen(self,b):
		if b.getvalueatboard(self.updatedposition)=='Q':
			return True
		else:
			return False
	def checkAir(self,b):
		if b.getvalueatboard(self.updatedposition)=='.':
			return True
		else:
			return False
	def checkStair(self,b):
		if b.getvalueatboard(self.updatedposition)=='H':
			return True
		else:
			return False
	def checkFireball(self,b):
		if b.getvalueatboard(self.updatedposition)=='O':
			return True
		else:
			return False
	def checkAirFireball(self,b):
		if b.getvalueatboard(self.updatedposition)=='.':
			return True
		else:
			return False

class Pl(Person):
	
	def __init__(self,b,cnt):
		self.__score=cnt
		self.__position=(25,3)
		self.__reloadcount=0
		self.__curr ='c'
		b.setvalueatboard((25,3),'P')
		
	def getScore(self):
		return self.__score

	def incrementScore(self):
		self.__score+=5
	
	def getPlPosition(self):
		return self.__position
	
	def update_updatedposition(self,b,inp):
		if inp=='w':
			self.updatedposition = ((self.__position[0]-1)%b.getrow(),self.__position[1]%b.getcol())
		
		elif inp=='a':
			self.updatedposition = (self.__position[0]%b.getrow(),(self.__position[1]-1)%b.getcol())
	
		elif inp=='s':
			self.updatedposition = ((self.__position[0]+1)%b.getrow(),self.__position[1]%b.getcol())
	
		elif inp=='d':
			self.updatedposition = (self.__position[0]%b.getrow(),(self.__position[1]+1)%b.getcol())
		else:
			pass
	
	def move(self,b,inp,gamelevel):
		if(inp ==' '):
			jd=getchar()
			if(jd=='d'):
				self.updatedposition = ((self.__position[0])%b.getrow(),(self.__position[1]+4)%b.getcol())
				if ((b.getvalueatboard(self.updatedposition)=='_' or b.getvalueatboard(self.updatedposition)=='C'or b.getvalueatboard(self.updatedposition)=='H' or b.getvalueatboard(self.updatedposition)=='D' or b.getvalueatboard(self.updatedposition)=='O') and self.__position[1]<=35):	   	   	        
					self.updatedposition = ((self.__position[0]-1)%b.getrow(),(self.__position[1]+1)%b.getcol())	
			      		if b.getvalueatboard(self.updatedposition)=='.':
						b.setvalueatboard(self.__position,'_')
						b.setvalueatboard(self.updatedposition,'P')
						self.__position = self.updatedposition	
						b.printlist()
						time.sleep(0.2)
					elif b.getvalueatboard(self.updatedposition)=='H':
						b.setvalueatboard(self.__position,'_')
						b.setvalueatboard(self.updatedposition,'P/H')
						self.__position = self.updatedposition	
						b.printlist()
						time.sleep(0.2)

					self.updatedposition = ((self.__position[0]-1)%b.getrow(),(self.__position[1]+1)%b.getcol())
					if b.getvalueatboard(self.updatedposition)=='.':
						if b.getvalueatboard(self.__position)=='P/H':
							b.setvalueatboard(self.__position,'H')
							b.setvalueatboard(self.updatedposition,'P')
							self.__position = self.updatedposition	
							b.printlist()
							time.sleep(0.2)
						else:	
							b.setvalueatboard(self.__position,'.')
							b.setvalueatboard(self.updatedposition,'P')
							self.__position = self.updatedposition	
							b.printlist()
							time.sleep(0.2)
					elif b.getvalueatboard(self.updatedposition)=='P/H':						
						b.setvalueatboard(self.__position,'.')
						b.setvalueatboard(self.updatedposition,'P/H')
						self.__position = self.updatedposition	
						b.printlist()
						time.sleep(0.2)
					elif b.getvalueatboard(self.updatedposition)=='H':
						b.setvalueatboard(self.__position,'.')
						b.setvalueatboard(self.updatedposition,'P/H')
						self.__position = self.updatedposition	
						b.printlist()
						time.sleep(0.2)
					
					self.updatedposition = ((self.__position[0]+1)%b.getrow(),(self.__position[1]+1)%b.getcol())
					if b.getvalueatboard(self.updatedposition)=='.':
						if b.getvalueatboard(self.__position)=='P/H':
							b.setvalueatboard(self.__position,'H')
							b.setvalueatboard(self.updatedposition,'P')
							self.__position = self.updatedposition	
							b.printlist()
							time.sleep(0.2)
						else:	
							b.setvalueatboard(self.__position,'.')
							b.setvalueatboard(self.updatedposition,'P')
							self.__position = self.updatedposition	
							b.printlist()
							time.sleep(0.2)

					elif b.getvalueatboard(self.updatedposition)=='P/H':
						b.setvalueatboard(self.__position,'.')
						b.setvalueatboard(self.updatedposition,'P/H')
						self.__position = self.updatedposition	
						b.printlist()
						time.sleep(0.2)
					elif b.getvalueatboard(self.updatedposition)=='H':
						b.setvalueatboard(self.__position,'.')
						b.setvalueatboard(self.updatedposition,'P/H')
						self.__position = self.updatedposition	
						b.printlist()
						time.sleep(0.2)
					self.updatedposition = ((self.__position[0]+1)%b.getrow(),(self.__position[1]+1)%b.getcol())
					if(b.getvalueatboard(self.updatedposition)=='H'):
						b.setvalueatboard(self.__position,'.')
						b.setvalueatboard(self.updatedposition,'P/H')
						self.__position = self.updatedposition
						b.printlist()	
						time.sleep(0.2)					
					elif self.checkCoin(b)==True:
						self.collectCoin(gamelevel) 			
						b.setvalueatboard(self.__position,'.')
						b.setvalueatboard(self.updatedposition,'P')
						self.__position = self.updatedposition
						b.printlist()	
						time.sleep(0.2)					
					elif self.checkDonkey(b)==True:
						b.setvalueatboard(self.__position,'.')			
						b.setvalueatboard(self.updatedposition,'D')	
						self.__position = self.updatedposition
						b.printlist()	
						time.sleep(0.2)						
						return -1
					elif self.checkFireball(b)==True:
						b.setvalueatboard(self.__position,'.')			
						b.setvalueatboard(self.updatedposition,'O')	
						self.__position = self.updatedposition
						b.printlist()	
						time.sleep(0.2)						
						return -1
					elif b.getvalueatboard(self.__position)=='P/H':
						b.setvalueatboard(self.__position,'H')
						b.setvalueatboard(self.updatedposition,'P')
						self.__position = self.updatedposition
						b.printlist()	
						time.sleep(0.2)						
						
					else:						
						b.setvalueatboard(self.__position,'.')
						b.setvalueatboard(self.updatedposition,'P')
						self.__position = self.updatedposition	
						b.printlist()	
						time.sleep(0.2)
				else:
					pass
			elif(jd=='a'):
				self.updatedposition = ((self.__position[0])%b.getrow(),(self.__position[1]-4)%b.getcol()) 
				if (b.getvalueatboard(self.updatedposition)=='_' or b.getvalueatboard(self.updatedposition)=='C' or b.getvalueatboard(self.updatedposition)=='H' or b.getvalueatboard(self.updatedposition)=='D' or b.getvalueatboard(self.updatedposition)=='O') and self.__position[1]>=5:
					self.updatedposition = ((self.__position[0]-1)%b.getrow(),(self.__position[1]-1)%b.getcol())	
					if b.getvalueatboard(self.updatedposition)=='.':
						b.setvalueatboard(self.__position,'_')
						b.setvalueatboard(self.updatedposition,'P')
						self.__position = self.updatedposition	
						b.printlist()
						time.sleep(0.2)
					elif b.getvalueatboard(self.updatedposition)=='H':
						b.setvalueatboard(self.__position,'_')
						b.setvalueatboard(self.updatedposition,'P/H')
						self.__position = self.updatedposition	
						b.printlist()
						time.sleep(0.2)
					self.updatedposition = ((self.__position[0]-1)%b.getrow(),(self.__position[1]-1)%b.getcol())
					if b.getvalueatboard(self.updatedposition)=='.':
						if b.getvalueatboard(self.__position)=='P/H':
							b.setvalueatboard(self.__position,'H')
							b.setvalueatboard(self.updatedposition,'P')
							self.__position = self.updatedposition	
							b.printlist()
							time.sleep(0.2)
						else:	
							b.setvalueatboard(self.__position,'.')
							b.setvalueatboard(self.updatedposition,'P')
							self.__position = self.updatedposition	
							b.printlist()
							time.sleep(0.2)

					elif b.getvalueatboard(self.updatedposition)=='P/H':
						b.setvalueatboard(self.__position,'H')
						b.setvalueatboard(self.updatedposition,'P')
						self.__position = self.updatedposition	
						b.printlist()
						time.sleep(0.2)
					elif b.getvalueatboard(self.updatedposition)=='H':
						b.setvalueatboard(self.__position,'.')
						b.setvalueatboard(self.updatedposition,'P/H')
						self.__position = self.updatedposition	
						b.printlist()
						time.sleep(0.2)
					
			      		self.updatedposition = ((self.__position[0]+1)%b.getrow(),(self.__position[1]-1)%b.getcol())
					if b.getvalueatboard(self.updatedposition)=='.':
						if b.getvalueatboard(self.__position)=='P/H':
							b.setvalueatboard(self.__position,'H')
							b.setvalueatboard(self.updatedposition,'P')
							self.__position = self.updatedposition	
							b.printlist()
							time.sleep(0.2)
						else:	
							b.setvalueatboard(self.__position,'.')
							b.setvalueatboard(self.updatedposition,'P')
							self.__position = self.updatedposition	
							b.printlist()
							time.sleep(0.2)


					elif b.getvalueatboard(self.updatedposition)=='P/H':
						b.setvalueatboard(self.__position,'H')
						b.setvalueatboard(self.updatedposition,'P')
						self.__position = self.updatedposition	
						b.printlist()
						time.sleep(0.2)
					elif b.getvalueatboard(self.updatedposition)=='H':
						b.setvalueatboard(self.__position,'.')
						b.setvalueatboard(self.updatedposition,'P/H')
						self.__position = self.updatedposition	
						b.printlist()
						time.sleep(0.2)
					
					self.updatedposition = ((self.__position[0]+1)%b.getrow(),(self.__position[1]-1)%b.getcol())
					if(b.getvalueatboard(self.updatedposition)=='H'):
						b.setvalueatboard(self.__position,'.')
						b.setvalueatboard(self.updatedposition,'P/H')
						self.__position = self.updatedposition
						b.printlist()	
						time.sleep(0.2)					
					elif self.checkCoin(b)==True:
						self.collectCoin(gamelevel) 			
						b.setvalueatboard(self.__position,'.')
						b.setvalueatboard(self.updatedposition,'P')
						self.__position = self.updatedposition
						b.printlist()	
						time.sleep(0.2)					
					elif self.checkDonkey(b)==True:
						b.setvalueatboard(self.__position,'.')			
						b.setvalueatboard(self.updatedposition,'D')	
						self.__position = self.updatedposition
						b.printlist()	
						time.sleep(0.2)						
						return -1
					elif self.checkFireball(b)==True:
						b.setvalueatboard(self.__position,'.')			
						b.setvalueatboard(self.updatedposition,'O')	
						self.__position = self.updatedposition
						b.printlist()	
						time.sleep(0.2)						
						return -1
					elif b.getvalueatboard(self.__position)=='P/H':
						b.setvalueatboard(self.__position,'H')
						b.setvalueatboard(self.updatedposition,'P')
						self.__position = self.updatedposition
						b.printlist()	
						time.sleep(0.2)						
					
					else:						
						b.setvalueatboard(self.__position,'.')
						b.setvalueatboard(self.updatedposition,'P')
						self.__position = self.updatedposition	
						b.printlist()	
						time.sleep(0.2)
				else:
					pass
		else:		
			self.update_updatedposition(b,inp)
			if self.checkDonkey(b)==True:
				b.setvalueatboard(self.__position,'_')			
				prev=b.getvalueatboard(self.updatedposition)
				b.setvalueatboard(self.updatedposition,'D')	
				self.__position = self.updatedposition
				return -1
			if self.checkFireball(b)==True:
				b.setvalueatboard(self.__position,'_')			
				prev=b.getvalueatboard(self.updatedposition)
				b.setvalueatboard(self.updatedposition,'O')	
				self.__position = self.updatedposition			
				return -1	
				
			elif self.checkWall(b)==True:
				pass
			elif self.checkCoin(b)==True and b.getvalueatboard(self.__position)=='P/H':
				self.collectCoin(gamelevel) 			
				b.setvalueatboard(self.__position,'H')		
				b.setvalueatboard(self.updatedposition,'P')
				self.__position = self.updatedposition	
			elif self.checkCoin(b)==True:
				self.collectCoin(gamelevel) 			
				b.setvalueatboard(self.__position,'_')			
				b.setvalueatboard(self.updatedposition,'P')
				self.__position = self.updatedposition
				#if h==-1:
				#	return 2
			elif self.checkStair(b)==True and b.getvalueatboard(self.__position)!='P/H':
				b.setvalueatboard(self.__position,'_')
				b.setvalueatboard(self.updatedposition,'P/H')
				self.__position = self.updatedposition
			elif self.checkStair(b)==True and b.getvalueatboard(self.__position)=='P/H':
				b.setvalueatboard(self.__position,'H')
				b.setvalueatboard(self.updatedposition,'P/H')
				self.__position = self.updatedposition
		
			elif self.checkQueen(b)==True:
				b.setvalueatboard(self.__position,'_')
				b.setvalueatboard(self.updatedposition,'W')			
				self.__position = self.updatedposition
				return 2
			elif self.checkAir(b)==True:
				pass
			elif b.getvalueatboard(self.__position)=='P/H':
				b.setvalueatboard(self.__position,'H')
				b.setvalueatboard(self.updatedposition,'P')
				self.__position = self.updatedposition
			else:
				b.setvalueatboard(self.__position,'_')
				b.setvalueatboard(self.updatedposition,'P')
				self.__position = self.updatedposition
		
			
	def collectCoin(self,gamelevel):
		self.incrementScore()
			#self.__reloadcount+=1
	
		#	if self.__reloadcount%(30*(gamelevel))==0:
		#		return -1
	
class Donkey(Person):
	
	def __init__(self,b):
		self.__position = (5,3)
		b.setvalueatboard((5,3),'D')
	
	def getDonkeyPosition(self):
		return self.__position

	def update_updatedposition(self,b):
		mov = randint(1,2)
		if mov==1:
			self.updatedposition = (self.__position[0]%b.getrow(),(self.__position[1]-1)%b.getcol())
		elif mov==2:
			self.updatedposition = (self.__position[0]%b.getrow(),(self.__position[1]+1)%b.getcol())

	def move(self,b):
		self.update_updatedposition(b)
		if self.checkPl(b)==True and b.getvalueatboard(self.__position)!='D/H':
			b.setvalueatboard(self.__position,'H')
			b.setvalueatboard(self.updatedposition,'D')
			self.__position = self.updatedposition
			return -1			
		elif self.checkPl(b)==True:
			b.setvalueatboard(self.__position,'_')
			b.setvalueatboard(self.updatedposition,'D')
			self.__position = self.updatedposition
			return -1			
		elif self.checkWall(b)==True:
			pass
		elif self.checkDonkey(b)==True:
			pass

		elif self.checkStair(b)==True and b.getvalueatboard(self.__position)=='_':
			b.setvalueatboard(self.__position,'_')
			b.setvalueatboard(self.updatedposition,'D/H')
			self.__position = self.updatedposition
		elif self.checkStair(b)==True and b.getvalueatboard(self.__position)=='D/H':
			b.setvalueatboard(self.__position,'H')
			b.setvalueatboard(self.updatedposition,'D/H')
			self.__position = self.updatedposition
		elif self.checkStair(b)==True and b.getvalueatboard(self.__position)=='C/D':
			b.setvalueatboard(self.__position,'C')
			b.setvalueatboard(self.updatedposition,'D/H')
			self.__position = self.updatedposition
		elif self.checkStair(b)==True:
			b.setvalueatboard(self.__position,'_')
			b.setvalueatboard(self.updatedposition,'D/H')
			self.__position = self.updatedposition		
		
		elif self.checkCoin(b)==True and b.getvalueatboard(self.__position)=='D/H':
			b.setvalueatboard(self.__position,'H')
			b.setvalueatboard(self.updatedposition,'C/D')
			self.__position = self.updatedposition
		elif self.checkCoin(b)==True and b.getvalueatboard(self.__position)=='D/H':
			b.setvalueatboard(self.__position,'H')
			b.setvalueatboard(self.updatedposition,'C/D')
			self.__position = self.updatedposition
		elif self.checkCoin(b)==True and b.getvalueatboard(self.__position)=='C/D':
			b.setvalueatboard(self.__position,'C')
			b.setvalueatboard(self.updatedposition,'C/D')
			self.__position = self.updatedposition
		elif self.checkCoin(b)==True and b.getvalueatboard(self.__position)!='C/D':
			b.setvalueatboard(self.__position,'_')
			b.setvalueatboard(self.updatedposition,'C/D')
			self.__position = self.updatedposition
		elif b.getvalueatboard(self.__position)=='D/H':
			b.setvalueatboard(self.__position,'H')
			b.setvalueatboard(self.updatedposition,'D')
			self.__position = self.updatedposition
		elif self.checkAir(b)==True:
			pass		
		else:
			if b.getvalueatboard(self.__position)=='C/D':
				b.setvalueatboard(self.__position,'C')
				b.setvalueatboard(self.updatedposition,'D')
				self.__position = self.updatedposition

			else:
				b.setvalueatboard(self.__position,'_')
				b.setvalueatboard(self.updatedposition,'D')
				self.__position = self.updatedposition

class Fireball(Person):
	def __init__(self,b):
		self.__position = (5,4)
		b.setvalueatboard((5,4),'O')
		self.__prev='d'
	
	def getFireballPosition(self):
		return self.__position
	def getFireballx(self):
		return self.__position[0]

	def update_updatedposition(self,b):
		if(self.__prev=='d'):
			mov=2
		else:
			mov=1
		if mov==1:
			self.updatedposition = (self.__position[0]%b.getrow(),(self.__position[1]-1)%b.getcol())
		elif mov==2:
			self.updatedposition = (self.__position[0]%b.getrow(),(self.__position[1]+1)%b.getcol())
		if self.updatedposition[0]==25 and self.updatedposition[1]==1:						
			if self.checkPl(b)==True:
				b.setvalueatboard(self.__position,'_')
				b.setvalueatboard(self.updatedposition,'O')
				self.__position = (-1,-1)
				return -1
			else:			
				b.setvalueatboard(self.updatedposition,'_')
				b.setvalueatboard(self.__position,'_')
				self.updatedposition = (-1,-1)
				self.__position=self.updatedposition

	def move(self,b):
		self.update_updatedposition(b)
		if self.updatedposition[0]==-1 and self.updatedposition[1]==-1:
			pass
		if(self.updatedposition[0]+1=='H'):
			ab=randint(1,2)
			if(ab==1):
				self.updatedposition = ((self.updatedposition[0]+4)%b.getrow(),self.updatedposition[1]%b.getcol())
		if self.checkPl(b)==True and b.getvalueatboard(self.__position)=='O/H':
			b.setvalueatboard(self.__position,'H')
			b.setvalueatboard(self.updatedposition,'O')
			self.__position = self.updatedposition
			return -1			
		elif self.checkPl(b)==True:
			b.setvalueatboard(self.__position,'_')
			b.setvalueatboard(self.updatedposition,'O')
			self.__position = self.updatedposition
			return -1			
		elif self.checkWall(b)==True:
			if self.__prev=='d':
				self.__prev='a'
			else:
				self.__prev='d'
			self.update_updatedposition(b)		
		elif self.checkDonkey(b)==True:
			pass
		elif self.checkCoin(b)==True and b.getvalueatboard(self.__position)=='O/H':
			b.setvalueatboard(self.__position,'H')
			b.setvalueatboard(self.updatedposition,'C/O')
			self.__position = self.updatedposition
		elif self.checkCoin(b)==True and b.getvalueatboard(self.__position)!='C/O':
			b.setvalueatboard(self.__position,'_')
			b.setvalueatboard(self.updatedposition,'C/O')
			self.__position = self.updatedposition
		elif self.checkStair(b)==True and b.getvalueatboard(self.__position)=='_':
			b.setvalueatboard(self.__position,'_')
			b.setvalueatboard(self.updatedposition,'O/H')
			self.__position = self.updatedposition
		elif self.checkStair(b)==True and b.getvalueatboard(self.__position)=='O/H':
			b.setvalueatboard(self.__position,'H')
			b.setvalueatboard(self.updatedposition,'O/H')
			self.__position = self.updatedposition
		elif self.checkStair(b)==True and b.getvalueatboard(self.__position)=='C/O':
			b.setvalueatboard(self.__position,'C')
			b.setvalueatboard(self.updatedposition,'O/H')
			self.__position = self.updatedposition
		elif self.checkFireball(b)==True:
			b.setvalueatboard(self.__position,'O')
			b.setvalueatboard(self.updatedposition,'O')
			self.__position = self.updatedposition
		elif self.checkStair(b)==True:
			b.setvalueatboard(self.__position,'_')
			b.setvalueatboard(self.updatedposition,'O/H')
			self.__position = self.updatedposition		
		elif self.checkCoin(b)==True and b.getvalueatboard(self.__position)=='O/H':
			b.setvalueatboard(self.__position,'H')
			b.setvalueatboard(self.updatedposition,'C/O')
			self.__position = self.updatedposition
		elif self.checkCoin(b)==True and b.getvalueatboard(self.__position)=='C/O':
			b.setvalueatboard(self.__position,'C')
			b.setvalueatboard(self.updatedposition,'C/O')
			self.__position = self.updatedposition
		elif b.getvalueatboard(self.__position)=='O/H':
			b.setvalueatboard(self.__position,'H')
			b.setvalueatboard(self.updatedposition,'O')
			self.__position = self.updatedposition
		elif self.checkAirFireball(b)==True:			
			if self.__prev=='d':
				self.updatedposition = ((self.__position[0]+4)%b.getrow(),(self.__position[1]+1)%b.getcol())
			else:
				self.updatedposition = ((self.__position[0]+4)%b.getrow(),(self.__position[1]-1)%b.getcol())
			if self.checkCoin(b)==True and b.getvalueatboard(self.__position)=='C/O':
				b.setvalueatboard(self.__position,'C')
				b.setvalueatboard(self.updatedposition,'C/O')
				self.__position = self.updatedposition
			elif self.checkCoin(b)==True:
				b.setvalueatboard(self.__position,'_')
				b.setvalueatboard(self.updatedposition,'C/O')
				self.__position=self.updatedposition
			else:
				b.setvalueatboard(self.__position,'_')
				b.setvalueatboard(self.updatedposition,'O')
				self.__position=self.updatedposition
			dd=randint(1,2)
			if dd==1:
				self.__prev='d'
			else:
				self.__prev='a'
		else:
			if b.getvalueatboard(self.__position)=='C/O':
				b.setvalueatboard(self.__position,'C')
				b.setvalueatboard(self.updatedposition,'O')
				self.__position = self.updatedposition

			else:
				b.setvalueatboard(self.__position,'_')
				b.setvalueatboard(self.updatedposition,'O')
				self.__position = self.updatedposition	


