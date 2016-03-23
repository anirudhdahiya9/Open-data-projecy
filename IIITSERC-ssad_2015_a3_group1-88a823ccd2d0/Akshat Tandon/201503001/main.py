import pygame
import constants
import levels
import sys
import board

def main():


	""" The main function of the game """

	pygame.init()
	screen = pygame.display.set_mode((constants.SCREEN_WIDTH,
									constants.SCREEN_HEIGHT))
	pygame.display.set_caption('Donkey Kong by Akshat Tandon 201503001')
	clock = pygame.time.Clock()
	current_level = levels.LevelOne(screen)
	stop = False

	#Play background music
	pygame.mixer.init()
	pygame.mixer.music.load('background.ogg')
	pygame.mixer.music.set_endevent(pygame.constants.USEREVENT)
	pygame.mixer.music.play(-1)

	# The main game loop
	while not stop:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				stop = True

			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_a:
					current_level.knight.move_left()
				if event.key == pygame.K_d:
					current_level.knight.move_right()
				if event.key == pygame.K_w:
					current_level.knight.move_up()
				if event.key == pygame.K_s:
					current_level.knight.move_down()
				if event.key == pygame.K_SPACE:
					current_level.knight.jump()
				if event.key == pygame.K_q:
					stop = True

			if event.type == pygame.KEYUP:
				if event.key == pygame.K_a and current_level.knight.get_x_vector() < 0:
					current_level.knight.stop_horizontal()
				if event.key == pygame.K_d and current_level.knight.get_x_vector() > 0:
					current_level.knight.stop_horizontal()
				if event.key == pygame.K_w and current_level.knight.get_y_vector() < 0:
					current_level.knight.stop_vertical()
				if event.key == pygame.K_s and current_level.knight.get_y_vector() > 0:
					current_level.knight.stop_vertical()

		# Update the sprites for the current frame 
		current_level.update()
		
		# Draw the current frame
		current_level.draw()

		# Check if the player is dead/alive 
		if current_level.check_alive_player() == False:
			stop = True

		# Ensures that FPS number of frames are updated and drawn per second
		clock.tick(constants.FPS)

		# Display the current frame contents on the display surface
		pygame.display.flip()

		# Checks if the user has quit the game
		if stop == True:
			pygame.quit()
			sys.exit(0)

		# Checks if the player has reached the princess and loads the next 
		# level if it is so
		elif current_level.check_level_cleared() == True:
			if type(current_level) == levels.LevelOne:
				current_level = levels.LevelTwo(screen)
				current_level.knight.score += board.Board.final_score

			elif type(current_level) == levels.LevelTwo:
				current_level = levels.LevelThree(screen)
				current_level.knight.score += board.Board.final_score

			elif type(current_level) == levels.LevelThree:
				print 'Game Over,You succesfully cleared all the levels'
				pygame.quit()
				sys.exit(0)






if __name__ == '__main__':
	main()

