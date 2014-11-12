class SameGame():

    def __init__(self):
        pass

    def new_game(self, nb_col, nb_line):
        self.nb_col = nb_col
        self.nb_line = nb_line
        self.board = [['A' for i in range(nb_col)] for j in range(nb_line)]

    @property
    def not_finished(self):
        return self.board[-1] != [' ' for i in range(self.nb_col)]
