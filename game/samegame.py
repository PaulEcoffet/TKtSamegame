import random

class SameGame():

    def __init__(self):
        self.possible_colors = ['B', 'O', 'A', 'M', 'V', 'R']

    def new_game(self, nb_col, nb_line, nb_colors):
        self.score = 0
        self.used_colors = self.possible_colors[:nb_colors]
        self.nb_col = nb_col
        self.nb_line = nb_line
        self.board = [[random.choice(self.used_colors) for i in range(nb_col)]
                      for j in range(nb_line)]

    @property
    def not_finished(self):
        """Declare si le jeu est fini ou pas"""
        return self.board[-1] != [' ' for i in range(self.nb_col)]

    def clear_same(self, line, col):
        """
        Supprime les éléments de même couleurs s'ils sont plus
        de trois.
        """
        def clear_inner_same(line, col, current):


        glyphe = [(1, 0), (0, 1), (-1, 0), (-1, 0)]
        current = self.board[line][col]
        same_colors_nearby = set([(line, col)])
        for i, j in glyphe:
            same_colors_nearby.union(
                clear_inner_same(line+i, line+j, current))


class Board():
    pass
