import pygame
import pygame.locals as pl

from graphique.screen import Screen
from game.samegame import SameGame


class MenuScreen(Screen):
    def __init__(self, interface):
        self.interface = interface
        new_game_button = pygame.sprite.Sprite()
        new_game_button.image = pygame.image.load("graphique/img/new_game.png").convert()
        new_game_button.rect = new_game_button.image.get_rect(center=(400, 300))

        quit_button_game = pygame.sprite.Sprite()
        quit_button_game.image = pygame.image.load("graphique/img/quit.png").convert()
        quit_button_game.rect = quit_button_game.image.get_rect(top=new_game_button.rect.bottom)

        self.buttons = pygame.sprite.Group(new_game_button,quit_button_game)
        self.clickable = [(new_game_button,self.new_game),
                     (quit_button_game,self.interface.quitter)]

    def draw(self):
        dim = self.interface.window.get_rect()
        screen = pygame.Surface((dim.width, dim.height))
        self.buttons.draw(screen)
        return screen

    def new_game(self):
        game = SameGame()
        game.new_game(10,10,4)
        self.interface.change_screen(BoardScreen, game)

    def load_game(self):
        self.interface.change_screen(LoadScreen)
