import random
import sys

# Test Dice 2x2
DICE2x2 = [
    ["A"] * 6,
    ["B"] * 6,
    ["C"] * 6,
    ["D"] * 6,
]

# Test Dice 3x3
DICE3x3 = [
    ["A"] * 6,
    ["B"] * 6,
    ["C"] * 6,
    ["D"] * 6,
    ["E"] * 6,
    ["F"] * 6,
    ["S"] * 6,
    ["H"] * 6,
    ["I"] * 6,
]

DICE4x4 = [
    ["A", "A", "E", "E", "G", "N"],
    ["A", "B", "B", "J", "O", "O"],
    ["A", "C", "H", "O", "P", "S"],
    ["A", "F", "F", "K", "P", "S"],
    ["A", "O", "O", "T", "T", "W"],
    ["C", "I", "M", "O", "T", "U"],
    ["D", "E", "I", "L", "R", "X"],
    ["D", "E", "L", "R", "V", "Y"],
    ["D", "I", "S", "T", "T", "Y"],
    ["E", "E", "G", "H", "N", "W"],
    ["E", "E", "I", "N", "S", "U"],
    ["E", "H", "R", "T", "V", "W"],
    ["E", "I", "O", "S", "S", "T"],
    ["E", "L", "R", "T", "T", "Y"],
    ["H", "I", "M", "N", "Qu", "U"],
    ["H", "L", "N", "N", "R", "Z"],
]


# Classic boggle: http://www.bananagrammer.com/2013/10/the-boggle-cube-redesign-and-its-effect.html
DICE4x4_CLASSIC = [
    ["A", "A", "C", "I", "O", "T"],
    ["A", "B", "I", "L", "T", "Y"],
    ["A", "B", "J", "M", "O", "Qu"],
    ["A", "C", "D", "E", "M", "P"],
    ["A", "C", "E", "L", "R", "S"],
    ["A", "D", "E", "N", "V", "Z"],
    ["A", "H", "M", "O", "R", "S"],
    ["B", "F", "I", "O", "R", "X"],
    ["D", "E", "N", "O", "S", "W"],
    ["D", "K", "N", "O", "T", "U"],
    ["E", "E", "F", "H", "I", "Y"],
    ["E", "G", "I", "N", "T", "V"],
    ["E", "G", "K", "L", "U", "Y"],
    ["E", "H", "I", "N", "P", "S"],
    ["E", "L", "P", "S", "T", "U"],
    ["G", "I", "L", "R", "U", "W"],
]


class Die:
    def __init__(self, faces):
        self.faces = faces

    def roll(self):
        return random.choice(self.faces)


def get_dice(board_size=4):
    if board_size == 2:
        return [Die(faces) for faces in DICE2x2]
    elif board_size == 3:
        return [Die(faces) for faces in DICE3x3]
    elif board_size == 4:
        return [Die(faces) for faces in DICE4x4]
    else:
        sys.exit(f"Invalid board size: {board_size}")
