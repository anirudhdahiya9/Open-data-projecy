import random

def build_stage(stage,startx,starty,endx,endy,ele):
    if startx == endx:
        for i in range(endy-starty):
            stage[i+starty][startx] = ele 
    if starty == endy:
        for i in range(endx-startx):
            stage[starty][i+startx] = ele
        
display_width = 1200
display_height = 450
block_size = 15

stage = [[[] for i in range(display_width/block_size)] for i in range(display_height/block_size)] # [height - y][width - x]

##for i in range(display_height/block_size):
##    for j in range(display_width/block_size):
##        if i == 0 or j == 0 or i == (display_height/block_size)-1 or j == (display_width/block_size)-1:
##            stage[i][j] = 'X'
##        else:
##            stage[i][j] = ''

##WALLS AND FLOORS
build_stage(stage,0,0,display_width/block_size,0,'X')
build_stage(stage,0,0,0,display_height/block_size,'X')
build_stage(stage,0,display_height/block_size-1,display_width/block_size-1,display_height/block_size-1,'X')
build_stage(stage,display_width/block_size-1,0,display_width/block_size-1,display_height/block_size,'X')

build_stage(stage,display_width/(4*block_size),0,display_width/(4*block_size),2,'X')
build_stage(stage,display_width/(4*block_size)+9,0,display_width/(4*block_size)+9,2,'X')
build_stage(stage,display_width/(4*block_size),2,display_width/(4*block_size)+10,2,'X')                                  # display_width/block_size
build_stage(stage,1,5,(65*display_width)/(110*block_size),5,'X')                                                         # display_height/block_size 
build_stage(stage,display_width/(11*block_size),9,display_width/block_size,9,'X')
build_stage(stage,1,13,(8*display_width)/(11*block_size),13,'X')
build_stage(stage,(2*display_width)/(11*block_size),17,display_width/block_size,17,'X')
build_stage(stage,1,21,(7*display_width)/(11*block_size),21,'X')
build_stage(stage,(display_width)/(3*block_size),25,display_width/block_size,25,'X')

##LADDERS
build_stage(stage,display_width/(4*block_size)+7,2,display_width/(4*block_size)+7,5,'H')
build_stage(stage,(display_width)/(3*block_size)+5,25,(display_width)/(3*block_size)+5,29,'H')
build_stage(stage,(display_width)/(3*block_size)+20,21,(display_width)/(3*block_size)+20,25,'H')
build_stage(stage,(display_width)/(3*block_size)+14,20,(display_width)/(3*block_size)+14,21,'H')
build_stage(stage,(display_width)/(3*block_size)+14,17,(display_width)/(3*block_size)+14,19,'H')
build_stage(stage,(3*display_width)/(11*block_size),17,(3*display_width)/(11*block_size),21,'H')
build_stage(stage,(3*display_width)/(11*block_size)+10,15,(3*display_width)/(11*block_size)+10,17,'H')
build_stage(stage,(3*display_width)/(11*block_size)+10,13,(3*display_width)/(11*block_size)+10,14,'H')
build_stage(stage,(display_width)/(3*block_size)+28,13,(display_width)/(3*block_size)+28,17,'H')
build_stage(stage,(3*display_width)/(11*block_size)-5,9,(3*display_width)/(11*block_size)-5,13,'H')
build_stage(stage,(3*display_width)/(11*block_size)+22,5,(3*display_width)/(11*block_size)+22,9,'H')
build_stage(stage,(3*display_width)/(11*block_size)-10,5,(3*display_width)/(11*block_size)-10,7,'H')
build_stage(stage,(3*display_width)/(11*block_size)-10,8,(3*display_width)/(11*block_size)-10,9,'H')

#COINS
stage[28][random.randrange(1,(display_width)/(3*block_size)+4)] = 'C'
stage[28][random.randrange((display_width)/(3*block_size)+6,display_width/block_size-1)] = 'C'
stage[28][random.randrange((display_width)/(3*block_size)+6,display_width/block_size-1)] = 'C'
stage[24][random.randrange((display_width)/(3*block_size)+1,(display_width)/(3*block_size)+19)] = 'C'
stage[24][random.randrange((display_width)/(3*block_size)+21,display_width/block_size-1)] = 'C'
stage[24][random.randrange((display_width)/(3*block_size)+21,display_width/block_size-1)] = 'C'
stage[20][random.randrange((display_width)/(3*block_size)+15,(7*display_width)/(11*block_size))] = 'C'
stage[20][random.randrange((3*display_width)/(11*block_size)+1,(display_width)/(3*block_size)+13)] = 'C'
stage[20][random.randrange(1,(3*display_width)/(11*block_size)-1)] = 'C'
stage[16][random.randrange((2*display_width)/(11*block_size)+1,(3*display_width)/(11*block_size)+9)] = 'C'
stage[16][random.randrange((3*display_width)/(11*block_size)+11,(display_width)/(3*block_size)+27)] = 'C'
stage[16][random.randrange((display_width)/(3*block_size)+29,display_width/block_size)] = 'C'
stage[12][random.randrange(1,(3*display_width)/(11*block_size)-6)] = 'C'
stage[12][random.randrange((3*display_width)/(11*block_size)-6,(8*display_width)/(11*block_size))] = 'C'
stage[12][random.randrange((3*display_width)/(11*block_size)-6,(8*display_width)/(11*block_size))] = 'C'
stage[8][random.randrange(display_width/(11*block_size)+1,(3*display_width)/(11*block_size)-11)] = 'C'
stage[8][random.randrange((3*display_width)/(11*block_size)-9,(3*display_width)/(11*block_size)+21)] = 'C'
stage[8][random.randrange((3*display_width)/(11*block_size)+23,display_width/block_size-1)] = 'C'
stage[4][random.randrange(display_width/(4*block_size)+8,(65*display_width)/(110*block_size))] = 'C'
stage[4][random.randrange(display_width/(4*block_size)+8,(65*display_width)/(110*block_size))] = 'C'

#QUEEN

stage[1][display_width/(4*block_size)+3] = 'Q' 

##for i in range(display_height/block_size):
##    for j in range(display_width/block_size):
##        print stage[i][j],
##    print '\n'
