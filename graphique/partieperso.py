from tkinter import *
from game.samegame import SameGame


class PartiePerso(Frame):

    def __init__(self, menuFrame):
        super().__init__()
        self.menu = menuFrame
        new = Frame(self)
        new = Toplevel(self)
        new.title("Demo 2")
        self.valid = False
        nb_line_label = Label(new, text="Nombre de lignes")
        nb_line_label.grid(row=1, column=0, sticky='NSWE')
        nb_col_label = Label(new, text="Nombre de colonnes")
        nb_col_label.grid(row=2, column=0, sticky=W+N+S+E)
        nb_color_label = Label(new, text="Nombre de couleurs")
        nb_color_label.grid(row=3, column=0, sticky=W+N+S+E)

        self.nb_line = IntVar(value=7)
        self.nb_col = IntVar(value=7)
        self.nb_colors = IntVar(value=3)

        slider_color = Scale(new, variable=self.nb_line,
                             orient=HORIZONTAL, from_=6, to=12)
        slider_color.grid(row=1, column=1, sticky=W+N+S+E)

        slider_nb_col = Scale(new, variable=self.nb_col,
                              orient=HORIZONTAL, from_=6, to=12)
        slider_nb_col.grid(row=2, column=1, sticky=W+N+S+E)

        self.slider_nb_line = Scale(new, variable=self.nb_colors,
                                    orient=HORIZONTAL, from_=2,
                                    to=len(SameGame.possible_colors))
        self.slider_nb_line.grid(row=3, column=1, sticky=W+N+S+E)

        new_game_button = Button(new, text="NOUVELLE PARTIE",
                                 command=self.new_game)
        new_game_button.grid(row=4, column=0, columnspan=2, sticky=W+N+S+E)

    def new_game(self):
        self.menu.new_game(self.nb_line.get(), self.nb_col.get(),
                           self.nb_colors.get())
        self.destroy()

    def help(self):
        pass
