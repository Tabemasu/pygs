import pygame
import sys
from resource import ResourceImage, ResourceLoader
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
renderer = Renderer(screen, IMAGE_SIZE)
images = tuple(ResourceImage(name, renderer) 
               for name in ('corner', 'intersection', 'side', 
                            'bstone', 'wstone'))
RL = ResourceLoader('images', images)
RL.loadImages()
corner, intersection, side, black_stone, white_stone = images
renderer.renderBoard(board_size, corner.getImage(), 
                     side.getImage(), intersection.getImage())

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
#        elif event.type == pygame.MOUSEBUTTONUP:
#            x, y = pygame.mouse.get_pos()
#            turn = game_state.getTurn()
#            pos = (x/IMAGE_SIZE, y/IMAGE_SIZE)
#            if board.addStone(pos, turn):
#                draw_board(board_size, screen, corner, side, intersection)
#                draw_stones(screen, board, black_stone, white_stone)
#                game_state.nextTurn()
#        elif event.type == pygame.KEYDOWN:
#            debug(board)

