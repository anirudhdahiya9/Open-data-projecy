import pygame
import random
from images import *
from fireball import *
from board import *
from colors import *
from characters import *
pygame.init()
clock = pygame.time.Clock()

"""
white = (255,255,255)
red = (255,0,0)
black =(0,0,0)

class Door(pygame.sprite.Sprite) :
    def __init__(self) :
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("door.png")
        self.image = pygame.transform.scale(self.image,[50,50])
        self.rect = self.image.get_rect()
        self.rect.left = 450
        self.rect.bottom = 785
    
    def remove_fireballs(self,all_fireball_list) :
        hit_list = pygame.sprite.spritecollide(self,all_fireball_list,True)

"""
"""
class Board:
    def __init__(self,height,width,all_barrier_list,all_platform_list,all_ladder_list,all_coin_list,prev_coins):
        self.height = height
        self.width = width
        self.screen = pygame.display.set_mode((self.width,self.height))
        self.platform_dict = {}
        pygame.display.update()
        self.create_platforms(all_barrier_list,all_platform_list)
        self.create_ladders(all_ladder_list)
        self.create_coins(all_platform_list,all_coin_list)
        self.level_font = pygame.font.SysFont("comicsansms",50)
        self.other_font = pygame.font.SysFont("comicsansms",40)
        self.coins = prev_coins

    def create_platforms(self,all_barrier_list,all_platform_list) :    
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

    def create_ladders(self,all_ladder_list) :
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

    def create_coins(self,all_platform_list,all_coin_list) :
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

    def update(self,alsp,person_sprite_list,all_coin_list,all_ladder_list,background,level,coin_list,coin_image,prev_coins,fireball_list) :
        coi = len(coin_list) * 5
        fie = len(fireball_list) *25
        self.coins = prev_coins +coi - fie
        self.screen.fill(white)
        self.screen.blit(background.image, background.rect)
        self.screen.blit(coin_image.image, coin_image.rect)
        self.screen.blit(self.level_font.render("Level",True,(255,255,0)),(90,20))
        self.screen.blit(self.level_font.render(str(level),True,(255,255,0)),(140,70))
        self.screen.blit(self.other_font.render(str(self.coins),True,(255,255,255)),(150,170))
        alsp.draw(self.screen)
        all_ladder_list.draw(self.screen)
        all_coin_list.draw(self.screen)
        person_sprite_list.draw(self.screen)
        pygame.display.update()
        clock.tick(60)
"""
"""
class Person (pygame.sprite.Sprite) :
    def __init__(self,image,size) :
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(image)
        self.image = pygame.transform.scale(self.image,[size,size])
        self.rect = self.image.get_rect()
        self.speed_x = 0
        self.speed_y = 0
        self.size = size

class Queen(Person) :
    def __init__(self,platform_dict,image,size) :
        super(Queen,self).__init__(image,size)
        self.rect.x = platform_dict[8].rect.left + 20
        self.rect.y = platform_dict[8].rect.top - size

class Donkey(Person) :
    def __init__(self,platform_dict,image,size) :
        super(Donkey,self).__init__(image,size)
        self.rect.x = platform_dict[7].rect.left + 20
        self.rect.y = platform_dict[7].rect.top - size
        self.motion_check = 0
        self.flag = True
    
    def update(self,platform_dict) :
        if(self.motion_check == 0) :
            self.flag = random.choice([True,False])
        if self.flag is True :
            self.rect.x += 5
        else :
            self.rect.x -= 5
        self.motion_check += 1
        if(self.rect.x <= platform_dict[7].rect.left) :
            self.flag = True
            self.rect.left = platform_dict[7].rect.left + 10
        elif(self.rect.x >= platform_dict[7].rect.right - self.size) :
            self.flag = False
            self.rect.right = platform_dict[7].rect.right
        if self.motion_check == 50 :
            self.motion_check = 0


class Player(Person) :
    def __init__(self , height,image,size):
        super(Player,self).__init__(image,size)
        self.rect.x =450 
        self.rect.y = height-50
        self.coin_list=[]
        self.is_climbing_up = False
        self.is_climbing_down = False
        self.from_platform = 1
        self.to_platform = 1
        self.motion_complete = True
        self.fireball_list = []

    def motion(self,xchange, ychange):
        self.speed_x += xchange
        self.speed_y += ychange

    def update(self,all_barrier_list,all_coin_list,all_ladder_list,platform_dict,all_fireball_list):
        if self.motion_complete is True :
            self.gravity()
            self.rect.x += self.speed_x
            hit_list = pygame.sprite.spritecollide(self,all_barrier_list,False)
            self.coin_list += pygame.sprite.spritecollide(self,all_coin_list,True)
            fireball_count = pygame.sprite.spritecollide(self,all_fireball_list,True)
            if len(fireball_count) > 0 :
                self.rect.x = 450
                self.rect.y = 750
            self.fireball_list += fireball_count
            for hit_objects in hit_list :
                if self.speed_x > 0 :
                    self.rect.right = hit_objects.rect.left
                elif self.speed_x < 0 :
                    self.rect.left = hit_objects.rect.right
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
        if self.motion_complete is False :
            self.ladder_motion(platform_dict)
        self.check_platform(platform_dict)

    def check_platform(self, platform_dict) :
        i = 1
        while i <= 7 :
            if( self.rect.bottom == platform_dict[i].rect.top) :
                self.from_platform = i
                break
            i += 1
    
    def ladder_motion(self,platform_dict) :
        if self.is_climbing_up is True :
            if self.to_platform > self.from_platform:
                plat = self.to_platform
            else :
                plat = self.from_platform
            if self.rect.top <= platform_dict[plat].rect.bottom :
                self.motion_complete = True 
                self.is_climbing_up = False
                self.rect.bottom = platform_dict[plat].rect.bottom
            else :
                self.rect.y -= 5
        elif self.is_climbing_down is True :
            if self.to_platform < self.from_platform:
                plat = self.to_platform
            else :
                plat = self.from_platform
            if self.rect.bottom >= platform_dict[plat].rect.top :
                self.motion_complete = True 
                self.is_climbing_down = False
                self.rect.bottom = platform_dict[plat].rect.top
            else :
                self.rect.y += 5

    def gravity(self,gravity_value = .7) :
        if self.speed_y == 0 :
            self.speed_y =1
        else :
            self.speed_y += gravity_value
    
    def climb_up(self,all_ladder_list,platform_dict) :
        if self.motion_complete is True :
            ladder_list = pygame.sprite.spritecollide(self,all_ladder_list,False)
            if len(ladder_list) >= 1 :
                self.is_climbing_up = True
                self.motion_complete = False
                self.is_climbing_down = False
                self.to_platform = self.from_platform + 1
            else :
                self.is_climbing_up = False
                self.motion_complete = True
        else :
            self.is_climbing_up = True
    
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
                self.to_platform = self.from_platform - 1
            else :
                self.is_climbing_down = False
                self.motion_complete = True
        else :
            self.is_climbing_down = True

    def loadimage(self , image_name):
        self.image = pygame.image.load(image_name)
        self.image = pygame.transform.scale(self.image,[35,35])

"""
"""
class Platform(pygame.sprite.Sprite ) :
     def __init__(self , width , height , x, y, platform_type,image_name):
        self.width = width
        self.height = height
        pygame.sprite.Sprite.__init__(self)
        if platform_type == "line" :
            self.image = pygame.Surface([width,height])
            self.image.fill(white)
            self.rect = self.image.get_rect()
            self.rect.x = x
            self.rect.y = y
        elif platform_type == "platform_picture" :
            self.image = pygame.image.load(image_name)
            self.image = pygame.transform.scale(self.image,[width,height])
            self.rect = self.image.get_rect()
            self.rect.x = x 
            self.rect.y = y


class Ladder(pygame.sprite.Sprite) :
    def __init__(self,xpoint,ypoint) :
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("ladder.png")
        self.image = pygame.transform.scale(self.image,[30,100])
        self.rect = self.image.get_rect()
        self.rect.x = xpoint
        self.rect.y = ypoint


class Coin(pygame.sprite.Sprite) :
    def __init__(self,xpoint,ypoint) :
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("coin.png")
        self.image = pygame.transform.scale(self.image,[30,30])
        self.rect = self.image.get_rect()
        self.rect.x = xpoint
        self.rect.y = ypoint
"""
def gameplay(width,height,level,background,coin_image,prev_coins) :
    alsp = pygame.sprite.Group()
    all_barrier_list = pygame.sprite.Group()
    all_platform_list = pygame.sprite.Group()
    all_ladder_list = pygame.sprite.Group()
    person_sprite_list = pygame.sprite.Group()
    all_coin_list = pygame.sprite.Group()
    all_placement_list = pygame.sprite.Group()
    all_fireball_list = pygame.sprite.Group()
    queen_list = pygame.sprite.Group()

    board = Board(height,width,all_barrier_list,all_platform_list,all_ladder_list,all_coin_list,prev_coins)
    door = Door()
    player = Player(board.height,"mario_standing.png",35)
    alsp.add(door)
    
    queen = Queen(board.platform_dict,"queen.png",35)
    donkey= Donkey(board.platform_dict,"dkong.png",45)
    person_sprite_list.add(player)
    person_sprite_list.add(donkey)
    person_sprite_list.add(queen)
    alsp.add(all_barrier_list)
    alsp.add(all_ladder_list)
    queen_list.add(queen)

    mainloop = False 
    make_fire = 0
    while not mainloop:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                mainloop = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    mainloop = True
                if event.key == pygame.K_a:
                    #player.loadimage("mario_left.png")
                    player.motion(-7,0)
                if event.key == pygame.K_w :
                    player.climb_up(all_ladder_list,board.platform_dict)
                if event.key == pygame.K_s :
                    player.climb_down(all_ladder_list,board.platform_dict)
                if event.key == pygame.K_d:
                   # player.loadimage("mario_right.png")
                    player.motion(7,0) 
                if event.key == pygame.K_SPACE:
                    if player.speed_y ==0 :
                        player.motion(0,-10)
            if event.type == pygame.KEYUP:
                #player.loadimage("mario_standing.png")
                if event.key == pygame.K_a:
                    if(player.speed_x !=0) :
                        player.speed_x = 0
                if event.key == pygame.K_d:
                    if(player.speed_x !=0) :
                        player.speed_x = 0
                if event.key == pygame.K_SPACE:
                    if(player.speed_y !=0) :
                        player.speed_y = 0
                if event.key == pygame.K_w :
                    player.is_climbing_up = False
                    player.speed_y = 0
                if event.key == pygame.K_s:
                    player.is_climbing_down = False
                    player.speed_y = 0
            print (event)
        
        donkey.update(board.platform_dict)
        if  make_fire == 0 :
            fire = Fireballs(donkey.rect.x,donkey.rect.y)
            person_sprite_list.add(fire)
            all_fireball_list.add(fire)
        if make_fire == 100 :
            make_fire = -1
        make_fire += 1
        for fireballs in all_fireball_list :
            fireballs.motion(all_barrier_list,all_ladder_list,all_fireball_list,person_sprite_list)

        door.remove_fireballs(all_fireball_list)
        player.update(all_barrier_list,all_coin_list,all_ladder_list,board.platform_dict,all_fireball_list)
        board.update(alsp,person_sprite_list,all_coin_list,all_ladder_list,background,level,player.coin_list,coin_image,prev_coins,player.fireball_list)
        pygame.display.update()
        hit_queen = pygame.sprite.spritecollide(player,queen_list,False)
        if len(hit_queen) > 0 :
            return (board.coins) ;
    pygame.quit()
    quit()


def main() :

    width = 1800
    height = 800
    background = Images("type4.jpg",[0,0],height,width)
    coin_image = Images("coin.png",[90,180],40,40)
    flag = True
    level = 1
    prev_coins = 0
    while flag is True :
        print (level)
        prev_coins = gameplay(width,height,level,background,coin_image,prev_coins)
        level += 1
main()


