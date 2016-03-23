import pygame
import constants
import person


class Princess(person.Person):


	""" Class which defines the princess object """

	def __init__(self,left,bottom):

		""" Constructor for the Princess class """
		super(Princess,self).__init__(0,0,50,70,'p3_stand.png')
		self.rect.bottom = bottom
		self.rect.left = left


