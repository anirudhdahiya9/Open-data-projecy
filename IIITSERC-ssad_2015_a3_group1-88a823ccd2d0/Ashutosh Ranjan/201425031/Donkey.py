class Donkey(Person):
     def opposeWall(self,b):
         if b.boardvalue(self.updatedposition)=='X':
             return True
         else:
             return False
