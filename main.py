import os
import sys
from sokoban import Map
from search_methods.solver import Solver

if __name__ == '__main__':
    algorithm = sys.argv[1]
    input_file = sys.argv[2]

    crt_map = Map.from_yaml(input_file)
    filename = os.path.basename(input_file)
    filename = filename.split(".")[0]

    print(f"Start solving {filename} with {algorithm}")
    solver = Solver(crt_map, filename, algorithm, pulls_allowed=False, cache_heuristic=True)
    solver.solve()

    print(f"Finished processing test {filename}")
