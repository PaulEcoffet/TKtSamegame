import pygame
import pygame.locals as pl

from game.samegame import SameGame

class PygameInterface(object):

    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode((800, 600))
        self.game = SameGame()
        self.fps_clock = pygame.time.Clock()
        self.do_run = True
        self.run()

    def run(self):
        while self.do_run:
            self.do_events()
            self.display_all()
            self.fps_clock.tick(60)


    def do_events(self):
        for event in pygame.event.get():
            if event.type == pl.QUIT:
                self.do_run = False

    def display_all(self):
        pass
