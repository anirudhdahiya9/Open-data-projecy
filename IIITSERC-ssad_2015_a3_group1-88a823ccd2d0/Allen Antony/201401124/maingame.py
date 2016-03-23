import pygame
import random
from images import *
from fireball import *  
from board import *
from colors import *
from characters import *
""" Importing all the necessary modules """

pygame.init()                                        #initalizing pygame
clock = pygame.time.Clock()                          #setting the clock to manage frames per second



""" The Main Game : This is where the core of the game is """

def gameplay(width,height,level,background,coin_image,prev_coins,heart_image,speed,frequency) :
            
   
    """ Creating all the sprite lists """
    
    alsp = pygame.sprite.Group()
    all_barrier_list = pygame.sprite.Group()
    all_platform_list = pygame.sprite.Group()
    all_ladder_list = pygame.sprite.Group()
    person_sprite_list = pygame.sprite.Group()
    all_coin_list = pygame.sprite.Group()
    all_placement_list = pygame.sprite.Group()
    all_fireball_list = pygame.sprite.Group()
    queen_list = pygame.sprite.Group()

    board = Board(height,width,all_barrier_list,all_platform_list,all_ladder_list,all_coin_list,prev_coins)     #Creating the basic Board
    door = Door()                                                                                               #Creating the Door
    player = Player(board.height,"mario_standing.png",35)                                                       #Creating the player
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

        """ This is the main-game loop : It accounts for event managing """
       
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                mainloop = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    mainloop = True
                if event.key == pygame.K_a:
                    #player.loadimage("mario_left.png")                             #uncomment this line to have another image when player is moving left
                    if player.motion_complete is True :
                        player.motion(-7,0)
                if event.key == pygame.K_w :
                    player.climb_up(all_ladder_list,board.platform_dict)
                if event.key == pygame.K_s :
                    player.climb_down(all_ladder_list,board.platform_dict)
                if event.key == pygame.K_d:
                   # player.loadimage("mario_right.png")                            #uncomment this line to have another image when player is moving right
                    if player.motion_complete is True :
                        player.motion(7,0) 
                if event.key == pygame.K_SPACE:
                    if player.motion_complete is True :
                        if player.speed_y ==0 :
                            player.motion(0,-10)
            if event.type == pygame.KEYUP:
                #player.loadimage("mario_standing.png")                             #uncomment this line to have another picture when mario is standing
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
        

        """ Making the fireballs """
        donkey.update(board.platform_dict)
        if  make_fire == 0 :
            fire = Fireballs(donkey.rect.x,donkey.rect.y)
            person_sprite_list.add(fire)
            all_fireball_list.add(fire)
        if make_fire == frequency :
            make_fire = -1
        make_fire += 1
        for fireballs in all_fireball_list :
            fireballs.motion(all_barrier_list,all_ladder_list,all_fireball_list,person_sprite_list,speed)
        door.remove_fireballs(all_fireball_list)

        """ Updating the Player and the Board"""

        player.update(all_barrier_list,all_coin_list,all_ladder_list,board.platform_dict,all_fireball_list)
        board.update(alsp,person_sprite_list,all_coin_list,all_ladder_list,background,level,player.coin_list,coin_image,prev_coins,player.fireball_list,player.life,heart_image)
        pygame.display.update()
        [queenx,queeny] = queen.getPosition()
        hit_queen = pygame.sprite.spritecollide(player,queen_list,False)
        if len(hit_queen) > 0 :
            board.coins += 50
            return (board.coins) ;
    pygame.quit()
    quit()


def main() :

    width = 1800
    height = 800
    background = Images("type4.jpg",[0,0],height,width)
    coin_image = Images("coin.png",[90,180],40,40)
    heart_image = Images("heart.png",[90,230],40,40)
    flag = True
    level = 1
    prev_coins = 0
    frequency = 150
    speed = 3
    while flag is True :
        print (level)
        prev_coins = gameplay(width,height,level,background,coin_image,prev_coins,heart_image,speed,frequency)
        level += 1
        speed += 1
        frequency -= 20
main()


