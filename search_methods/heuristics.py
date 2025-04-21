def manhattan_dist(coord1, coord2):
    return abs(coord1[0] - coord2[0]) + abs(coord1[1] - coord2[1])

def heuristic(state):
    box_positions = [coords for coords in state.positions_of_boxes]
    target_positions = state.targets

    player_coord = (state.player.x, state.player.y)
    min_dist_player = min([manhattan_dist(player_coord, box) for box in box_positions])

    # to later use for determing the optimal position for each box
    r = []
    for box in box_positions:
        nr = []
        for target in target_positions:
            nr.append(manhattan_dist(target, box))
        r.append(nr)
    
    return min_dist_player