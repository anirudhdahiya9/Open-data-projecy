###############################################################################
#  Documentation                                                              #
#                                                                             #
#  Pygame was used to make this game. To run the game simply run main.py. See #
#  the README file for further details                                        #
###############################################################################

# Importing the required system modules
import os
from random import randint, random
import pygame
import sys

# Importing custom modules
from character import *
from objects import *

# Starting pygame
pygame.init()


# All game functions maintained in one main class
class MainGameClass:
    """The main game class, holding the screen object and dimensions, as well as
       Everything that appears on the screen. This contains objects of players
       and hazards.
    """
    # Some values that decide the dimensions of the game field
    walls_thickness = 8
    floor_thickness = 15
    width = 1240
    height = 560

    # Intitialising the empty lists, for readability
    fireballs = []
    coins = []
    floor_tops = []
    floor_bottoms = []
    ladders = []
    broken_ladders = []

    # Initial level
    level = 1

    # Character objects created
    mario = Player(10, 520)
    donkey = Villan(20, 20)
    peach = Princess(280, 5)

    def generate_coins(self):
        "Populates self.coins with random locations"
        # Divides the screen into 10 sectors, and generates 2 coins in each
        # For an even distribution of coins
        for i in range(10):
            for j in range(2):
                rand_x = randint(0, 100) + 100 * i+1
                rand_y = randint(0, 300) + 100
                self.coins += [GoldCoin(rand_x, rand_y)]

        # Generates rectangle object for each coin location
        for coin in self.coins:
            pos = coin.GetPosition()
            coin.sprite = pygame.Rect(pos[0], pos[1], 10, 10)
            if coin.sprite.collidelist(self.floor_bottoms) != -1:
                coin.move_y(-10)

    def gen_map(self):
        "Creates the map blueprint and generates floor and walls, randomly"

        # Walls
        self.left_wall = pygame.Rect(0, 0, self.walls_thickness, self.height)
        self.right_wall = pygame.Rect(self.width-self.walls_thickness, 0,
                                      self.walls_thickness, self.height)

        # Bottom floor
        self.floor_tops += [pygame.Rect(0, self.height-15,
                                        self.width, self.floor_thickness-10)]
        self.floor_bottoms += [pygame.Rect(0, self.height-10,
                                           self.width, self.floor_thickness)]

        # 1st Floor
        width = randint(0, 3) + 6
        # width = random() * 4 // 1 + 6
        end = 10 - width
        self.floor_bottoms += [pygame.Rect(0, 470, self.width/10*width,
                                           self.floor_thickness)]
        self.floor_tops += [pygame.Rect(0, 465, self.width/10*width,
                                        self.floor_thickness-10)]
        ladder_loc = random() * (width - 7) // 1 + 7
        self.ladders += [pygame.Rect(self.width/10*ladder_loc, 465, 30, 70)]

        # 2nd Floor
        width = randint(0, 3) + 6
        width = random() * 4 // 1 + 6
        end = 10 - width
        self.floor_bottoms += [pygame.Rect(self.width/10*end, 390,
                                           self.width/10*width,
                                           self.floor_thickness)]
        self.floor_tops += [pygame.Rect(self.width/10*end, 385,
                                        self.width/10*width,
                                        self.floor_thickness-10)]
        ladder_loc = random() * (width - 7) // 1 + 7
        end = 10 - ladder_loc
        self.ladders += [pygame.Rect(self.width/10*end, 385, 30, 70)]

        # 3rd Floor
        width = random() * 4 // 1 + 6
        end = 10 - width
        self.floor_bottoms += [pygame.Rect(0, 295,
                                           self.width/10*width,
                                           self.floor_thickness)]
        self.floor_tops += [pygame.Rect(0, 290, self.width/10*width,
                                        self.floor_thickness-10)]
        ladder_loc = random() * (width - 7) // 1 + 7
        self.ladders += [pygame.Rect(self.width/10*ladder_loc, 290, 30, 85)]

        # 4th Floor
        width = randint(0, 3) + 6
        width = random() * 4 // 1 + 6
        end = 10 - width
        self.floor_bottoms += [pygame.Rect(self.width/10*end, 200,
                                           self.width/10*width,
                                           self.floor_thickness)]
        self.floor_tops += [pygame.Rect(self.width/10*end, 195,
                                        self.width/10*width,
                                        self.floor_thickness-10)]
        ladder_loc = random() * (width - 7) // 1 + 7
        end = 10 - ladder_loc
        self.ladders += [pygame.Rect(self.width/10*end, 195, 30, 85)]

        # 5th Floor
        self.floor_bottoms += [pygame.Rect(0, 115,
                                           self.width/10*6,
                                           self.floor_thickness)]
        self.floor_tops += [pygame.Rect(0, 110,
                                        self.width/10*6,
                                        self.floor_thickness-10)]
        self.ladders += [pygame.Rect(self.width/10*6, 110, 30, 75)]

        # Princess Floor
        self.floor_tops += [pygame.Rect(self.width/10*2, 30,
                                        self.width/15,
                                        self.floor_thickness-10)]
        self.floor_bottoms += [pygame.Rect(self.width/10*2, 35,
                                           self.width/15,
                                           self.floor_thickness)]
        self.ladders += [pygame.Rect(self.width/10*2+self.width/15,
                                     30, 30, 70)]
        self.floor_bottoms += [pygame.Rect(self.width/10*2+self.width/15+30,
                                           35, self.width/15,
                                           self.floor_thickness)]
        self.floor_tops += [pygame.Rect(self.width/10*2+self.width/15+30, 30,
                                        self.width/15,
                                        self.floor_thickness-10)]
        # Broken Ladders
        self.broken_ladders += [pygame.Rect(self.width/10*5, 385, 30, 30)]
        self.broken_ladders += [pygame.Rect(self.width/10, 290, 30, 30)]

    def __init__(self):
        "To initialise the screen and the map"
        # The screen is init, as slightly larger than the width and height to
        # display the score, level etc.
        self.screen = pygame.display.set_mode((self.width, self.height + 100))

        # To generate a map, and fill the list with it.
        self.gen_map()

        # To generate the coins, randomly
        self.generate_coins()

        # To set the font for all displayed text
        self.font = pygame.font.SysFont("ubuntu", 30)

        # To unset the game end conditon
        self.done = 0

        # To create a clock object
        self.clock = pygame.time.Clock()

    def render_map(self):
        "Remakes each characters rectangle object"
        # To make rectangles for the characters
        pos = self.mario.GetPosition()
        self.mario.sprite = pygame.Rect(pos[0], pos[1], 10, 25)
        pos = self.donkey.GetPosition()
        self.donkey.sprite = pygame.Rect(pos[0], pos[1], 50, 50)
        pos = self.peach.GetPosition()
        self.peach.sprite = pygame.Rect(pos[0], pos[1], 10, 30)

        # To make rectangles for the good/bad objects
        for ball in self.fireballs:
            pos = ball.GetPosition()
            ball.sprite = pygame.Rect(pos[0], pos[1], 15, 15)
        for coin in self.coins:
            pos = coin.GetPosition()
            coin.sprite = pygame.Rect(pos[0], pos[1], 10, 10)

        # To draw the floors
        for floor in self.floor_bottoms:
            pygame.draw.rect(self.screen, (250, 0, 0), floor)
        for floor in self.floor_tops:
            pygame.draw.rect(self.screen, (250, 0, 0), floor)

        # To draw the walls
        pygame.draw.rect(self.screen, (250, 0, 0), self.left_wall)
        pygame.draw.rect(self.screen, (250, 0, 0), self.right_wall)

        # To draw the ladders
        for ladder in self.ladders:
            pygame.draw.rect(self.screen, (50, 0, 50), ladder)
        for broken in self.broken_ladders:
            pygame.draw.rect(self.screen, (50, 0, 50), broken)

        # To draw the fireballs
        for ball in self.fireballs:
            pygame.draw.rect(self.screen, (250, 250, 250), ball.sprite)

        # To draw the coins
        for coin in self.coins:
            # pygame.draw.rect(self.screen, (250, 250, 0),coin.sprite)
            pygame.draw.circle(self.screen, (250, 250, 0),
                               coin.GetPosition(), 5, 5)

        # To draw the characters
        if not self.done:
            pygame.draw.rect(self.screen, (0, 250, 0), self.mario.sprite)
            if self.mario.facing:
                pygame.draw.circle(self.screen, (0, 250, 0),
                                   (self.mario.GetPosition()[0] + 2,
                                    self.mario.GetPosition()[1]), 10, 10)
            else:
                pygame.draw.circle(self.screen, (0, 250, 0),
                                   (self.mario.GetPosition()[0] + 9,
                                    self.mario.GetPosition()[1]), 10, 10)
        pygame.draw.rect(self.screen, (50, 50, 0), self.donkey.sprite)
        pygame.draw.circle(self.screen, (50, 50, 0),
                           (self.donkey.GetPosition()[0] + 25,
                            self.donkey.GetPosition()[1] - 15), 20, 20)
        pygame.draw.rect(self.screen, (250, 69, 180), self.peach.sprite)
        pygame.draw.circle(self.screen, (250, 69, 180),
                           (self.peach.GetPosition()[0] + 5,
                            self.peach.GetPosition()[1] + 5), 10, 10)

        # Printing the game text
        self.screen.blit(self.font.render("Lives Left: "+str(self.mario.lives),
                                          True,
                                          (0, 128, 0)),
                         (20, self.height + 10))
        self.screen.blit(self.font.render("Score: "+str(self.mario.score),
                                          True, (0, 128, 0)),
                         (self.width-150, self.height + 10))
        self.screen.blit(self.font.render("Level: "+str(self.level), True,
                                          (0, 128, 0)), (550, self.height+10))

    def check_wall(self, character):
        """Takes a Character object and returns 0, if no collision with walls
           1 if with left wall, and 2 if with right wall
        """
        if character.sprite.colliderect(self.left_wall):
            return 1
        if character.sprite.colliderect(self.right_wall):
            return 2
        else:
            return 0

    def reset_map(self):
        "Resets the positions of all the characters."
        # Clears all the hazards
        self.fireballs = []
        self.coins = []

        # Reset to spawn point
        self.mario.SetPosition(self.mario.spawn_point)
        self.donkey.SetPosition(self.donkey.spawn_point)

        # Replaces the current map with another one
        self.floor_bottoms = []
        self.floor_tops = []
        self.ladders = []
        self.gen_map()
        self.done = 0

        # Waits for 100 ms, to avoid multiple resets with one key press
        pygame.time.delay(100)

    def user_control(self):
        "Takes the key pressed by the player and does the command"
        # Gets the currently pressed key
        pressed = pygame.key.get_pressed()

        # If touching a ladder climb up
        if pressed[pygame.K_UP]:
            if self.mario.sprite.collidelist(self.ladders) != -1:
                self.mario.move_y(-3)
        # If touching a ladder climb down
        if pressed[pygame.K_DOWN]:
            ladder_list = self.ladders + self.broken_ladders
            if self.mario.sprite.collidelist(ladder_list) != -1:
                self.mario.move_y(3)

        # Horizontal movement
        if pressed[pygame.K_a] or pressed[pygame.K_LEFT]:
            if not self.mario.sprite.colliderect(self.left_wall):
                if not self.mario.jumping:
                    self.mario.move_x(-5)
                else:
                    self.mario.move_x(-11)
                self.mario.facing = 1
        if pressed[pygame.K_d] or pressed[pygame.K_RIGHT]:
            if not self.mario.sprite.colliderect(self.right_wall):
                if not self.mario.jumping:
                    self.mario.move_x(5)
                else:
                    self.mario.move_x(11)
                self.mario.facing = 0

        # If not jumping, and not touching ladders, then jump
        # cond2 = (self.mario.sprite.collidelist(self.ladders) == -1)
        if pressed[pygame.K_SPACE] and not self.mario.jumping:
            self.mario.jump(11)

        # To exit the game
        if pressed[pygame.K_q]:
            sys.exit()
        # To reset the game
        if pressed[pygame.K_r]:
            self.mario.score = 0
            self.mario.lives = 3
            self.reset_map()

    def check_player_death(self):
        "Checks if the player is touching a hazard and takes actions, if true"
        fire_sprite_list = [x.sprite for x in self.fireballs]
        cond1 = self.mario.sprite.colliderect(self.donkey.sprite)
        cond2 = (self.mario.sprite.collidelist(fire_sprite_list) != -1)
        if cond1 or cond2:
            self.mario.lives -= 1
            self.mario.score = max(0, self.mario.score-25)
            self.mario._x = self.mario.spawn_point[0]
            self.mario._y = self.mario.spawn_point[1]
        # If no more lives, lose the game
        if not self.mario.lives:
            self.done = 1

    def check_player_win(self):
        "Checks if the player has won the game and generates the next level"
        if self.mario.sprite.colliderect(self.peach.sprite):
            self.mario.score += 50
            self.level += 1
            self.reset_map()

    def gravity(self):
        "Calculates the gravity for all the objects on the map"
        self.mario.fall(self.floor_tops+self.ladders,
                        self.floor_bottoms, self.ladders+self.broken_ladders)
        self.donkey.fall(self.floor_tops, self.floor_bottoms, self.ladders)
        for ball in self.fireballs:
            ladder_list = self.ladders+self.broken_ladders
            ball.fall(self.floor_tops, self.floor_bottoms, ladder_list)
        for coin in self.coins:
            coin.fall(self.floor_tops, self.floor_bottoms)

    def spawn_fireball(self):
        "Spawns a fireball at Donkey's current position"
        position = self.donkey.GetPosition()
        self.fireballs += [Hazard(position[0]+50, position[1])]

    def fireball_movement(self):
        "Calculates the path to be taken for each fireball"
        for ball in self.fireballs:
            if self.check_wall(ball):
                ball.direction *= -1
            ball.move_x(ball.direction*2)
        # If fireball has reached the player spawn point, despawn the it
        while 1:
            for i in range(len(self.fireballs)):
                cond1 = self.fireballs[i].GetPosition()[1] > 480
                cond2 = self.fireballs[i].GetPosition()[0] < 200
                if cond1 and cond2:
                    del self.fireballs[i]
                    break
            else:
                break

    def Collect_coins(self, index):
        "Collects coins when the player touches them"
        if index == -1:
            return
        self.mario.score += 5
        del self.coins[index]

    def GameLoop(self):
        """Main Game Loop, which is the function which calls all
           other functions, if required
         """
        while True:
            # To blank out the screen
            self.screen.fill((0, 0, 0))
            # To deal with close button event
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            # To move donkey kong randomly
            self.donkey.villan_movement()
            self.fireball_movement()

            # If the player still has lives left, take input from player.
            # Else display "game over" and ask for retry
            if not self.done:
                # To get input from the player
                self.user_control()

                # Collecting coins
                coin_list = [x.sprite for x in self.coins]
                self.Collect_coins(self.mario.sprite.collidelist(coin_list))

                #  if self.mario.score >= 100:
                #      self.mario.lives += self.mario.score/100
                #      self.mario.score %= 100

                # Randomly spawns fireballs, the rate increasing with the level
                if randint(0, 225) - self.level//5 < 1:
                    self.spawn_fireball()

                # Checking the game end conditions
                self.check_player_death()
                self.check_player_win()

            else:
                # Display message and take in [Q]uit or [R]etry as inputs
                self.screen.blit(self.font.render("GAME OVER [R]etry/[Q]uit",
                                                  True,
                                                  (128, 0, 0)),
                                 (400, self.height+50))
                pressed = pygame.key.get_pressed()
                if pressed[pygame.K_q]:
                    sys.exit()
                if pressed[pygame.K_r]:
                    self.score = 0
                    self.mario.lives = 3
                    self.reset_map()

            # To deal with jumping and collision checks
            # If not touching the floor, accelerate down
            self.gravity()

            # To display the changes and update the screen
            self.render_map()
            pygame.display.flip()
            self.clock.tick(60)

if __name__ == "__main__":
    GameScreen = MainGameClass()
    GameScreen.GameLoop()
