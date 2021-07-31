import sys

from board import Board

auto_or_manual = input("Autogenerate a board (a) or enter a board manually (m): ")
if auto_or_manual.lower() == "a":
    board_size = input("Enter board size: ")
    BOARD_SIZE = int(board_size)
    BOARD = Board(board_size=BOARD_SIZE)
    print(f"Creating {BOARD_SIZE} x {BOARD_SIZE} BOARD")
elif auto_or_manual.lower() == "m":
    human_input = input("Enter the board: ")
    BOARD = Board(input_string=human_input)
else:
    sys.exit("Invalid choice")

BOARD.print()
BOARD.print_possible_words(listname="twl06")
BOARD.print()
