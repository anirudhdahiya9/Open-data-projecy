import pygame
import graphics
import constants

class RopeBlock(pygame.sprite.Sprite):

	def __init__(self):

		super(RopeBlock,self).__init__()
		self.graphic_obj = graphics.Graphics('blocks.png')
		self.image = self.graphic_obj.extract_graphic(393,864,5,70)
		self.rect = self.image.get_rect()


class LadderBlock(pygame.sprite.Sprite):


	""" Class which defines the individual ladder block """

	def __init__(self):

		"""Constructor for LadderBlock class """
		super(LadderBlock,self).__init__()
		self.graphic_obj = graphics.Graphics('blocks.png')
		self.image = self.graphic_obj.extract_graphic(502,71,73,74)
		self.rect = self.image.get_rect()


class BrokenLadderBlock(pygame.sprite.Sprite):


	""" Class which defines the individual broken ladder block """

	def __init__(self):

		"""Constructor for BrokenLadderBlock class """
		super(BrokenLadderBlock,self).__init__()
		self.graphic_obj = graphics.Graphics('blocks.png')
		self.image = self.graphic_obj.extract_graphic(647,80,73,64)
		self.rect = self.image.get_rect()


class Ladder(object):


	""" Class which defines the Ladder object """

	all_ladders = pygame.sprite.Group()	# Class variable which stores every ladder block object 
	all_ropes = pygame.sprite.Group()

	def __init__(self,left,bottom):

		""" Constructor for Ladder class """
		super(Ladder,self).__init__()

		self.block_one = LadderBlock()		# Initializes one ladder block object 
		self.block_one.rect.left = left
		self.block_one.rect.bottom = bottom + 5
		self.rope_one = RopeBlock()
		self.rope_one.rect.left = left + 33
		self.rope_one.rect.bottom = bottom + 5
		Ladder.all_ladders.add(self.block_one)	# Adds the ladder block in all_ladders group
		Ladder.all_ropes.add(self.rope_one)

		self.block_two = LadderBlock()		# Initialize another block object
		self.block_two.rect.left = left
		self.block_two.rect.bottom = self.block_one.rect.top + 20	
		self.rope_two = RopeBlock()
		self.rope_two.rect.left = left + 33
		self.rope_two.rect.bottom = self.block_one.rect.top + 20
		Ladder.all_ladders.add(self.block_two)	# Adds the second ladder block in all_ladders
		Ladder.all_ropes.add(self.rope_two)										# block as well

															
	def update():

		"""Updates all the Ladder blocks """
		Ladder.all_ladders.update()
		Ladder.all_ropes.update()

	@staticmethod
	def draw(screen):

		""" Draws all the ladder block """
		Ladder.all_ladders.draw(screen)
		# Ladder.all_ropes.draw(screen)


class BrokenLadder(object):


	""" Class which defines the individual broken ladder block """

	all_broken_ladders = pygame.sprite.Group() # Class variable which stores every broken ladder block

	def __init__(self,left,bottom):

		""" Constructor for BrokenLadder object """
		super(BrokenLadder,self).__init__()
		self.block_one = LadderBlock()
		self.block_one.rect.left = left
		self.block_one.rect.bottom = bottom + 5
		BrokenLadder.all_broken_ladders.add(self.block_one)
		self.block_two = BrokenLadderBlock()
		self.block_two.rect.left = left
		self.block_two.rect.bottom = self.block_one.rect.top + 20
		BrokenLadder.all_broken_ladders.add(self.block_two)
		
	def update():

		""" Updates all the broken ladder blocks """
		BrokenLadder.all_broken_ladders.update()

	@staticmethod
	def draw(screen):

		""" Draws all the broken ladder blocks on the screen """
		BrokenLadder.all_broken_ladders.draw(screen)


