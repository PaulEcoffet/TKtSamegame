import pygame
import pygame.locals as pl

from game.samegame import SameGame
from screen import *
from graphique.screen import Screen

class Board_Screen(Screen):
  
    def __init__(self,interface):
        self.interface = interface
        self.game = interface.game
        self.colors = {'A' :pygame.Color(55,55,55),
                       'B' :pygame.Color(155,55,55),
                       'C' :pygame.Color(55,155,55),
                       'D' :pygame.Color(55,55,155),
                       'E' :pygame.Color(55,0,55),
                       'F' :pygame.Color(0,55,55)}
        
        self.buttons = pygame.sprite.Group(new_game_button,quit_button_game)
        self.clickable = [(new_game_button,self.interface.new_game),
                     (quit_button_game,self.interface.quitter)]
        self.dim = (50,50)
        self.createGrid()
        

    def createGrid(self):
        self.grid = []
        for line in range(self.game.nb_lines):
            self.grid.append([])
            for col in range(self.game.nb_col):
                self.grid[line].append(pygame.Surface(self.dim))
                self.grid[line][col].fill(self.colors[self.game.board[line][col]])

    def draw(self):
        group = pygame.sprite.Group
        for i in range(len(self.grid)):
            draw.rect(i)
        dim = self.interface.window.get_rect()
        screen = pygame.Surface((dim.width, dim.height))
        self.buttons.draw(screen)
        return screen

    
    

    
                
        
