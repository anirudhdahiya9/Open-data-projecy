from person import *
import time
import os

class Mario(Person):
	""" Mario class inheriting from Person """
	def __init__(self, startX = 30, startY = 1 ):      #Mario starts at bottom left of the board	
		self._x = startX
		self._y = startY
		self._lives=3

	"""To make mario jump"""
	def mjump(self,ch,sc,fb):
		if(sc.checkPlatform(self._x,self._y,ch)==True):		
			if sc.retChar(self._x-1,self._y) == 'H':
					prev='H'
			else:
					prev=' '

			flag=0
			x=0
			y=0
			check=0
			if ch=='d':										#Right jump
				count=2
				while(count>0):								#First half of jump, going up
					sc.printMario(self._x,self._y,prev)
					
					for i in range(0,len(fb)):
						ans=fb[i].fmove(sc)						
					
					prev=sc.retChar(self._x-1,self._y+1)
					sc.printMario(self._x-1,self._y+1, 'P')
					print ""
					os.system("clear")
					sc.printScreen()
					self._x -= 1
					self._y += 1
					if prev=='O':						#collision while jumping
						flag=1
						x=self._x-1
						y=self._y+1
						break
					time.sleep(0.5)
					count -=1
				for i in range(0,len(fb)):
					ans=fb[i].fmove(sc)

				count =2
				if(flag ==0):									#2nd half of jump, going down
					while count>0:
						sc.printMario(self._x,self._y,prev)
						prev=sc.retChar(self._x+1,self._y+1)
						sc.printMario(self._x+1,self._y+1, 'P')
						print ""
						os.system("clear")
						sc.printScreen()
						self._x += 1
						self._y += 1
						if prev=='O':								#collision while jumping
							flag=1
							x=self._x+1
							y=self._y+1
							break
						time.sleep(0.5)
						count -=1
					for i in range(0,len(fb)):
						ans=fb[i].fmove(sc)


			if ch=='a':											#Similarly for left jump
				count=2
				while count>0:
					sc.printMario(self._x,self._y,prev)
					prev=sc.retChar(self._x-1,self._y-1)
					sc.printMario(self._x-1,self._y-1, 'P')
					print ""
					os.system("clear")
					sc.printScreen()
					self._x -= 1
					self._y -= 1
					if prev=='O':
						flag=1
						x=self._x-1
						y=self._y-1
						break
					time.sleep(0.5)
					count -=1
				for i in range(0,len(fb)):
						ans=fb[i].fmove(sc)

				count=2
				if flag==0:
					while count>0:
						sc.printMario(self._x,self._y,prev)
						prev=sc.retChar(self._x+1,self._y-1)
						sc.printMario(self._x+1,self._y-1, 'P')
						print ""
						os.system("clear")
						sc.printScreen()
						self._x += 1
						self._y -= 1
						if prev == 'O':
							flag=1
							x=self._x+1
							y=self._y-1
							break
						time.sleep(0.5)
						count -=1
					for i in range(0,len(fb)):
						ans=fb[i].fmove(sc)

			if flag==1:
				check=sc.checkCollision(' ',fb,self)
				if check==1:
					return 1
				else:
					return 0

	"""Mario dies"""
	def die(self,sc): 
		self._lives-=1
		sc.changeScore(25)
		if self._lives==0:
			os.system("clear")
			print "you lost! You couldn't save the queen!"
			print "Your final score is:"+str(sc.getScore())
			print "Enter 1 to continue or 2 to exit the game:"
			ans=raw_input()
			return ans

	"""To reposition mario"""
	def reposition(self,x,y):
		self._x=x
		self._y=y

	"""Return number of lives"""
	def getLives(self):
		return self._lives

	"""Return X"""
	def getX(self):
		return self._x

	"""Return Y"""
	def getY(self):
		return self._y
	
	"""Reset lives back to 3"""
	def resetlives(self):
		self._lives=3
