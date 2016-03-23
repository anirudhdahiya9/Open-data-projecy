import pygame
import constants
import donkey
import board


class LevelOne(board.Board):


	""" Class which defines the first level of the game """

	def __init__(self,screen):

		""" Constructor for the LevelOne class """
		super(LevelOne,self).__init__(screen)
		self.villain_one = None
		self._set_villain()

	def _set_villain(self):

		""" 
			Sets the number of donkeys and their positions for
			the first level.
		"""
		self.villain_one = donkey.Donkey(100 , constants.THREE_Y,0,500)
		self.active_sprite_list.add(self.villain_one)


class LevelTwo(board.Board):


	""" Class which defines the second level of the game """

	def __init__(self,screen):

		""" Constructor for the LevelTwo class """
		super(LevelTwo,self).__init__(screen)
		self.villain_one =None
		self.villain_two = None
		self._set_villain()

	def _set_villain(self):

		"""
			Sets the number of donkeys and their positions for
			the second level of the game.
		"""
		self.villain_one = donkey.Donkey(100 , constants.THREE_Y,0,500)
		self.active_sprite_list.add(self.villain_one)

		self.villain_two = donkey.Donkey(900, constants.TWO_Y,700,950)
		self.active_sprite_list.add(self.villain_two)


class LevelThree(board.Board):


	""" Class which defines the third level of the game """

	def __init__(self,screen):

		""" Constructor for the third level of the game """
		super(LevelThree,self).__init__(screen)
		self.villain_one =None
		self.villain_two = None
		self.villain_three = None
		self._set_villain()

	def _set_villain(self):

		"""
			Sets the number of donkeys and their positions for 
			the third level of the game
		"""
		self.villain_one = donkey.Donkey(100 , constants.THREE_Y,0,500)
		self.active_sprite_list.add(self.villain_one)

		self.villain_two = donkey.Donkey(900, constants.TWO_Y,700,950)
		self.active_sprite_list.add(self.villain_two)

		self.villain_three = donkey.Donkey(200, constants.ONE_Y,0,300)
		self.active_sprite_list.add(self.villain_three)




