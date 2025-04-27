import os
import time
from typing import Callable
from sokoban.gif import save_images, create_gif
from search_methods.ida_star import ida_star
from search_methods.beam_search import beam_search
from sokoban.map import Map
from search_methods.heuristics import Heuristic

IDA_STAR = "ida*"
BEAM_SEARCH = "beam-search"
BEAM_WIDTH = 30
BEAM_LIMIT = 100000

class Solver:
    def __init__(self, map: Map, testname : str, algorithm : str, cache_heuristic : bool = False) -> None:
        self.map = map
        self.heuristic = Heuristic(cache_heuristic)
        self.testname = testname
        self.algoritm = algorithm
        self.statistics = []

    def solve(self):
        if self.algoritm == IDA_STAR:
            self.solve_ida_star()
        elif self.algoritm == BEAM_SEARCH:
            self.solve_beam_search()
        else:
            print("Unknown algorithm")

    def generic_solve(self, alg_name: str, func : Callable, *args):
        start_time = time.time()
        result, explored_states = func(self.map, self.heuristic, *args)
        total_time = time.time() - start_time
        print(f"{self.testname} - {total_time}")

        if not result:
            print(f"{alg_name} didn't find a result")
        else:
            last_state = result[len(result) - 1]
            self.save_result__as_gif(result, alg_name)
            self.statistics.append(self.get_statistics(last_state, explored_states, alg_name, total_time))

    def solve_ida_star(self):
        self.generic_solve(IDA_STAR, ida_star)

    def solve_beam_search(self):
        self.generic_solve(BEAM_SEARCH, beam_search, BEAM_WIDTH, BEAM_LIMIT)
    
    def save_result__as_gif(self, array_result, type):
        save_images(array_result, os.path.join("images", self.testname, type))
        create_gif(os.path.join("images", self.testname, type), self.testname,  os.path.join("gif", type))

    def get_statistics(self, last_state, explored_states, method_name, tm):
        return {
            "name" : self.testname,
            "method": method_name,
            "explored_states": explored_states,
            "solution_length": last_state.explored_states,
            "undo_moves": last_state.undo_moves,
            "time" : tm,
            "heuristic" : "best",
            "no_pulls" : True,
            "caching" : self.heuristic.precalculated is not None
        }

