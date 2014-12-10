import random
import pickle

from game.errors import NotEnoughCellsError, InvalidCellError


class SameGame():
    
    possible_colors = ["B","O","A",
                        "M","V",
                        "R"] 

    def new_game(self, nb_line, nb_col, nb_colors):
        self.score = 0
        self.nb_colors = nb_colors
        self.used_colors = SameGame.possible_colors[:nb_colors]
        self.nb_line = nb_line
        self.nb_col = nb_col
        self.board = [[random.choice(self.used_colors) for i in range(nb_col)]
                      for j in range(self.nb_line)]

    @property
    def won(self):
        """Declare si le jeu est gagné ou non"""
        return self.board[-1][0] == ' '

    @property
    def not_finished(self):
        return not self.won and self.can_play

    @property
    def can_play(self):
        can_play = False
        visited = [[False for i in range(self.nb_col)]
                    for j in range(self.nb_line)]
        for i in range(self.nb_line):
            if can_play:
                break
            for j in range(self.nb_col):
                if not visited[i][j] and self.board[i][j] != ' ':
                    if len(self.get_same_nearby(i,j, visited)) >= 3:
                        can_play = True
                        break
        return can_play

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

    def click_on_cell(self, line, col):
        if not 0 <= line < self.nb_line or not 0 <= col < self.nb_col:
            raise InvalidCellError('Invalid coords')
        if self.board[line][col] == ' ':
            raise InvalidCellError('Can not click on empty cell')
        nearby = self.get_same_nearby(line, col)
        nb_same = len(nearby)
        if nb_same < 3:
            raise NotEnoughCellsError()
        self.remove_cells(nearby)
        self.adjust_board()
        self.score += (nb_same-2)**2

    def remove_cells(self, cells):
        for cell in cells:
            self.board[cell[0]][cell[1]] = ' '

    def adjust_board(self):
        for j in range(self.nb_col):
            top = self.nb_line
            for i in reversed(range(self.nb_line)):
                if self.board[i][j] != ' ':
                    top -= 1
                    if top != i:
                        self.board[i][j], self.board[top][j] = self.board[top][j], self.board[i][j]

        right = -1
        for j in range(self.nb_col):
            if self.board[-1][j] != ' ':
                right += 1
                if right != j:
                    self.swap_col(right, j)

    def swap_col(self, col1, col2):
        for i in range(self.nb_line):
            self.board[i][col1], self.board[i][col2] = self.board[i][col2], self.board[i][col1]
