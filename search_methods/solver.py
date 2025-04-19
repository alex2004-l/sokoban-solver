from sokoban.map import Map


class Solver:
    def __init__(self, map: Map, heuristic: callable, type: str) -> None:
        self.map = map
        self.heuristic = heuristic

    def solve(self):
        raise NotImplementedError
