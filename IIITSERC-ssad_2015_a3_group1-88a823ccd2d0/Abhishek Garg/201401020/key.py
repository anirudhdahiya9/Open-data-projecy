class key():
	def __init__(self,width,height,x,y):
		self.__width=width
		self.__height=height
		self.x=x
		self.y=y
		
	def change_level(self,surface_copy,level):
		if level==2 or level==3:
			surface_copy[1][6]='x'
			surface_copy[2][6]='x'
			surface_copy[1][9]='x'
			surface_copy[2][9]='x'
			surface_copy[self.x][self.y]='K'
			return surface_copy
		
	def player_gets_key(self,surface):
		if surface[self.x][self.y]=='P':
			return True
		return False
		
	def restore_surface_copy(self,surface_copy):
		surface_copy[1][6]=' '
		surface_copy[2][6]=' '
		surface_copy[1][9]=' '
		surface_copy[2][9]=' '
		surface_copy[self.x][self.y]=' '
		return surface_copy
		
