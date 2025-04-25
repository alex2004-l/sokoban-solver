from search_methods.utils import static_deadlock_cells, check_deadlock
from sokoban import Map
from typing import Callable

counter = 0

def ida_star(state : Map, heuristic: Callable):
    global counter
    counter = 0
    deadlock_cells = static_deadlock_cells(state)

    threshold = heuristic(state)
    path = [state]
    while True:
        visited = {}
        distance, is_solved = ida_star_rec(state, heuristic, 0, threshold, path, visited, deadlock_cells)
        if is_solved:
            return path, counter
        if distance == float("inf"):
            return None, counter

        threshold = distance
        # print(f"Threshold - {threshold}")


def ida_star_rec(state : Map, heuristic, distance, threshold, path, visited, deadlock_cells):
    global counter
    counter += 1

    if state.is_solved():
        return distance, True

    estimate = distance + heuristic(state)
    if estimate > threshold:
        return estimate, False

    # Transposition table
    key = state.serialize()
    if key in visited and visited[key] <= distance:
        return float("inf"), False
    visited[key] = distance

    min_estimate = float("inf")
    for neigh in state.get_neighbours():
        if check_deadlock(neigh, deadlock_cells):
            continue
        path.append(neigh)
        t, is_solved = ida_star_rec(neigh, heuristic, distance + 1, threshold, path, visited, deadlock_cells)
        if is_solved:
            return t, True
        if t < min_estimate:
            min_estimate = t
        path.pop()
    return min_estimate, False