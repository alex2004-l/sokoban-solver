from sokoban import Map
from search_methods.solver import Solver
import os
import shutil

def delete_images():
    image_directory = "images"
    for img_dir in os.listdir(image_directory):
        dir_path = os.path.join(image_directory, img_dir)
        if os.path.isdir(dir_path):
            shutil.rmtree(dir_path)

if __name__ == '__main__':
    test_directory = "tests"

    statistics = []

    for test in os.listdir(test_directory):
        test_name = os.path.join(test_directory, test)
        crt_map = Map.from_yaml(test_name)
        test = test.split(".")[0]
        print(f"Start solving {test}")

        solver = Solver(crt_map, test, cache_heuristic=False)
        statistics += solver.solve()
        print(f"Finished processing test {test}")
    print(statistics)

    delete_images()
