from person import *
class Donkey(Person):#donkey class inherits person class
    def __init__(self,px,py):
        self.__direction=1 #direction of the donkey (1 for right, -1 for left)
        Person.__init__(self,x=px,y=py)#calls constructor of the base class

    def getDirection(self):#returns the direction 
        return self.__direction

    def setDirection(self,direction):#sets the direction
        self.__direction=direction

if __name__=="__main__":
    main()
