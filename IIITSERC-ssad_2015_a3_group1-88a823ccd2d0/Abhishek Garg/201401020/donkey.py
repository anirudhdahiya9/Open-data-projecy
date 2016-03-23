import random
from person import Person
from fireball import fireball
class donkey(Person):
	def __init__(self,surface,x,y,dir):
		self.__surface=surface
		Person.__init__(self,x,y)
#		self.__donk_y=donk_y
#		self.__donk_x=donk_x
		self.__surface[self.x][self.y]='D'
		self.__donk_dir=dir
				
	def donk_move(self,Fire,surface,flag):
		surface[self.x][self.y]=' '
		self.x = self.x + self.__donk_dir
		self.__donk_dir = -(self.__donk_dir)
		if self.__donk_dir==-1:
			Fire.createBall(self.x,self.y)
		if surface[self.x][self.y]!='P':
			surface[self.x][self.y]='D'
			
		if self.__donk_dir==1 and flag==0:
			surface[self.x+1][self.y]='O'
		return surface
	
	def donk_hits_player(self,surface):
		if surface[self.x][self.y]=='P':
			return -1
		return 1
