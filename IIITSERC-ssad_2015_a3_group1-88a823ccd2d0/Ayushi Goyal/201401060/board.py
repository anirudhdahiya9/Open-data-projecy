from random import *

class Board:
    def __init__(self,height=33,width=80): #constructor
        self.__height=height
        self.__width=width
        self.__stairflag=0
        self.__prev_x=self.getHeight()-2
        self.__prev_y=1
        self.__screen=[]
        self.createBoard()
        self.printBoard()
        self.__dch=" "
        self.__fch=" "


    def setScreen(self,x,y,ch):#sets the screen with the passed character
        self.__screen[x][y]=ch

    def getHeight(self): #returns the height of the board 
        return self.__height

    def getStairFlag(self):#returns stairflag
        return self.__stairflag

    def getWidth(self): #returns the width of the board
        return self.__width

    def getScreen(self,x,y):#return the character at the given position
        return self.__screen[x][y]
    
    def createBoard(self): #calls the functions for creating the board
        self.createRoof()
        self.createWalls()
        self.setBoard()

    def createRoof(self): #creates the top and the bottom of the board
        l1=[]
        for i in range(1,self.getWidth()):
            l1.append('x')

        self.__screen.insert(len(self.__screen),l1)

        for i in range(1,self.getHeight()-1):
            self.__screen.insert(len(self.__screen),[])
            for j in range(0,self.getWidth()):
                self.__screen[i].append(" ")

        self.__screen.insert(len(self.__screen),l1)
       
    def createWalls(self): # creates the side walls of the board
        for i in range(0,self.getHeight()):
            self.__screen[i][0]="x"
            self.__screen[i][self.getWidth()-2]="x"


    def setBoard(self): #function to set the interiors of the board
        self.setFloor()
        self.setCoins()
        self.setCage()
        self.setStairs()


    def printBoard(self): #prints the board
        for i in range(0,self.getHeight()):
            print ''.join(self.__screen[i])

    def setFloor(self): #sets the floor on each level
        for i in range(4,self.getHeight()-1,4):
            side=randint(0,1)  #to randomly generate if the floor starts from the wall or in the middle(0->from the wall,1->from middle)
            maxlength=self.getWidth()-5 #maximum length of the board
            start=1
            if side==1: #starts from the middle
                maxlength-=5
                start=5

            while maxlength>8: 
                length=randint(1,maxlength) #to randonly generate the length of the floor
                for j in range(start,start+length):
                    self.__screen[i][j]="x"

                maxlength-=length
                maxlength-=3 #to leave a gap of 3 spaces between the floors
                start+=length+3


    def setCage(self): #to build the cage
        self.__screen[0][10]=self.__screen[0][14]="x"
        self.__screen[1][10]=self.__screen[1][14]="x"
        for i in range(10,15):
            self.__screen[2][i]="x"
            self.__screen[1][12]="Q"
            for i in range(11,14): #for stairs
                if self.__screen[4][i]=="x":
                    self.__screen[2][i]=self.__screen[3][i]="H"
                    break

    def setCoins(self): #to set the coins
        for i in range(3,self.getHeight(),4):
            no_of_coins=randint(1,5) #generates number of coins on each level
            count=1
            while count<=no_of_coins:
                position=randint(1,self.getWidth()-5)
                if self.__screen[i+1][position]=="x" and self.__screen[i][position]!="c":
                    self.__screen[i][position]="c"
                    count+=1

    def setStairs(self): #builds the stairs
        for i in range(8,self.getHeight(),4):
            no_of_stairs=randint(1,2) #generates the number of stairs on each level
            count=1
            broken=False
            while count<=no_of_stairs:
                position=randint(1,self.getWidth()-5)#randomly generates the position of the stairs
                if self.__screen[i-4][position]=="x" and self.__screen[i][position]=="x" and self.__screen[i][position+1]=="x" and self.__screen[i][position-1]=="x" and self.__screen[i-1][position]!="c": #checks suitable conditions for building the stairs
                    for j in range(i-4,i):
                        self.__screen[j][position]="H"
                    if broken==False and no_of_stairs>1:#broken stairs
                        self.__screen[i-2][position]=" "
                        broken=True
                 
                    count+=1

    def assignPlayer(self,posx,posy):#sets the player on the board
        if self.__stairflag==1:#if the player "was" on the stairs
            self.__screen[self.__prev_x][self.__prev_y]="H"
        if self.__screen[posx][posy]=="H":#if the player "is" on the stairs
            self.__stairflag=1
        if self.__screen[posx][posy]!="H":#if the player is not on the stairs
            self.__stairflag=0
        self.__screen[posx][posy]="P"
        self.__prev_x=posx
        self.__prev_y=posy

    def checkNotWall(self,x,y):
        if self.__screen[x][y]=="x":
            return False
        return True

    def checkStairs(self,x,y,obj):
        if obj.__class__.__name__=="Fireball":#if the passed obj is a fireball
           if self.__screen[x][y]=="H":
               return True
           else: 
               return False 
        if self.__screen[x][y]=="H" or (self.__screen[x][y]!="x" and self.__stairflag==1):#if the passed obj is a player
            return True
        return False

    def checkBrokenStairs(self,x,y):#checks broken stairs
        if self.__screen[x][y]==" ":
            return True
        return False

    def checkCoin(self,x,y):#checks for coins
        if self.__screen[x][y]=="c":
            return True
        return False

    def checkFloorPlayer(self,x,y):#checks for floor for player
        if self.__screen[x+1][y]==" " and self.__stairflag==0:
            self.__screen[x][y]=" "
            return False
        return True

    def checkFloorDonkey(self,x,y,direction):#checks floor for donkey
        if self.__screen[x+1][y+direction]==" ":
            return False
        return True

    def checkCollision(self,obj1,obj2):#checks collision between two objects
        if obj1.getPositionX()==obj2.getPositionX() and obj1.getPositionY()==obj2.getPositionY():
            return True
        return False

         

    def initiateDonkey(self):#initialises the donkey on the board
        for i in range(1,self.getWidth()-1):
            if self.__screen[4][i]!=" ":
                flag=1
                pos=i
                break
        if flag==1:
            self.__screen[3][pos]="D"
        return pos

    def assignDonkey(self,x,y,direction):#further assignments of the donkey on the board
        if self.__dch!="P":
            self.__screen[x][y-direction]=self.__dch
        self.__dch=self.__screen[x][y]
        self.__screen[x][y]="D"

    def assignFireball(self,x,y,direction,fch):#assigning the fireball on the board
        if fch!="D" and fch!="O" and fch!="P" and self.__screen[x][y-direction]!="D" and self.__screen[x][y-direction]!="P":
            self.__screen[x][y-direction]=fch
        fch=self.__screen[x][y]
        self.__screen[x][y]="O"
        return fch



if __name__=="__main__":
    main()
