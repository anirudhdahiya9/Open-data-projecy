from random import randint

#The board Class. Capable of creating dynamic boards of any size!
class board:
    def __init__(self,x,y):
        #Initilialize the board variables
        self.MAXX = x
        self.MAXY = y
        self.a = []
        self.stair = []
        self.create()
    
    def create(self):
        #Create the air
        for i in xrange(self.MAXY):
            tmp = []
            for j in xrange(self.MAXX):
                tmp.append(' ')
            self.a.append(tmp)
        
        #Create the borders
        for i in xrange(self.MAXX):
            self.a[0][i] = 'X'
            self.a[self.MAXY-1][i] = 'X'
        for i in xrange(self.MAXY):
            self.a[i][0] = 'X'
            self.a[i][self.MAXX-1] = 'X'
    
        #Create the locations of the stairs
        for i in xrange(((self.MAXY-2)//4)-1):
            self.stair.append(randint(2,self.MAXX-2))
    
        #Create the X co-ordinate of the princess
        self.ps = randint(2,self.MAXX-3)
        self.stair.append(self.ps)

        #Create the path between the two stairs - 
        #one coming from below and one joining above
        for i in xrange(((self.MAXY-2)//4)-1):
            self.lr = randint(1,self.MAXX//5)
            self.ll = randint(3,self.MAXX//5)
            for j in xrange(abs(self.stair[i+1]-self.stair[i])+1+self.lr+self.ll):
                self.a[4*i+4][min(max(0,(min(self.stair[i],self.stair[i+1])-self.ll))+j,self.MAXX-1)] = 'X'  
        
        #Create the box around the princess
        self.a[self.MAXY-2][self.ps-2] = 'X'
        self.a[self.MAXY-2][self.ps+2] = 'X'
        for i in xrange(5):
            self.a[self.MAXY-3][self.ps-2+i] = 'X'
    
        #Create the ladders from the ladder points to 4 stairs below
        for i in xrange((self.MAXY-2)//4):
            for j in xrange(4):
                self.a[4*i+4-j][self.stair[i]] = 'H'

        #Create the Princess Ladder
        self.a[self.MAXY-3][self.ps] = 'H'

        #Over-write the last ladder piece with the princess.  
        self.a[self.MAXY-2][self.ps] = 'Q'

        #Place the Donkey at the left-most thing.
        for i in xrange(self.MAXX-1):
            i = self.MAXX-2-i
            if self.a[self.MAXY-6][i] == 'X':
                self.pos_don = [self.MAXY-5,i]
                break

    #Return the created board.
    def show(self):
        return self.a[:][:]

    #Return the starting locations of the player and the donkey.
    def startloc(self):
        self.pos_per = [1,self.MAXX-2]
        self.pos_pri = [self.MAXY-2,self.ps]
        

