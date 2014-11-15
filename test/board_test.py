import unittest
import copy

from game.samegame import SameGame

mock_board = [
    ['O', 'O', 'B'],
    ['B', 'O', 'A'],
    ['B', 'A', 'A']
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
        game.board = copy.copy(mock_board)
        same = game.get_same_nearby(1, 1)
        self.assertCountEqual(same, [(0,0), (0, 1), (1, 1)])
