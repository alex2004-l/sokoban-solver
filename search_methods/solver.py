from sokoban.gif import save_images, create_gif
from search_methods.ida_star import ida_star
from search_methods.beam_search import beam_search
import os

class Solver:
    def __init__(self, map, heuristic, testname) -> None:
        self.map = map
        self.heuristic = heuristic
        self.testname = testname

    def solve(self):
        self.solve_ida_star()
        # self.solve_beam_search()

    def solve_ida_star(self):
        ida_result = ida_star(self.map, self.heuristic)
        if not ida_result:
            print("Ida* didn't find a solution")
        else:
            save_images(ida_result, os.path.join("images", self.testname))
            create_gif(os.path.join("images", self.testname), self.testname, "gif")

    def solve_beam_search(self):
        beam_search_result = beam_search(self.map, self.heuristic)
        if not beam_search_result:
            print("Beam search didn't find a solution")
        else:
            save_images(beam_search_result, os.path.join("images", self.testname))
            create_gif(os.path.join("images", self.testname), self.testname, "gif")
