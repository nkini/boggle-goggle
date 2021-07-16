import random
from pprint import pprint

import dice
from util import get_words
from solver import Solver


class Board:
    def __init__(self, board_size=4, board=None):
        if not board:
            self.board_size = board_size
            self.dice = dice.get_dice(self.board_size)
            self.shuffle_board()
        else:
            self.board = board
            self.board_size = len(board)

    def print(self):
        for i in range(self.board_size):
            for j in range(self.board_size):
                print(self.board[i][j], end="\t")
            print()

    def shuffle_board(self):
        # Randomly assign a face to each die
        rolled_dice = [die.roll() for die in self.dice]
        # Randomly shuffle the rolled dice
        shuffled_dice = random.sample(rolled_dice, len(rolled_dice))
        # Reshape to NxN
        N = self.board_size
        self.board = [[shuffled_dice[i + j * N] for i in range(N)] for j in range(N)]

    def print_possible_words(self, listname):
        solver = Solver(self.board, listname)
        solution = solver.solve()
        print("Possible words:")
        pprint(solution)
        print("Num words in solution:", len(solution))
        print("Num words checked:", solver.total_words_checked)
        print("Total time elapsed:", solver.solving_time)
