from sokoban.map import Map, OBSTACLE_SYMBOL
from itertools import permutations

def manhattan_dist(coord1, coord2):
    return abs(coord1[0] - coord2[0]) + abs(coord1[1] - coord2[1])

def heuristic2(state):
    box_positions = [coords for coords in state.positions_of_boxes]
    target_positions = state.targets

    player_coord = (state.player.x, state.player.y)
    min_dist_player = min([manhattan_dist(player_coord, box) for box in box_positions])

    r = []
    for box in box_positions:
        nr = []
        for target in target_positions:
            nr.append(manhattan_dist(target, box))
        r.append(min(nr))
    
    return min_dist_player + sum(r)

def heuristic(state):
    box_positions = [coords for coords in state.positions_of_boxes]
    target_positions = state.targets

    player_coord = (state.player.x, state.player.y)
    min_dist_player = min([manhattan_dist(player_coord, box) - 1 for box in box_positions])

    # to later use for determing the optimal position for each box
    r = [[manhattan_dist(target, box) - 1 for target in target_positions] for box in box_positions]

    idxs = range(len(target_positions))
    min_sum = float("inf")

    for perm in permutations(idxs):
        current_sum = sum([r[i][perm[i]] for i in idxs])
        if current_sum < min_sum:
            min_sum = current_sum

    return min_sum + min_dist_player

def get_deadlock_cells(start_state):
    c_map = start_state.map
    result = set()
    for row in range(len(c_map)):
        for column in range(len(c_map[0])):
            if c_map[row][column] == 0:
                left = column - 1 < 0 or c_map[row][column - 1] == OBSTACLE_SYMBOL
                right = column + 1 >= start_state.width or c_map[row][column + 1] == OBSTACLE_SYMBOL
                above = row - 1 < 0 or c_map[row - 1][column] == OBSTACLE_SYMBOL
                below = row + 1 >= start_state.length or c_map[row + 1][column] == OBSTACLE_SYMBOL
                if (left and above) or (left and below) or (right and above) or (right and below):
                    result.add((row, column))
    return result

def check_deadlock(state : Map, deadlock_cells = None):
    if not deadlock_cells:
        deadlock_cells = get_deadlock_cells(state)
    for box in state.positions_of_boxes:
        if box in deadlock_cells:
            return True
    return False