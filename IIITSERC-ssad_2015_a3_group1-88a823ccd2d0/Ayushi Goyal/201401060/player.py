from person import *
class Player(Person):#player class inherits the person class
    def __init__(self,name,px,py):
        self.__lives=3 #the lives of the player
        self.__score=0 #the score of the player
        self.__level=1 #the level of the player
        self.__name=name #name of the player
        Person.__init__(self,x=px,y=py) #calls the constructor of the base class

    def getName(self):#return ths name of the player
        return self.__name

    def getScore(self):#return the score
        return self.__score

    def getLives(self):#return the lives
        return self.__lives

    def getLevel(self):#returns the level
        return self.__level

    
    def setScore(self,x):#sets the score
        self.__score+=x

    def setLives(self,live):#sets the lives
        self.__lives+=live

    def setLevel(self,level):#sets the level
        self.__level+=level

    def printDetails(self):#displays the details of the player
        print "PLAYER NAME : "+str(self.getName())
        print "SCORE : " + str(self.getScore())
        print "LIVES : " + str(self.getLives())
        print "LEVEL : " + str(self.getLevel())

if __name__=="__main__":
    main()
