"""
    This program is a TicTacToe game. It marks the board for each move and returns a winner if any.
"""
from enum import Enum
from typing import List

DIAGONAL, ANTI_DIAGONAL = 0, 1


class TicTacToe:
    """
    Class to implement Tictactoe game
    """
    class STATES(Enum):
        """
        class to store static state variables
        """
        CROSS_TURN = 0
        NAUGHT_TURN = 1
        DRAW = 2
        CROSS_WON = 3
        NAUGHT_WON = 4

    def __init__(self) -> None:
        # Initializing the board
        self.column_counters = [[0, 0] for _ in range(3)]  # Space O(N)
        self.row_counters = [[0, 0] for _ in range(3)]  # Space O(N)
        self.diagonal_counters = [[0, 0] for _ in range(2)]  # Space O(N)

    def place_marker(self, symbol: str, row: int, column: int) -> int:
        """
        :param symbol: Player name
        :param row: Row of the matrix
        :param column: Column in the matrix
        :return: Which player wins or if it's a draw
        """

        if symbol == 'o':
            player = 1
        else:
            player = 0

        # pylint: disable=W0105
        '''
        For every column adding updating the score for each player.
        The score for o is updated at position 0 and for x the position is 1 in all lists            
        '''

        self.column_counters[column][player] += 1
        self.row_counters[row][player] += 1

        # pylint: disable=W0105,W1401
        """
        We know it's a diagonal when column is same as row.
        If we consider \ diagonal.
        Whereas the / diagonal positions can be calculated by comparing
        row + column + 1 with 3 (Total number of rows)
        """

        if row == column:
            # diagonal \
            self.diagonal_counters[DIAGONAL][player] += 1
        if row + column + 1 == 3:
            # diagonal /
            self.diagonal_counters[ANTI_DIAGONAL][player] += 1

        result = self.who_wins(self.column_counters[column])
        if result != TicTacToe.STATES.DRAW.value:
            return result

        result = self.who_wins(self.row_counters[row])
        if result != TicTacToe.STATES.DRAW.value:
            return result

        result = self.who_wins(self.diagonal_counters[DIAGONAL])
        if result != TicTacToe.STATES.DRAW.value:
            return result

        result = self.who_wins(self.diagonal_counters[ANTI_DIAGONAL])
        if result != TicTacToe.STATES.DRAW.value:
            return result

        return result

    @staticmethod
    def who_wins(arr: List) -> int:  # Time O(1)
        """
        :param arr: Array of column or row
        :return: The winner
        """
        if arr[1] == 3:
            return TicTacToe.STATES.NAUGHT_WON.value

        if arr[0] == 3:
            return TicTacToe.STATES.CROSS_WON.value

        return TicTacToe.STATES.DRAW.value


if __name__ == '__main__':
    obj = TicTacToe()
    moves = [[0, 0, 'x'], [0, 2, 'o'], [1, 1, 'x'],
             [0, 1, 'o'], [2, 2, 'x'], [1, 0, 'o'], [2, 1, 'x']]

    for move in moves:
        print('Input', move)
        res = obj.place_marker(move[2], move[0], move[1])
        # print('Output', result)
        if res == 4:
            print('Naught Won!')
        elif res == 3:
            print('Cross Won!')
        else:
            print('Draw')
