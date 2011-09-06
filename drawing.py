import pygame
from resource import ResourceImage

BLACK = 0; WHITE = 1
class Renderer(object):
  def __init__(self, surface):
    self.surface = surface
    self.black_stone_image = ResourceImage("bstone.bmp")
    self.white_stone_image = ResourceImage("wstone.bmp")
    self.board_corner_image = ResourceImage("corner.bmp")
    self.board_side_image = ResourceImage("side.bmp")
    self.board_intersection_image = ResourceImage("intersection.bmp")
  def draw(self, image, position):
    self.surface.blit(image, position)
  def rotate(self, image, degrees):
    return pygame.transform.rotate(image, degrees)
  def renderBoard(self, board):
    self.constructBoardImage(board.getSize(), 
                             self.board_corner_image.getImageSize())
    stone_image_size = self.black_stone_image.getImageSize()
    for stone_position, color in board.getStones():
      if color == BLACK:
        # Make a function to do the stuff below
        self.draw(self.black_stone_image.getImage(),
                  scale(stone_image_size, stone_position))
      elif color == WHITE:
        self.draw(self.white_stone_image.getImage(),
                  scale(stone_image_size, stone_position))

  def constructBoardImage(self, size, image_size):
    corner = self.board_corner_image.getImage()
    side = self.board_side_image.getImage()
    intersection = self.board_intersection_image.getImage()
    corners = ((corner, (0, 0)),
               (self.rotate(corner, 90), (0, size-1)),
               (self.rotate(corner, 270), (size-1, 0)),
               (self.rotate(corner, 180), (size-1, size-1)))
    # generator for top and bottom sides
    tb = ((img, (x, y)) for y, img in
          ((0, self.rotate(side, 270)),
           (size-1, self.rotate(side, 90)))
          for x in xrange(1, size-1))
    # generator for left and right sides
    lr = ((img, (x, y)) for x, img in
          ((0, side),
           (size-1, self.rotate(side, 180)))
          for y in xrange(1, size-1))
    # generator for the rest
    middle = ((intersection, (x, y)) for x in xrange(1, size-1)
              for y in xrange(1, size-1))
    for section in (corners, tb, lr, middle):
      for img, pos in section:
        self.draw(img, scale(image_size, pos))

def scale(scalar, coord):
  xc, yc = coord
  return xc*scalar, yc*scalar
