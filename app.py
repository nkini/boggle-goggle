from flask import Flask, render_template, request
from board import Board
from util import get_board_input

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")

@app.route("/play")
def play():
    BOARD = Board(board_size=4)
    BOARD.solve(listname="twl06")
    return render_template("board.html", board=BOARD)

@app.route("/solve")
def solve():
    if 'board' in request.args:
        board_input = get_board_input(request.args['board'])
        BOARD = Board(board=board_input)
        BOARD.solve(listname="twl06")
        return render_template("board.html", board=BOARD)
    else:
        return render_template("board-input.html")
