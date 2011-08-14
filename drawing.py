import pygame

IMAGE_SIZE = 32

def scale(scalar, coord):
  xc, yc = coord
  return xc*scalar, yc*scalar

def draw_stones(target, board, black, white):
    imgs = (black, white) # assume color is either 0 or 1
    for group in board.groups:
        color = group.color
        for stone in group.stones:
            target.blit(imgs[color], scale(IMAGE_SIZE, stone))

def draw_board(size, target, corner, side, other):
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
    middle = ((other, (x, y)) for x in xrange(1, size-1)
              for y in xrange(1, size-1))
    for section in (corners, tb, lr, middle):
        for img, pos in section:
            target.blit(img, scale(IMAGE_SIZE, pos))
