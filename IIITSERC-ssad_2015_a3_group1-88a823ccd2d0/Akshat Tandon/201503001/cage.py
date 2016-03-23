import pygame
import graphics
import constants


class Cage(pygame.sprite.Sprite):


	""" Class which defines a cage block """
	
	def __init__(self):

		"""Constructor for Cage class """
		super(Cage,self).__init__()
		self.graphic_obj = graphics.Graphics('chain.png')
		self.image = self.graphic_obj.extract_graphic(24,1,22,68)
		self.rect = self.image.get_rect()

class CageOne(object):


	""" Class which defines the cage surrounding the princess """
	all_cages = pygame.sprite.Group()

	def __init__(self):
 
		super(CageOne,self).__init__()
		self.block_one = Cage()
		self.block_one.rect.left = constants.FOUR_X1 + 100
		self.block_one.rect.bottom = constants.FOUR_Y
		CageOne.all_cages.add(self.block_one)
		self.block_two = Cage()
		self.block_two.rect.left = constants.FOUR_X1 + 100
		self.block_two.rect.bottom = self.block_one.rect.top
		CageOne.all_cages.add(self.block_two)

	def update():

		""" Updates the cage blocks """
		CageOne.all_cages.update()

	@staticmethod
	def draw(screen):

		""" Draws the cage on the screen """
		CageOne.all_cages.draw(screen)
