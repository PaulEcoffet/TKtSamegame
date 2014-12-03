from tkinter import *
from game.samegame import SameGame

class MenuFrame(Frame):

    def __init__(self,master):
        super().__init__(master)
        quit_button = Button(self,text="QUITTER",command=master.destroy)
        quit_button.pack(side=LEFT, fill=BOTH)
        new_game_button = Button(self,text="NEW GAME",command=self.new_game)
        new_game_button.pack(side=LEFT, fill=BOTH)

    def new_game(self):
        game = SameGame()
        game.new_game(10,10,4)
        
        
