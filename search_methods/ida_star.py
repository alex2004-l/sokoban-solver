from sokoban import Map

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
        print(threshold)


def ida_star_rec(state : Map, heuristic, distance, threshold, path, visited, deadlock_cells):
    global counter
    counter += 1

    if state.is_solved():
        return distance, True
    
    estimate = distance + heuristic.heuristic(state)
    if estimate > threshold:
        return estimate, False

    # Transposition table
    key = state.serialize()
    if key in visited and visited[key] <= distance:
        return float("inf"), False
    visited[key] = distance

    min_estimate = float("inf")
    for neigh in state.get_neighbours_without_pull_moves():
        # doesn't take into account deadlock neighbours
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


def ida_star_with_pulls(state : Map, heuristic):
    global counter
    counter = 0

    threshold = heuristic.heuristic(state)
    path = [state]
    while True:
        visited = {}
        distance, is_solved = ida_star_rec_with_pulls(state, heuristic, 0, threshold, path, visited)
        if is_solved:
            return path, counter
        if distance == float("inf"):
            return None, counter
        threshold = distance
        print(f"Threshold - {threshold}")


def ida_star_rec_with_pulls(state : Map, heuristic, distance, threshold, path, visited):
    global counter
    counter += 1

    if state.is_solved():
        return distance, True
    
    estimate = distance + heuristic.heuristic(state)
    if estimate > threshold:
        return estimate, False

    # Transposition table
    key = state.serialize()
    if key in visited and visited[key] <= distance:
        return float("inf"), False
    visited[key] = distance

    min_estimate = float("inf")
    for neigh in state.get_neighbours():
        path.append(neigh)
        t, is_solved = ida_star_rec_with_pulls(neigh, heuristic, distance + 1, threshold, path, visited)
        if is_solved:
            return t, True
        if t < min_estimate:
            min_estimate = t
        path.pop()
    return min_estimate, False