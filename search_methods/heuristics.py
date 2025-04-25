from itertools import permutations
from scipy.optimize import linear_sum_assignment
import numpy as np

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

def heuristic3(state):
    box_positions = [coords for coords in state.positions_of_boxes]
    target_positions = state.targets

    player_coord = (state.player.x, state.player.y)
    min_dist_player = min([manhattan_dist(player_coord, box) for box in box_positions]) - 1

    # r = [[manhattan_dist(target, box) for target in target_positions] for box in box_positions]
    r = []
    for box in box_positions:
        if box not in precalculated:
            precalculated[box] = [manhattan_dist(target, box) for target in target_positions]
        r.append(precalculated[box])

    idxs = range(len(target_positions))
    min_sum = float("inf")

    for perm in permutations(idxs):
        current_sum = sum([r[i][perm[i]] for i in idxs])
        if current_sum < min_sum:
            min_sum = current_sum

    row_ind, col_ind = linear_sum_assignment(r)
    total_dist = r[row_ind, col_ind].sum()

    return total_dist + min_dist_player


precalculated = {}
def heuristic(state):
    box_positions = [coords for coords in state.positions_of_boxes]
    target_positions = state.targets

    player_coord = (state.player.x, state.player.y)
    min_dist_player = min([manhattan_dist(player_coord, box) for box in box_positions]) - 1

    # r = [[manhattan_dist(target, box) for target in target_positions] for box in box_positions]
    r = []
    for box in box_positions:
        if box not in precalculated:
            precalculated[box] = [manhattan_dist(target, box) for target in target_positions]
        r.append(precalculated[box])

    r = np.array(r)

    # idxs = range(len(target_positions))
    # min_sum = float("inf")

    # for perm in permutations(idxs):
    #     current_sum = sum([r[i][perm[i]] for i in idxs])
    #     if current_sum < min_sum:
    #         min_sum = current_sum

    row_ind, col_ind = linear_sum_assignment(r)
    total_dist = r[row_ind, col_ind].sum()

    return total_dist + min_dist_player