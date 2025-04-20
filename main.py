from sokoban import Box, DOWN, Map, Player
from search_methods.solver import Solver
from search_methods.heuristics import heuristic

if __name__ == '__main__':
    map_from_yaml = Map.from_yaml('tests/easy_map2.yaml')

    plot_flag = True
    crt_map = map_from_yaml

    solver = Solver(crt_map, heuristic)

    solver.solve_ida_star()
