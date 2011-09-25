class Group(object):
    """ Holds all information about a group, including color
    the position of stones and liberties."""
    def __init__(self, color):
        self.color = color
        self.stones = set()
        self.liberties = set()

    def addStone(self, position):
        self.stones.add(position)

    def addLiberties(self, liberties):
        self.liberties.update(liberties)

    def inAtari(self):
        return len(self.liberties) == 1

    def connect(self, groups):
        for group in groups:
            self.stones |= group.stones
            self.liberties |= group.liberties

    def getStones(self):
        return self.stones
