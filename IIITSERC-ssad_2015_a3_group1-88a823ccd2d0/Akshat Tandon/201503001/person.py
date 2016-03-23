import item


class Person(item.Item):


	"""
		This class inherits from Item class and is the superclass of 
		Player,Donkey and Princess subclasses
	"""

	def __init__(self,x,y,width,height,image_path):

		""" Constructor of Person class"""
		super(Person,self).__init__(x,y,width,height,image_path)

	def get_position(self):

		"""
			Returns the top left coordinates of the sprite rectangle
		"""
		return (self.rect.x, self.rect.y)

