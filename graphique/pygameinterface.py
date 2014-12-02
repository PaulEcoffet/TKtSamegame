import pygame
import pygame.locals as pl

from game.samegame import SameGame

class PygameInterface(object):

    def __init__(self):
        pygame.init()
        try:
            self.window = pygame.display.set_mode((800, 600))
            self.game = None
            self.do_run = True
            self.run()
            self.screen = MenuScreen()
        finally:
            pygame.quit()

    def run(self):
        self.chargerMenu()
        while self.do_run:
            self.do_events()
            self.screen.update()
            self.window.flip(self.screen.draw())

    def do_events(self):
        for event in pygame.event.get():
            if event.type == pl.QUIT:
                self.do_run = False
            elif event.type == pl.MOUSEBUTTONUP and event.button == 1:
                for c in self.clickable:
                    if c[0].rect.collidepoint(*event.pos):
                        c[1]()

    def display_all(self):
        pygame.display.flip()

    def chargerMenu(self):
        new_game_button = pygame.sprite.Sprite()
        new_game_button.image = pygame.image.load("new_game.png").convert()
        new_game_button.rect = new_game_button.image.get_rect(center=(300, 300))

        quit_button_game = pygame.sprite.Sprite()
        quit_button_game.image = pygame.image.load("quit.png").convert()
        quit_button_game.rect = quit_button_game.image.get_rect(center=(100, 300))

        buttons = pygame.sprite.Group(new_game_button,quit_button_game)
        buttons.draw(self.window)
        self.clickable = [(new_game_button,self.new_game),
                     (quit_button_game,self.quitter)]


    def quitter(self):
        self.do_run =False

    def new_game(self):
        self.game = SameGame()
        self.game.new_game(10,10,4)
