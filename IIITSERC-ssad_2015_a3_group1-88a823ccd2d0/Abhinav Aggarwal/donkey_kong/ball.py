class Fireball:
    '''The fireballs'''

    def __init__(self,S,ID,x_init,y_init):
        
        self._x=x_init
        self._y=y_init
        S.MAP[self._y][self._x]='O'
        self._id=ID
        self.direction=1 #1 right, -1 left ,0 falling down
    
    def get_position(self):
        '''Return the position of the fireball as (y,x) tuple'''

        return (self._y,self._x)

    def fall_down(self,S):
        '''Makes the fireball fall down'''

        S.MAP[self._y][self._x]=S.fixedMAP[self._y][self._x]
        self._y+=1
        S.MAP[self._y][self._x]='O'

    def move_lr(self,S):
        '''To move the fireball left or right'''
        
        if self.check_wall(S)==1:
            self.switch_direction()   
        S.MAP[self._y][self._x]=S.fixedMAP[self._y][self._x]
        self._x+=self.direction
        S.MAP[self._y][self._x]='O'
    
    def switch_direction(self):
        '''Switches the direction of the fireball'''

        if self.direction==1:
            self.direction=-1
        elif self.direction==-1:
            self.direction=1

    def check_wall(self,S):
        '''Checks if the fireball is about to collide with a wall'''

        if S.fixedMAP[self._y][self._x+self.direction]=='X':
            return 1
        else:
            return 0
    
    def on_ground(self,S):
        '''Checks if the fireball is on the ground'''
        
        if S.fixedMAP[self._y+1][self._x]=='X':
            return 1
        else:
            return 0

    def on_ladder(self,S):
        '''Checks if the fireball is on a ladder'''

        if S.fixedMAP[self._y+1][self._x]=='H':
            return 1
        else:
            return 0
