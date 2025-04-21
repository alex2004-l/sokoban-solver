
def beam_search(start_state, heuristic, beam_width, limit):
    beam = [(start_state, [], heuristic(start_state))]
    discovered = set()
    discovered.add(start_state.__str__())

    while beam and len(discovered) < limit:
        successors = []
        for state, seq, _ in beam:
            if state.is_solved():
                return seq
            for neigh in state.get_neighbours():
                if neigh.__str__() not in discovered:
                    discovered.add(neigh.__str__())
                    successors.append((neigh, seq + [neigh], heuristic(neigh)))
        beam = sorted(successors, key=lambda x: x[2])[:beam_width]

    return None