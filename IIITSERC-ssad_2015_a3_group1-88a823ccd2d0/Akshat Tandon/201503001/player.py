import pygame
import constants
import person
import landforms
import ladder
import fireball
import sys
import donkey
import cage 
import coin

class Player(person.Person):


	"""	Defines the player object.It inherits from Person class."""

	def __init__(self):

		"""Constructor for Player class."""
		super(Player,self).__init__(0,0,50,70,'p2_stand.png')
		self.rect.left = 0
		self.rect.bottom = constants.SCREEN_HEIGHT
		self.score = 0
		self.life = constants.PLAYER_LIFE
		self.__princess = None
		self.__reached_princess = False
		self.mode = 'GRAVITY'
		self.__first_flag = True
		self.__second_flag = False

	def update(self):

		"""
			Moves the player acording to the user and also checks if it
			has collected any coins,has been hit with a fireball or has
			reached the princess.
		"""
		if self.mode == 'GRAVITY':
			super(Player,self).update()

		elif self.mode == 'LADDER':
			
			self.rect.y += self._y_vector
			if self._y_vector < 0:
				collided_blocks = pygame.sprite.spritecollide(self,landforms.Platform.all_blocks,False)
				for block in collided_blocks:
					if  self.rect.bottom <= block.rect.bottom:
						self.rect.bottom = block.rect.top
						self.mode = 'GRAVITY'
			elif self.rect.y > 0:
				if self.__first_flag == True:
					collided_blocks = pygame.sprite.spritecollide(self,landforms.Platform.all_blocks,False)
					if len(collided_blocks) == 0:
						self.__first_flag = False
				elif self.__first_flag == False:
					collided_blocks = pygame.sprite.spritecollide(self,landforms.Platform.all_blocks,False)
					if len(collided_blocks) > 0:
						self.rect.bottom = block.rect.top
					self.__first_flag = True 
					self.mode = 'GRAVITY'

		self.__check_collision()

	def move_left(self):

		""" Moves the player left """
		self.set_x_vector(-1 * constants.PLAYER_SPEED)

	def move_right(self):

		""" Moves the player right """
		self.set_x_vector(constants.PLAYER_SPEED)

	def move_up(self):

		""" Checks if there is a ladder and only then allowes the player to move up """
		if self.mode == 'GRAVITY':
			collided_ladders = pygame.sprite.spritecollide(self,ladder.Ladder.all_ropes,False)
			if len(collided_ladders) > 0:
				self.set_y_vector(-1 * constants.SPEED_ON_LADDER)
				self.mode = 'LADDER'
		elif self.mode == 'LADDER':
			self.set_y_vector(-1 * constants.SPEED_ON_LADDER)

	def move_down(self):

		""" Checks if there is a ladder and only then allows the player to move down """
		if self.mode == 'GRAVITY':
			self.rect.y += 80
			collided_ladders = pygame.sprite.spritecollide(self,ladder.Ladder.all_ropes,False)
			self.rect.y -= 80
			if len(collided_ladders) > 0:
				self.set_y_vector(constants.SPEED_ON_LADDER)
				self.mode = 'LADDER'
		elif self.mode == 'LADDER':
			self.set_y_vector(constants.SPEED_ON_LADDER)
			

	def jump(self):

		""" 
			Makes the player jump only after checking if the player is on the 
			ground or standing on a platform
		"""
		self.rect.y += 2
		collided_blocks = pygame.sprite.spritecollide(self,landforms.Platform.all_blocks,False)
		self.rect.y -= 2
		if len(collided_blocks) > 0 or self.rect.bottom == constants.SCREEN_HEIGHT:
			self.set_y_vector(-10)

	def __check_collision(self):

		"""
			Checks if the player has collided with any of the game elements 
			such as coin,fireball,princess and donkey.If a player has collided
			takes appropriate action.
		"""
		self.__collect_coin()
		self.__check_fireball()
		self.__check_princess()
		self.__check_donkey()
		self.__check_cage()

	def __collect_coin(self):

		"""
			Checks if there is a coin at players current position.If it is so then increment 
			the players score and make the coin disappear.
		"""
		collided_coins = pygame.sprite.spritecollide(self,landforms.Platform.all_coins,True)
		for gold_coin in collided_coins:
			self.score += 5
			
			coin.Coin.coin_sound.play()

	def __check_fireball(self):

		"""
			Checks if the player is hit with a fireball.
		"""
		collided_fireballs = pygame.sprite.spritecollide(self,fireball.Fireball.all_fireballs,True)
		if len(collided_fireballs) > 0:
			fireball.Fireball.flame_sound.play()
			self.life -= 1
			self.score -= 25
			self.rect.left = 0
			self.mode = 'GRAVITY'
			self.rect.bottom = constants.SCREEN_HEIGHT

	def set_princess(self,princess):

		""" Assigns princess to the player """
		self.__princess = princess

	def __check_princess(self):

		""" Checks whether the player has reached the princess or not """
		flag = pygame.sprite.collide_rect(self,self.__princess)
		if flag == True:
			self.__check_princess = True

	def check_reached_princess(self):

		""" Returns true if the player has reached the princess """
		return self.__check_princess

	def __check_donkey(self):

		""" 
			Checks if the player has collided with a donkey.If it has ,reduces 
			the life and points of the player and sends him back to the starting
			position.
		"""
		collided_donkeys = pygame.sprite.spritecollide(self,donkey.Donkey.all_donkeys,False)
		if len(collided_donkeys) > 0:
			self.mode = 'GRAVITY'
			self.life -= 1
			self.score -= 25
			self.rect.left = 0
			self.rect.bottom = constants.SCREEN_HEIGHT

	def __check_cage(self):

		"""
			Restricts the player to move through the cage
		"""
		collided_cages = pygame.sprite.spritecollide(self,cage.CageOne.all_cages,False)
		for cage_block in collided_cages:
			self.rect.left = cage_block.rect.right


