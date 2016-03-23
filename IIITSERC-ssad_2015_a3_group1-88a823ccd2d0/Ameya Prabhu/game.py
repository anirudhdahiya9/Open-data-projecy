########################################
#      MADE BY : AMEYA PRABHU          #
#      201402004    CSD                #   
########################################

import getboard
import people
import random
import sys
import os
import time
import copy
from random import randint

''' source for getch : http://code.activestate.com/recipes/577977-get-single-keypress/ '''
try:
    import tty, termios
except ImportError:
    try:
        import msvcrt
    except ImportError:
        raise ImportError('getch not available')
    else:
        getch = msvcrt.getch
else:
    def getch():
        fd = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd)
        try:
            tty.setraw(fd)
            ch = sys.stdin.read(1)
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
        return ch
''' cited code ends '''

class game():
    #Start Donkey-Kong!
    def __init__(self,x,y,lives,points,level):
        #Set the Board Size
        self.MAXX = x
        self.MAXY = y

        #Get all the main information
        self.levelno=level
        self.b1 = getboard.board(self.MAXX ,self.MAXY)

        #We have 3 layers of the board - orig_board is the base layer, 
        #upd_board is the dynamic layer on top
        #and coins_board is the coins generated on the board
        self.orig_board = self.b1.show()
        self.upd_board = copy.deepcopy(self.orig_board)
        self.coins_board = copy.deepcopy(self.orig_board)

        #Make the coins board
        for i in xrange(self.MAXY):
            for j in xrange(self.MAXX):
                if self.orig_board[i-1][j]=='X' and randint(1,1000)%10==0:
                    self.coins_board[i][j]='C'

        #Initiliaze Normal Content - Player locations, donkey Location, etc
        # for simple extension of the game
        self.b1.startloc()
        self.p1 = people.player()
        self.p1.lives=lives
        self.p1.points=points
        self.d1 = people.donkey()
        self.loc = []
        [self.p1.y,self.p1.x] = self.b1.pos_per
        [self.destx,self.desty] = self.b1.pos_pri
        [self.d1.y,self.d1.x] = self.b1.pos_don
        self.donkey_dir = randint(0,100)%2
        self.fire=False

    def show(self):
        #Generate the Updated Board
        self.upd_board=copy.deepcopy(self.orig_board)
        self.upd_board[self.p1.y][self.p1.x]='P'
        self.upd_board[self.d1.y][self.d1.x]='D'
        
        for i in self.loc:
            self.upd_board[i[1]][i[0]]='O'
        
        #Print out the updated board with all the colours.
        for i in xrange(self.MAXY):
            self.s=""
            
            for j in xrange( self.MAXX ):
                if(self.upd_board[self.MAXY-i-1][self.MAXX-j-1]=='X'):
                    self.s+=('\033[1m'+'\033[91m' + 'X' + '\033[0m')
                elif(self.upd_board[self.MAXY-i-1][self.MAXX-j-1]=='P'):
                    self.s+=('\033[1m'+'\033[92m' + 'P' + '\033[0m')
                elif(self.upd_board[self.MAXY-i-1][self.MAXX-j-1]=='O'):
                    self.s+=('\033[1m'+'\033[95m' + 'O' + '\033[0m')
                elif(self.upd_board[self.MAXY-i-1][self.MAXX-j-1]=='D'):
                    self.s+=('\033[1m'+'\033[94m' + 'D' + '\033[0m')
                elif(self.upd_board[self.MAXY-i-1][self.MAXX-j-1]=='H'):
                    self.s+=('\033[1m'+'\033[96m' + 'H' + '\033[0m') 
                elif(self.coins_board[self.MAXY-i-1][self.MAXX-j-1]=='C'):
                    self.s+=('\033[1m'+'\033[93m' + 'C' + '\033[0m')
                else: 
                    self.s+=self.upd_board[self.MAXY-i-1][self.MAXX-j-1]
            
            print self.s

        #Print the Text to be printed Below
        print "POINTS "+str(self.p1.points)+" LIVES "+str(self.p1.lives)+" LEVEL "+str(self.levelno)

    def get_input(self):
        #This is the function we use for the input of a character
        self.inp = getch()
        print self.inp

        #Respect the PEP-8 Standards and try to follow it
        if (self.orig_board[self.p1.y][self.p1.x]!='H' and \
        self.orig_board[self.p1.y-1][self.p1.x]!='X' and \
        self.orig_board[self.p1.y-1][self.p1.x]!='H'):
            self.p1.fall()
            self.p1.fall()
            self.p1.fall()
            self.p1.fall()

        #To Quit - Press q 
        if self.inp=='q':
            sys.exit()

        #To climb - Press W. Implemented by combining various functions thrice 
        if self.inp == 'w':
            for d in xrange(3):
                self.p1.climb_up()
                self.show()
                time.sleep(0.05)
                os.system("clear")
                self.set_player_var()

        #To go down - Press S.
        if self.inp == 's':
            self.p1.climb_down()

        #To go right - Press d
        if self.inp == 'd':
            self.p1.move_right()

        #To go left - Press a
        if self.inp == 'a':
            self.p1.move_left()

        #IMPROVEMENT- To jump left - Press e and not space. 
        #It refreshes the screen multiple times 
        if self.inp == 'e':
            #Jump twice up-left
            for d in xrange(2):
                self.p1.move_up_left()
                self.show()
                time.sleep(0.05)
                os.system("clear")
                self.set_player_var()
            
            #Jump twice down-left
            for d in xrange(2):
                self.p1.move_down_left()
                self.show()
                time.sleep(0.05)
                os.system("clear")
                self.set_player_var()
                self.show()

        #IMPROVEMENT - To jump right - Press r and not space.
        #It refreshes the screen multiple times
        if self.inp == 'r' :
            #Jump twice up-right
            for d in xrange(2):
                self.p1.move_up_right()
                self.show()
                time.sleep(0.05)
                os.system("clear")
                self.set_player_var()
            
            #Jump twice down-right
            for d in xrange(2):
                self.p1.move_down_right()
                self.show()
                time.sleep(0.05)
                os.system("clear")
                self.set_player_var()
                self.show()

    def set_player_var(self):
        #Set Various variables to change them in their functions as 
        #the original variables are not acessible due to encapsulation.
        
        #Checks Floor
        if self.b1.a[self.p1.y-1][self.p1.x]=='X':
            self.set6=1
        else:
            self.set6=0

        #Checks Stairs
        if self.orig_board[self.p1.y][self.p1.x]=='H':
            self.set1=1
        else:
            self.set1=0

        #Checks Collision with Fireball
        #Depricated. No longer used
        if self.b1.a[self.p1.y][self.p1.x]=='O':
            self.set2=1
        else:
            self.set2=0

        #Checks collection of coin
        if self.b1.a[self.p1.y][self.p1.x]=='C':
            self.set3=1
        else:
            self.set3=0

        #Checks wall on the right
        if self.b1.a[self.p1.y][self.p1.x-1]=='X':
            self.set4=1
        else:
            self.set4=0

        #Checks wall on the left
        if self.b1.a[self.p1.y][self.p1.x+1]=='X':
            self.set5=1
        else:
            self.set5=0
        
        #Checks for collision with all the fireballs
        for i in self.loc:
            if i==[self.p1.x,self.p1.y]:
                self.fire=True
                break
            else:
                self.fire=False

        #Collects the coins
        if self.coins_board[self.p1.y][self.p1.x]=='C':
            self.coin=True
            self.coins_board[self.p1.y][self.p1.x]=' '
        else:
            self.coin=False

        #Send all variables to their respective classes.
        self.p1.setcondition(self.coin,self.fire)
        self.p1.setvar(self.p1.x,self.p1.y,self.set6,self.set1,self.set4,self.set5)

    def set_donkey_var(self):

        #Set similar variables for the donkey to automate his behaviour to move to right.
        try:
            if((self.b1.a[self.d1.y-1][self.d1.x-1]!='X' \
            and self.b1.a[self.d1.y-1][self.d1.x-1]!='H') \
            or self.b1.a[self.d1.y][self.d1.x-1]=='X'):
                self.set1=False
            else:
                self.set1=True
        except:
        #In some cases, there is an exception which gets thrown. So, this is the fix.
                self.set1=False

        #Similar setting to be adopted for allowing the donkey to move left
        try:
        #Same code except x changed.
            if (self.b1.a[self.d1.y-1][self.d1.x+1]!='X' \
            and self.b1.a[self.d1.y-1][self.d1.x+1]!='H') \
            or self.b1.a[self.d1.y][self.d1.x+1]=='X':
                self.set2=False
            else:
                self.set2=True
        except:
            self.set2=False

        #Copy the variables to its respectable class as encapsulation is important.
        self.d1.setvar_donkey(self.set2,self.set1)

        #Reset the variables.
        self.set3=True
        self.set1=True
        self.set2=True

        #Set the variables for the fireballs array which each contains a fireball.
        for i in self.d1.fireballs:
            #Same code. Read above.
            try:
                if (self.b1.a[i.y-1][i.x-1]!='X' and self.b1.a[i.y-1][i.x-1]!='H') or self.b1.a[i.y][i.x-1]=='X':
                    self.set1=True
                else:
                    self.set1=False
            except:
                self.set1=True

            #Same Again.    
            try:
                if (self.b1.a[i.y-1][i.x+1]!='X' and self.b1.a[i.y-1][i.x+1]!='H') or self.b1.a[i.y][i.x+1]=='X':
                    self.set2=True
                else:
                    self.set2=False
            except:
                self.set2=True

            #Just checking if there is floor below.
            if (self.b1.a[i.y-1][i.x]!='X'):
                self.set3=False
            else:
                self.set3=True

            #Transfer to its respective class
            self.d1.setvarfireball(i,self.set3,False,self.set1,self.set2)

        #Move the Donkey!
        self.loc=self.d1.move()

        #Try to emit a fireball!
        self.d1.emitfireball()

    #End the Game ! Next Iteration Begin!
    def end_game(self):
        #Game Ends as Princess is reached!
        if self.upd_board[self.p1.y][self.p1.x]=='Q':
            self.p1.points+=50
            self.levelno+=1
            return True
        else:
        #Game ends due to collision with fireball
            return self.fire

    #Helper Functions
    def get_life(self):
        return self.p1.lives

    def get_levelno(self):
        return self.levelno

    def get_coins(self):
        return self.p1.points

#The main function is here!
if __name__ == "__main__":
    
    #Some Globals which are constants
    lives=3
    points=0
    level=1
    while(1):
        
        #DYNAMICEALLY CHANGE THE BOARD SIZE! NOTE: PLEASE CONSTRAIN THE Y TO BE 2(MOD4).
        g= game(80,30,lives,points,level)

        #The main game loop.
        while g.end_game()==False:
            #Refresh the window
            os.system("clear")

            #Call all the functions in order
            g.show()
            g.set_player_var()
            g.set_donkey_var()
            g.get_input()
            lives=g.get_life()
            points=g.get_coins()

        #Update the level
        level=g.get_levelno()

        #If lives ==0. Game over !
        if lives<=0:
            break
    print "-------------------GAME OVER-------------------"
    