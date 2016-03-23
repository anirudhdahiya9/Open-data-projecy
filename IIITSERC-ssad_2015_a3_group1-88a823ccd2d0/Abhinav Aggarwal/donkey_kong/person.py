from ball import *

class Person:
    '''The characters of the game'''

    def __init__(self):                
        self._onground=1                

    def get_position(self):
        '''Returns the position of the person as a tuple of its (y,x) coordinates wrt top-left corner as (0,0)'''
        
        return (self._y,self._x)
    
    def set_position(self,y,x):
        '''Sets the position coordinates of the person'''

        self._x=x
        self._y=y

    def move_left(self,S):
        '''Moves the person left'''


        '''Changing the current block on which the player is standing'''
        if self.onladder==1:
            S.MAP[self._y][self._x]='H'
            self.onladder=0
        else:
            S.MAP[self._y][self._x]=' '
        
        '''Taking required action depending upon the next block'''
        if S.MAP[self._y][self._x-1]=='H':
            self.onladder=1
        elif S.MAP[self._y][self._x-1]=='C':
            self.collect_coin(S)
            S.fixedMAP[self._y][self._x-1]=' '
        
        '''Changing the next block on which step is to be taken'''
        self._x-=1
        S.MAP[self._y][self._x]='P'
        
    def move_right(self,S):
        '''Moves the person right'''
        
        '''Changing the current block on which the player is standing'''
        if self.onladder==1:
            S.MAP[self._y][self._x]='H'
            self.onladder=0
        else:
            S.MAP[self._y][self._x]=' '
        
        '''Taking required action depending upon the next block'''
        if S.MAP[self._y][self._x+1]=='H':
            self.onladder=1
        elif S.MAP[self._y][self._x+1]=='C':
            self.collect_coin(S)
            S.fixedMAP[self._y][self._x+1]=' '
        
        '''Changing the next block on which step is to be taken'''
        self._x+=1
        S.MAP[self._y][self._x]='P'

    def climbup(self,S):
        '''Person Climbs one step up the ladder'''

        S.MAP[self._y][self._x]='H'
        self._y-=1
        self.onground=0
        if S.fixedMAP[self._y][self._x]==' ':
            self.onladder=0
            self.onground=1
        elif S.fixedMAP[self._y][self._x]=='C':
            self.collect_coin(S)
            S.fixedMAP[self._y][self._x]=' '
            self.onladder=0
            self.onground=1
        S.MAP[self._y][self._x]='P'
      
    def climbdown(self,S):
        '''Person Climbs one step down the ladder'''

        S.MAP[self._y][self._x]='H'
        self._y+=1
        self.onground=0
        if S.fixedMAP[self._y+1][self._x]=='X':
            self.onground=1 
        S.MAP[self._y][self._x]='P'
    
    def jump(self,S,direction):
        '''Person jumps one step up/down depending upon the direction'''

        if direction=="up":
            if self.onladder==1:
                S.MAP[self._y][self._x]='H'
                self.onladder=0
            else:
                S.MAP[self._y][self._x]=' '
            self._y-=1
            S.MAP[self._y][self._x]='P'
        elif direction=="down":
            if self.onladder==1:
                S.MAP[self._y][self._x]='H'
                self.onladder=0
            else:
                S.MAP[self._y][self._x]=' '
            self._y+=1
            S.MAP[self._y][self._x]='P'
        if S.fixedMAP[self._y][self._x]=='H':
            self.onladder=1
            
    def jump_horizontal(self,S):
        '''Person takes one step left/right during the jump,depending upon the horizontal direction of motion'''
        
        if self.jump_hordir==1:
            if S.MAP[self._y][self._x+1]!='X' and S.MAP[self._y][self._x+1]!='H':
                if self.onladder==1:
                    S.MAP[self._y][self._x]='H'
                    self.onladder=0
                else:
                    S.MAP[self._y][self._x]=' '
                self._x+=1
                S.MAP[self._y][self._x]='P'
        elif self.jump_hordir==-1:
            if S.MAP[self._y][self._x-1]!='X' and S.MAP[self._y][self._x-1]!='H':
                if self.onladder==1:
                    S.MAP[self._y][self._x]='H'
                    self.onladder=0
                else:
                    S.MAP[self._y][self._x]=' '
                self._x-=1
                S.MAP[self._y][self._x]='P'
        if S.fixedMAP[self._y][self._x]=='H':
            self.onladder=1
        if S.fixedMAP[self._y][self._x]=='C':
            self.collect_coin(S)
            S.fixedMAP[self._y][self._x+1]=' '

class Player(Person):
    '''The player of the game'''

    def __init__(self):
        self._x=4
        self._y=24
        self.onground=1
        self.onladder=0
        self.inair=0
        self.jumpstage=0
        self.jump_hordir=0  # 0 vertical, 1 right, -1 left
        self.lives=3

    def collect_coin(self,S):
        '''+5 coin for the person'''

        S.update_score(5)

    def reset(self,S):
        '''Kills the person and spawns it at the start'''

        S.MAP[self._y][self._x]=S.fixedMAP[self._y][self._x]
        self._x=4
        self._y=24
        S.MAP[self._y][self._x]='P'
        self.onladder=0
        self.onground=1
        self.inair=0
 
class Donkey(Person):
    '''The donkey of the game'''

    def __init__(self):
        
        self._y=4
        self._x=2
        self._RTEXTREME=12
        self.LTEXTREME=2
        self.direction=1    # 0=rest,1=right,-1=left
        self.isball=1       # 1 if ball in hand , else 0
        self.balls_active=0
    
    def get_position(self):
        '''Return the position of the donkey as a tuple of its (y,x) coordinates wrt top left as (0,0)'''
        
        return (self._y,self._x)

    def drop_ball(self,S,Balls):
        '''Makes the Donkey drop the fireball at this coordinate'''

        Balls.append(Fireball(S,self.balls_active+1,self._x+1,self._y))
        self._direction=-1

    def move(self,S):
        '''Donkey takes one step according to its present state'''

        S.MAP[self._y][self._x]=' '
        self._x+=self.direction
        S.MAP[self._y][self._x]='D'

