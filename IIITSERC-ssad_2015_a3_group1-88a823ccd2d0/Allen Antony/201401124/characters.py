import pygame
import random
from colors import *

""" The class person is the parent call to all the characters in the game """

class Person (pygame.sprite.Sprite) :

    """ initializing the person class """
    def __init__(self,image,size) :
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(image)
        self.image = pygame.transform.scale(self.image,[size,size])
        self.rect = self.image.get_rect()
        self.speed_x = 0
        self.speed_y = 0
        self.size = size
    def update(self) :
        raise NotImplementedError

""" class queen for the queen character """

class Queen(Person) :

    """ initializing the queen class """

    def __init__(self,platform_dict,image,size) :
        super(Queen,self).__init__(image,size)
        self.rect.x = platform_dict[8].rect.left + 20
        self.rect.y = platform_dict[8].rect.top - size

    """ function to get the position of the queen """                          #one of the required functions

    def getPosition(self) :
        return [self.rect.x,self.rect.y]

"""class for the donkey """

class Donkey(Person) :
    
    """ initializing """
    def __init__(self,platform_dict,image,size) :
        super(Donkey,self).__init__(image,size)
        self.rect.x = platform_dict[7].rect.left + 20
        self.rect.y = platform_dict[7].rect.top - size
        self._motion_check = 0
        self._flag = True
    
    """ function update to update the position of the donkey randomly"""

    def update(self,platform_dict) :
        if(self._motion_check == 0) :
            self._flag = random.choice([True,False])
        if self._flag is True :
            self.rect.x += 5
        else :
            self.rect.x -= 5
        self._motion_check += 1
        if(self.rect.x <= platform_dict[7].rect.left) :
            self._flag = True
            self.rect.left = platform_dict[7].rect.left + 10
        elif(self.rect.x >= platform_dict[7].rect.right - self.size) :
            self._flag = False
            self.rect.right = platform_dict[7].rect.right
        if self._motion_check == 50 :
            self._motion_check = 0


"""class for the player"""

class Player(Person) :
    """initializing"""
    def __init__(self , height,image,size):
        super(Player,self).__init__(image,size)
        self.rect.x =450 
        self.rect.y = height-50
        self.coin_list=[]
        self.is_climbing_up = False
        self.is_climbing_down = False
        self._from_platform = 1
        self._to_platform = 1
        self.motion_complete = True
        self.fireball_list = []
        self.life = 10

    """ function to get the coins"""                                            #one of the required functions
    
    def collectCoin(self,all_coin_list) :
        self.coin_list += pygame.sprite.spritecollide(self,all_coin_list,True)
    
    """function to change the speed of the player"""
    
    def motion(self,xchange, ychange):
        self.speed_x += xchange
        self.speed_y += ychange

    """function to check wall collisions"""                                         #one of the required functions

    def checkWall(self,all_barrier_list) :
        if self.motion_complete is True :
            self.gravity()
            self.rect.x += self.speed_x
            hit_list = pygame.sprite.spritecollide(self,all_barrier_list,False)
            for hit_objects in hit_list :
                if self.speed_x > 0 :
                    self.rect.right = hit_objects.rect.left
                elif self.speed_x < 0  :
                    self.rect.left = hit_objects.rect.right
    
    """function to check other collisions """                                      #one of the required functions

    def checkCollision(self,all_barrier_list) :
        self.rect.y += self.speed_y
        if self.motion_complete is True :
            hit_list = pygame.sprite.spritecollide(self,all_barrier_list,False)
            for hit_objects in hit_list :
                if self.speed_y > 0 :
                    self.rect.bottom = hit_objects.rect.top
                    self.speed_y = 0
                elif self.speed_y < 0 :
                    self.rect.top = hit_objects.rect.bottom
                    self.speed_y = 0
  

    """function to update the position of the player """

    def update(self,all_barrier_list,all_coin_list,all_ladder_list,platform_dict,all_fireball_list):
        self.checkWall(all_barrier_list)
        self.collectCoin(all_coin_list)
        fireball_count = pygame.sprite.spritecollide(self,all_fireball_list,True)
        if len(fireball_count) > 0 :
            self.rect.x = 450
            self.rect.y = 750
            self.life -= 1
            self.motion_complete = True
        self.checkCollision(all_barrier_list)
        if self.motion_complete is False :
            self.ladder_motion(platform_dict)
        self.check_platform(platform_dict)

    """function to see which platform the player is currently on """

    def check_platform(self, platform_dict) :
        i = 1
        while i <= 7 :
            if( self.rect.bottom == platform_dict[i].rect.top) :
                self._from_platform = i
                break
            i += 1
    
    """ function to manage the motion of the player on a ladder """

    def ladder_motion(self,platform_dict) :
        if self.is_climbing_up is True :
            if self._to_platform > self._from_platform:
                plat = self._to_platform
            else :
                plat = self._from_platform
            if self.rect.top <= platform_dict[plat].rect.bottom :
                self.is_climbing_up = False
                self.rect.bottom = platform_dict[plat].rect.bottom - 30
                self.motion_complete = True 
            else :
                self.rect.y -= 5
        elif self.is_climbing_down is True :
            if self._to_platform < self._from_platform:
                plat = self._to_platform
            else :
                plat = self._from_platform
            if self.rect.bottom >= platform_dict[plat].rect.top :
                self.is_climbing_down = False
                self.rect.bottom = platform_dict[plat].rect.top
                self.motion_complete = True 
            else :
                self.rect.y += 5

    """function to add gravity """

    def gravity(self,gravity_value = .7) :
        if self.speed_y == 0 :
            self.speed_y =1
        else :
            self.speed_y += gravity_value
    
    """ function to climb up the ladder """

    def climb_up(self,all_ladder_list,platform_dict) :
        if self.motion_complete is True :
            ladder_list = pygame.sprite.spritecollide(self,all_ladder_list,False)
            if len(ladder_list) >= 1 :
                self.is_climbing_up = True
                self.motion_complete = False
                self.is_climbing_down = False
                self._to_platform = self._from_platform + 1
            else :
                self.is_climbing_up = False
                self.motion_complete = True
        else :
            self.is_climbing_up = True

    """ function to climb down the ladder """

    def climb_down(self,all_ladder_list,platform_dict) :
        if self.motion_complete is True :
            flag = False
            self.rect.y +=40
            collision_list = pygame.sprite.spritecollide(self,all_ladder_list,False)
            if(len(collision_list) > 0) :
                flag = True
            else :
                flag = False
            self.rect.y -= 40
            if flag is True :
                self.is_climbing_down = True
                self.motion_complete = False
                self.is_climbing_up = False
                self._to_platform = self._from_platform - 1
            else :
                self.is_climbing_down = False
                self.motion_complete = True
        else :
            self.is_climbing_down = True

    """function to load the image """
    def loadimage(self , image_name):
        self.image = pygame.image.load(image_name)
        self.image = pygame.transform.scale(self.image,[35,35])

