"""
	Module whch contains the lanforms such as blocks and platforms for the game
"""

import pygame
import constants
import graphics
import coin
import random


class Block(pygame.sprite.Sprite):


	"""
		Class which defines a single block which is used for building
		platforms.
	"""

	def __init__(self):

		""" Constructor for Block class """
		super(Block,self).__init__()
		self.graphic_obj = graphics.Graphics('blocks.png')
		self.image = self.graphic_obj.extract_graphic(506,506,68,25)
		self.rect = self.image.get_rect()

	def set_x(self,x):

		""" Sets the top left x coordinate of the block """
		self.rect.x = x

	def set_y(self,y):

		""" Sets the top left y coordinate of the block """
		self.rect.y = y


class Platform(object):


	"""
		Class which defines the platform object.It acts as a superclass for 
		Class' of actual platforms.
	"""

	# Sprite group of all the blocks in the game
	all_blocks = pygame.sprite.Group()
	# Sprite group of all the coins in the game 
	all_coins = pygame.sprite.Group()

	def __init__(self):

		"""Constructor for the Platform class """
		super(Platform,self).__init__()
		self.block_list = pygame.sprite.Group()
		self.coins_list = pygame.sprite.Group()

	def update(self):

		""" Updates all the blocks and coins for the current frame """
		self.block_list.update()
		self.coins_list.update()

	def draw(self,screen):

		""" Draws all the blocks and coins for the current frame """
		self.block_list.draw(screen)
		self.coins_list.draw(screen)


class ZeroPlatform(Platform):

	"""
		Class which defines the ground.
	"""
	
	def __init__(self):

		""" Constructor for the ZeroPlatform class """
		super(ZeroPlatform,self).__init__()
		# Randomly add coins on this platform
		for i in range(70,constants.SCREEN_WIDTH,68):
			random_num = random.randint(0,100)
			if random_num % 2 == 0:
				gold_coin = coin.Coin()
				gold_coin.rect.left = i + 5
				gold_coin.rect.bottom = constants.SCREEN_HEIGHT
				self.coins_list.add(gold_coin)
				Platform.all_coins.add(gold_coin)	


class FirstPlatform(Platform):


	"""
		Class which defines the first platform which is just above the gorund.
	"""

	def __init__(self):

		""" Constructor for the FirstPlatform class """
		super(FirstPlatform,self).__init__()
		for i in range(constants.ONE_X1,constants.ONE_X2,68):
			# Add blocks
			block = Block()
			block.set_x(i)
			block.set_y(constants.ONE_Y)
			self.block_list.add(block)
			Platform.all_blocks.add(block)
			# Randomly add coins 
			random_num = random.randint(0,100)
			if random_num % 2 == 0:
				gold_coin = coin.Coin()
				gold_coin.rect.left = i + 5
				gold_coin.rect.bottom = constants.ONE_Y
				self.coins_list.add(gold_coin)
				Platform.all_coins.add(gold_coin)


class SecondPlatform(Platform):


	""" Class which defines the second platform """

	def __init__(self):

		""" Constructor for SecondPlatform class """
		super(SecondPlatform,self).__init__()
		for i in range(constants.TWO_X1,constants.TWO_X2,68):
			# Add block
			block = Block()
			block.set_x(i)
			block.set_y(constants.TWO_Y)
			self.block_list.add(block)
			Platform.all_blocks.add(block)
			# Randomly add coins
			random_num = random.randint(0,100)
			if random_num % 2 == 0:
				gold_coin = coin.Coin()
				gold_coin.rect.left = i + 5
				gold_coin.rect.bottom = constants.TWO_Y
				self.coins_list.add(gold_coin)
				Platform.all_coins.add(gold_coin)


class ThirdPlatform(Platform):


	""" Class which defines the third platform """
		
	def __init__(self):

		"""Constructor for ThirdPlatform class """
		super(ThirdPlatform,self).__init__()
		for i in range(constants.THREE_X1,constants.THREE_X2,68):
			# Add blocks
			block = Block()
			block.set_x(i)
			block.set_y(constants.THREE_Y)
			self.block_list.add(block)
			Platform.all_blocks.add(block)
			# Randomly add coins
			random_num = random.randint(0,100)
			if random_num % 2 == 0:
				gold_coin = coin.Coin()
				gold_coin.rect.left = i + 5
				gold_coin.rect.bottom = constants.THREE_Y
				self.coins_list.add(gold_coin)
				Platform.all_coins.add(gold_coin)


class FourthPlatform(Platform):


	""" Class which defines the fourth platform """

	def __init__(self):

		""" Constructor for FourthPlatform class """
		super(FourthPlatform,self).__init__()
		for i in range(constants.FOUR_X1,constants.FOUR_X2,68):
			# Add blocks
			block = Block()
			block.set_x(i)
			block.set_y(constants.FOUR_Y)
			self.block_list.add(block)
			Platform.all_blocks.add(block)
			#Randomly add coins
			random_num = random.randint(0,100)
			if random_num % 2 == 0:
				gold_coin = coin.Coin()
				gold_coin.rect.left = i + 5
				gold_coin.rect.bottom = constants.FOUR_Y
				self.coins_list.add(gold_coin)
				Platform.all_coins.add(gold_coin)
		
