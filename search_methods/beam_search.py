from sokoban.map import Map

def beam_search(start: Map, heuristic, beam_width : int, limit : int):
    beam = [(start, [start], heuristic.heuristic(start))]

    discovered = set()
    discovered.add(start.serialize())
    explored_states = 0

    deadlock_cells = start.static_deadlock_cells()

    while beam and len(discovered) < limit:
        successors = []
        for state, seq, _ in beam:
            explored_states += 1
            if state.is_solved():
                return seq, explored_states
            for neigh in state.get_neighbours_without_pull_moves(): 
                if neigh.check_deadlock(deadlock_cells):
                    continue
                if neigh.serialize() not in discovered:
                    discovered.add(neigh.serialize())
                    successors.append((neigh, seq + [neigh], heuristic.heuristic(neigh)))
        beam = sorted(successors, key=lambda x: x[2])[:beam_width]

    return None, explored_states

def beam_search_with_pulls(start: Map, heuristic, beam_width : int, limit : int):
    beam = [(start, [start], heuristic.heuristic(start))]

    discovered = set()
    discovered.add(start.serialize())
    explored_states = 0

    while beam and len(discovered) < limit:
        successors = []
        for state, seq, _ in beam:
            explored_states += 1
            if state.is_solved():
                return seq, explored_states
            for neigh in state.get_neighbours():
                if neigh.serialize() not in discovered:
                    discovered.add(neigh.serialize())
                    successors.append((neigh, seq + [neigh], heuristic.heuristic(neigh)))
        beam = sorted(successors, key=lambda x: x[2])[:beam_width]

    return None, explored_states