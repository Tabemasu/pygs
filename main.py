import pygame
import sys
from logic import *
from drawing import IMAGE_SIZE, scale, draw_board, draw_stones

BLACK = 0; WHITE = 1

class GameState(object):
    def __init__(self, player_turn):
        self.player_color = player_turn
    def nextTurn(self):
        # assumes colors are 0 and 1
        self.player_color = int(not self.player_color)
    def getTurn(self):
        return self.player_color

pygame.init()
running = True
board_size = 19
game_state = GameState(BLACK)
board = Board(board_size)

corner, intersection, side, black_stone, white_stone = tuple(
    pygame.image.load('images/%s.bmp' % fname)
    for fname in ('corner', 'intersection', 'side', 'bstone', 'wstone'))
black_stone.set_colorkey((255,0,0))
white_stone.set_colorkey((255,0,0))

window_size = scale(IMAGE_SIZE, (board_size,)*2)
screen = pygame.display.set_mode(window_size)
draw_board(board_size, screen, corner, side, intersection)

def debug(board):
    print board.ko
    print
    print len(board.groups)
    print
    for group in board.groups:
        print group.stones
        print
        print group.liberties
        print

while running:
    pygame.display.flip()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONUP:
            x, y = pygame.mouse.get_pos()
            turn = game_state.getTurn()
            pos = (x/IMAGE_SIZE, y/IMAGE_SIZE)
            if board.addStone(pos, turn):
                draw_board(board_size, screen, corner, side, intersection)
                draw_stones(screen, board, black_stone, white_stone)
                game_state.nextTurn()
        elif event.type == pygame.KEYDOWN:
            debug(board)


