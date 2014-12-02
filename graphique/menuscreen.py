import pygame
import pygame.locals as pl

from graphique.screen import Screen

class MenuScreen(Screen):
    def __init__(self, interface):
        self.interface = interface
        new_game_button = pygame.sprite.Sprite()
        new_game_button.image = pygame.image.load("new_game.png").convert()
        new_game_button.rect = new_game_button.image.get_rect(center=(300, 300))

        quit_button_game = pygame.sprite.Sprite()
        quit_button_game.image = pygame.image.load("quit.png").convert()
        quit_button_game.rect = quit_button_game.image.get_rect(center=(100, 300))

        self.buttons = pygame.sprite.Group(new_game_button,quit_button_game)
        self.clickable = [(new_game_button,self.interface.new_game),
                     (quit_button_game,self.interface.quitter)]

    def draw(self):
        dim = self.interface.window.get_rect()
        screen = pygame.Surface((dim.width, dim.height))
        self.buttons.draw(screen)
        return screen
