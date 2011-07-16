import pygame

def draw_stones(target, board, black, white):
    for group in board.groups:
        color = group.color
        for stone in group.stones:
            x, y = stone
            pos = (x*32, y*32)
            if color == 0:
                target.blit(white, pos)
            else:
                target.blit(black, pos)

def draw_board(size, target, corner, side, other):
    x = 0
    y = 0
    for x in range(size):
        for y in range(size):
            pos = (x*32, y*32)
            if x == 0:
                if y == 0:
                    target.blit(corner, pos)
                elif y == (size-1):
                    target.blit(pygame.transform.rotate(corner, 90), pos)
                else:
                    target.blit(side, pos)
            elif x == (size-1):
                if y == 0:
                    target.blit(pygame.transform.rotate(corner, 270), pos)
                elif y == (size-1):
                    target.blit(pygame.transform.rotate(corner, 180), pos)
                else:
                    target.blit(pygame.transform.rotate(side, 180), pos)
            elif y == 0:
                target.blit(pygame.transform.rotate(side, 270), pos)
            elif y == (size-1):
                target.blit(pygame.transform.rotate(side, 90), pos)
            else:
                target.blit(other, pos)
