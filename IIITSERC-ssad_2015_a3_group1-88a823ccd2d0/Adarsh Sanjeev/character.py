from random import randint, random
import pygame


class Character:
    "The base class for all the characters"
    # Bool, To check if the player is jumping
    jumping = 0
    vertical_velocity = 0

    def __init__(self, x, y, weight=3):
        self.spawn_point = (x, y)
        # Protected variables
        self._x = x
        self._y = y
        # Weight controls the rate at which it falls down
        self.weight = weight

    def GetPosition(self):
        "Return position of the object"
        return (int(self._x), int(self._y))

    def SetPosition(self, position):
        """Takes one tuple of two integers as
           argument. Sets the position of the object
           to the value of the tuple
        """
        self._x = position[0]
        self._y = position[1]

    def move_x(self, x):
        "Takes one int as argument and adds it to the x coordinate"
        self._x += x

    def move_y(self, y):
        "Takes one int as argument and adds it to the y coordinate"
        self._y += y

    def jump(self, y):
        "Takes one argument, jumps with velocity equal to the argument"
        self.vertical_velocity -= y
        self.jumping = 1

    def fall(self, floor, floor_bottom, ladders):
        """To calculate the vertical movement of the object.
           Only argument is the list of floor, which it should stop at
        """
        # If it doesn't touch any entry of the list, fall down.
        # Else, if it just touched the floor, move the player slightly up
        # to compensate for the overlap before the function is called.
        if self.sprite.collidelist(floor) == -1:
            self.vertical_velocity += self.weight
        elif self.vertical_velocity > 0:
            self.jumping = 0
            self.vertical_velocity = 0
        # If colliding with the bottom half of the floor, move up.
        cond1 = self.sprite.collidelist(floor_bottom) != -1
        cond2 = self.sprite.collidelist(ladders) == -1
        if cond1 and cond2:
            self.move_y(-0.5)
        self.move_y(self.vertical_velocity)


class Player(Character):
    "The derived class for the player"
    score = 0
    lives = 3
    # If facing is one, face along positive x axis, else along negative
    facing = 0

    def __init__(self, x, y):
        Character.__init__(self, x, y)
        self.sprite = pygame.Rect(x, y, 10, 25)


class Villan(Character):
    "The derived class for the boss"
    # If direction is one, face along positive x axis, else along negative
    direction = 1

    def __init__(self, x, y):
        Character.__init__(self, x, y)
        self.sprite = pygame.Rect(x, y, 50, 50)

    def villan_movement(self):
        "To calculate and change the movement of the villan"
        # Checks if villan is out of bounds, or if a random int is true.
        # If yes, change direction
        x = self.GetPosition()[0]
        if x < 20 or x > 650 or randint(0, 250) < 1:
            self.direction *= -1
        # If jumping, don't move horizontally
        if not self.jumping:
            self.move_x(self.direction)


class Princess(Character):
    "The derived class for princess"
    # If direction is one, face along positive x axis, else along negative
    direction = 1

    def __init__(self, x, y):
        Character.__init__(self, x, y)
        self.sprite = pygame.Rect(x, y, 10, 30)
