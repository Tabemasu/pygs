class Colors:
  black, white = range(2)

def scale(scalar, coordinate):
  x, y = coordinate
  return x*scalar, y*scalar

def shiftPos(pos, direction):
    x, y = pos; i, j = direction
    return (x+i, y+j)

def validPos(pos, size):
    x, y = pos
    return not (outOfRange(x, 0, size)) and (not outOfRange(y, 0, size))

def outOfRange(number, lower_bound, upper_bound):
    return (number < lower_bound or number >= upper_bound)
      
def edgeCase(point, lower_bound, upper_bound):
  return (point == lower_bound or point == upper_bound)
