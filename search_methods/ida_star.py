from sokoban import Map
from typing import Callable

counter = 0

def ida_star(state : Map, heuristic):
    global counter
    counter = 0
    deadlock_cells = state.static_deadlock_cells()

    threshold = heuristic.heuristic(state)
    path = [state]
    while True:
        visited = {}
        distance, is_solved = ida_star_rec(state, heuristic, 0, threshold, path, visited, deadlock_cells)
        if is_solved:
            return path, counter
        if distance == float("inf"):
            return None, counter
        threshold = distance
        print(f"Threshold {threshold}")


def ida_star_rec(state : Map, heuristic, distance, threshold, path, visited, deadlock_cells):
    global counter
    counter += 1

    if state.is_solved():
        return distance, True
    
    if state.check_deadlock(deadlock_cells):
        return float("inf"), False

    # Transposition table
    key = state.serialize()
    if key in visited and visited[key] <= distance:
        return float("inf"), False
    visited[key] = distance

    estimate = distance + heuristic.heuristic(state)
    if estimate > threshold:
        return estimate, False

    min_estimate = float("inf")
    for neigh in state.get_neighbours_without_pull_moves():
        if neigh.check_deadlock(deadlock_cells):
            continue
        path.append(neigh)
        t, is_solved = ida_star_rec(neigh, heuristic, distance + 1, threshold, path, visited, deadlock_cells)
        if is_solved:
            return t, True
        if t < min_estimate:
            min_estimate = t
        path.pop()
    return min_estimate, False