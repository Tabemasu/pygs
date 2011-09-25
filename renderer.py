import pygame
from resource import ResourceImage
from utility import Colors, scale, edgeCase

class Renderer(object):
  def __init__(self, surface, image_size):
    self.surface = surface
    self.image_size = image_size
    self.special_coordinates = []
    self.black_stone_image = ResourceImage("bstone.bmp")
    self.white_stone_image = ResourceImage("wstone.bmp")
    self.board_star_image = ResourceImage("star.bmp")
    self.board_corner_image = ResourceImage("corner.bmp")
    self.board_side_image = ResourceImage("side.bmp")
    self.board_intersection_image = ResourceImage("intersection.bmp")

  def draw(self, image, position):
    self.surface.blit(image, position)

  def rotate(self, image, degrees):
    return pygame.transform.rotate(image, degrees)
  
  def getImageSize(self):
    return self.image_size

  def getImageFromColor(self, color):
    if color == Colors.black:
      return self.black_stone_image.getImage()
    elif color == Colors.white:
      return self.white_stone_image.getImage()
  
  def getImageFromCoordinate(self, coordinate, size):
    intersection = self.board_intersection_image.getImage()
    side = self.board_side_image.getImage()
    corner = self.board_corner_image.getImage()
    star = self.board_star_image.getImage()
    low = 0; high = size
    x, y = coordinate
    if coordinate in self.special_coordinates:
      return star
    elif not edgeCase(x, low, high) and not edgeCase(y, low, high):
       return intersection
    elif x == low and not edgeCase(y, low, high):
      return side
    elif x == high and not edgeCase(y, low, high):
      return self.rotate(side, 180)
    elif not edgeCase(x, low, high) and y == low:
      return self.rotate(side, 270)
    elif not edgeCase(x, low, high) and y == high:
      return self.rotate(side, 90)
    elif coordinate == (low, low):
      return corner
    elif coordinate == (low, high):
      return self.rotate(corner, 90)
    elif coordinate == (high, low):
      return self.rotate(corner, 270)
    elif coordinate == (high, high):
      return self.rotate(corner, 180)

  def renderBoard(self, board):
    board_size = board.getSize()
    print self.special_coordinates
    if not self.special_coordinates:
      self.generateSpecialCoordinates(board_size-1)
    self.constructBoardImage(board_size, self.getImageSize())
    for stone in board.getStones():
      self.draw(self.getImageFromColor(stone.getColor()),
                scale(self.image_size, stone.getPosition()))
  
  def constructBoardImage(self, size, image_size):
    for x in xrange(size):
      for y in xrange(size):
        coordinate = (x, y)
        self.draw(self.getImageFromCoordinate(coordinate, (size-1)),
                  scale(image_size, coordinate))

  def generateSpecialCoordinates(self, size):
    print 'c'
    starpoints = []
    left_star_coordinate = 3
    mid_coordinate = size/2
    right_star_coordinate = size - left_star_coordinate
    coordinates = [left_star_coordinate, mid_coordinate, right_star_coordinate]
    for first_coordinate in coordinates:
      for second_coordinate in coordinates:
        starpoint = (first_coordinate, second_coordinate)
        starpoints.append(starpoint)
    self.special_coordinates = starpoints
