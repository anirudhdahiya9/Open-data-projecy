import pygame
import constants
import graphics
import landforms
import ladder


class Item(pygame.sprite.Sprite):


	""" 
		Defines objects which interacts with the landforms of the game such as platforms,
		ladders.This forms the base class for all other interactive objects of the game.It ensures
		that the objects are in accordance to the laws of physics.
	"""

	def __init__(self,x,y,width,height,image_path):

		""" 
			Constructor of the Item class which is responsible for getting the image of the 
			object class from the sprite sheet.
		"""
		super(Item,self).__init__()
		self.graphic_obj = graphics.Graphics(image_path)
		self.image = self.graphic_obj.extract_graphic(x,y,width,height)
		self.rect = self.image.get_rect()
		self._x_vector = 0
		self._y_vector = 0

	def update(self):

		"""
			Responsible for adding gravity effects,making the object move ,ensuring that
			the object remains within the screen area
		"""
		# Add effect of gravity on item
		self.__gravity_effect()
		# Moves the item left/right 
		self.rect.x += self._x_vector
		# Moves the item top/bottom 
		self.rect.y += self._y_vector
		# Maintains items position on the current platform and ensures that
		# the gravity on item is counteracted when the item is on a platform
		self.__check_platform()
		# Maintains that the player does not leave the board width and height
		self.__check_wall()		

	def __gravity_effect(self):

		""" Adds the effect of gravity on items """
		self._y_vector += constants.GRAVITY

	def __check_board(self):

		""" Ensures that the item remains within the confinements of the screen """
		if self.rect.left <= 0:
			self.rect.left = 0
		elif self.rect.right >= constants.SCREEN_WIDTH:
			self.rect.right = constants.SCREEN_WIDTH
	

	def __check_ground(self):

		""" Ensures that the item does not go below the ground platform """
		if self.rect.bottom > constants.SCREEN_HEIGHT:
			self.rect.bottom = constants.SCREEN_HEIGHT
			self._y_vector = 0

	def __check_platform(self):

		""" Counteracts the effect of gravity when item is on a platform """
		collided_blocks = pygame.sprite.spritecollide(self,landforms.Platform.all_blocks,False)
		for block in collided_blocks:
			if self._y_vector > 0 :
				self.rect.bottom = block.rect.top
			self._y_vector = 0

	def __check_wall(self):

		""" Ensures that the item is within the confinements of the board """
		self.__check_board()
		self.__check_ground()

	def set_x_vector(self,x):

		""" Sets the x component of items motion """
		self._x_vector = x

	def set_y_vector(self,y):

		""" Sets the y component of item motion """
		self._y_vector = y

	def get_x_vector(self):

		""" Returns the x component of items motion """
		return self._x_vector

	def get_y_vector(self):

		""" Returns the y component of items motion """
		return self._y_vector

	def move_left(self):

		"""  Must be implementent in a sublass according to motion of the item """
		raise NotImplementedError("Subclass must implement abstract method")

	def move_right(self):

		"""  Must be implementent in a sublass according to motion of the item """
		raise NotImplementedError("Subclass must implement abstract method")

	def stop_horizontal(self):
		
		""" Stops the item in horizontal direction """
		self._x_vector = 0

	def stop_vertical(self):

		"""Stops the item in vertical direction """
		self._y_vector = 0