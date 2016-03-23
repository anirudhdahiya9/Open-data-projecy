from board import *
from player import *
from donkey import *
from fireball import *
import time
import os

def getchar():
	"""Returns a single character from standard input""" """Function taken from Github : https://gist.github.com/jasonrdsouza/1901709"""
	import tty, termios, sys
	fd = sys.stdin.fileno()
	old_settings = termios.tcgetattr(fd)
	try:
		tty.setraw(sys.stdin.fileno())
		ch = sys.stdin.read(1)
	finally:
		termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
	return ch


def jump(P,B):#jumps the player
    key=getchar()#inputs the character
    if key=='a' or key=='A':
        os.system('clear')
        B.setScreen(P.getPositionX(),P.getPositionY()," ")#sets the location on the board with " "
        #check for walls and stairs
        if B.checkNotWall(P.getPositionX()-1,P.getPositionY()-1) and B.checkStairs(P.getPositionX()-1,P.getPositionY()-1,P) is False:            
            #if true gives new position
            P.setPos(P.getPositionX()-1,P.getPositionY()-1)
            B.assignPlayer(P.getPositionX(),P.getPositionY())
            B.printBoard()
            time.sleep(0.5)
            os.system('clear')
        else :
            return 
        B.setScreen(P.getPositionX(),P.getPositionY()," ")
        if B.checkNotWall(P.getPositionX()-1,P.getPositionY()-1) and B.checkStairs(P.getPositionX()-1,P.getPositionY()-1,P) is False:            
            P.setPos(P.getPositionX()-1,P.getPositionY()-1)
            B.assignPlayer(P.getPositionX(),P.getPositionY())
            B.printBoard()
            time.sleep(0.5)
            os.system('clear')
        else :
            P.setPos(P.getPositionX()+1,P.getPositionY())
            B.assignPlayer(P.getPositionX(),P.getPositionY())
            B.printBoard()
            time.sleep(0.5)
            os.system('clear')
            return 
        B.setScreen(P.getPositionX(),P.getPositionY()," ")
        if B.checkNotWall(P.getPositionX()+1,P.getPositionY()-1) and B.checkStairs(P.getPositionX()+1,P.getPositionY()-1,P) is False:            
            P.setPos(P.getPositionX()+1,P.getPositionY()-1)
            B.assignPlayer(P.getPositionX(),P.getPositionY())
            B.printBoard()
            time.sleep(0.5)
            os.system('clear')
        else :

            P.setPos(P.getPositionX()+2,P.getPositionY())
            B.assignPlayer(P.getPositionX(),P.getPositionY())
            B.printBoard()
            time.sleep(0.5)
            os.system('clear')

            return 
        B.setScreen(P.getPositionX(),P.getPositionY()," ")
        if B.checkNotWall(P.getPositionX()+1,P.getPositionY()-1) and B.checkStairs(P.getPositionX()+1,P.getPositionY()-1,P) is False:            
            P.setPos(P.getPositionX()+1,P.getPositionY()-1)
            B.assignPlayer(P.getPositionX(),P.getPositionY())
            B.printBoard()
            time.sleep(0.5)
            os.system('clear')
        else :
            P.setPos(P.getPositionX()+1,P.getPositionY())
            B.assignPlayer(P.getPositionX(),P.getPositionY())
            B.printBoard()
            time.sleep(0.5)
            os.system('clear')
            return 
   

    if key=='w' or key=='W':#jumpimg straigth up
        os.system('clear')
        B.setScreen(P.getPositionX(),P.getPositionY()," ")
        if B.checkNotWall(P.getPositionX()-1,P.getPositionY()) and B.checkStairs(P.getPositionX()-1,P.getPositionY(),P) is False:            
            P.setPos(P.getPositionX()-1,P.getPositionY())
            B.assignPlayer(P.getPositionX(),P.getPositionY())
            B.printBoard()
            time.sleep(0.5)
            os.system('clear')
        else :
            return 
        B.setScreen(P.getPositionX(),P.getPositionY()," ")
        if B.checkNotWall(P.getPositionX()-1,P.getPositionY()) and B.checkStairs(P.getPositionX()-1,P.getPositionY(),P) is False:            
            P.setPos(P.getPositionX()-1,P.getPositionY())
            B.assignPlayer(P.getPositionX(),P.getPositionY())
            B.printBoard()
            time.sleep(0.5)
            os.system('clear')
        else :
            P.setPos(P.getPositionX()+1,P.getPositionY())
            B.assignPlayer(P.getPositionX(),P.getPositionY())
            B.printBoard()
            time.sleep(0.5)
            os.system('clear')
            return 
        B.setScreen(P.getPositionX(),P.getPositionY()," ")
        if B.checkNotWall(P.getPositionX()+1,P.getPositionY()) and B.checkStairs(P.getPositionX()+1,P.getPositionY(),P) is False:            
            P.setPos(P.getPositionX()+1,P.getPositionY())
            B.assignPlayer(P.getPositionX(),P.getPositionY())
            B.printBoard()
            time.sleep(0.5)
            os.system('clear')
        else :

            P.setPos(P.getPositionX()+2,P.getPositionY())
            B.assignPlayer(P.getPositionX(),P.getPositionY())
            B.printBoard()
            time.sleep(0.5)
            os.system('clear')

            return 
        B.setScreen(P.getPositionX(),P.getPositionY()," ")
        if B.checkNotWall(P.getPositionX()+1,P.getPositionY()) and B.checkStairs(P.getPositionX()+1,P.getPositionY(),P) is False:            
            P.setPos(P.getPositionX()+1,P.getPositionY())
            B.assignPlayer(P.getPositionX(),P.getPositionY())
            B.printBoard()
            time.sleep(0.5)
            os.system('clear')
        else :
            P.setPos(P.getPositionX()+1,P.getPositionY())
            B.assignPlayer(P.getPositionX(),P.getPositionY())
            B.printBoard()
            time.sleep(0.5)
            os.system('clear')
            return 
        
        
    if key=='d' or key=='D':#jumping right
        os.system('clear')
        B.setScreen(P.getPositionX(),P.getPositionY()," ")
        if B.checkNotWall(P.getPositionX()-1,P.getPositionY()+1) and B.checkStairs(P.getPositionX()-1,P.getPositionY()+1,P) is False:            
            P.setPos(P.getPositionX()-1,P.getPositionY()+1)
            B.assignPlayer(P.getPositionX(),P.getPositionY())
            B.printBoard()
            time.sleep(0.5)
            os.system('clear')
        else :
            return 
        B.setScreen(P.getPositionX(),P.getPositionY()," ")
        if B.checkNotWall(P.getPositionX()-1,P.getPositionY()+1) and B.checkStairs(P.getPositionX()-1,P.getPositionY()+1,P) is False:            
            P.setPos(P.getPositionX()-1,P.getPositionY()+1)
            B.assignPlayer(P.getPositionX(),P.getPositionY())
            B.printBoard()
            time.sleep(0.5)
            os.system('clear')
        else :
            P.setPos(P.getPositionX()+1,P.getPositionY())
            B.assignPlayer(P.getPositionX(),P.getPositionY())
            B.printBoard()
            time.sleep(0.5)
            os.system('clear')
            return 
        B.setScreen(P.getPositionX(),P.getPositionY()," ")
        if B.checkNotWall(P.getPositionX()+1,P.getPositionY()+1) and B.checkStairs(P.getPositionX()+1,P.getPositionY()+1,P) is False:            
            P.setPos(P.getPositionX()+1,P.getPositionY()+1)
            B.assignPlayer(P.getPositionX(),P.getPositionY())
            B.printBoard()
            time.sleep(0.5)
            os.system('clear')
        else :

            P.setPos(P.getPositionX()+2,P.getPositionY())
            B.assignPlayer(P.getPositionX(),P.getPositionY())
            B.printBoard()
            time.sleep(0.5)
            os.system('clear')

            return 
        B.setScreen(P.getPositionX(),P.getPositionY()," ")
        if B.checkNotWall(P.getPositionX()+1,P.getPositionY()+1) and B.checkStairs(P.getPositionX()+1,P.getPositionY()+1,P) is False:            
            P.setPos(P.getPositionX()+1,P.getPositionY()+1)
            B.assignPlayer(P.getPositionX(),P.getPositionY())
            B.printBoard()
            time.sleep(0.5)
            os.system('clear')
        else :
            P.setPos(P.getPositionX()+1,P.getPositionY())
            B.assignPlayer(P.getPositionX(),P.getPositionY())
            B.printBoard()
            time.sleep(0.5)
            os.system('clear')
            return 
       

def move(P,B):#to move the player
    key=getchar()
    x=P.getPositionX()
    y=P.getPositionY()
    if key=='q' or key=='Q':#to quit
        exit()
    elif key=='a' or key=='A':#to move to left
        if B.checkNotWall(x,y-1):
            if P.getPositionX()%4==3:
                B.setScreen(x,y," ")
                if B.checkCoin(x,y-1):
                    P.setScore(5)
                P.setPos(x,y-1)

    elif key=='d' or key=='D':#to move to right
        if B.checkNotWall(x,y+1):
            if P.getPositionX()%4==3:
                B.setScreen(x,y," ")
                if B.checkCoin(x,y+1):
                    P.setScore(5)
                P.setPos(x,y+1)

    elif key=='s' or key=='S':#to climb dowm the stairs
        if B.checkStairs(x+1,y,P):
            if B.checkBrokenStairs(x+1,y) is False:
                B.setScreen(x,y," ")
                if B.checkCoin(x+1,y):
                    P.setScore(5)
                P.setPos(x+1,y)


    elif key=='w' or key=='W':#to climb dowm the stairs
        if B.checkStairs(x-1,y,P):
            if B.checkBrokenStairs(x-1,y) is False :
                if B.checkCoin(x-1,y):
                    P.setScore(5)
                P.setPos(x-1,y)

            elif B.getScreen(x-2,y)==" " or B.getScreen(x-2,y)=="x":
                if B.checkCoin(x-1,y):
                    P.setScore(5)
                P.setPos(x-1,y)



    elif key==" ":#to jump
        jump(P,B)

    if B.getScreen(P.getPositionX(),P.getPositionY())=="Q":#if the player reaches the queen returns true
        return True
    return False



def main():
    os.system('clear')
    name=raw_input("enter your name : ")#inputs the name
    B=Board()#creates board instance
    os.system('clear')
    P=Player(name,B.getHeight()-2,1)#creates player instance
    print "hi, "+P.getName()+", welcome to the game"
    print
    st= "The game starts in 5  seconds"
    print st
    time.sleep(5)

    while True:
        B=Board()
        P.setPos(B.getHeight()-2,1)#sets initial position of the player
        D=Donkey(3,B.initiateDonkey())#creates donkey instance
        fireball=[]#creates list that will contain the fireball
        count=1
        while True:
            os.system('clear')
            B.assignPlayer(P.getPositionX(),P.getPositionY())

            #assigning position to donkey
            if B.checkFloorDonkey(D.getPositionX(),D.getPositionY(),D.getDirection()) and B.checkNotWall(D.getPositionX(),D.getPositionY()+D.getDirection()):
                D.setPos(D.getPositionX(),D.getPositionY()+D.getDirection())
                B.assignDonkey(D.getPositionX(),D.getPositionY(),D.getDirection())
            else:
                D.setDirection(D.getDirection()*-1)

            #assigning position to player

            while B.checkFloorPlayer(P.getPositionX(),P.getPositionY()) is False and P.getPositionX()%4==3:
                P.setPos(P.getPositionX()+4,P.getPositionY())
                B.assignPlayer(P.getPositionX(),P.getPositionY())

            for f in fireball:#to check collision with fireball
                if B.checkCollision(f,P):
                    P.setLives(-1)
                    P.setScore(-25)
                    B.setScreen(P.getPositionX(),P.getPositionY()," ")
                    P.setPos(B.getHeight()-2,1)
                    B.assignPlayer(P.getPositionX(),P.getPositionY())
                    break
        
            if B.checkCollision(D,P):#checks the collision between the donkey and the player
                P.setLives(-1)
                P.setScore(-25)
                P.setPos(B.getHeight()-2,1)
                B.assignPlayer(P.getPositionX(),P.getPositionY())


            #assigning position to fireball
            if count%20==0:
                if B.getScreen(D.getPositionX(),D.getPositionY()+1)=="H":
                    count-=1
                else:
                    fireball.append(Fireball(D.getPositionX(),D.getPositionY()+1))#generates a fireball every 20 steps
        
            for f in fireball:#to iterate over the entire fireball list
                flag=0
                demo_ch="D"
                while B.checkStairs(f.getPositionX()+1,f.getPositionY(),f):#to check if the next position of fireball has stairs 
                    if B.checkBrokenStairs(f.getPositionX()+3,f.getPositionY()) is False:#to check for broken stairs
                        if f.getfch()=="D" or f.getfch()=="P" or f.getfch()=="O":
                            f.setfch(" ")
                        B.setScreen(f.getPositionX(),f.getPositionY(),f.getfch())
                        f.setDirection(random.choice([-1,1]))#randomly generates the direction of the fireball
                        f.setPos(f.getPositionX()+4,f.getPositionY()+f.getDirection())#to set new position of fireball
                        flag=1

                    else:
                        B.setScreen(f.getPositionX(),f.getPositionY(),f.getfch())
                        f.setPos(f.getPositionX(),f.getPositionY()+f.getDirection())

                if flag==0:
                    if B.checkNotWall(f.getPositionX(),f.getPositionY()+f.getDirection()):#checks the wall
                        f.setPos(f.getPositionX(),f.getPositionY()+f.getDirection())
                        f.setfch(B.assignFireball(f.getPositionX(),f.getPositionY(),f.getDirection(),f.getfch()))
                        while B.checkFloorPlayer(f.getPositionX(),f.getPositionY()) is False:#iterates till there is floor below the fireball
                            f.setPos(f.getPositionX()+4,f.getPositionY())
                            f.setDirection(random.choice([1,-1]))
                            flag=1
                    else:
                        if f.getPositionX()==B.getHeight()-2:#removes the fireball if it reaches th wall of the lowest floor
                            B.setScreen(f.getPositionX(),f.getPositionY(),f.getfch())
                            fireball.remove(f)
                            continue
                        f.setDirection(f.getDirection()*-1)#changes the direction of the fireball on reaching the wall
                        f.setPos(f.getPositionX(),f.getPositionY()+f.getDirection())
                        if f.getfch()!="c":
                            demo_ch=" "
                ch=B.assignFireball(f.getPositionX(),f.getPositionY(),f.getDirection(),demo_ch)


                if flag==1:
                    f.setfch(ch)

                if B.checkCollision(f,P):#checks the collision between the fireball and the player
                    P.setLives(-1)
                    P.setScore(-25)
                    B.setScreen(P.getPositionX(),P.getPositionY()," ")
                    P.setPos(B.getHeight()-2,1)
                    B.assignPlayer(P.getPositionX(),P.getPositionY())

            count+=1

            if B.checkCollision(D,P):#checks the collision between the donkey and the player
                P.setLives(-1)
                P.setScore(-25)
                P.setPos(B.getHeight()-2,1)
                B.assignPlayer(P.getPositionX(),P.getPositionY())

 
            B.printBoard()
            if P.getLives()<=0:#checks the number of lives left
                os.system('clear')
                print "game over"
                temp=getchar()
                exit()

            P.printDetails()
            print "Enter Move : "
            levelflag=move(P,B)
            if levelflag==True:#if the queen is rescued?
                P.setScore(50)
                P.setLevel(1)
                os.system('clear')
                print "Level Up......"
                break


if __name__=="__main__":
    main()
