from sokoban.gif import save_images, create_gif
from search_methods.ida_star import ida_star

IDA_STAR = "ida_star"
BEAM_SEARCH = "beam_search"

class Solver:
    def __init__(self, map, heuristic) -> None:
        self.map = map
        self.heuristic = heuristic

    def solve(self):
        self.solve_ida_star()
        self.solve_beam_search()

    def solve_ida_star(self):
        ida_result = ida_star(self.map, self.heuristic)
        if not ida_result:
            print("Ida* didn't find a solution")
        else:
            save_images(ida_result, "images")
            create_gif("images", "test", "gif")

    def solve_beam_search(self):
        pass
