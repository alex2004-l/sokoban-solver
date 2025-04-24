from itertools import permutations
from sokoban.map import Map, OBSTACLE_SYMBOL, BOX_SYMBOL, TARGET_SYMBOL
import sys

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
    r = [[manhattan_dist(target, box) for target in target_positions] for box in box_positions]

    idxs = range(len(target_positions))
    min_sum = float("inf")

    for perm in permutations(idxs):
        current_sum = sum([r[i][perm[i]] for i in idxs])
        if current_sum < min_sum:
            min_sum = current_sum
    

    return min_sum + min_dist_player