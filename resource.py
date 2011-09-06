import os
import pygame
        
class ResourceImage(object):
    def __init__(self, name, colorkey=(255,0,0)):
        self.image = self.load(os.path.join("images", name))
        self.imageSize = self.image.get_size()
        self.default_colorkey = colorkey
        self.setColorKey(colorkey)
    def load(self, path):
        return pygame.image.load(path)
    def getImageSize(self):
        # For now just return the width of the image
        return self.imageSize[0]
    def getImage(self):
        return self.image
    def setColorKey(self, colorkey):
        self.image.set_colorkey(colorkey)
