import random

class SameGame():

    def __init__(self):
        self.possible_colors = ['B', 'O', 'A', 'M', 'V', 'R']

    def new_game(self, nb_col, nb_line, nb_colors):
        self.used_colors = self.possible_colors[:nb_colors]
        self.nb_col = nb_col
        self.nb_line = nb_line
        self.board = [[random.choice(self.used_colors)
                       for i in range(nb_col)]
                      for j in range(nb_line)]

    @property
    def not_finished(self):
        """Declare si le jeu est fini ou pas"""
        return self.board[-1] != [' ' for i in range(self.nb_col)]
