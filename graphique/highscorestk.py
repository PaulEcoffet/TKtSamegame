from tkinter import *
from game.highscores import Highscores
from game.samegame import SameGame


class HighscoresFrame(Frame):
    """
    Écran affichant les meilleurs scores pour chaque configuration
    """

    def __init__(self, interface):
        self.interface = interface
        super().__init__(interface.root)
        self.highscores = Highscores('high.scores')

        config_frame = Frame(self)
        self.scorelist = Listbox(self)
        nb_line_label = Label(config_frame, text="Nombre de lignes")
        nb_line_label.grid(row=1, column=0, sticky='NSWE')
        nb_col_label = Label(config_frame, text="Nombre de colonnes")
        nb_col_label.grid(row=2, column=0, sticky=W+N+S+E)
        nb_color_label = Label(config_frame, text="Nombre de couleurs")
        nb_color_label.grid(row=3, column=0, sticky=W+N+S+E)

        self.nb_line = IntVar(value=7)
        self.nb_col = IntVar(value=7)
        self.nb_colors = IntVar(value=3)
        self.nb_line.trace('w', self.update_score)
        self.nb_col.trace('w', self.update_score)
        self.nb_colors.trace('w', self.update_score)

        slider_color = Scale(config_frame, variable=self.nb_line,
                             orient=HORIZONTAL, from_=6, to=12)
        slider_color.grid(row=1, column=1, sticky=W+N+S+E)

        slider_nb_col = Scale(config_frame, variable=self.nb_col,
                              orient=HORIZONTAL, from_=6, to=12)
        slider_nb_col.grid(row=2, column=1, sticky=W+N+S+E)

        self.slider_nb_line = Scale(config_frame, variable=self.nb_colors,
                                    orient=HORIZONTAL, from_=2,
                                    to=len(SameGame.possible_colors))
        self.slider_nb_line.grid(row=3, column=1, sticky=W+N+S+E)
        self.scorelist.pack(side=TOP, expand=True, fill=BOTH)
        config_frame.pack(side=TOP)

        self.update_score()

        back_to_menu = Button(self, text="Retour menu", command=self.interface.switch_to_menu)
        back_to_menu.pack(side=BOTTOM)

    def update_score(self, *args):
        """
        Met à jour la liste des score en fonction de la configuration choisie
        """
        scores = self.highscores.get_scores(self.nb_line.get(), self.nb_col.get(),
                                            self.nb_colors.get())
        items = ['' for i in range(10)]
        if not scores:
            items[0] = 'Pas de score dans cette catégorie'
        else:
            for i, score in enumerate(scores[:10]):
                items[i] = '{}: {} ({})'.format(i+1, score[0], score[1])
        self.scorelist.delete(0, END)
        self.scorelist.insert(END, *items)
