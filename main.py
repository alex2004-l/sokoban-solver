from sokoban import Map
from search_methods.solver import Solver
from search_methods.heuristics import heuristic
import os
import shutil

if __name__ == '__main__':
    test_directory = "tests"
    image_directory = "images"

    for test in os.listdir(test_directory):
        if not test.startswith("large_map2"):
            continue
        test_name = os.path.join(test_directory, test)
        crt_map = Map.from_yaml(test_name)
        test = test.split(".")[0]
        # print(f"Start solving {test}")

        solver = Solver(crt_map, heuristic, test)
        solver.solve()
        # print(f"Finished processing test {test}")
    
    
    for img_dir in os.listdir(image_directory):
        dir_path = os.path.join(image_directory, img_dir)

        if os.path.isdir(dir_path):
            shutil.rmtree(dir_path)
