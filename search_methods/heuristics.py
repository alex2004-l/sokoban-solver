from itertools import permutations
from scipy.optimize import linear_sum_assignment
import numpy as np

def manhattan_dist(coord1, coord2):
    return abs(coord1[0] - coord2[0]) + abs(coord1[1] - coord2[1])

class Heuristic:
    def __init__(self, caching: bool):
        if caching:
            self.precalculated = {}
        else:
            self.precalculated = None

    def clear_cache(self):
        self.precalculated.clear()

    def third_heuristic(self, state):
        box_positions = [coords for coords in state.positions_of_boxes]
        target_positions = state.targets

        player_coord = (state.player.x, state.player.y)
        min_dist_player = min([manhattan_dist(player_coord, box) for box in box_positions])

        r = []
        for box in box_positions:
            r.append(min([manhattan_dist(target, box) for target in target_positions]))
        return min_dist_player + sum(r)

    def second_heuristic(self, state):
        box_positions = [coords for coords in state.positions_of_boxes]
        target_positions = state.targets

        player_coord = (state.player.x, state.player.y)
        min_dist_player = min([manhattan_dist(player_coord, box) for box in box_positions]) - 1

        r = []
        for box in box_positions:
            if box not in self.precalculated:
                self.precalculated[box] = [manhattan_dist(target, box) for target in target_positions]
            r.append(self.precalculated[box])

        idxs = range(len(target_positions))
        min_sum = float("inf")

        for perm in permutations(idxs):
            current_sum = sum([r[i][perm[i]] for i in idxs])
            if current_sum < min_sum:
                min_sum = current_sum

        return min_sum + min_dist_player

    def heuristic(self, state):
        box_positions = [coords for coords in state.positions_of_boxes]
        target_positions = state.targets

        player_coord = (state.player.x, state.player.y)
        min_dist_player = min([manhattan_dist(player_coord, box) for box in box_positions]) - 1

        if self.precalculated:
            r = []
            for box in box_positions:
                if box not in self.precalculated:
                    self.precalculated[box] = [manhattan_dist(target, box) for target in target_positions]
                r.append(self.precalculated[box])
        else:
            r = [[manhattan_dist(target, box) for target in target_positions] for box in box_positions]
        r = np.array(r)

        row_ind, col_ind = linear_sum_assignment(r)
        total_dist = r[row_ind, col_ind].sum()

        return total_dist + min_dist_player
