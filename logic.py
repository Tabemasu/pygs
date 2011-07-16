UP = (0,1); RIGHT = (1,0); DOWN = (0,-1); LEFT = (-1,0)

class Group(object):
    """ Holds all information about a group, including color
    the position of stones and liberties."""
    def __init__(self, color):
        self.color = color
        self.stones = set([])
        self.liberties = set([])
    def addStone(self, position):
        self.stones.add(position)
    def addLiberties(self, liberties):
        self.liberties.update(liberties)
    def removeLiberties(self, liberties):
        for lib in liberties:
            self.liberties.remove(lib)
    def inAtari(self):
        return len(self.liberties) == 1
    def connect(self, groups):
        for group in groups:
            self.stones = self.stones.union(group.stones)
            self.liberties = self.liberties.union(group.liberties)

class Board(object):
    """ Holds all information about all groups and size of the board """
    def __init__(self, size):
        self.size = size
        self.groups = []
        self.ko = None
    def addGroup(self, color, pos, libs):
        new_group = Group(color)
        new_group.addStone(pos)
        new_group.addLiberties(libs)
        self.groups.append(new_group)
    def removeGroups(self, groups):
        if isinstance(groups, Group):
            self.groups.remove(groups)
        else:
            for group in groups:
                self.groups.remove(group)
    def addStone(self, pos, color):
        # Return True or False based on success.
        if self.badPos(pos):
            return False
        p1, p2, liberties = self.getNeighbors(self.getValidPositions(pos), color)
        koStatus = self.koHandler(pos, p1, p2, liberties)
        if koStatus == None:
            if self.illegalMove(p1, liberties):
                return False
            self.ko = None
        elif not koStatus:
            return False
        for group in p2:
            if group.inAtari():
                liberties = self.freeLiberties(group, pos, liberties)
                self.groups.remove(group)
        if p1 == []:
            self.addGroup(color, pos, liberties)
        else:
            base_group = p1[0]
            rest = p1[1:]
            base_group.addStone(pos)
            base_group.addLiberties(liberties)
            base_group.connect(rest)
            base_group.liberties.remove(pos)
            self.removeGroups(rest)
        for group in p2:
            group.removeLiberties([pos])
        return True
    def getValidPositions(self, pos):
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
        p1 = []; p2 = []; liberties = []
        for position in positions:
            neighbor = self.getNeighborAt(position)
            if isinstance(neighbor, Group):
                if neighbor.color == color and neighbor not in p1:
                    p1.append(neighbor)
                elif neighbor.color != color and neighbor not in p2:
                    p2.append(neighbor)
            else:
                liberties.append(neighbor)
        return (p1, p2, liberties)
    def getNeighborAt(self, position):
        #returns a group object, or a position corresponding to a liberty
        for group in self.groups:
            if position in group.stones:
                return group
        return position
    def getAdjacent(self, position):
        return (shiftPos(position, UP), shiftPos(position, RIGHT),
                shiftPos(position, DOWN), shiftPos(position, LEFT))
    def freeLiberties(self, group, pos, liberties):
        for position in group.stones:
            adj_positions = self.getAdjacent(position)
            for adj_position in adj_positions:
                neighbor = self.getNeighborAt(adj_position)
                if isinstance(neighbor, Group) and neighbor.color != group.color:
                    neighbor.liberties.add(position)
                elif neighbor == pos:
                    liberties.append(position)
        return liberties
    def illegalMove(self, p1, liberties):
        if liberties == []:
            for group in p1:
                if group.inAtari(): pass
                else: return False
            return True
        else: return False
    def koHandler(self, pos, p1, p2, liberties):
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
                    for stone in group.stones:
                        self.ko = stone
                    return True
    def badPos(self, pos):
        for group in self.groups:
            for stone in group.stones:
                if pos == stone:
                    return True
def shiftPos(pos, direction):
    x, y = pos; i, j = direction
    return (x+i, y+j)
def validPos(pos, size):
    x, y = pos
    return not (outOfRange(x, 0, size)) and (not outOfRange(y, 0, size))
def outOfRange(number, lower_bound, upper_bound):
    return (number < lower_bound or number >= upper_bound)
