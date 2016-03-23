from gen import *
class Board(object):
    def __init__(self, length, breadth):
        self.length=length
        self.breadth=breadth
        self.Matrix = [[''] for x in range(self.length)]

    def create_board(self):
        for i in range(self.length):
            for j in range(self.breadth):
                self.Matrix[i] += ' '
                if(i==0 or j==0 or j==89 or i==29):
                    self.Matrix[i][j]='X'
                else:
                    self.Matrix[i][j]=' '

        self.create_wall(5,0,75)
        self.create_wall(10,25,89)
        self.create_wall(14,10,85)
        self.create_wall(19,0,89)
        self.create_wall(24,0,89)
        self.create_wall(2,12,28)

        self.create_ladder(19,30,5)
        self.create_ladder(14,57,5)
        self.create_ladder(24,68,5)
        self.create_ladder(10,28,4)
        self.create_ladder(5,70,5)
        self.create_ladder(2,25,3)

        self.create_broken_ladder(19,70,5)
        self.create_broken_ladder(5,34,5)

        """self.print_board()"""


    def create_wall(self,height,wall_left,wall_right):
        for i in range (self.length):
                if height == i:
                    j=wall_left
                    while j<=wall_right:
                        self.Matrix[i][j] = 'X'
                        j=j+1;

    def create_ladder(self,ladder_x, ladder_y, ladder_height):
        for i in range (self.breadth):
            if i==ladder_x:
                for j in range (self.breadth):
                    if j==ladder_y:
                        for k in range (ladder_height):
                            self.Matrix[i+k][j]='H'

    def create_broken_ladder(self,ladder_x, ladder_y, ladder_height):
        for i in range (self.breadth):
            if i==ladder_x:
                for j in range (self.breadth):
                    if j==ladder_y:
                        for k in range (ladder_height):
                            if k==2:
                                continue
                            self.Matrix[i+k][j]='H'

    def get_Matrix(self):
        return self.Matrix
