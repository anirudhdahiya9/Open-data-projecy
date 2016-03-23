import random

class coins():
	def __init__ (self,width,height):
		self.__width=width
		self.__height=height
		self.__coins_list=[]
		
	def generate_coins(self):
		self.__coins_list=[]
		tfwidth=(4*self.__width)/5
		for i in (10,18,26):
			i-=1
			temp=random.sample(range(2,tfwidth-2),3)
			for j in temp:
				self.__coins_list.append([i,j])
				
		for i in (6,14,22):
			i-=1
			temp=random.sample(range(self.__width-tfwidth+2,self.__width-2),3)
			for j in temp:
				self.__coins_list.append([i,j])
			
		i=self.__height-2
		temp=random.sample(range(2,self.__width-3),5)
		for j in temp:
			self.__coins_list.append([i,j])
			
			
	def place_coins(self,surface):
		for x in self.__coins_list:
			if surface[x[0]][x[1]]==' ':
				surface[x[0]][x[1]]='C'
		return surface
		
	def player_gets_a_coin(self,x,y):
		for i in self.__coins_list:
			if i[0]==x and i[1]==y:
				self.__coins_list.remove(i)
				return 1
		return -1
