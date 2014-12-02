import pygame
import pygame.locals as pl

from game.samegame import SameGame
from graphique.menuscreen import MenuScreen

class PygameInterface(object):

    def __init__(self):
        pygame.init()
        try:
            self.window = pygame.display.set_mode((800, 600))
            self.game = None
            self.do_run = True
            self.screen = MenuScreen(self)
            self.run()
        finally:
            pygame.quit()

    def run(self):
        while self.do_run:
            self.do_events()
            self.screen.update()
            self.window.blit(self.screen.draw(), (0,0))
            pygame.display.flip()

    def do_events(self):
        for event in pygame.event.get():
            if event.type == pl.QUIT:
                self.do_run = False
            elif event.type == pl.MOUSEBUTTONUP and event.button == 1:
                for c in self.screen.clickable:
                    if c[0].rect.collidepoint(*event.pos):
                        c[1]()

    def quitter(self):
        self.do_run =False

    def new_game(self):
        self.game = SameGame()
        self.game.new_game(10,10,4)
