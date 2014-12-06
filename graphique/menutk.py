from tkinter import * 
from game.samegame import SameGame
from graphique.boardtk import BoardFrame
import pickle
import tkinter.filedialog

class MenuFrame(Frame):

    def __init__(self,interface):
        self.interface = interface
        super().__init__(interface.root)
        quit_button = Button(self,text="QUITTER",command=interface.root.destroy)
        quit_button.pack(side=LEFT, fill=BOTH)
        new_game_button = Button(self,text="NEW GAME",command=self.new_game)
        new_game_button.pack(side=LEFT, fill=BOTH)
        load_button = Button(self,text="NEW GAME",command=self.load_game)
        load_button.pack(side=LEFT,fill=BOTH)

    def new_game(self):
        game = SameGame()
        game.new_game(4,4,4)
        self.interface.switch_frame(BoardFrame,game)

    def load_game(self):
        f = tkinter.filedialog.askopenfile(mode='rb',initialdir = '../saves/' )
        game = pickle.load(f)
        self.interface.switch_frame(BoardFrame, game)
