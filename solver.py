import time

from util import get_words_and_prefixes


def convert_human_input_to_solver_input(human_input):
    """
    :param str human_input: e.g. 'aqyw ooez vois rags'
    :rtype: list
    :returns: [['a','qu','y','w'],
               ['o','o','e','z'],
               ['v','o','i','s'],
               ['r','a','g','s']]
    """
    human_input = human_input.lower()
    has_q = "q" in human_input
    rows = human_input.split()
    grid = [list(row) for row in rows]
    if not has_q:
        return grid
    return [["qu" if char == "q" else char for char in row] for row in grid]


class Solver:
    def __init__(self, input_string, listname):
        self.board = convert_human_input_to_solver_input(input_string)
        self.N = len(self.board)
        self.MIN_WORD_LENGTH = 3
        allowed_words, valid_prefixes = get_words_and_prefixes(listname)
        self.allowed_words = [word.lower() for word in allowed_words]
        self.valid_prefixes = valid_prefixes
        self.solution = set()
        self.total_words_checked = 0

    def solve(self):
        start = time.time()
        for x in range(self.N):
            for y in range(self.N):
                visited = [[False] * self.N for _ in range(self.N)]
                self._bfs_solver(x, y, word_so_far="", visited=visited)
        end = time.time()
        self.stats = {
            "total_words_checked": self.total_words_checked,
            "total_words_found": len(self.solution),
            "solving_time": end - start,
        }

    def _bfs_solver(self, x, y, word_so_far, visited):
        visited[x][y] = True
        word_so_far += self.board[x][y]
        if len(word_so_far) >= self.MIN_WORD_LENGTH:
            self.total_words_checked += 1
            if word_so_far in self.allowed_words:
                self.solution.add(word_so_far)
        if word_so_far not in self.valid_prefixes:
            return
        for nextx, nexty in self._possible_next_indices(x, y, visited):
            visited_copy = [[is_visited for is_visited in row] for row in visited]
            visited_copy[nextx][nexty] = True
            self._bfs_solver(nextx, nexty, word_so_far, visited_copy)

    def _possible_next_indices(self, i, j, visited):
        minX, minY = max(0, i - 1), max(0, j - 1)
        maxX, maxY = min(i + 1, self.N - 1), min(j + 1, self.N - 1)
        for x in range(minX, maxX + 1):
            for y in range(minY, maxY + 1):
                if not visited[x][y] and (x, y) != (i, j):
                    yield x, y
