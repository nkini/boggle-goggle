import random
from pprint import pprint

import dice
from util import get_words
from solver import Solver


def convert_human_input_to_board(human_input):
    '''
    :param str human_input: e.g. 'aqyw ooez vois rags'
    :rtype: list
    :returns: [['A','Qu','Y','W'],
               ['O','O','E','Z'],
               ['V','O','I','S'],
               ['R','A','G','S']]
    '''
    human_input = human_input.upper()
    has_q = "Q" in human_input
    rows = human_input.split()
    grid = [list(row) for row in rows]
    if not has_q:
        return grid
    return [["Qu" if char == "Q" else char for char in row] for row in grid]


class Board:
    def __init__(self, board_size=4, input_string=None):
        if not input_string:
            self.board_size = board_size
            self.dice = dice.get_dice(self.board_size)
            self.shuffle_board()
        else:
            self.board = convert_human_input_to_board(input_string)
            self.board_size = len(self.board)

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

    def get_solver_input(self):
        return self.get_human_input()

    def get_human_input(self):
        human_input = ''
        for row in self.board:
            for char in row:
                if char.lower() == 'qu':
                    human_input += 'q'
                else:
                    human_input += char.lower()
            human_input += ' '
        return human_input[:-1]

    def solve(self, listname):
        solver_input = self.get_solver_input()
        self.solver = Solver(solver_input, listname)
        self.solver.solve()
        return self.solver

    def print_possible_words(self, listname):
        self.solve(listname)
        print("Possible words:")
        pprint(self.solver.solution)
        print("Num words in solution:", self.solver.stats["total_words_found"])
        print("Num words checked:", self.solver.stats["total_words_checked"])
        print("Total time elapsed:", self.solver.stats["solving_time"])
