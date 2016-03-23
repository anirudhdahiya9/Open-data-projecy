import pygame 
import random
from colors import *
pygame.init()

""" The Fireball class """
class Fireballs(pygame.sprite.Sprite) :
    def __init__(self,x,y) :
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("fire.png")
        self.image = pygame.transform.scale(self.image,[20,20])
        self.rect = self.image.get_rect()
        self.rect.left = x
        self.speed_y = 0
        self.rect.top = y+15
        self.move = random.choice(["Left","Right"])
        self.flag = False
        self.platform = 0
        self.ladders = pygame.sprite.Group()
    
    """function to randomly generate the motion of the fireballs """
    def motion(self,all_barrier_list,all_ladder_list,all_fireball_list,person_sprite_list,speed) :
        if self.flag is False :
            self.rect.bottom += 50 
            collide = pygame.sprite.spritecollide(self,all_ladder_list,False) 
            self.rect.bottom -= 50
            for objects in collide :
                if objects not in self.ladders :
                    self.ladders.add(objects)
                    flag = random.choice([True,False])
                    if flag is True :
                        self.platform = objects.rect.bottom
                        self.rect.top = objects.rect.bottom - 85
        self.gravity()
        if self.move == "Left" :
            self.rect.left -= speed
            hit_list = pygame.sprite.spritecollide(self,all_barrier_list,False)
            for objects in hit_list :
                self.rect.left = objects.rect.right
                self.move = "Right"
        elif self.move == "Right" :
            self.rect.right += speed
            hit_list = pygame.sprite.spritecollide(self,all_barrier_list,False)
            for objects in hit_list :
                self.rect.right = objects.rect.left
                self.move = "Left"
        self.rect.y += self.speed_y
        if self.flag is False : 
            hit_list = pygame.sprite.spritecollide(self,all_barrier_list,False)
            for hit_objects in hit_list :
                if self.speed_y > 0 :
                    self.rect.bottom = hit_objects.rect.top
                    self.speed_y = 0
                elif self.speed_y < 0 :
                    self.rect.top = hit_objects.rect.bottom
                    self.speed_y = 0
        if self.rect.bottom == self.platform :
            self.flag = False
    
    """ funtion to generate gravity """
    def gravity(self,gravity_value = .5) :
        if self.speed_y == 0 :
            self.speed_y =1
        else :
            self.speed_y += gravity_value

