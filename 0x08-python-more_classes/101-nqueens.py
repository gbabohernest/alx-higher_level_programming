#!/usr/bin/python3
"""Solves the n-queen puzzle challenge"""


class Chessboard:
    """Solves the N-queens puzzle.

     Encapsulates the logic for initializing,
     solving, and finding solutions of placing
     N non-attacking queens on an NxN chessboard.

     N must be an integer greater than or equal to 4.
    """

    def __init__(self, n):
        """initialize a board of n size."""
        self.n = n
        self.board = [[' ' for _ in range(n)] for _ in range(n)]
        self.solutions = []

    def is_safe(self, row, col):
        """checks if it is safe
           to place a queen at
           the given position.
        """
        # check the row
        for i in range(col):
            if self.board[row][i] == 'Q':
                return False

        # check upper-left diagonal
        for i, j, in zip(range(row, -1, -1), range(col, -1, -1)):
            if self.board[i][j] == 'Q':
                return False

        # check lower-left diagonal
        for i, j, in zip(range(row, self.n), range(col, -1, -1)):
            if self.board[i][j] == 'Q':
                return False

        return True

    def solve(self, col):
        """Explore possible solutions recursively"""

        if col == self.n:
            solution = []
            for row in self.board:
                for i in range(self.n):
                    if row[i] == 'Q':
                        # found a solution, add it to the list
                        solution.append([self.board.index(row), i])
            self.solutions.append(solution)
            return

        for row in range(self.n):
            if self.is_safe(row, col):
                self.board[row][col] = 'Q'
                self.solve(col + 1)
                self.board[row][col] = ' '

    def find_solutions(self):
        """Return all solutions found"""

        self.solve(0)
        return self.solutions


def main():
    """Entry to the program.
       Handle command line
       input and printing of
       the solutions
    """

    import sys

    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    if sys.argv[1].isdigit() is False:
        print("N must be a number")
        sys.exit(1)

    if int(sys.argv[1]) < 4:
        print("N must be at least 4")
        sys.exit(1)

    n = int(sys.argv[1])

    chessboard = Chessboard(n)
    solutions = chessboard.find_solutions()

    for solution in solutions:
        print("{}".format(solution), end="")
        print()


if __name__ == "__main__":
    main()
