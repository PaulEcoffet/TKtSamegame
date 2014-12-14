from tkinter import *
from game.highscores import Highscores


class HighscoresFrame(Frame):

    def __init__(self, interface):
        self.interface = interface
        super().__init__(interface.root)
        self.highscores = Highscores('high.scores')

        self.scorelist = Listbox(self)
        nb_line_label = Label(new, text="Nombre de lignes")
        nb_line_label.grid(row=1, column=0, sticky='NSWE')
        nb_col_label = Label(new, text="Nombre de colonnes")
        nb_col_label.grid(row=2, column=0, sticky=W+N+S+E)
        nb_color_label = Label(new, text="Nombre de couleurs")
        nb_color_label.grid(row=3, column=0, sticky=W+N+S+E)

        self.nb_line = IntVar(value=7)
        self.nb_col = IntVar(value=7)
        self.nb_colors = IntVar(value=3)
        self.nb_line.trace('w',  self.update_score)
        self.nb_col.trace('w',  self.update_score)
        self.nb_colors.trace('w',  self.update_score)

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