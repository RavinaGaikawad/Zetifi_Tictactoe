import unittest
from tic_tac_toe import TicTacToe


class TestTicTacToe(unittest.TestCase):
    def test_set_params(self):
        moves = [[0, 0, 'o'], [0, 2, 'x'], [1, 1, 'o'], [0, 1, 'x'], [2, 2, 'o'], [1, 0, 'x'], [2, 1, 'o']]
        t = TicTacToe()
        result = 0
        for move in moves:
            result = t.place_marker(move[2], move[0], move[1])
            self.assertIsNotNone(result)

        self.assertIs(result, 4)

    def test_who_wins(self):
        t = TicTacToe()
        testcase1 = [1, 0]
        testcase2 = [3, 0]

        result = t.who_wins(testcase1)
        self.assertIs(result, 2)

        result = t.who_wins(testcase2)
        self.assertIs(result, 4)


if __name__ == '__main__':
    unittest.main()
