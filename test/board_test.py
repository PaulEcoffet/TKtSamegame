"""
Module de test pour la logique du jeu
"""

__author__ = 'François Gouet, Paul Ecoffet'


import unittest
from game.errors import NotEnoughCellsError, InvalidCellError
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
        game.__init__(4, 5, 3)
        self.assertEqual(len(game.board), 4)
        self.assertEqual(len(game.board[0]), 5)
        self.assertEqual(len(game.used_colors), 3)
        self.assertEqual(game.score, 0)

    def test_check_nearby(self):
        game = SameGame()
        game.__init__(3, 3, 3)
        game.board = copy.deepcopy(mock_board)
        same = game.get_same_nearby(1, 1)
        self.assertCountEqual(same, [(0,0), (0, 1), (1, 1)])

    def test_remove_cells(self):
        game = SameGame()
        game.__init__(3, 3, 3)
        game.board = copy.deepcopy(mock_board)
        game.remove_cells([(1,1), (0, 1)])
        self.assertEqual(game.board, removed_cell_board)

    def test_adjust_vertically(self):
        game = SameGame()
        game.__init__(3, 3, 3)
        game.board = copy.deepcopy(adjust_vertically)
        game.adjust_board()
        self.assertEqual(game.board, solution_adjust_vertically)

    def test_adjust_horizontally(self):
        game = SameGame()
        game.__init__(3, 3, 3)
        game.board = copy.deepcopy(adjust_horizontally)
        game.adjust_board()
        self.assertEqual(game.board, solution_adjust_horizontally)

    def test_click_on_cell(self):
        game = SameGame()
        game.__init__(3, 3, 3)
        game.board = copy.deepcopy(mock_board)
        score = game.score
        game.click_on_cell(2, 1)
        self.assertEqual(game.board, mock_click_bottom)
        self.assertEqual(game.score, score+1)

    def test_click_on_cell_error(self):
        game = SameGame()
        game.__init__(3, 3, 3)
        game.board = copy.deepcopy(mock_board)
        score = game.score
        self.assertRaises(NotEnoughCellsError, game.click_on_cell, 1, 0)
        self.assertEqual(game.board, mock_board)
        self.assertEqual(game.score, score)

    def test_can_play(self):
        game = SameGame()
        game.__init__(3, 3, 3)
        game.board = copy.deepcopy(mock_board)
        self.assertTrue(game.can_play)
        game.click_on_cell(2, 1)
        self.assertFalse(game.can_play)

    def test_won(self):
        game = SameGame()
        game.__init__(3, 3, 3)
        game.board = copy.deepcopy(mock_board)
        self.assertFalse(game.won)
        game.click_on_cell(1, 1)
        self.assertFalse(game.won)
        game.click_on_cell(2, 1)
        self.assertFalse(game.won)
        game.click_on_cell(2, 0)
        self.assertTrue(game.won)

    def test_not_finished_by_winning(self):
        game = SameGame()
        game.__init__(3, 3, 3)
        game.board = copy.deepcopy(mock_board)
        self.assertTrue(game.not_finished)
        game.click_on_cell(1, 1)
        self.assertTrue(game.not_finished)
        game.click_on_cell(2, 1)
        self.assertTrue(game.not_finished)
        game.click_on_cell(2, 0)
        self.assertFalse(game.not_finished)

    def test_not_finished_no_moves(self):
        game = SameGame()
        game.__init__(3, 3, 3)
        game.board = copy.deepcopy(mock_board)
        self.assertTrue(game.not_finished)
        game.click_on_cell(2, 1)
        self.assertFalse(game.not_finished)

    def test_invalid_cell_error(self):
        game = SameGame()
        game.__init__(3, 3, 3)
        game.board = copy.deepcopy(removed_cell_board)
        self.assertRaises(InvalidCellError, game.click_on_cell, 0, 1)
        self.assertRaises(InvalidCellError, game.click_on_cell, -1, 0)
