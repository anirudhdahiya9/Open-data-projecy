import pygame
import constants
import item
import ladder
import random


class Fireball(item.Item):


	""" Class which defines the fireballs of the game """
	all_fireballs = pygame.sprite.Group()	# Class variable which stores all the 
										# fireballs currently present in a frame.
	pygame.mixer.init()
	flame_sound = pygame.mixer.Sound('handleFlame.ogg')

	def __init__(self,left,bottom):

		""" Constructor for the Fireball class """
		super(Fireball,self).__init__(22,22,24,27,'fireball.png')
		self.rect.left = left
		self.rect.bottom = bottom
		self.direction = 'RIGHT'

		# For randomizing the motion of fireball
		self.random_number = random.randint(0,10)
		self.__count = 0
		self.__threshold = 150

	def update(self):

		""" Updates fireballs position for the current frame """
		if self.direction == 'LEFT':
			self.set_x_vector(-1 * constants.FIREBALL_SPEED)
		else:
			self.set_x_vector(constants.FIREBALL_SPEED)

		super(Fireball,self).update()

		self.__change_direction()	# Reverses direction if it hits a wall.
		self.__check_ladder()		# Checks whether there is a ladder for going down.
		self.__check_validity()		# Checks whether it has striked the bottom left 
									# position of the board
		# For randomizing the motion of fireball
		self.__count += 1
		if self.__count >= self.__threshold:
			self.random_number = random.randint(0,10)
			self.__count = 0
			self.__threshold = random.randint(0,200)

	def __change_direction(self):

		""" Reverses  the direction of the fireball if it hits 
			the boundary wall.
		"""
		if self.rect.left <= 0:
			self.direction = 'RIGHT'
		elif self.rect.right >= constants.SCREEN_WIDTH:
			self.direction = 'LEFT'

	def __check_ladder(self):
		
		""" 
			Check whether a ladder is available for moving down or 
			not.If it is,randomly decide whether to move down or
			continue moving on the platform.
		"""
		# Moves the fireball down and sees if it collides with the ladder or not.If it collides
		# then a ladder is present for moving down. 
		self.rect.top += 100
		collided_ladders = pygame.sprite.spritecollide(self,ladder.Ladder.all_ladders,False)
		self.rect.top -= 100

		# Randomly decide to take the ladder or continue moving.
		if len(collided_ladders) > 0 and self.random_number % 2 == 0:
			self.rect.top += 100
			random_number = random.randint(0,10)
			# If falling through stairs,randomly decide the direction
			# after falldown.
			if random_number % 2 == 0:
				self.direction = 'RIGHT'
			else:
				self.direction = 'LEFT'

	def __check_validity(self):

		""" 
			Checks whether fireball has reached the bottom left corner of
			the board or not.If it has delete the fireball.
		"""
		if self.rect.left == 0 and self.rect.bottom == constants.SCREEN_HEIGHT:
			self.kill()

	@staticmethod
	def draw(screen):

		"""
			Class method for drawing all the fireballs currently present 
			on the board.
		"""
		Fireball.all_fireballs.draw(screen)

