import os
import sys
import pygame

class ResourceLoader(object):
    def __init__(self, path, resources):
        self.path = path
        self.resources = resources
    def loadImages(self):
            for resource in self.resources:
                filename = os.path.join(self.path, (resource.name+".bmp"))
                resource.load(self.loadFile(filename))
    def loadFile(self, filename):
        try:
            return pygame.image.load(filename)
        except pygame.error:
            print "Error, can't find file: " + filename
            sys.exit()
        
class ResourceImage(object):
    def __init__(self, name, renderer, image=None, colorkey=(255,0,0)):
        self.name = name
        self.image = image
        self.default_colorkey = colorkey
        self.renderer = renderer
        if image is not None:
            self.setColorKey(self.default_colorkey)
    def load(self, image):
        self.image = image
        self.setColorKey(self.default_colorkey)
    def getImage(self):
        return self.image
    def setColorKey(self, colorkey):
        self.image.set_colorkey(colorkey)
    def render(self):
        self.renderer.render(x, y, self.image)
