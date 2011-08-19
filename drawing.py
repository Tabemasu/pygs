import pygame

class Renderer(object):
  def __init__(self, surface, image_size):
    self.surface = surface
    self.image_size = image_size
  def renderStone(self, position, stone_image):
    self.surface.blit(stone_image
                      ,scale(self.image_size, position))
  def renderBoard(self, size, corner, side, intersection):
    corners = ((corner, (0, 0)),
               (pygame.transform.rotate(corner, 90), (0, size-1)),
               (pygame.transform.rotate(corner, 270), (size-1, 0)),
               (pygame.transform.rotate(corner, 180), (size-1, size-1)))
    # generator for top and bottom sides
    tb = ((img, (x, y)) for y, img in
          ((0, pygame.transform.rotate(side, 270)),
           (size-1, pygame.transform.rotate(side, 90)))
          for x in xrange(1, size-1))
    # generator for left and right sides
    lr = ((img, (x, y)) for x, img in
          ((0, side),
           (size-1, pygame.transform.rotate(side, 180)))
          for y in xrange(1, size-1))
    # generator for the rest
    middle = ((intersection, (x, y)) for x in xrange(1, size-1)
              for y in xrange(1, size-1))
    for section in (corners, tb, lr, middle):
      for img, pos in section:
        self.surface.blit(img, scale(self.image_size, pos))

def scale(scalar, coord):
  xc, yc = coord
  return xc*scalar, yc*scalar
