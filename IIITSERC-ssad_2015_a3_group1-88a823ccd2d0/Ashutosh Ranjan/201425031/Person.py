import * from boardLayout
import * from Donkey

class Person(self):
    def __init__(self,name):
        self.name=name

     def opposeWall(self,ui):
        if ui.boardvalue(self.newposition)=='X':
            return True
        else:
            return False
     def coinCheck(self,b):
         if ui.boardvalue(self.newposition)=='C':
            return True
         else:
            return False
    def checkLadder(self,b):
        if ui.boardvalue(self.newposition)=='H':
            return True
        else:
            return False



