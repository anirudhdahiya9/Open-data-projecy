import pygame

import constants

class Graphics(object):
	"""
		Graphics class is used to extract images from
		a sprite sheet which can then be used in the
		game
	"""

	def __init__(self,image_path):
		"""
		Constructor used to initialize a Graphics type object by loading
		the sprite sheet.
		"""

		self.__sprite_sheet = pygame.image.load(image_path).convert()


	def extract_graphic(self,x,y,width,height):
		"""
			From the sprite sheet it extracts the rectangular area whose top 
			left coordinates are at (x,y) having the passed in width and 
			height.
		"""
		#Creates a pygame surface and embeds the extracted image on it
		image = pygame.Surface((width,height)).convert()
		image.blit(self.__sprite_sheet,(0,0),(x,y,width,height))

		#Makes the color BLACK transparent in the extracted image
		image.set_colorkey(constants.BLACK)
		return image

