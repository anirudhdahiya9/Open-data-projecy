from character import *


class Hazard(Character):
    "The derived class for the scary fireball"
    # If direction is 1, move along positive x axis, else negative.
    direction = 1

    def __init__(self, x, y):
        Character.__init__(self, x, y, 0.5)
        self.sprite = pygame.Rect(x, y, 10, 30)

    # Similar to base class' fall function, except randomly changes direction
    def fall(self, floor, floor_bottom, ladder):
        """To calculate the vertical movement of the object.
           First argument is the list of floor, which it should stop at
           Second is list of ladders, thorugh which the fireballs can fall
        """
        # If not touching a floor, or if touching a ladder, fall down.
        cond1 = self.sprite.collidelist(floor) == -1
        cond2 = self.sprite.collidelist(ladder) != -1
        if cond1 or cond2:
            self.vertical_velocity += self.weight
        # Else, if hitting the floor with some speed, randomly change direction
        # and set jumping flag to 0
        elif self.vertical_velocity > 0:
            if self.vertical_velocity > 2:
                self.direction = 1 if randint(0, 1) else -1
            self.jumping = 0
            self.vertical_velocity = 0
        # If colliding with bottom half of floor, implying overlap,
        # slowly move up to reverse it.
        if self.sprite.collidelist(floor_bottom) != -1:
            self.move_y(-0.5)
        # To change the position, as calculated
        self.move_y(self.vertical_velocity)


class GoldCoin(Character):
    "The derived class for the shiny coins"

    def __init__(self, x, y):
        Character.__init__(self, x, y, 0.5)
        self.sprite = pygame.Rect(x, y, 10, 30)

    def GetPosition(self):
        """A different GetPosition function, from the parent.
           type of position is float, and the value must
           always return an int.
        """
        return (int(self._x), int(self._y))

    def fall(self, floor, floor_bottom):
        if self.sprite.collidelist(floor) == -1:
            self.vertical_velocity += self.weight
        elif self.vertical_velocity > 0:
            self.jumping = 0
            self.vertical_velocity = 0
        if self.sprite.collidelist(floor_bottom) != -1:
            self.move_y(-0.5)
        self.move_y(self.vertical_velocity)
