from sokoban import Map

def find_box_coord(map : Map):
    result = []
    for box_name in map.boxes:
        box = map.boxes[box_name]
        result.append((box.x, box.y))
    return result

def find_target_coord(map : Map):
    return map.targets

def find_player_coord(map : Map):
    return map.player.x, map.player.y

def manhattan_dist(coord1, coord2):
    manhattan_d = abs(coord1[0] - coord2[0]) + abs(coord1[1] - coord2[1])
    return manhattan_d

def heuristic(state: Map):
    box_positions = find_box_coord(state)
    target_positions = find_target_coord(state)

    player_coord = find_player_coord(state)
    min_dist_player = min([manhattan_dist(player_coord, box) for box in box_positions])

    # to later use for determing the optimal position for each box
    r = []
    for box in box_positions:
        nr = []
        for target in target_positions:
            nr.append(manhattan_dist(target, box))
        r.append(nr)
    
    return min_dist_player