display_width = 1200
display_height = 450
block_size = 15

class person:
    def __init__(self):
        self.pos_x = 0
        self.pos_y = 0
        self.init_x = 0
        self.init_y = 0

class player(person):
    def __init__(self):
        self.init_x = display_height-2*block_size
        self.init_y = 2*block_size
        self.coins = 0
        self.cc = 0
        self.lives = 3
        
    def collectCoin(self):
        self.coins += 5
        print self.coins

    def getPosition(self):
        return self.pos_x,self.pos_y

    def collided(self):
        self.lives -= 1
        
##    def ret_coin(self):
##        cc=__coins
##        return cc
    
            
class donkey(person):
    def __init__(self):
        self.pos_x = 3
        self.pos_y = 4

   
##a=player()
##
##a.collect_coin()
##a.collect_coin()
##
##k=a.ret_coin
##
##print k,"Outside"

