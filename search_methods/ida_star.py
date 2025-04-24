from search_methods.utils import get_deadlock_cells, check_deadlock
from sokoban import Map

counter = 0
deadlock_cells = set()

def ida_star(state, heuristic):
    global counter
    global deadlock_cells

    counter = 0
    deadlock_cells = get_deadlock_cells(state)

    threshold = heuristic(state)
    path = [state]
    while True:
        visited = {}
        distance, is_solved = ida_star_rec(state, heuristic, 0, threshold, path, visited)
        if is_solved:
            return path, counter
        if distance == float("inf"):
            return None, counter
        
        threshold = distance
        print(f"New threshlod {threshold}")

def ida_star_rec(state : Map, heuristic, distance, threshold, path, visited):
    global counter
    counter += 1

    estimate = distance + heuristic(state)

    # if estimate == float("inf"):
    #     return float("inf"), False
    if estimate > threshold:
        return estimate, False

    if state.is_solved():
        return distance, True
    
    # if check_deadlock(state, deadlock_cells):
    #     return float("inf"), False
    
    # Transposition table
    key = state.__str__()
    if key in visited and visited[key] <= distance:
        return float("inf"), False
    visited[key] = distance

    min_estimate = float("inf")
    for neigh in state.get_neighbours_without_pull_moves():
        path.append(neigh)
        t, is_solved = ida_star_rec(neigh, heuristic, distance + 1, threshold, path, visited)
        if is_solved:
            return t, True
        if t < min_estimate and t != -1:
            min_estimate = t
        path.pop()
    return min_estimate, False