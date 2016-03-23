class set_screen():
	def __init__(self,surface,width,height):
		self.surface=surface
		self.width=width
		self.height=height
		tfwidth=(4*self.width)/5

		for i in range(self.width):                         #walls
			self.surface[0][i]='x'
			self.surface[self.height-1][i]='x'
		for i in range(self.height):
			self.surface[i][0]='x'
			self.surface[i][self.width-1]='x'

		for i in range(6,12):
			self.surface[3][i]='x'

		for i in(10,18,26):
			for j in range(tfwidth):
				self.surface[i][j]='x'
		for i in (6,14,22):
			for j in range(self.width-tfwidth,self.width):
				self.surface[i][j]='x'

		for i in range(3,6):                  #stairs
			self.surface[i][10]='H'
		for i in range(6,10):
			self.surface[i][20]='H'
#			self.surface[i][14]='H'
		self.surface[9][14]='H'
		self.surface[6][14]='H'
		for i in range(10,14):
			self.surface[i][8]='H'
		self.surface[12][11]='H'
		self.surface[13][11]='H'
		for i in range(14,18):
			self.surface[i][20]='H'
		for i in range(18,22):
			self.surface[i][10]='H'
		self.surface[18][3]='H'
		self.surface[19][3]='H'
		self.surface[20][3]='H'
		for i in range(22,26):
			self.surface[i][22]='H'
			self.surface[i][16]='H'
		self.surface[24][16]=' '
		for i in range(26,30):
			self.surface[i][14]='H'
			
			
			
#		for i in range(1,self.height-1):
#			surface[i][7]='H'
