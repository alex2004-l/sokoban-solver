
# https://www.algorithms-and-technologies.com/iterative_deepening_a_star/python
# added visited states -> i should change it to 

def ida_star(state, heuristic):
    threshold = heuristic(state)
    path = [state]
    while True:
        distance, is_solved = ida_star_rec(state, heuristic, 0, threshold, path, set())
        if is_solved:
            return path
        if distance == float("inf"):
            return None
        
        threshold = distance


def ida_star_rec(state, heuristic, distance, threshold, path, visited):
    if state.is_solved():
        return distance, True

    estimate = distance + heuristic(state)
    if estimate > threshold:
        return estimate, False
    
    min_estimate = float("inf")
    visited.add(state.__str__())

    for neigh in state.get_neighbours():
        if neigh.__str__() in visited:
            continue
        path.append(neigh)
        t, is_solved = ida_star_rec(neigh, heuristic, distance + 1, threshold, path, visited)
        if is_solved:
            return t, True
        if t < min_estimate:
            min_estimate = t
        path.pop()

    visited.remove(state.__str__())
    return min_estimate, False