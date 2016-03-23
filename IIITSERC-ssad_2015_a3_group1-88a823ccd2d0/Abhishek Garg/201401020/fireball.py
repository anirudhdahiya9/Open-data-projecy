import copy
import random
from player import player
class fireball():
	def __init__(self,surface,surface_copy,width,height):
		self.__fireballs=[]
		self.surface=surface
		self.surface_copy=surface_copy
		self.__width=width
		self.__height=height
		self.fireballs_copy=[]
		self.flag=2
		#self.dir_list=[[0,0],[1,-1],[1,0],[1,1],[0,-1],[0,0],[0,1],[-1,-1],[-1,0],[-1,1]]
	
	def createBall(self,x,y):
		if self.surface[x][y]!='P':
			if self.flag==0:
				self.surface[x][y]='O'
				self.__fireballs.append([x,y,0,1,0])
		self.flag=(self.flag+1)%3
		
	def update_balls_direction(self):
		for x in self.__fireballs:
#			if (x[1]+1==width-1 or x[1]-1==0) and x[0]==height-2:
#				self.__fireballs.remove(x)	
			if self.surface_copy[x[0]+1][x[1]]=='H' and x[4]==0:
				x[2]=random.randint(0,1)
				if x[2]==1:
					x[3]=0
					x[4]=1
			elif self.surface_copy[x[0]+1][x[1]]==' ' and x[4]==0:
				x[2]=1
				x[3]=0
				x[4]=1
			elif self.surface_copy[x[0]+1][x[1]]=='x' and x[4]==1:
				x[4]=0
				x[2]=0
				x[3]=random.randint(0,1)
				if x[3]==0:
					x[3]=-1
			elif (x[1]+1==self.__width-1 or x[1]-1==0) and x[0]!=self.__height-2:
				x[3]=-x[3]

	def update_balls_location(self,surface):
		self.fireballs_copy=copy.deepcopy(self.__fireballs)   #finally fixed the buggy part
		for x in self.fireballs_copy:                       #now player can move any number of steps
			if x[0]==29 and (x[1]==1 or x[1]==28):
				if x in self.__fireballs:
					self.__fireballs.remove(x)
		self.update_balls_direction()
		for x in self.__fireballs:
#			print x[0], x[2]
#			print x[1], x[3]
			x[0]+=x[2]
			x[1]+=x[3]
			if surface[x[0]][x[1]]!='x' and surface[x[0]][x[1]]!='P' and surface[x[0]][x[1]]!='D':
				surface[x[0]][x[1]]='O'
		return surface
					
	def fireball_hits_player(self,surface):
		for x in self.__fireballs:
			if surface[x[0]][x[1]]=='P':
				return -1
		return 1
		
	def remove_fireballs(self):
		self.__fireballs=[]
		
	def check_for_swap(self,surface,player_dir):
		for x in self.fireballs_copy:
			if surface[x[0]][x[1]]=='P':
				if x[2]==-player_dir[0] and x[3]==-player_dir[1]:
					return -1
		return 1
