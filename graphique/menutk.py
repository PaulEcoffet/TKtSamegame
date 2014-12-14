from tkinter import *
from game.samegame import SameGame
from graphique.boardtk import BoardFrame
import pickle
import tkinter.filedialog
from graphique.partieperso import PartiePerso

class MenuFrame(Frame):

    def __init__(self, interface):
        self.interface = interface
        super().__init__(interface.root)
        for i in range(3):
            self.grid_columnconfigure(i, weight = 2, minsize=10)
            self.grid_rowconfigure(i, weight = 2, minsize=10)
        img = PhotoImage(file="graphique/img/beaugosse.gif")
        lab_img = Label(self, image=img)
        lab_img.image = img
        lab_img.grid(row=0, column=0, columnspan=3)

        easy = Button(self, text="PARTIE FACILE",
                      command=lambda:self.new_game(4, 4, 2))
        easy.grid(row=1, column=0, columnspan=2, sticky='NSWE')
        medium = Button(self, text="PARTIE MOYENNE",
                        command=lambda:self.new_game(8, 8, 4))
        medium.grid(row=2, column=0, columnspan=2, sticky='NSWE')
        hard = Button(self, text="PARTIE DIFFICILE",
                      command=lambda:self.new_game(12, 12, 6))
        hard.grid(row=3, column=0, columnspan=2, sticky='NSWE')
        
        new_game_button = Button(self, text="PARTIE PERSO",
                                 command=self.new_perso_game)
        new_game_button.grid(row=4, column=0, columnspan=2, sticky=W+N+S+E)
        load_button = Button(self, text="CHARGER UNE PARTIE",
                             command=self.load_game)
        load_button.grid(row=3, column=2, sticky=W+N+S+E)
        load_button = Button(self, text="AIDE", command=self.help)
        load_button.grid(row=2, column=2, sticky=W+N+S+E)

    def new_game(self, nb_lines, nb_col, nb_colors):
        game = SameGame(nb_lines, nb_col, nb_colors)
        self.interface.switch_frame(BoardFrame, game)

    def new_perso_game(self):
        PartiePerso(self)

    def load_game(self):
        try:
            save = tkinter.filedialog.askopenfile(mode='rb',
                                                  initialdir='saves/')
            game = pickle.load(save)
        except Exception as error:
            print(error) # Show error
        else:
            if isinstance(game, SameGame):
                self.interface.switch_frame(BoardFrame, game)

    def help(self):
        pass
