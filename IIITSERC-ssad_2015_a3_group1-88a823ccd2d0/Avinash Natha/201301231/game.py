import pygame
import board
import characters
import time

pygame.init()

white = (255,255,255)
black = (0,0,0)
red = (255,0,0)

display_width = 1200
display_height = 450

Player = characters.player()
Donkey = characters.donkey()

gameDisplay = pygame.display.set_mode((display_width, display_height+50))
pygame.display.set_caption('Donkey Kong')

block_size = 15
FPS = 20

init_y = Player.init_x                                   #display_height-2*block_size
init_x = Player.init_y                                   #2*block_size

clock = pygame.time.Clock()

font = pygame.font.SysFont(None, 20)

keys_pressed = pygame.key.get_pressed()

def text_objects(text,colour):
    textSurface = font.render(text, True, colour)
    return textSurface, textSurface.get_rect()

def message_to_screen(msg,colour):
    textSurf, textRect = text_objects(msg,colour)
    textRect.center = (display_width/2 ,display_height/2)
    gameDisplay.blit(textSurf, textRect)

def checkCollision(stage,lead_x,lead_y,firelist):
    for ball in firelist:
        if ball[1] == lead_x and ball[0] == lead_y:
            Player.collided()
            lead_x = Player.init_x
            lead_y = Player.init_y

def gameLoop(init_coins):

    lead_x = init_x
    lead_y = init_y

    lead_x_change = 0
    lead_y_change = 0

    gameExit = False
    gameOver = False

    board.stage[Donkey.pos_y][Donkey.pos_x]='D'

    loop_count = 100

    jumpFlag = 0
    
    Player.coins = init_coins
    
    firelist = []

    keys_pressed = pygame.key.get_pressed()
    
    while not gameExit:
        while gameOver == True:
            keys_pressed = pygame.key.get_pressed()
            gameDisplay.fill(white)
            message_to_screen("Are You Sure? (y/n)",red)
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        gameExit = True
                        gameOver = False
                if keys_pressed[pygame.K_y]:
                    gameExit = True
                    gameOver = False
                if keys_pressed[pygame.K_n]:
                    gameOver = False

        lead_x_change = 0
        lead_y_change = 0

        keys_pressed = pygame.key.get_pressed()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameExit = True
                
        if keys_pressed[pygame.K_SPACE]:
            if jumpFlag == 0 and board.stage[lead_y/block_size+1][lead_x/block_size] == 'X' or board.stage[lead_y/block_size+1][lead_x/block_size] == 'H':
                lead_y_change = -block_size
                jumpFlag = 1
            if board.stage[lead_y/block_size-1][lead_x/block_size] == 'X':
                lead_y_change = 0
                jumpFlag = 0

##            if event.type == pygame.KEYDOWN:
##                    if event.key == pygame.K_SPACE and jumpFlag == 0:
##                        lead_y_change = -block_size
##                        print "JUMP!!"
##                        jumpFlag = 1
##            if event.type == pygame.KEYDOWN:
##                if event.key == pygame.K_LEFT:
##                    lead_x_change = -block_size
##                    #lead_y_change = 0
##                if event.key == pygame.K_RIGHT:
##                    lead_x_change = block_size
##                    #lead_y_change = 0
##                if event.key == pygame.K_UP:
##                    lead_x_change = 0
##                if event.key == pygame.K_DOWN:
##                    lead_x_change = 0
##                if event.key == pygame.K_q:
##                    gameOver = True
##            if event.type == pygame.KEYUP:
##                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
##                    lead_x_change = 0
##                if event.key == pygame.K_DOWN or event.key == pygame.K_UP:
##                    #lead_y_change = 0
##                    pass        

        if keys_pressed[pygame.K_RIGHT]:
            lead_x_change = block_size

        if keys_pressed[pygame.K_LEFT]:
            lead_x_change = -block_size

        if keys_pressed[pygame.K_q]:
            gameOver = True       

        if keys_pressed[pygame.K_UP]:
            if board.stage[lead_y/block_size][lead_x/block_size] == 'H':
                lead_y_change = -block_size
                lead_x_change = 0
            else:
                lead_y_change = 0
                
        if keys_pressed[pygame.K_DOWN]:
            if board.stage[lead_y/block_size+1][lead_x/block_size] == 'H':
                lead_y_change = block_size
            else:
                lead_y_change = 0

        if loop_count == 100:
            ball = [Donkey.pos_y,Donkey.pos_x+1,1,0]  #3-dir flag 4-fall flag
            firelist.append(ball)
            loop_count = 0
            #print ball

        if loop_count < 100:
            loop_count += 1
        
        if (board.stage[lead_y/block_size+1][lead_x/block_size] != 'X' and board.stage[lead_y/block_size+1][lead_x/block_size] != 'H' ) and jumpFlag == 0:
            lead_y_change = block_size

        if board.stage[lead_y/block_size+1][lead_x/block_size] != 'X' and board.stage[lead_y/block_size][lead_x/block_size] == 'H':
            lead_x_change = 0
        if board.stage[lead_y/block_size+1][lead_x/block_size] == 'X' and board.stage[lead_y/block_size][lead_x/block_size] != 'H':
            lead_y_change = 0
        if board.stage[lead_y/block_size+1][lead_x/block_size] == [] and board.stage[lead_y/block_size][lead_x/block_size] == 'H':
            if keys_pressed[pygame.K_UP]:
                lead_y_change = -block_size
            else:
                lead_y_change = 0
       

##        if fallFlag == 1 and board.stage[lead_y/block_size+1][lead_x/block_size] != []:
##            lead_y_change = 0
##            fallFlag = 0
        

        if board.stage[lead_y/block_size][(lead_x/block_size)+1] == 'X' and board.stage[lead_y/block_size][lead_x/block_size] != 'H':
            lead_x_change=0
            if keys_pressed[pygame.K_LEFT]:
                lead_x_change = -block_size

        if board.stage[lead_y/block_size][(lead_x/block_size)-1] == 'X' and board.stage[lead_y/block_size][lead_x/block_size] != 'H':
            lead_x_change=0
            if keys_pressed[pygame.K_RIGHT]:
                    lead_x_change = block_size


##        if keys_pressed[pygame.K_SPACE]:
##            if jumpFlag == 0:
##                print "JUMP!!"
##                lead_y_change = -block_size
##                jumpFlag = 1
##            else:
##                print "NO JUMP!!"
##                lead_y_change = 0
                    
##        if jumpFlag == 10 and board.stage[lead_y/block_size+1][lead_x/block_size] == 'X':
##            lead_y_change = 0
##            jumpFlag == 0
##        elif jumpFlag == 10:
##            lead_y_change = block_size 
        
        if jumpFlag == 3:
            lead_y_change = 0
            jumpFlag = 0

        if jumpFlag == 2:
            lead_y_change = -block_size
            jumpFlag = 3
            if board.stage[lead_y/block_size-1][lead_x/block_size] == 'X':
                lead_y_change = block_size
                jumpFlag = 0

        if jumpFlag == 1:
            lead_y_change = -block_size
            jumpFlag = 2                 
          
        for fireball in firelist:
            if fireball[3] == 0:
                if board.stage[fireball[0]+1][fireball[1]] == [] :
                    fireball[3] = 1
                    fireball[0] += 1
                else:
                    fireball[1] += fireball[2] 
            if fireball[3] == 1:
                if board.stage[fireball[0]+1][fireball[1]] == 'X' :
                    fireball[2] = -1*fireball[2]
                    fireball[3] = 0
                    fireball[1] += fireball[2]
                else:
                    fireball[0] += 1
            
        
            #print fire[1]," ",fire[0]

        #pygame.display.update()

        #print loop_count,"loop",len(firelist)
        
        lead_x += lead_x_change
        lead_y += lead_y_change

        if board.stage[lead_y/block_size][lead_x/block_size] == 'C' :
            Player.collectCoin()
            board.stage[lead_y/block_size][lead_x/block_size] = []

        if board.stage[lead_y/block_size][lead_x/block_size] == 'Q' :
            gameLoop(Player.coins+50)

        checkCollision(board.stage,lead_x,lead_y,firelist)
        
        Player.pos_x = lead_x
        Player.pos_y = lead_y

        checkCollision(board.stage,lead_x,lead_y,firelist)
        
        gameDisplay.fill(white)
        #pygame.draw.rect(gameDisplay,black,[lead_x,lead_y,block_size,block_size])
        player = font.render('P', True, black)
        gameDisplay.blit(player,(lead_x,lead_y))
        
        score_str = "Score :"+str(Player.coins)
        score = font.render(score_str, True, black)
        gameDisplay.blit(score,((display_width)/3,(display_height)+25))
        #del(score_str)

        for i in range(display_height/block_size):
            for j in range(display_width/block_size):
                #if board.stage[i][j] != []:
                    #sample = ""
                    #sample = sample.join(board.stage[i][j])
                    renboard=font.render(board.stage[i][j], True, black)
                    gameDisplay.blit(renboard,(j*block_size,i*block_size))
                    #del(sample)

        for fire in firelist:
            ball = font.render('O', True, black)
            gameDisplay.blit(ball,(fire[1]*block_size,fire[0]*block_size))

        pygame.display.update()

        clock.tick(10)

    pygame.quit()
    quit()

gameLoop(0)
