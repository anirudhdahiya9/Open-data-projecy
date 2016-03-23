import curses


def checkWall(board,position,move):
    if move == "left":
        if position[1] - 1 <= 0 or board[position[0]][position[1] - 1] == "X":
            return True
        else:
            return False
    elif move == "right":
        if position[1] + 1 >= 79 or board[position[0]][position[1] + 1] == "X":
            return True
        else:
            return False
    elif move == "up":
        if position[0] - 1 <= 0:
            return True
        else:
            return False


def checkBase(board,position,move):
    if move == "left":
        if board[position[0] + 1][position[1] - 1] == "X" or board[position[0] + 1][position[1] - 1] == "H":
            return True
        else:
            return False
    elif move == "right":
        if board[position[0] + 1][position[1] + 1] == "X" or board[position[0] + 1][position[1] + 1]  == "H":
            return True
        else:
            return False

def getchar():
    import tty, termios, sys
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    try:
        tty.setraw(sys.stdin.fileno())
        ch = sys.stdin.read(1)
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
    return ch


def startscreen(level):
    screen = curses.initscr()
    screen.clear()
    screen.border("X","X","X","X")
    screen.addstr(7,40,"Level %d" % level)
    screen.addstr(10,33,"Press 1 to play game!")
    screen.addstr(11,33,"Press 2 to exit")
    x = screen.getch()
    curses.endwin()

def endscreen(status):
    screen = curses.initscr()
    screen.clear()
    screen.border("X","X","X","X")
    screen.addstr(7,40,"You %s" % status)
    time.sleep(1)
    curses.endwin()
