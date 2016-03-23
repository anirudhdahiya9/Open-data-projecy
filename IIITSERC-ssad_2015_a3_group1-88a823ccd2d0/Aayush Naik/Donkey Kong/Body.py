

class Body:

    """Super class of Donkey, Player, and Fireball.

    This makes sense because all of them have similar behaviour."""

    def __init__(self, lev):
        self._levelObj = lev
        self._fireCoordinates = []

    def getLevelProperties(self):
        """Gets certain values from the Level class."""

        self.ladderCoordinates = self._levelObj.retLadderCoordinates()
        self.coinCoordinates, self.coinCount =\
            self._levelObj.retCoinProperties()
        self.levelB = self._levelObj.retBlueP()
        self.pSpawnPoint = self._levelObj.retSpawnPoint()
        self.prinPoint = self._levelObj.retPrincessPoint()

    def fireCoordinatesUpdate(self, co):
        """Adds to & updates a list of the fireball co-ordinates."""

        self._fireCoordinates = []
        self._fireCoordinates.extend(co)

    def getPosition(self, char):
        """Gets the position of a certain character from the Level board."""

        for i, x in enumerate(self.levelB):
            if char in x:
                self.bodyPos = [i, x.index(char)]
                return self.bodyPos

    def gravity(self, pos):
        return [pos[0]+1, pos[1]]
