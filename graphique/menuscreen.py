import pygame
import pygame.locals as pl

from graphique.screen import Screen

class MenuScreen(Screen):
    def __init__(self, interface):
        self.clickable = []
        self.interface = interface

    def draw(self):
        pass
