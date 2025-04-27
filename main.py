from sokoban import Map
from search_methods.solver import Solver
from search_methods.heuristics import Heuristic
import os
import shutil
import pandas as pd

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
        if not test.startswith("super"):
            continue
        test_name = os.path.join(test_directory, test)
        crt_map = Map.from_yaml(test_name)
        test = test.split(".")[0]
        print(f"Start solving {test}")

        solver = Solver(crt_map, test)
        statistics += solver.solve()
        print(f"Finished processing test {test}")
    print(statistics)
    
    df = pd.DataFrame(statistics)
    ida_star_df = df[df["method"] == "ida_star"]
    beam_search_df = df[df["method"] == "beam_search"]

    ida_star_df.to_csv("ida_stats_no_deadlock.csv", mode="a", header=False, index=False)
    beam_search_df.to_csv("beam_stats_no_deadlock.csv", mode="a", header=False, index=False)
    df.to_csv("combined_no_deadlock.csv", mode="a", header=False, index=False)

    delete_images()
