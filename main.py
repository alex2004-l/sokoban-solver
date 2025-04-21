from sokoban import Box, DOWN, Map, Player
from search_methods.solver import Solver
from search_methods.heuristics import heuristic
import os

if __name__ == '__main__':
    test_directory = "tests"

    for test in os.listdir(test_directory):
        test_name = os.path.join(test_directory, test)
        crt_map = Map.from_yaml(test_name)
        test = test.split(".")[0]
        if not test.startswith("easy") and not test.startswith("medium"):
            continue
        print(f"Start solving {test}")

        solver = Solver(crt_map, heuristic, test)
        solver.solve()
        print(f"Finished processing test {test}")
