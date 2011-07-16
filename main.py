import pygame
import sys
from logic import *
from drawing import draw_board, draw_stones

class GameState(object):
    def __init__(self, player_turn):
        self.player_color = player_turn
    def nextTurn(self):
        if self.player_color == WHITE:
           self.player_color = BLACK
        else: self.player_color = WHITE
    def getTurn(self):
        return self.player_color

pygame.init()
running = True
corner = pygame.image.load("images/corner.bmp")
intersection = pygame.image.load("images/intersection.bmp")
side = pygame.image.load("images/side.bmp")
black_stone = pygame.image.load("images/bstone.bmp")
black_stone.set_colorkey((255,0,0))
white_stone = pygame.image.load("images/wstone.bmp")
white_stone.set_colorkey((255,0,0))
board_size = 9
window_size = (board_size*32, board_size*32)
screen = pygame.display.set_mode(window_size)
draw_board(board_size, screen, corner, side, intersection)
WHITE = 0
BLACK = 1
game_state = GameState(BLACK)
board = Board(board_size)

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
            pos = (x/32, y/32)
            if board.addStone((x/32,y/32), turn):
                draw_board(board_size, screen, corner, side, intersection)
                draw_stones(screen, board, black_stone, white_stone)
                game_state.nextTurn()
        elif event.type == pygame.KEYDOWN:
            debug(board)


