import os
import pygame
        
class ResourceImage(object):
    def __init__(self, name, colorkey=(255,0,0)):
        self.image = self.load(os.path.join("images", name))
        self.default_colorkey = colorkey
        self.setColorKey(colorkey)
    def load(self, path):
        return pygame.image.load(path)
    def getImage(self):
        return self.image
    def setColorKey(self, colorkey):
        self.image.set_colorkey(colorkey)
