import pygame
from main import *
pygame.init()

display_game=pygame.display.set_mode((0,0),pygame.FULLSCREEN)
#display_game=pygame.display.set_mode((1280,720))
pygame.display.set_caption('Donkey Kongy')
displaysize= display_game.get_size()

mainloop=True
fps=pygame.time.Clock()	

background=pygame.image.load('../images/background.jpg').convert_alpha()
background=pygame.transform.scale(background,displaysize)

play=pygame.image.load('../images/play_btn.png')
play_glow=pygame.image.load('../images/play_glow.png')
#play=pygame.transform.scale(play,(30,30))
exit=pygame.image.load('../images/exit_btn.png')
exit_glow=pygame.image.load('../images/exit_glow.png')

while mainloop:

	for event in pygame.event.get():
			if event.type == pygame.KEYDOWN:
				if event.key==pygame.K_q:
					mainloop=False

	display_game.blit(background,(0,0))
	display_game.blit(play,(displaysize[0]*0.6,displaysize[1]*0.3))	

	display_game.blit(exit,(displaysize[0]*0.6,displaysize[1]*0.55))


	if displaysize[0]*0.6<=pygame.mouse.get_pos()[0]<=displaysize[0]*0.6+306 and displaysize[1]*0.3<=pygame.mouse.get_pos()[1]<=displaysize[1]*0.3+120:
		display_game.blit(play_glow,(displaysize[0]*0.6,displaysize[1]*0.3))		
		mousepress=pygame.mouse.get_pressed()
		if mousepress[0]:
			while True:
				a=main(display_game)
				if a[0]==True:
					score = pygame.font.Font(None, 50)
					scoretext = score.render("Final Score ~ "+str(a[1]), 1, (255, 255, 255))
					game_status=False
					while not game_status:
						for event in pygame.event.get():
							if event.type == pygame.KEYDOWN:
								if event.key==pygame.K_q:
									game_status=True
						display_game.blit(background,(0,0))
						over = pygame.font.Font(None, 50)
						overtext = over.render("Press 'q' to continue next level", 1, (255, 255, 255))
						display_game.blit(scoretext,(display_game.get_size()[0]*0.6,display_game.get_size()[1]*0.3))
						display_game.blit(overtext,(display_game.get_size()[0]*0.6,display_game.get_size()[1]*0.5))
						pygame.display.flip()

						fps.tick(60)
				else:
					break

	elif displaysize[0]*0.6<=pygame.mouse.get_pos()[0]<=displaysize[0]*0.6+306 and displaysize[1]*0.55<=pygame.mouse.get_pos()[1]<=displaysize[1]*0.55+120:
		display_game.blit(exit_glow,(displaysize[0]*0.6,displaysize[1]*0.55))
		mousepress=pygame.mouse.get_pressed()
		if mousepress[0]:
			mainloop=False 
	pygame.display.flip()
	fps.tick(60)

pygame.quit()
quit()
