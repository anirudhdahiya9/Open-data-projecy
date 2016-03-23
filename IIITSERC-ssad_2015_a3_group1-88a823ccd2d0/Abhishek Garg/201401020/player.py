#player
from person import Person
class player(Person):
	def __init__(self,surface,x,y):
		self.__surface=surface
		Person.__init__(self,x,y)
		self.__start_x=x
		self.__start_y=y
#		self.__pos_x=x
#		self.__pos_y=y
		self.prev_dir=[0,0]
		self.cur_dir=[0,0]
		self.__surface[x][y]='P'
		
	def bring_to_ground(self,surface,x,y):
		while surface[x+1][y]==' ':
			x+=1
		return x
		
	def move(self,surface,dir):
		self.prev_dir=self.cur_dir
		if dir=='w':
			if surface[self.x][self.y]=='H' and surface[self.x-1][self.y]!='x':				
				self.x-=1
				self.cur_dir=[-1,0]
		if dir=='s':
			if surface[self.x+1][self.y]=='H':
				self.x+=1
				self.cur_dir=[1,0]
		if dir=='a':
			if surface[self.x][self.y-1]!='x':
				self.y-=1
				self.cur_dir=[0,-1]
				self.x=self.bring_to_ground(surface,self.x,self.y)
		if dir=='d':
			if surface[self.x][self.y+1]!='x':
				self.y+=1
				self.cur_dir=[0,1]
				self.x=self.bring_to_ground(surface,self.x,self.y)

		surface[self.x][self.y]='P'             #update position of p on surface
		return surface
	
	def queen_captured(self,queen_x,queen_y):
		if self.x==queen_x and self.y==queen_y:
			return True
		return False
		
	def get_pos(self):
		return [self.x,self.y]
		
	def reset_player_pos(self,surface):
		surface[self.x][self.y]=' '
		self.x=self.__start_x
		self.y=self.__start_y
		surface[self.x][self.y]='P'
		return surface

			
