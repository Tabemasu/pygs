import pygame
import sys
from logic import *
from drawing import scale, Renderer

BLACK = 0; WHITE = 1
IMAGE_SIZE = 32

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
window_size = scale(IMAGE_SIZE, (board_size,)*2)
screen = pygame.display.set_mode(window_size)
renderer = Renderer(screen)
renderer.renderBoard(board)

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
                renderer.renderBoard(board)
                game_state.nextTurn()
        elif event.type == pygame.KEYDOWN:
            debug(board)

