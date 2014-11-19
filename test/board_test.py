import unittest
import copy

from game.samegame import SameGame

mock_board = [
    ['O', 'O', 'B'],
    ['B', 'O', 'A'],
    ['B', 'A', 'A']
]

mock_click_bottom = [
    ['O', ' ', ' '],
    ['B', 'O', ' '],
    ['B', 'O', 'B']
]

removed_cell_board = [
    ['O', ' ', 'B'],
    ['B', ' ', 'A'],
    ['B', 'A', 'A']
]

adjust_vertically = [
    ['O', 'A', 'B'],
    ['A', ' ', 'A'],
    [' ', ' ', 'B']
]

solution_adjust_vertically = [
    [' ', ' ', 'B'],
    ['O', ' ', 'A'],
    ['A', 'A', 'B']
]

adjust_horizontally = [
    ['O', ' ', 'B'],
    ['A', ' ', 'A'],
    [' ', ' ', 'B']
]

solution_adjust_horizontally = [
    [' ', 'B', ' '],
    ['O', 'A', ' '],
    ['A', 'B', ' ']
]

class BoardTest(unittest.TestCase):

    def test_new_game(self):
        game = SameGame()
        game.new_game(4, 5, 3)
        self.assertEqual(len(game.board), 4)
        self.assertEqual(len(game.board[0]), 5)
        self.assertEqual(len(game.used_colors), 3)
        self.assertEqual(game.score, 0)

    def test_check_nearby(self):
        game = SameGame()
        game.new_game(3, 3, 3)
        game.board = copy.deepcopy(mock_board)
        same = game.get_same_nearby(1, 1)
        self.assertCountEqual(same, [(0,0), (0, 1), (1, 1)])

    def test_remove_cells(self):
        game = SameGame()
        game.new_game(3, 3, 3)
        game.board = (mock_board)
        game.remove_cells([(1,1), (0, 1)])
        self.assertEqual(game.board, removed_cell_board)

    def test_adjust_vertically(self):
        game = SameGame()
        game.new_game(3, 3, 3)
        game.board = copy.deepcopy(adjust_vertically)
        game.adjust_board()
        self.assertEqual(game.board, solution_adjust_vertically)

    def test_adjust_horizontally(self):
        game = SameGame()
        game.new_game(3, 3, 3)
        game.board = copy.deepcopy(adjust_horizontally)
        game.adjust_board()
        self.assertEqual(game.board, solution_adjust_horizontally)

    def test_click_on_cell(self):
        game = SameGame()
        game.new_game(3, 3, 3)
        game.board = copy.deepcopy(mock_board)
        score = game.score
        game.click_on_cell(2, 1)
        self.assertEqual(game.board, mock_click_bottom)
        self.assertEqual(game.score, score+1)
