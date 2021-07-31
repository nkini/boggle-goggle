from flask import Flask, render_template, request, send_from_directory
from board import Board
from solver import Solver

import os
import json

app = Flask(__name__)


@app.route("/favicon.ico")
def favicon():
    return send_from_directory(os.path.join(app.root_path, "static"), "favicon.ico")


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/play")
def play():
    BOARD = Board(board_size=4)
    return render_template("board.html", board=BOARD)


@app.route("/solve")
def solve():
    if "board" in request.args:
        BOARD = Board(input_string=request.args["board"])
        return render_template("board.html", board=BOARD)
    else:
        return render_template("board-input.html")


@app.route("/solve_get_json")
def get_solution_json():
    # TODO: This input handling needs some cleaning up
    solver = Solver(input_string=request.args["board"], listname="twl06")
    solver.solve()
    return json.dumps(
        {
            "solution": {
                "num_words": solver.stats["total_words_found"],
                "words": sorted(solver.solution),
            }
        }
    )
