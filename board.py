from stone import Stone
from group import Group
from utility import shiftPos, validPos, outOfRange
UP = (0,1); RIGHT = (1,0); DOWN = (0,-1); LEFT = (-1,0)

class Board(object):
    """ Holds all information about all groups and size of the board """
    def __init__(self, size):
        self.size = size
        self.groups = set()
        self.stones = {}
        self.ko = None

    def getSize(self):
        return self.size

    def getStones(self):
        stones = []
        for position, color in self.stones.items():
            stones.append(Stone(position, color))
        return stones

    def addGroup(self, color, pos, libs):
        new_group = Group(color)
        new_group.addStone(pos)
        new_group.addLiberties(libs)
        self.groups.add(new_group)

    def removeGroups(self, groups):
        for group in groups:
            self.groups.remove(group)

    def addStoneToBoard(self, pos, color):
        # Return True or False based on success.
        if self.badPos(pos):
            return False
        p1, p2, liberties = self.getNeighbors(self.getValidAdjPositions(pos),
                                              color)
        if not self.legalMove(pos, p1, p2, liberties):
            return False
        for group in p2:
            if group.inAtari():
                liberties = self.freeLiberties(group, pos, liberties)
                self.groups.remove(group)
                self.removeStonesFromMapping(group.getStones())
        if not p1:
            self.addGroup(color, pos, liberties)
        else:
            base_group = p1.pop(); rest = p1
            base_group.addStone(pos)
            base_group.addLiberties(liberties)
            base_group.connect(rest)
            base_group.liberties.remove(pos)
            self.removeGroups(rest)
        for group in p2:
            group.liberties.remove(pos)
        self.addStoneToMapping(pos, color)
        return True

    def getValidAdjPositions(self, pos):
        #returns positions in range of the board size
        adj_positions = self.getAdjacent(pos)
        valid_positions = []
        for position in adj_positions:
            if validPos(position, self.size):
                valid_positions.append(position)
        return valid_positions

    def getNeighbors(self, positions, color):
        #returns a tuple containing a list of the current players groups,
        #a list of the opponents groups, and a list of coordinates corresponding
        #to liberties.
        p1 = set(); p2 = set(); liberties = set()
        for position in positions:
            neighbor = self.getNeighborAt(position)
            if neighbor is not None:
                if neighbor.color == color: player = p1
                else: player = p2
                player.add(neighbor)
            else: liberties.add(position)
        return (p1, p2, liberties)

    def getNeighborAt(self, position):
        # returns the group at this position if there is one
        for group in self.groups:
            if position in group.stones:
                return group
        return None

    def getAdjacent(self, pos):
        return tuple(shiftPos(pos, dir) for dir in (UP, RIGHT, DOWN, LEFT))

    def freeLiberties(self, group, pos, liberties):
        for position in group.stones:
            for adj_position in self.getAdjacent(position):
                neighbor = self.getNeighborAt(adj_position)
                if neighbor is not None and neighbor.color != group.color:
                    neighbor.liberties.add(position)
                elif adj_position == pos:
                    liberties.add(position)
        return liberties

    def suicideMove(self, p1, liberties, captured):
        # I think you had a bug here before when you weren't checking captures
        if captured: return False
        if not liberties:
            for group in p1:
                if not group.inAtari(): return False
            return True
        else: return False

    def legalMove(self, pos, p1, p2, liberties):
        # handle ko first
        captured = []
        for group in p2:
            if group.inAtari():
                captured.append(group)
        if len(captured) == 1:
            group = captured[0]
            if len(group.stones) == 1 and len(p1) == 0 and len(liberties) == 0:
                if pos == self.ko:
                    return False
                else:
                    for pos in group.stones:
                        self.ko = pos
                    return True
        if self.suicideMove(p1, liberties, captured):
            return False
        self.ko = None
        return True

    def badPos(self, pos):
        for group in self.groups:
            for stone in group.stones:
                if pos == stone:
                    return True

    def addStoneToMapping(self, pos, color):
        self.stones[pos] = color

    def removeStonesFromMapping(self, stone_positions):
        for stone_position in stone_positions:
            del self.stones[stone_position]
