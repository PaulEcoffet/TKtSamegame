import pygame
import pygame.locals as pl

class Screen():

    def __init__(self, interface):
        self.interface = interface
        self.clickable = None

    def update(self):
        pass

    def draw(self):
        raise NotImplemented
