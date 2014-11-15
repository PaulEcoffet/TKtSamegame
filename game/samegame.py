import random

class SameGame():

    def __init__(self):
        self.possible_colors = ['B', 'O', 'A', 'M', 'V', 'R']

    def new_game(self, nb_line, nb_col, nb_colors):
        self.score = 0
        self.used_colors = self.possible_colors[:nb_colors]
        self.nb_line = nb_line
        self.nb_col = nb_col
        self.board = [[random.choice(self.used_colors) for i in range(nb_col)]
                      for j in range(self.nb_line)]

    @property
    def not_finished(self):
        """Declare si le jeu est fini ou pas"""
        return self.board[-1] != [' ' for i in range(self.nb_col)]

    def get_same_nearby(self, line, col, visited=None):
        """Retourne la liste des cases de même couleur autour de la case x,y"""
        glyphe = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        if not visited:
            visited = [[False for i in range(self.nb_col)]
                        for j in range(self.nb_line)]
        seen = [(line, col)]
        visited[line][col] = True
        for linestep, colstep in glyphe:
            line2 = line + linestep
            col2 = col + colstep
            if (0 <= col2 < self.nb_col and 0 <= line2 < self.nb_line
                    and self.board[line][col] == self.board[line2][col2]
                    and not visited[line2][col2]):
                new_seen = self.get_same_nearby(line2, col2,
                                                visited)
                seen += new_seen
        return seen
