from tkinter import * 
from game.samegame import SameGame
from graphique.boardtk import BoardFrame
import pickle
import tkinter.filedialog

class MenuFrame(Frame):

    def __init__(self,interface):
        self.interface = interface
        super().__init__(interface.root)
        
        nb_line_label=Label(self,text="nombre de lignes")
        nb_line_label.pack(side=LEFT, fill=BOTH)
        slider_color = Scale(self, orient= HORIZONTAL,from_=6, to=12,
                             command=self.set_nb_line)
        slider_color.pack(side=LEFT, fill=BOTH)

        nb_col_label=Label(self,text="nombre de colonnes")
        nb_col_label.pack(side=LEFT, fill=BOTH)
        slider_nb_col = Scale(self, orient= HORIZONTAL,from_=6, to=12,
                             command=self.set_nb_col)
        slider_nb_col.pack(side=LEFT, fill=BOTH)

        nb_color_label=Label(self,text="nombre de couleurs")
        nb_color_label.pack(side=LEFT, fill=BOTH)
        slider_nb_line = Scale(self, orient= HORIZONTAL,from_=2, to=len(SameGame.possible_colors),
                             command=self.set_nb_color)
        slider_nb_line.pack(side=LEFT, fill=BOTH)
        
        new_game_button = Button(self,text="NEW GAME",command=self.new_game)
        new_game_button.pack(side=LEFT, fill=BOTH)
        load_button = Button(self,text="NEW GAME",command=self.load_game)
        load_button.pack(side=LEFT,fill=BOTH)

    def new_game(self):
        game = SameGame()
        game.new_game(self.nb_col,self.nb_line,self.nb_colors)
        self.interface.switch_frame(BoardFrame,game)

    def load_game(self):
        f = tkinter.filedialog.askopenfile(mode='rb',initialdir = '../saves/' )
        game = pickle.load(f)
        self.interface.switch_frame(BoardFrame, game)

    def set_nb_col(self,n):
        self.nb_col = int(n)
    def set_nb_color(self,n):
        self.nb_colors = int(n)
    def set_nb_line(self,n):
        self.nb_line = int(n)
        
