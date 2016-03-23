import pygame

	
size=16


class player(person):
	def __init__(self,name,initX,initY):
		person.__init__(name,initX,initY)
		
		self.marioright =pygame.image.load('../images/m1.png')
		self.marioright=pygame.transform.scale(self.marioright,(size,size))
		
		self.mariowalkright=pygame.image.load('../images/m2.png')
		self.mariowalkright=pygame.transform.scale(self.mariowalkright,(size,size))

		self.mariowalkleft=pygame.transform.scale(self.mariowalkright,(size,size))
		self.mariowalkleft=pygame.transform.flip(mariowalkright,1,0)

		self.marioleft=pygame.transform.scale(self.marioright,(size,size))
		self.marioleft=pygame.transform.flip(marioleft,1,0)

		self.mario=self.marioright
