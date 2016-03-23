import threading
import time
from random import randint
from board import *
from classes import *
from functions import *
import os


class donkeyThread(threading.Thread):
    def __init__(self,threadId,name,donkey,board,playerThread):
        threading.Thread.__init__(self)
        self.__threadId = threadId
        self.__name = name
        self.__statusChecker = playerThread
        self.__donkey = donkey
        self.__board = board
    def getThreadName(self):
        return self.__name
    def run(self):
        counter = 0
        while self.__statusChecker.isAlive():
            move = randint(0,1)
            present_pos = self.__donkey.getPosition()
            counter = 0
            while counter < 58:
                present_pos = self.__donkey.getPosition()
                self.__board[present_pos[0]][present_pos[1]] = self.__donkey.showPrevious()
                self.__donkey.setPrevious(self.__board[present_pos[0]][present_pos[1] + 1])
                self.__donkey.setPositon([present_pos[0],present_pos[1] + 1])
                print self.__donkey.getPosition()
                self.__board[present_pos[0]][present_pos[1] + 1] = self.__donkey.sym()
                os.system("printf \033c")
                printBoard(self.__board)
                time.sleep(0.5)
                counter = counter + 1
            while counter >= 0:
                present_pos = self.__donkey.getPosition()
                self.__board[present_pos[0]][present_pos[1]] = self.__donkey.showPrevious()
                self.__donkey.setPrevious(self.__board[present_pos[0]][present_pos[1] - 1])
                self.__donkey.setPositon([present_pos[0],present_pos[1] - 1])
                self.__board[present_pos[0]][present_pos[1] - 1] = self.__donkey.sym()
                os.system("printf \033c")
                printBoard(self.__board)
                time.sleep(0.5)
                counter = counter - 1

class playerThread(threading.Thread):
    def __init__(self,threadId,name,player,board):
        threading.Thread.__init__(self)
        self.__threadId = threadId
        self.__name = name
        self.__new_player = player
        self.__board = board
    def getThreadName(self):
        return self.__name 
    def run(self):
        move = " "
        printBoard(self.__board)
        while move != "q":
            move = getchar()
            if move == "a":
                present_pos = self.__new_player.getPosition()
                if self.__board[present_pos[0]][present_pos[1] - 1] == "D":
                    endscreen("Lost")
                    exit()
                elif self.__board[present_pos[0]][present_pos[1] - 1] == "Q":
                    enscreen("Won")
                elif checkWall(self.__board,present_pos,"left"):
                    pass
                elif not checkBase(self.__board,present_pos,"left"):
                    x = present_pos[0] + 1
                    y = present_pos[1] - 1
                    down_count = 0
                    while self.__board[x][y] != "X":
                        x = x + 1
                        down_count = down_count + 1
                    self.__board[present_pos[0]][present_pos[1]] = self.__new_player.showPrevious()
                    if self.__board[present_pos[0]][present_pos[1] - 1] == "C":
                        self.__new_player.Increase_score()
                        self.__new_player.setPrevious(" ")
                        self.__board[present_pos[0]][present_pos[1] - 1 ] = self.__new_player.sym()
                    else:
                        self.__new_player.setPrevious(self.__board[present_pos[0]][present_pos[1] - 1])
                        self.__board[present_pos[0]][present_pos[1] - 1] = self.__new_player.sym()
                    self.__new_player.setPositon([present_pos[0],present_pos[1] - 1])
                    os.system("printf \033c")
                    printBoard(self.__board)
                    for i in xrange(0,down_count):
                        present_pos = self.__new_player.getPosition()
                        self.__board[present_pos[0]][present_pos[1]] = self.__new_player.showPrevious()
                        self.__new_player.setPrevious(self.__board[present_pos[0] + 1][present_pos[1]])
                        self.__new_player.setPositon([present_pos[0] + 1,present_pos[1]])
                        self.__board[present_pos[0] + 1][present_pos[1]] = self.__new_player.sym()
                        os.system("printf \033c")
                        printBoard(self.__board)
                        time.sleep(0.1)
                else:
                    self.__board[present_pos[0]][present_pos[1]] = self.__new_player.showPrevious()
                    if self.__board[present_pos[0]][present_pos[1] - 1] == "C":
                        self.__new_player.Increase_score()
                        self.__new_player.setPrevious(" ")
                        self.__board[present_pos[0]][present_pos[1] - 1 ] = self.__new_player.sym()
                    else:
                        self.__new_player.setPrevious(self.__board[present_pos[0]][present_pos[1] - 1])
                        self.__board[present_pos[0]][present_pos[1] - 1] = self.__new_player.sym()
                    self.__new_player.setPositon([present_pos[0],present_pos[1] - 1])
                    os.system("printf \033c")
                    printBoard(self.__board)
            elif move == "d":
                present_pos = self.__new_player.getPosition()
                if checkWall(self.__board,present_pos,"right"):
                    pass
                elif not checkBase(self.__board,present_pos,"right"):
                    x = present_pos[0] + 1
                    y = present_pos[1] + 1
                    count_down = 0
                    while self.__board[x][y] != "X":
                        x = x + 1
                        count_down = count_down + 1
                    self.__board[present_pos[0]][present_pos[1]] = self.__new_player.showPrevious()
                    if self.__board[present_pos[0]][present_pos[1] + 1] == "C":
                        self.__new_player.Increase_score()
                        self.__new_player.setPrevious(" ")
                        self.__board[present_pos[0]][present_pos[1] + 1] = self.__new_player.sym()
                    else:
                        self.__new_player.setPrevious(self.__board[present_pos[0]][present_pos[1] + 1])
                        self.__board[present_pos[0]][present_pos[1] + 1] = self.__new_player.sym()
                    self.__new_player.setPositon([present_pos[0],present_pos[1] + 1])
                    os.system("printf \033c")
                    printBoard(self.__board)
                    for i in xrange(0,count_down):
                        present_pos = self.__new_player.getPosition()
                        self.__board[present_pos[0]][present_pos[1]] = self.__new_player.showPrevious()
                        if self.__board[present_pos[0] + 1][present_pos[1]] == "C":
                            self.__new_player.Increase_score()
                            self.__new_player.setPrevious(" ")
                            self.__board[present_pos[0] + 1][present_pos[1]] = self.__new_player.sym()
                        else:
                            self.__new_player.setPrevious(self.__board[present_pos[0] + 1][present_pos[1]])
                            self.__new_player.setPositon([present_pos[0] + 1,present_pos[1]])
                            self.__board[present_pos[0] + 1][present_pos[1]] = self.__new_player.sym()
                            os.system("printf \033c")
                            printBoard(self.__board)
                            time.sleep(0.1)
                else:
                    self.__board[present_pos[0]][present_pos[1]] = self.__new_player.showPrevious()
                    if self.__board[present_pos[0]][present_pos[1] + 1] == "C":
                        self.__new_player.Increase_score()
                        self.__new_player.setPrevious(" ")
                        self.__board[present_pos[0]][present_pos[1] + 1] = self.__new_player.sym()
                    else:
                        self.__new_player.setPrevious(self.__board[present_pos[0]][present_pos[1] + 1])
                        self.__board[present_pos[0]][present_pos[1] + 1] = self.__new_player.sym()
                    self.__new_player.setPositon([present_pos[0],present_pos[1] + 1])
                    os.system("printf \033c")
                    printBoard(self.__board)
            elif move == "w":
                present_pos = self.__new_player.getPosition()
                if checkWall(self.__board,present_pos,"up"):
                    pass
                else:
                    if self.__new_player.showPrevious() == "H":
                        self.__board[present_pos[0]][present_pos[1]] = self.__new_player.showPrevious()
                        if self.__board[present_pos[0] - 1][present_pos[1]] == "C":
                            self.__new_player.Increase_score()
                            self.__new_player.setPrevious(" ")
                            self.__board[present_pos[0] - 1][present_pos[1]] = " "
                        self.__new_player.setPrevious(self.__board[present_pos[0] - 1][present_pos[1]])
                        self.__new_player.setPositon([present_pos[0]-1,present_pos[1]])
                        self.__board[present_pos[0] - 1][present_pos[1]] = self.__new_player.sym()
                        os.system("printf \033c")
                        printBoard(self.__board)
                    else:
                        pass
            elif move == "s":
                present_pos = self.__new_player.getPosition()
                if checkWall(self.__board,present_pos,"down"):
                    pass
                else:
                    if  self.__board[present_pos[0] + 1][present_pos[1]] == "H":
                        self.__board[present_pos[0]][present_pos[1]] = self.__new_player.showPrevious()
                        self.__new_player.setPrevious(self.__board[present_pos[0] + 1][present_pos[1]])
                        self.__new_player.setPositon([present_pos[0] + 1,present_pos[1]])
                        self.__board[present_pos[0] + 1][present_pos[1]] = self.__new_player.sym()
                        os.system("printf \033c")
                        printBoard(self.__board)
                    else:
                        pass
            elif move == " ":

                present_pos = self.__new_player.getPosition()
                if (self.__board[present_pos[0] + 1][present_pos[1]] == "X" or (self.__board[present_pos[0] + 1][present_pos[1]] == "H" and self.__new_player.showPrevious() == " " and self.__board[present_pos[0] - 1][present_pos[1]] != "H")) and self.__new_player.showPrevious() == " ":
                    x = present_pos[0]
                    y = present_pos[1]
                    count_up = 0
                    while self.__board[x][y] != "X" and count_up < 3:
                        x = x - 1
                        count_up = count_up + 1
                    for i in xrange(0,count_up - 1):
                        present_pos = self.__new_player.getPosition()
                        self.__board[present_pos[0]][present_pos[1]] = self.__new_player.showPrevious()
                        if self.__board[present_pos[0] - 1][present_pos[1]] == "C":
                            self.__new_player.Increase_score()
                            self.__new_player.setPrevious(" ")
                            self.__board[present_pos[0] - 1][present_pos[1]] = " "
                        self.__new_player.setPrevious(self.__board[present_pos[0] - 1][present_pos[1]])
                        self.__new_player.setPositon([present_pos[0]-1,present_pos[1]])
                        self.__board[present_pos[0] - 1][present_pos[1]] = self.__new_player.sym()
                        os.system("printf \033c")
                        printBoard(self.__board)
                        time.sleep(0.1)
                    for i in xrange(0,count_up - 1):
                        present_pos = self.__new_player.getPosition()
                        self.__board[present_pos[0]][present_pos[1]] = self.__new_player.showPrevious()
                        self.__new_player.setPrevious(self.__board[present_pos[0] + 1][present_pos[1]])
                        self.__new_player.setPositon([present_pos[0] + 1,present_pos[1]])
                        self.__board[present_pos[0] + 1][present_pos[1]] = self.__new_player.sym()
                        os.system("printf \033c")
                        printBoard(self.__board)
                        time.sleep(0.1)
