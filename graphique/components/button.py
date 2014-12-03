import pygame
import pygame.locals as pl

class Button(pygame.Sprite):

    HOVER = 0
    CLICKED = 1

    def __init__(self, image_path, rect=None, action):
        self._image_hover = pygame.image.load(image_path + '_hov.png').convert()
        self._image_click = pygame.image.load(image_path + '_clk.png').convert()
        self._image_none = pygame.image.load(image_path + '.png').convert()
        self.rect = rect
        self.action = action
        self.state = None

    def update(self):
        if self.rect.collidepoint(50, 50):


    def clicked(self):

    @property
    def image(self):
