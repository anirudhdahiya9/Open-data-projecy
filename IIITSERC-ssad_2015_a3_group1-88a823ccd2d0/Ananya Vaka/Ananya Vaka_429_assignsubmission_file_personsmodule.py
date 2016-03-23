import pygame

white = (255,255,255)
black = (0,0,0)
red = (255,0,0)
gold=(255,215,0)
blue =  (0,0,255)
green = (0,255,0)
pink = (255,105,180)
purple=(128,0,128)
silver=(192,192,192)
teal=(0,128,128)
brown=(139,69,19)
orange=(255,140,0)


class Person:
	def __init__(self,x,y):
		self.xp=x
		self.yp=y
	def Draw(self,gameDisplay):
		""" We will implement this in derived class """
		pass
	def getPosition(self):
		return self.xp,self.yp

class Player(Person):

	def __init__(self,x,y):
		self.xp=x
		self.yp=y
		self.__score=0

	def Draw(self,gameDisplay):
		pygame.draw.rect(gameDisplay,green,[self.xp,self.yp,20,20])
        
	def collectCoin(self):
		self.__score+=1

	def scoredisplay(self,gameDisplay):
		myfont = pygame.font.SysFont("monospace", 15)

		label = myfont.render("Your score is "+str(self.__score)+".", 1, (0,0,0))
		gameDisplay.blit(label, (100, 620))

class Donkey(Person):

	def move(self,count):
		if count==1 and self.xp<200:
			self.xp=self.xp+5
		if self.xp==200:
			count=0   
		if count==0 and self.xp>30:
			self.xp=self.xp-5
		if self.xp==30:
			count=1
		return count

     	def Draw(self,gameDisplay):
		img=pygame.image.load("Donkey_Kong_Profile.jpg")
		img=pygame.transform.scale(img,(40,40))
		gameDisplay.blit(img,(self.xp,self.yp))
		

		
