import pygame


class Wall(pygame.sprite.Sprite):
	""" Player cannot go through these walls """
	def __init__(self, x, y, size):

    # Calling sprite's constructor
	    pygame.sprite.Sprite.__init__(self)

	    self.image=pygame.image.load('../images/wall.png').convert_alpha()
	    self.image=pygame.transform.scale(self.image,(size,size))

	    self.rect = self.image.get_rect()
	    self.rect.y = y
	    self.rect.x = x


class Ladder(pygame.sprite.Sprite):
	""" Player can climb these ladders"""
	def __init__(self, x, y, size):

    # Calling sprite's constructor
	    pygame.sprite.Sprite.__init__(self)

	    self.image=pygame.image.load('../images/ladder.png').convert_alpha()
	    self.image=pygame.transform.scale(self.image,(size,size))

	    self.rect = self.image.get_rect()
	    self.rect.y = y
	    self.rect.x = x

class Coin(pygame.sprite.Sprite):
	""" Player can collect these coins"""
	def __init__(self, x, y, size):

    # Calling sprite's constructor
	    pygame.sprite.Sprite.__init__(self)

	    self.image=pygame.image.load('../images/coin.gif').convert_alpha()
	    self.image=pygame.transform.scale(self.image,(size,size))

	    self.rect = self.image.get_rect()
	    self.rect.y = y
	    self.rect.x = x
