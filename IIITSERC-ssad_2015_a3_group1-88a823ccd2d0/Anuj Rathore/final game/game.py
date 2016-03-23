import sys
import os
import random
import time     #time.sleep()

import termios
from person import *
from Board import *
from Queen import *
from Donkey import *
from Fireball import *
from Coin import *
from gen import *
from Player import *

start_time = time.time()
tracktime_start = time.time()

if __name__ == "__main__":

    print("\n\n\n\n\n\n")
    print '\t\t\033[1;41m[WELCOME TO DONKEY KONG]\033[1;m'
    print("\n\n\n\n")
    print "\033[1;42mPlay it on full screen\033[1;m",
    print "\t\t\033[1;42mPress any key to Continue...\033[1;m"
    input = getchar()
    score = 0
    while True:

        draw_layout = Board(30,90)
        draw_layout.create_board();
        coins = Coins(random.randint(6,8))
        coins.create_coins(draw_layout.get_Matrix())
        queen = Queen()
        queen.locate_queen(draw_layout.get_Matrix())
        player = Player(28,2,score)

        donkey = Donkey(4,6)
        donkey.locate_donkey(draw_layout.get_Matrix())
        track_time = 0

        fbList = []

        fb = FireBalls(donkey.getPosition(),draw_layout.get_Matrix())
        fbList.append(fb)

        player.print_player(draw_layout.get_Matrix())

        count = 1
        it = 0
        if (life == -1):
            os.system('clear')
            print("\n\n\n\n\n\n\n\n\n")
            print "\t\t\t\033[1;41mGAME OVER!!!\033[1;m"
            print("\n\n\n\n\n\n\n\n\n")
            sys.exit(0)

        while True:
            it += 1

            br=0
            donkey.movement(draw_layout.get_Matrix())

            for i in range(count):
                fbList[i].motion(donkey.getPosition(),draw_layout.get_Matrix())
                pos = fbList[i].getPosition()
                if player.checkCollision(pos,draw_layout.get_Matrix()):
                    br=1
                    score -=5
                    life -=1
                    break
            if br:
                break
            if player.collision_donkey(donkey.getPosition(),draw_layout.get_Matrix()):
                score -=5
                life -=1
                break

            player.fall(player.getPosition(),draw_layout.get_Matrix())

            if it % 100 == 41:
                if count < 4 + level:
                    fb = FireBalls(donkey.getPosition(),draw_layout.get_Matrix())
                    fbList.append(fb)
                    count = count + 1
                donkey.randomize_direction()
                start_time = time.time()

            player_position = player.getPosition()
            if (player_position[0] == 1):
                os.system('clear')
                level = level+1
                score +=10
                if (level == 3):
                    print "\n\n\n\n"
                    print "\t\t\033[1;42m[YOU SAVED THE PRINCESS]\033[1;m"
                    print("\n\n")
                    print "\t\t    \033[1;41mTHANK YOU MARIO...\033[1;m"
                    input = getchar()
                    sys.exit(0)


                else :
                    print "\n\n\n\n"
                    print "\t\t     \033[1;41m[YOU MADE DONKEY ANGRY]\033[1;m"
                    print("\n\n\n\n")
                    print "\t\t\033[1;41mNOW DONKEY WILL THROW MORE FIREBALLS\033[1;m"
                    print "\n\t\t\t  \033[1;42mLEVEL INCREASED\033[1;m"
                    print "\n\t\t     \033[1;42mPress any key to continue\033[1;m"
                    input = getchar()
                break




            os.system('clear')
            player.print_player(draw_layout.get_Matrix())
            print "SCORE : ",
            print score * 5,
            print "\t\t\t\t\t\t\t\t\tLife : ",
            print life

            input = getchar()

            if (input == 'd'):
                score = player.move_forward(draw_layout.get_Matrix())

            elif (input == 'a'):
                score = player.move_backward(draw_layout.get_Matrix())

            elif(input == 'w'):
                score = player.ascend_ladder(draw_layout.get_Matrix())

            elif(input == 's'):
                score = player.descend_ladder(draw_layout.get_Matrix())

            elif(input == ' '):
                player.jump(draw_layout.get_Matrix(),donkey)

            elif(input == 'q'):
                os.system('clear')
                print("\n\n\n\n\n\n\n\n\n")
                print "\t\t\t\033[1;41mThanks for playing the game...\033[1;m"
                print("\n\n\n\n\n\n\n\n\n")
                sys.exit(0)





            player.prev_input = input
