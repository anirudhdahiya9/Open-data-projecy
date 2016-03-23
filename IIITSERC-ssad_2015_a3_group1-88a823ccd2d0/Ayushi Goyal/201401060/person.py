class Person:#person class
    def __init__(self,x,y):
        self.__x=x #the x position 
        self.__y=y # the y position

    def getPositionX(self):
        return self.__x #returns the x position

    def getPositionY(self):
        return self.__y #return the y position

    def setPos(self,x,y): #set the new position
        self.__x=x
        self.__y=y

if __name__=="__main__":
    main()

