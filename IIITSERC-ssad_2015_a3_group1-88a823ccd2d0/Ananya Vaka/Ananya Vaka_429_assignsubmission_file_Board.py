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

class Board:
	def __init__(self):
		pass
	def Draw(self,gameDisplay):		
		pygame.draw.rect(gameDisplay,white,[30,30,740,540])
		pygame.draw.rect(gameDisplay,black,[30,480,540,12])
		pygame.draw.rect(gameDisplay,black,[260,390,540,12])
		pygame.draw.rect(gameDisplay,black,[30,300,540,12])
		pygame.draw.rect(gameDisplay,black,[260,210,540,12])
		pygame.draw.rect(gameDisplay,black,[30,120,540,12])
		pygame.draw.rect(gameDisplay,black,[30,70,100,13])
		pygame.draw.rect(gameDisplay,pink,[510,480,7,90])       
		pygame.draw.rect(gameDisplay,pink,[540,480,7,90])
		pygame.draw.rect(gameDisplay,purple,[510,510,30,5])
		pygame.draw.rect(gameDisplay,purple,[510,540,30,5])
		pygame.draw.rect(gameDisplay,pink,[280,390,7,90])       
		pygame.draw.rect(gameDisplay,pink,[310,390,7,90])
		pygame.draw.rect(gameDisplay,purple,[280,420,30,5])
		pygame.draw.rect(gameDisplay,purple,[280,450,30,5])
		pygame.draw.rect(gameDisplay,pink,[510,300,7,90])       
		pygame.draw.rect(gameDisplay,pink,[540,300,7,90])
		pygame.draw.rect(gameDisplay,purple,[510,330,30,5])
		pygame.draw.rect(gameDisplay,purple,[510,360,30,5])
		pygame.draw.rect(gameDisplay,pink,[280,210,7,90])       
		pygame.draw.rect(gameDisplay,pink,[310,210,7,90])
		pygame.draw.rect(gameDisplay,purple,[280,240,30,5])
		pygame.draw.rect(gameDisplay,purple,[280,270,30,5])
		pygame.draw.rect(gameDisplay,pink,[510,120,7,90])       
		pygame.draw.rect(gameDisplay,pink,[540,120,7,90])
		pygame.draw.rect(gameDisplay,purple,[510,150,30,5])
		pygame.draw.rect(gameDisplay,purple,[510,180,30,5])
