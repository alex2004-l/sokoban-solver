from search_methods.utils import get_deadlock_cells, check_deadlock

def beam_search(start, heuristic, beam_width, limit):
    beam = [(start, [], heuristic(start))]

    discovered = set()
    discovered.add(start.serialize())
    explored_states = 0

    deadlock_cells = get_deadlock_cells(start)

    while beam and len(discovered) < limit:
        successors = []
        for state, seq, _ in beam:
            explored_states += 1
            if state.is_solved():
                return seq, explored_states
            for neigh in state.get_neighbours(): 
                if check_deadlock(neigh, deadlock_cells):
                    continue
                if neigh.serialize() not in discovered:
                    discovered.add(neigh.serialize())
                    successors.append((neigh, seq + [neigh], heuristic(neigh)))
        beam = sorted(successors, key=lambda x: x[2])[:beam_width]

    return None, explored_states