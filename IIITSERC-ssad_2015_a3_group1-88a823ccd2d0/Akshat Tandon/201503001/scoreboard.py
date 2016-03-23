import pygame
import player
import constants


class ScoreBoard(object):


	""" Class which defines the score board of the game """

	def __init__(self,protagnist):

		""" Constructor for the ScoreBoard class """
		self.protagnist = protagnist
		self.font = pygame.font.Font('freesansbold.ttf',35)
		self.score_line = 'Score : ' + str(self.protagnist.score) + ' Life : ' + str(self.protagnist.life)
		self.text = self.font.render(self.score_line,True,constants.BLACK)

	def update(self):

		"""Update the score board for the current frame """
		self.score_line = 'Score : ' + str(self.protagnist.score) + ' Life : ' + str(self.protagnist.life)
		self.text = self.font.render(self.score_line,True,constants.BLACK)
		
	def draw(self,screen):

		"""Draw the score board for the current frame """
		screen.blit(self.text,(0,0))