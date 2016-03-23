import sys
import os
import termios
def getchar():

    fd = sys.stdin.fileno()

    if os.isatty(fd):

        old = termios.tcgetattr(fd)
        new = termios.tcgetattr(fd)
        new[3] = new[3] & ~termios.ICANON & ~termios.ECHO
        new[6] [termios.VMIN] = 1
        new[6] [termios.VTIME] = 0

        try:
            termios.tcsetattr(fd, termios.TCSANOW, new)
            termios.tcsendbreak(fd,0)
            ch = os.read(fd,7)

        finally:
            termios.tcsetattr(fd, termios.TCSAFLUSH, old)
    else:
        ch = os.read(fd,7)

    return(ch)

life = 2
level = 1

def print_board(Matrix):
    for i in range(30):
        for j in range(90):
            if Matrix[i][j] == 'X':
                print '\033[1;41mX\033[1;m',
                sys.stdout.write("")
            elif Matrix[i][j] == 'P':
                print '\033[1;32mP\033[1;m',
                sys.stdout.write("")
            elif Matrix[i][j] == 'O':
                print '\033[1;31mO\033[1;m',
                sys.stdout.write("")
            elif Matrix[i][j] == 'C':
                print '\033[1;33mC\033[1;m',
                sys.stdout.write("")
            elif Matrix[i][j] == 'H':
                print '\033[1;37mH\033[1;m',
                sys.stdout.write("")
            elif(Matrix[i][j] == 'Q'):
                print '\033[1;36mQ\033[1;m',
                sys.stdout.write("")
            else :
                print Matrix[i][j],
                sys.stdout.write("")

        print "\n",

def checkWall(x,y,Matrix):
    if Matrix[x][y] == 'X':
        return 1
    else:
        return 0
