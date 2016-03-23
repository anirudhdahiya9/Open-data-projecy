import pygame
import random
from platform import *
from colors import *
from ladders import *
from coins import *

clock = pygame.time.Clock()                #Setting the clock for frames per second


""" The Class Board sets all the elements seen on the screen"""

class Board:

    """ Initializing the class """

    def __init__(self,height,width,all_barrier_list,all_platform_list,all_ladder_list,all_coin_list,prev_coins):
        self.height = height
        self.width = width
        self.screen = pygame.display.set_mode((self.width,self.height))
        self.platform_dict = {}
        pygame.display.update()
        self._create_platforms(all_barrier_list,all_platform_list)
        self._create_ladders(all_ladder_list)
        self._create_coins(all_platform_list,all_coin_list)
        #self.level_font = pygame.font.SysFont("comicsansms",50)                    
        #self.other_font = pygame.font.SysFont("comicsansms",40)   #uncomment this line and the line above and comment the next two lines to get a better font
        self.level_font = pygame.font.SysFont("monospace",50)
        self.other_font = pygame.font.SysFont("monospace",40)
        self.coins = prev_coins

    """ This function randomly creates the platforms """

    def _create_platforms(self,all_barrier_list,all_platform_list) :    
        self.left_border   = Platform(2,  1500, 420, 0, "line","")
        self.right_border  = Platform(2 , 1500 ,1320, 0 , "line","")
        self.bottom_border = Platform(900, 15 , 420 , 785, "platform_picture","platform.png")
        self.top_border    = Platform(900, 15 , 420 ,0 , "platform_picture","platform.png")
        all_barrier_list.add([self.left_border,self.right_border,self.bottom_border,self.top_border])
        all_platform_list.add(self.bottom_border)
        counter = 1
        self.platform_dict = {counter : self.bottom_border}
        counter += 1;
        flag = random.choice([True,False])
        posiy = 685
        for i in range(6) :
            size = random.randint(500,700)
            if flag is True :
                posix = 420
                if i == 5 :
                    platform = Platform(size , 15 , posix , posiy ,"platform_picture","top.jpg")
                else :
                    platform = Platform(size , 15 , posix , posiy ,"platform_picture","platform.png")
                flag = False
            else :
                posix = 620
                posix += (self.right_border.rect.left - (posix+size))
                if i == 5 :
                    platform = Platform(size , 15,posix ,posiy ,"platform_picture","top.jpg")
                else :
                    platform = Platform(size , 15 , posix ,posiy , "platform_picture","platform.png")
                flag = True
            posiy -= 100
            self.platform_dict[counter] = platform
            counter += 1
            all_platform_list.add(platform)
            all_barrier_list.add(platform)
            i += 1 
        point = self.platform_dict[7].width/2 + self.platform_dict[7].rect.left - 100
        platform = Platform(200,15,point,self.platform_dict[7].rect.top - 100,"platform_picture","top_platform.jpg")
        all_platform_list.add(platform)
        all_barrier_list.add(platform)
        self.platform_dict[8] = platform
        wall1 = Platform(15,100,platform.rect.left,0,"platform_picture","top_platform.jpg")
        wall2 = Platform(15,100,platform.rect.right-15,0,"platform_picture","top_platform.jpg")
        all_barrier_list.add(wall1,wall2)


    """This function randomly creates the ladders """

    def _create_ladders(self,all_ladder_list) :
        xpoint = random.randint(self.platform_dict[2].rect.left + 100 , self.platform_dict[2].rect.right-50)
        ypoint = self.platform_dict[2].rect.top
        ladder = Ladder(xpoint,ypoint)
        all_ladder_list.add(ladder)
        counter=2
        while counter <=6 :
            if self.platform_dict[counter].rect.left == 420 :
                xpoint = random.randint(self.platform_dict[counter+1].rect.left ,self.platform_dict[counter].rect.right-30)
                ypoint = self.platform_dict[counter+1].rect.top
            else :
                xpoint = random.randint(self.platform_dict[counter].rect.left + 20, self.platform_dict[counter+1].rect.right-30)
                ypoint = self.platform_dict[counter+1].rect.top
            ladder = Ladder(xpoint,ypoint)
            all_ladder_list.add(ladder)
            counter +=1
        xpoint = random.randint(self.platform_dict[8].rect.left + 30,self.platform_dict[8].rect.right-50)
        ypoint = self.platform_dict[8].rect.top
        ladder = Ladder(xpoint,ypoint)
        all_ladder_list.add(ladder)


    """This function randomly creates the coins """

    def _create_coins(self,all_platform_list,all_coin_list) :
        for plat in all_platform_list :
            if plat.width != 200 and plat.width !=15 :
                number_of_coins = random.randint(2,9)
                i = 1
                while i <= number_of_coins :
                    xpoint = random.randint(plat.rect.left,plat.rect.right-30)
                    ypoint = plat.rect.top - 30
                    coin = Coin(xpoint,ypoint)
                    collide_list = pygame.sprite.spritecollide(coin,all_coin_list,True)
                    all_coin_list.add(coin)
                    i -= len(collide_list)
                    i += 1
    
    """This function is called to update the entire board """

    def update(self,alsp,person_sprite_list,all_coin_list,all_ladder_list,background,level,coin_list,coin_image,prev_coins,fireball_list,life,heart_image) :
        if life is 0 :
            pygame.quit()
            quit()
        coi = len(coin_list) * 5
        fie = len(fireball_list) *25
        self.coins = prev_coins +coi - fie
        self.screen.fill(white)
        self.screen.blit(background.image, background.rect)
        self.screen.blit(coin_image.image, coin_image.rect)
        self.screen.blit(heart_image.image, heart_image.rect)
        self.screen.blit(self.level_font.render("Level",True,(255,255,0)),(90,20))
        self.screen.blit(self.level_font.render(str(level),True,(255,255,0)),(140,70))
        self.screen.blit(self.other_font.render(str(self.coins),True,(255,255,255)),(150,170))
        self.screen.blit(self.other_font.render(str(life),True,(255,255,255)),(150,220))
        alsp.draw(self.screen)
        all_ladder_list.draw(self.screen)
        all_coin_list.draw(self.screen)
        person_sprite_list.draw(self.screen)
        pygame.display.update()
        clock.tick(60)

