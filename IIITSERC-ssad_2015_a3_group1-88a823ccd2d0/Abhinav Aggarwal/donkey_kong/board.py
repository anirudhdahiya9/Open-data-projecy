class Screen:
    '''The display screen of the game'''
    
    def __init__(self,score,lvl):
        
        self._score=score
        self._level=lvl
        self.MAP=[]
        self.generateMAP() 
    
    def update_score(self,n):
        '''Updates the score of the player'''

        self._score+=n

    def get_score(self):
        '''Returns the score of the player'''

        return self._score

    def generateMAP(self): 
        '''Loads the map from the file'''

        self.MAP=[]
        self.fixedMAP=[]
        i=-1
        f=open('MAP'+str(self._level)+'.txt','r')
        for line in f.readlines():
            i+=1
            self.MAP.append([])
            self.fixedMAP.append([])
            for char in line:
                if char!='\n':
                    self.MAP[i].append(char)
                    self.fixedMAP[i].append(char)

    def print_scr(self,P):
        '''Prints the map on the screen'''

        for line in self.MAP:
            for char in line:
                if char=='X':
                    print ('\033[1m'+'\033[95m' + 'X' + '\033[0m'),
                elif char=='O':
                    print ('\033[1m'+'\033[91m' + 'O' + '\033[0m'),
                elif char=='C':
                    print ('\033[1m'+'\033[93m' + 'C' + '\033[0m'),
                elif char=='H':
                    print ('\033[1m'+'\033[95m' + 'H' + '\033[0m'),
                elif char=='P':
                    print ('\033[1m'+'\033[36m' + 'P' + '\033[0m'),
                elif char=='Q':
                    print ('\033[1m'+'\033[92m' + 'Q' + '\033[0m'),
                elif char=='D':
                    print ('\033[1m'+'\033[94m' + 'D' + '\033[0m'),
                else:
                    print char,
            print ""
        s="LEVEL: "+str(self._level)+"      "+"SCORE: "+str(self._score)+"      "+"LIVES: "+str(P.lives)
        print '\033[1m'+s.center(180)+'\033[0m'

    def updatech(self,x,y,ch):
        '''Updates a character on the map'''

        self.MAP[x][y]=ch

    


