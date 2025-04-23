from sokoban.gif import save_images, create_gif
from search_methods.ida_star import ida_star
from search_methods.beam_search import beam_search
import os
import time
from search_methods.heuristics import get_deadlock_cells


class Solver:
    def __init__(self, map, heuristic, testname) -> None:
        self.map = map
        self.heuristic = heuristic
        self.testname = testname

    def solve(self):
        # print(get_deadlock_cells(self.map))
        self.solve_ida_star()
        self.solve_beam_search()

    def solve_ida_star(self):
        startTime = time.time()
        ida_result, explored_states = ida_star(self.map, self.heuristic)
        print(f"It took ida star {time.time() - startTime}")
        if not ida_result:
            print("Ida* didn't find a solution")
        else:
            self.__save__result__as_gif(ida_result,"ida_star", explored_states)

    def solve_beam_search(self):
        startTime = time.time()
        beam_search_result, explored_states = beam_search(self.map, self.heuristic, 20, 10000)
        print(f"It took beam search {time.time() - startTime}")
        if not beam_search_result:
            print("Beam search didn't find a solution")
        else:
            self.__save__result__as_gif(beam_search_result,"beam_search", explored_states)
    
    def __save__result__as_gif(self, array_result, type, explored_states):
        result = array_result[len(array_result) - 1]
        print(type)
        print(f"Stari intermediare pana la solutie {explored_states}")
        print(f"Numar de miscari de pull {result.undo_moves}")
        save_images(array_result, os.path.join("images", self.testname, type))
        create_gif(os.path.join("images", self.testname, type), self.testname,  os.path.join("gif", type))
