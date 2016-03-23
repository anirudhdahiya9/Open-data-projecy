import random
class Fireball:
    def __init__(self,x,y):
        self.__x=x #x position
        self.__y=y#y position
        self.__direction=1#direction(1 for right, -1 for left)
        self.__fch=" " #stores the character at before position

    def getPositionX(self):#returns the x position
        return self.__x
    def getPositionY(self):#returns the y position
        return self.__y
    def getfch(self):#returns the character
        return self.__fch
    def setPos(self,x,y):#sets the position
        self.__x=x
        self.__y=y

    def getDirection(self):#returns the direction
        return self.__direction

    def setDirection(self,direction):#sets the direction
        self.__direction=direction

    def setfch(self,fch):#sets the character
        self.__fch=fch

if __name__=="__main__":
    main()
