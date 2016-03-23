'''
Donkey Kong Game
    -ABHINAV AGGARWAL
    -201401128
'''


from board import *
from person import *
from kbhit import * 
import os
import time
from random import randint

level=1
score=0
def main():
    global score
    global level
    S=Screen(score,level)
    P=Player()
    D=Donkey()
    gameover=0     
    frame_move=0 # to slow down the movement of donkey
    Balls=[]
    kb=KBHit()
    collected_coins=[]
    while True:
        Dpos=D.get_position()
        Ppos=P.get_position()
        if S.fixedMAP[Ppos[0]][Ppos[1]]=='Q':
            score=S.get_score()+50
            if level==2:
                s="\033[1m"+"CONGRATULATIONS! YOU WIN"+"\033[0m"
                print s.center(180)
            return 0
        if Dpos==Ppos:
            gameover=1
        for b in Balls:
            Bpos=b.get_position()
            if Bpos==Ppos:
                gameover=1
        if gameover==1:
            gameover=0
            P.lives-=1
            score=S.get_score()-25
            S.update_score(-25)
            if P.lives==0:
                os.system("printf '\033c'")
                S.print_scr(P) 
                return 1
            P.reset(S)

        os.system("printf '\033c'")
        S.print_scr(P) 
        
        if frame_move%8==0:
            
            Dpos=D.get_position()
            if Dpos[1]==12:
                D.drop_ball(S,Balls)
                D.isball=0
                D.direction=-1
            elif D.isball==1 and Dpos[1]!=2:
                if randint(1,1000)%8==0:
                    D.drop_ball(S,Balls)
                    D.isball=0
                    D.direction=-1
            elif D.direction==-1 and Dpos[1]==2:
                D.isball=1
                D.direction=1
            D.move(S)
            
            for b in Balls:
                if b.direction==0 and b.on_ground(S)==0:
                    b.fall_down(S)
                else:
                    if b.direction==0 and b.on_ground(S)==1:
                        b.direction=randint(1,1000)%2
                        if b.direction==0:
                            b.direction=-1
                    if b.on_ladder(S)==1:
                        if randint(1,1000)%2==0:
                            b.fall_down(S)
                        else:
                            b.move_lr(S)
                    else:
                        b.move_lr(S)
                if b.on_ground(S)==0:
                    b.direction=0
                Bpos=b.get_position()
                if Bpos==(24,4):
                    Balls.remove(b)
                    S.MAP[Bpos[0]][Bpos[1]]=' '

        frame_move+=1
        
        if kb.kbhit():                                        #checks if there is a keypress on the keyboard
            c = kb.getch()
            termios.tcflush(sys.stdin, termios.TCIOFLUSH)     #flushes the input buffer    
            
            if ord(c) == 27 or c=='q': # ESC
                return 1
            
            if c=='a':
                Ppos=P.get_position()
                if S.MAP[Ppos[0]][Ppos[1]-1]!='X' and ( S.MAP[Ppos[0]+1][Ppos[1]-1]=='X' or S.MAP[Ppos[0]+1][Ppos[1]-1]=='H'):
                    P.move_left(S)
            
            elif c=='d':
                Ppos=P.get_position()
                if S.MAP[Ppos[0]][Ppos[1]+1]!='X' and ( S.MAP[Ppos[0]+1][Ppos[1]+1]=='X' or S.MAP[Ppos[0]+1][Ppos[1]+1]=='H'):
                    P.move_right(S)
            
            elif c=='w' and P.onladder:
                Ppos=P.get_position()
                if not(S.fixedMAP[Ppos[0]-1][Ppos[1]]==' ' and P.onground):
                    P.climbup(S)    
            
            elif c=='s':
                Ppos=P.get_position()
                if (P.onground and S.fixedMAP[Ppos[0]+1][Ppos[1]]=='H'):
                    S.MAP[Ppos[0]][Ppos[1]]=' '
                    P.set_position(Ppos[0]+1,Ppos[1])
                    S.MAP[Ppos[0]+1][Ppos[1]]='P'
                    P.onladder=1
                    P.onground=0
                elif P.onladder and S.fixedMAP[Ppos[0]+1][Ppos[1]]=='H':
                    P.climbdown(S)
            
            elif ord(c)==32: #SPACE
                if P.onladder==0 and P.inair==0:
                    P.inair=1
                    P.onground=0
                    P.jumpstage=0
                    P.jump_hordir=0
                    count=0
                    for i in range(1,100000):                 #checks for multiple keypress in case of diagonal jumps
                        if kb.kbhit():
                            c=kb.getch()
                            if c=='d':
                                P.jump_hordir=1
                            elif c=='a':
                                P.jump_hordir=-1
                            break
            else:
                pass

        if P.inair==1:
            count+=1
            if count%3==0:
                if P.jumpstage==0:
                    P.jumpstage=1
                    P.jump(S,"up")
                    if P.jump_hordir!=0:
                        P.jump_horizontal(S)
                        Ppos=P.get_position()
                        if S.MAP[Ppos[0]+2][Ppos[1]]==' ':
                            P.set_position(Ppos[0],Ppos[1]-P.jump_hordir)
                            S.MAP[Ppos[0]][Ppos[1]]=' '
                            S.MAP[Ppos[0]][Ppos[1]-P.jump_hordir]='P'
                            P.jump_hordir=0
                elif P.jumpstage==1:
                    P.jumpstage=2
                    P.jump(S,"up")
                    if P.jump_hordir!=0:
                        P.jump_horizontal(S)
                        Ppos=P.get_position()
                        if S.MAP[Ppos[0]+3][Ppos[1]]==' ':
                            P.set_position(Ppos[0],Ppos[1]-P.jump_hordir)
                            S.MAP[Ppos[0]][Ppos[1]]=' '
                            S.MAP[Ppos[0]][Ppos[1]-P.jump_hordir]='P'
                            P.jump_hordir=0
                elif P.jumpstage==2:
                    P.jumpstage=3
                    P.jump(S,"down")
                    if P.jump_hordir!=0:
                        P.jump_horizontal(S)
                        Ppos=P.get_position()
                        if S.MAP[Ppos[0]+2][Ppos[1]]==' ':
                            P.set_position(Ppos[0],Ppos[1]-P.jump_hordir)
                            S.MAP[Ppos[0]][Ppos[1]]=' '
                            S.MAP[Ppos[0]][Ppos[1]-P.jump_hordir]='P'
                            P.jump_hordir=0
                elif P.jumpstage==3:
                    P.jumpstage=4
                    P.jump(S,"down")
                    if P.jump_hordir!=0:
                        P.jump_horizontal(S)
                        Ppos=P.get_position()
                        if S.MAP[Ppos[0]+1][Ppos[1]]==' ':
                            P.set_position(Ppos[0],Ppos[1]-P.jump_hordir)
                            S.MAP[Ppos[0]][Ppos[1]]=' '
                            S.MAP[Ppos[0]][Ppos[1]-P.jump_hordir]='P'
                            P.jump_hordir=0
                    P.inair=0
                    P.onground=1
                    P.jump_hordir=0
                Ppos=P.get_position()
                if S.fixedMAP[Ppos[0]][Ppos[1]]=='H':
                    P.onladder=1
            
        time.sleep(0.05)
    kb.set_normal_term()

#if __name__=="__main__":
#    main()

while level<=2 and __name__=="__main__":
    if main()==1:
        s="\033[1m"+"GAME OVER!"+"\033[0m"
        print s.center(180)
        break
    level+=1
