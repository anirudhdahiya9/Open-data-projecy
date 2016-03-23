import pygame
import constants
import player
import donkey
import princess
import ladder
import landforms
import scoreboard
import fireball
import cage


class Board(object):


	"""
		Class which defines the Board of the game. It acts as a superclass 
		for all the game levels.
	"""
	final_score = 0

	def __init__(self,screen):

		""" Constructor for Board class """

		# Final Score at the end of the level
		

		# Sprite group which contains player,donkey and priness
		self.active_sprite_list = pygame.sprite.Group()

		# Initializes all the platforms for the game
		self.screen = screen
		self.platform_zero = landforms.ZeroPlatform()
		self.platform_one = landforms.FirstPlatform()
		self.platform_two = landforms.SecondPlatform()
		self.platform_three = landforms.ThirdPlatform()
		self.platform_four = landforms.FourthPlatform()

		# Initializes all the ladders for the game
		self.broken_ladder_one = ladder.BrokenLadder(200,constants.SCREEN_HEIGHT)
		self.ladder_two = ladder.Ladder(400,constants.SCREEN_HEIGHT)
		self.ladder_three = ladder.Ladder(300,constants.ONE_Y)
		self.ladder_four = ladder.Ladder(550,constants.TWO_Y)
		self.ladder_five = ladder.Ladder(450,constants.THREE_Y)

		# Initializes the cage surrounding the princess
		self.cage_one = cage.CageOne()

		# Initializes the player and princess for the game
		self.knight = player.Player()
		self.lady = princess.Princess(constants.SCREEN_HEIGHT - 100,constants.FOUR_Y)

		self.knight.set_princess(self.lady)

		# Add the player and princess the active sprite list
		self.active_sprite_list.add(self.knight)
		self.active_sprite_list.add(self.lady)

		# Set the score board for the game
		self.score_board = scoreboard.ScoreBoard(self.knight)

	def update(self):

		""" Updates the player,princess,donkey,fireballs and the score board """
		self.active_sprite_list.update()
		fireball.Fireball.all_fireballs.update()
		self.score_board.update()

	def draw(self):

		"""
			Draws the platforms,ladders,fireball,player,princess,donkey and
			the score board
		"""
		#Fills the screen with white color 
		self.screen.fill(constants.WHITE)

		# Draws all the platforms for the game 
		self.platform_zero.draw(self.screen)
		self.platform_one.draw(self.screen)
		self.platform_two.draw(self.screen)
		self.platform_three.draw(self.screen)
		self.platform_four.draw(self.screen)

		# Draws all the ladders for the game
		ladder.Ladder.draw(self.screen)
		ladder.BrokenLadder.draw(self.screen)

		# Draws the cage for the game 
		self.cage_one.draw(self.screen)

		# Draws all the fireballs
		fireball.Fireball.draw(self.screen)

		# Draws the player,donkey and princess 
		self.active_sprite_list.draw(self.screen)

		# Draws the score board
		self.score_board.draw(self.screen)

	def _set_villain(self):

		"""
			Sets the number of donkeys and their positions.Has to be
			implemented in the child class.
		"""
		raise NotImplementedError("Subclass must implement abstract method")

	def check_alive_player(self):

		""" Returns true if the player is alive.False otherwise """
		if self.knight.life == -1:
			return False
		else:
			return True

	def check_level_cleared(self):

		""" Returns whether player has completed the current level"""
		if self.knight.check_reached_princess() == True:
			Board.final_score = self.knight.score + 50
			return True
		else:
			return False




