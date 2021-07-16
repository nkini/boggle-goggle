from flask import Flask, render_template
from board import Board

app = Flask(__name__)


@app.route("/")
def index():
    BOARD = Board(board_size=4)
    BOARD.solve(listname="twl06")
    return render_template("index.html", board=BOARD)
