import pygame
from board import *

def main(display_game):
	

	class colors:
		def __init__(self,name,rgbval):
			self.name=name
			self.rgbval=rgbval

	def setcolornames():
		global white,black,red
		white=colors('white',(255,255,255))
		black=colors('black',(0,0,0))
		red=colors('red',(255,0,0))

	#Inital required variables
	initPos=[0,0]
	delta_x=0
	delta_y=0


	fps=pygame.time.Clock()	
	setcolornames()


	#Creating a board instance.
	displaysize=[display_game.get_size()[0],display_game.get_size()[1]]

	mainboard=board(displaysize[0],displaysize[1])
	function(displaysize[0],displaysize[1])
	function1(displaysize[0],displaysize[1])

	#Setting a window with width,height
	#display_game=pygame.display.set_mode((0,0),pygame.FULLSCREEN)
	

	#Creating the walls
	mainboard.drawgrid(display_game,initPos)


	mainboard.mario.wallList=mainboard.wallList
	mainboard.donkey.wallList=mainboard.wallList

	mainboard.mario.coinList=mainboard.coinList

	mainboard.mario.ladderList=mainboard.ladderList
	mainboard.mario.topladderList=mainboard.topladderList
	mainboard.mario.allladderposition=mainboard.allladderposition
	mainboard.donkey.topladderList=mainboard.topladderList


	mainboard.donkey.ladderList=mainboard.ladderList
	mainboard.mario.ladderposition=mainboard.ladderposition


	#print mainboard.ladderposition
	#print mainboard.topladderList

	mainboard.donkey.fireballsList=mainboard.fireballsList

	posX=mainboard.initPos[0]
	posY=mainboard.initPos[1]

	#mainboard.showgrid()
	x1=posX
	y1=posY

	game_status=True
	gamescore=-1

	while game_status:
		for event in pygame.event.get():
			if event.type == pygame.KEYDOWN:
				if event.key==pygame.K_q:
					game_status=False
					return (False,mainboard.mario.score)
				if event.key == pygame.K_a:
					if mainboard.mario.arrows[0]==1:
						person.moveLeft(mainboard.mario)

				elif event.key == pygame.K_d:
					if mainboard.mario.arrows[1]==1:
						person.moveRight(mainboard.mario)

				elif event.key == pygame.K_w:
					if mainboard.mario.arrows[2]==1:
						person.moveUp(mainboard.mario)

				elif event.key == pygame.K_s:
					if mainboard.mario.arrows[3]==1:
						person.moveDown(mainboard.mario)

				if event.key == pygame.K_SPACE:
					if mainboard.mario.arrows[4]==1:
						person.Jump(mainboard.mario)
				
			if event.type == pygame.KEYUP:
				if event.key == pygame.K_a and mainboard.mario.deltaX < 0:
					person.stopside(mainboard.mario)

					mainboard.mario.image=mainboard.mario.marioleft
				if event.key == pygame.K_d and mainboard.mario.deltaX > 0:
					person.stopside(mainboard.mario)
					mainboard.mario.image=mainboard.mario.marioright
				if event.key == pygame.K_w or event.key == pygame.K_s:
					person.stopup(mainboard.mario)
		

		if mainboard.mario.score!=gamescore:
			gamescore=mainboard.mario.score
			#print gamescore
		#print person.getLocation(mainboard.mario)
		#person.postopladders(mainboard.mario)


		#Code for ladders
		if mainboard.mario.movestate!=5:
			person.checkLadders(mainboard.mario)
		#Ends here


		#Code for fireballs goes here#
		mainboard.mario.fireballsList=mainboard.donkey.fireballsList
		#Ends here

		score = pygame.font.Font(None, 30)
		scoretext = score.render("Score ~ "+str(gamescore), 1, (255, 255, 255))
		
		livestext=score.render("Lives - "+str(mainboard.mario.lives),1, (255, 255, 255))
		mainboard.AllList.update()
		mainboard.donkey.fireballsList.update()

		display_game.fill(black.rgbval)	
		mainboard.donkey.fireballsList.draw(display_game)
		mainboard.AllList.draw(display_game)

		display_game.blit(scoretext,(50,20))
		display_game.blit(livestext,(1450,20))

		if mainboard.mario.lives==0 :

			score = pygame.font.Font(None, 50)
			scoretext = score.render("Final Score ~ "+str(mainboard.mario.score), 1, (255, 255, 255))
			game_status=False
			

			while not game_status:
				for event in pygame.event.get():
					if event.type == pygame.KEYDOWN:
						if event.key==pygame.K_q:
							game_status=True
				background=pygame.image.load('../images/background.jpg').convert_alpha()
				background=pygame.transform.scale(background,displaysize)
				display_game.blit(background,(0,0))
				over = pygame.font.Font(None, 50)
				overtext = over.render("Press 'q' to quit to main menu", 1, (255, 255, 255))
				display_game.blit(scoretext,(display_game.get_size()[0]*0.6,display_game.get_size()[1]*0.3))
				display_game.blit(overtext,(display_game.get_size()[0]*0.6,display_game.get_size()[1]*0.5))
				pygame.display.flip()

				fps.tick(60)
			return (False,mainboard.mario.score)


		if  mainboard.mario.gameover:
			mainboard.mario.score+=25
			return (True,mainboard.mario.score)

		pygame.display.flip()

		fps.tick(60)



