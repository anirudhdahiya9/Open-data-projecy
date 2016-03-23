from person import *
from Board import *
from gen import *
import time
class Player(Person, Board):
    def __init__(self,x,y,score):
        Person.__init__(self, "Player 1",28,2)
        Board.__init__(self,30,90)
        self.x=x
        self.y=y
        self.backup = ' '
        self.total_coins = score
        self.life = life


        self.prev_input = 'd'


    def collectCoin(self):
        self.total_coins+=1
        return self.total_coins

    def move_backward(self, Matrix):
        if (checkWall(self.x, self.y-1,Matrix)):
            pass

        else:
            if( self.x ==1 or self.x == 4 or self.x ==9 or self.x ==13 or
                self.x == 18 or self.x == 23 or self.x == 28 ):
                Matrix[self.x][self.y] = self.backup
                self.backup = Matrix[self.x][self.y - 1]

                if Matrix[self.x][self.y - 1] == 'C':
                    self.total_coins = self.collectCoin()
                    self.backup = ' '

                self.y -= 1
                Matrix[self.x][self.y] = 'P'
        return self.total_coins


    def move_forward(self, Matrix):
        if (checkWall(self.x,self.y+1,Matrix)):
            pass

        else:
            if( self.x ==1 or self.x == 4 or self.x ==9 or self.x ==13 or
                self.x == 18 or self.x == 23 or self.x == 28 ):
                Matrix[self.x][self.y] = self.backup
                self.backup = Matrix[self.x][self.y + 1]

                if Matrix[self.x][self.y + 1] == 'C':
                    self.total_coins= self.collectCoin()
                    self.backup = ' '

                self.y += 1
                Matrix[self.x][self.y] = 'P'
        return self.total_coins

    def ascend_ladder(self, Matrix):

        if self.backup == 'H':
            if checkWall(self.x+1,self.y,Matrix) and Matrix[self.x - 1][self.y] == 'H' and Matrix[self.x - 2][self.y] == 'H':
                Matrix[self.x][self.y] = 'H'
                Matrix[self.x - 1][self.y] = 'P'
                self.x = self.x - 1
            elif Matrix[self.x + 1][self.y] == 'H':
                if Matrix[self.x - 1][self.y] == 'H':
                    Matrix[self.x][self.y] = 'H'
                    Matrix[self.x - 1][self.y] = 'P'

                    self.x -= 1
                elif Matrix[self.x - 1][self.y] != 'H':
                    self.backup = Matrix[self.x - 1][self.y]
                    Matrix[self.x][self.y] = 'H'
                    Matrix[self.x - 1][self.y] = 'P'
                    self.x -= 1
        return self.total_coins

    def descend_ladder(self, Matrix):
        if self.backup == ' ' and Matrix[self.x+3][self.y] == 'H':
            Matrix[self.x][self.y] = self.backup
            self.backup = Matrix[self.x + 1][self.y]
            Matrix[self.x + 1][self.y] = 'P'
            self.x += 1
        elif self.backup == 'H' and Matrix[self.x + 1][self.y] != 'X':
            Matrix[self.x][self.y] = self.backup
            self.backup = Matrix[self.x + 1][self.y]
            Matrix[self.x + 1][self.y] = 'P'
            self.x += 1
        return self.total_coins


    def jump(self,Matrix,donkey):
        if (self.prev_input == 'd'):
            if(Matrix[self.x][self.y+1] != 'X' and
                Matrix[self.x][self.y+2] != 'X' and
                Matrix[self.x][self.y+3] != 'X' and
                Matrix[self.x][self.y+4] != 'X' and
                Matrix[self.x][self.y+5] != 'X' and
                Matrix[self.x][self.y+6] != 'X' and
                Matrix[self.x][self.y+7] != 'X' and
                Matrix[self.x][self.y+8] != 'X'):

                Matrix[self.x][self.y] = self.backup
                self.backup = Matrix[self.x-1][self.y+2]
                Matrix[self.x-1][self.y+2] = 'P'
                self.x-=1
                self.y+=2
                time.sleep(0.3)
                os.system('clear')
                self.print_player(Matrix)
                print "SCORE : ",
                print self.total_coins * 5,
                print "\t\t\t\t\t\t\t\t\tLife : ",
                print self.life

                Matrix[self.x][self.y] = self.backup
                self.backup = Matrix[self.x-1][self.y+2]
                Matrix[self.x-1][self.y+2] = 'P'
                self.x-=1
                self.y+=2
                time.sleep(0.3)
                os.system('clear')
                self.print_player(Matrix)
                print "SCORE : ",
                print self.total_coins * 5,
                print "\t\t\t\t\t\t\t\t\tLife : ",
                print self.life

                Matrix[self.x][self.y] = self.backup
                self.backup = Matrix[self.x+1][self.y+2]
                Matrix[self.x+1][self.y+2] = 'P'
                self.x+=1
                self.y+=2
                time.sleep(0.3)
                os.system('clear')
                self.print_player(Matrix)
                print "SCORE : ",
                print self.total_coins * 5,
                print "\t\t\t\t\t\t\t\t\tLife : ",
                print self.life
                #print it
                Matrix[self.x][self.y] = self.backup
                self.backup = Matrix[self.x+1][self.y+2]
                Matrix[self.x+1][self.y+2] = 'P'
                self.x+=1
                self.y+=2
                time.sleep(0.3)
                os.system('clear')
                self.print_player(Matrix)
                print "SCORE : ",
                print self.total_coins * 5,
                print "\t\t\t\t\t\t\t\t\tLife : ",
                print self.life


        elif(self.prev_input == 'a'):
            if(Matrix[self.x][self.y-1] != 'X' and
                Matrix[self.x][self.y-2] != 'X' and
                Matrix[self.x][self.y-3] != 'X' and
                Matrix[self.x][self.y-4] != 'X' and
                Matrix[self.x][self.y-5] != 'X' and
                Matrix[self.x][self.y-6] != 'X' and
                Matrix[self.x][self.y-7] != 'X' and
                Matrix[self.x][self.y-8] != 'X'):

                Matrix[self.x][self.y] = self.backup
                self.backup = Matrix[self.x-1][self.y-2]
                Matrix[self.x-1][self.y-2] = 'P'
                self.x-=1
                self.y-=2
                time.sleep(0.3)
                os.system('clear')
                self.print_player(Matrix)
                print "SCORE : ",
                print self.total_coins * 5,
                print "\t\t\t\t\t\t\t\t\tLife : ",
                print self.life

                Matrix[self.x][self.y] = self.backup
                self.backup = Matrix[self.x-1][self.y-2]
                Matrix[self.x-1][self.y-2] = 'P'
                self.x-=1
                self.y-=2
                time.sleep(0.3)
                os.system('clear')
                self.print_player(Matrix)
                print "SCORE : ",
                print self.total_coins * 5,
                print "\t\t\t\t\t\t\t\t\tLife : ",
                print self.life

                Matrix[self.x][self.y] = self.backup
                self.backup = Matrix[self.x+1][self.y-2]
                Matrix[self.x+1][self.y-2] = 'P'
                self.x+=1
                self.y-=2
                time.sleep(0.3)
                os.system('clear')
                self.print_player(Matrix)
                print "SCORE : ",
                print self.total_coins * 5,
                print "\t\t\t\t\t\t\t\t\tLife : ",
                print self.life

                Matrix[self.x][self.y] = self.backup
                self.backup = Matrix[self.x+1][self.y-2]
                Matrix[self.x+1][self.y-2] = 'P'
                self.x+=1
                self.y-=2
                time.sleep(0.3)
                os.system('clear')
                self.print_player(Matrix)
                print "SCORE : ",
                print self.total_coins * 5,
                print "\t\t\t\t\t\t\t\t\tLife : ",
                print self.life
        else:
            pass

    def checkCollision(self, position, Matrix):
        if self.x == position[0] and self.y-1 == position[1] :
            flag=1
            return flag

        elif self.x == position[0] and self.y + 1 == position[1] :
            flag=1
            return flag

        elif self.x == position[0] and self.y-2 == position[1] :
            flag=1
            return flag

        elif self.x == position[0] and self.y + 2 == position[1] :
            flag=1
            return flag

        elif self.x == position[0] and self.y  == position[1] :
            flag=1
            return flag

        elif self.y ==30 or self.y == 57 or self.y == 68 or self.y == 28 or self.y == 70 or self.y == 25 :
            if (self.y== position[1]):
                if self.x-1== position[0]:
                    flag=1
                    return flag

                elif self.x+1 == position[0] :
                    flag=1
                    return flag

                elif self.x-2 == position[0] :
                    flag=1
                    return flag

                elif self.x+2 == position[0]:
                    flag=1
                    return flag

                elif self.x == position[0]:
                    flag=1
                    return flag

        else:
            pass

    def collision_donkey(self, position, Matrix):
        if(self.x == position [0]):
            if(self.y == position[1] or self.y + 1== position[1] or self.y+2== position[1] or self.y-1 == position[1] or self.y-2 == position[1]):
                flag=1
                return flag


    def fall(self, position, Matrix):
        self.x = position[0]
        self.y = position[1]
        for i in range (4):
            if (Matrix[self.x+1][self.y] == ' '):
                Matrix[self.x][self.y] = ' '
                self.x+=1
                Matrix[self.x][self.y] = 'P'
                time.sleep(0.3)
                os.system('clear')
                self.print_player(Matrix)
                print "SCORE : ",
                print self.total_coins * 5,
                print "\t\t\t\t\t\t\t\t\tLife : ",
                print self.life



    def print_player(self, Matrix):
        Matrix[self.x][self.y] = 'P'
        print_board(Matrix)

    def getPosition(self):
        return self.x, self.y
