#!/usr/bin/python3
"""N Queens solution finder using backtracking with required error handling."""


import sys


'''Graphical representation of N queen

args = sys.argv

class Solution:
    """Class solution for N queens"""

    @staticmethod
    def solveNQueens(n):
        """Solve the N Queens problem"""
        if len(args) != 2:
                print('Usage: nqueens N')
                exit(1)
        try:
            n = int(n)
        except ValueError:
            print("N must be a number")
            exit(1)

        if n < 4:
            print("N must be at least 4")
            exit(1)

        # Initialize sets to track attacking positions
        n = int(n)
        col = set()
        posDiag = set() #(r + c)
        negDiag = set() # (r - c)

        result = []
        board = [['.'] * n for i in range(n)]

        def backtrack(r):
            """Backtrack to find a solution"""
            if r == n:
                copy = [''.join(row) for row in board]
                result.append(copy)
                return

            for c in range(n):
                if c in col or (r + c) in posDiag or (r - c) in negDiag:
                    continue

                # Place queen and mark the positions
                col.add(c)
                posDiag.add(r + c)
                negDiag.add(r - c)
                board[r][c] = 'Q'

                backtrack(r + 1) # Go to the next row

                # Remove the queen and unmark the positions
                col.remove(c)
                posDiag.remove(r + c)
                negDiag.remove(r - c)
                board[r][c] = '.'

        backtrack(0)
        return result



if __name__ == "__main__":
    solution = Solution.solveNQueens(args[1])
    for board in solution:
        for row in board:
            print(row)
        print()'''


def solveNQueens(n):
    """
    Solve the N Queens problem and print solutions in the specified format.
    """

    # Helper function to check if the position is valid for a queen
    def is_valid(board, row, col):
        """Check for queen in same column and diagonals"""
        for r, c in board:
            if c == col or (r + c == row + col) or (r - c == row - col):
                return False
        return True

    # Backtracking function to place queens
    def backtrack(row, board):
        """Backtrack to find a solution"""
        if row == n:
            # A solution is found; format as required and print
            print([[r, c] for r, c in board])
            return
        for col in range(n):
            if is_valid(board, row, col):
                board.append((row, col))
                backtrack(row + 1, board)
                board.pop()  # Remove the queen and backtrack

    # Start backtracking from the first row
    backtrack(0, [])


# Main entry point of the script
if __name__ == "__main__":
    # Check if the correct number of arguments is provided
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        exit(1)

    # Check if the argument is an integer and at least 4
    try:
        N = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        exit(1)

    if N < 4:
        print("N must be at least 4")
        exit(1)

    # Solve the N-Queens problem and print solutions.
    solveNQueens(N)
