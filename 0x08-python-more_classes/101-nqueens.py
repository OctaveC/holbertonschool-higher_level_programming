#!/usr/bin/python3
"""
This module defines a chassboard and solves the N queen puzzle
"""


from sys import argv

"""
class NQueen:
    """
  """  This class solves a N Queen puzzle for a given N"""
    """

    for ite in range(size):
"""

if len(argv) != 2:
    print("Usage: nqueens N")
    exit(1)
try:
    size = int(argv[1])
except ValueError:
    print("N must be a number")
    exit(1)
if size < 4:
    print("N must be at least 4")
    exit(1)
board = [0] * size


for ite in range(size)




def print_board(board):
    """ prints the solution """
    print("[", end="")
    for row in range(board):
        for column in range(board):
            if :
                print("[{}, {}]".format(row, column), end="")
                if row < size - 1:
                    print(", ", end="")
    print("]")
