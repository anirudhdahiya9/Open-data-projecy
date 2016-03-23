import pygame
from pygame.locals import *

#show message after completion of a level
def message_to_screen(msg,color,frame):
         font=pygame.font.SysFont(None,30)
         screen_text=font.render(msg, True, color)
         frame.gameDisplay.blit(screen_text, [frame.display_width/3,frame.display_height/2])


#show the current score of player
def show_score(msg,color,frame):
         font=pygame.font.SysFont(None,30)
         screen_text=font.render(msg, True, color)
         frame.gameDisplay.blit(screen_text, [3*frame.display_width/4,5*frame.block_size])


#show the number of lives of player
def show_lives(msg,color,frame):
         font=pygame.font.SysFont(None,30)
         screen_text=font.render(msg, True, color)
         frame.gameDisplay.blit(screen_text, [5*frame.block_size,5*frame.block_size])

#show the current level
def show_level(msg,color,frame):
         font=pygame.font.SysFont(None,30)
         screen_text=font.render(msg, True, color)
         frame.gameDisplay.blit(screen_text, [frame.display_width/2-4*frame.block_size,4*frame.block_size])


#show the score after completion of mission
def level_score(msg,color,frame):
         font=pygame.font.SysFont(None,30)
         screen_text=font.render(msg, True, color)
         frame.gameDisplay.blit(screen_text, [frame.display_width/2-4*frame.block_size,frame.display_height/2+2*frame.block_size])



#check collision of 2 objects
def checkcollision(x,y,a,b,frame):
        if abs(x-a)<=frame.block_size and abs(y-b)<frame.block_size:
                return 1
        else:
                return 0


#check coin collection
def collectcoin(x,y,a,b,frame):
        if abs(x-a)<frame.block_size and abs(y-b)<frame.block_size:
                return 1
        else:
                return 0


#check wall collision
def checkwall(x,y,frame):
        if x>frame.display_width-2*frame.block_size:
                return 1
        if x<frame.block_size:
                return 2
        return 0


#check airspace contact above ladders
def checkair(x,y,frame):
        if x==3*frame.w or x==3*frame.w+frame.block_size:
                if (y < frame.display_height-frame.h-frame.block_size and y > frame.display_height-2*frame.h-frame.block_size ) or (y < frame.display_height-3*frame.h-frame.block_size  and y > frame.display_height-4*frame.h-frame.block_size ) or (y < frame.display_height-5*frame.h-frame.block_size ):
                        return 1
                
        if x==2*frame.w or x==2*frame.w+frame.block_size:
                if (y > frame.display_height-frame.h-frame.block_size ) or (y < frame.display_height-2*frame.h-frame.block_size  and y > frame.display_height-3*frame.h-frame.block_size ) or (y < frame.display_height-4*frame.h-frame.block_size  and y > frame.display_height-5*frame.h-frame.block_size ) or y < frame.display_height-6*frame.h-frame.block_size :
                        return 1
        return 0

