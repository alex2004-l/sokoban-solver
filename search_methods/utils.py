from sokoban.map import Map, OBSTACLE_SYMBOL, BOX_SYMBOL, TARGET_SYMBOL

def static_deadlock_cells(start_state : Map):
    c_map = start_state.map
    result = []
    for row in range(len(c_map)):
        for column in range(len(c_map[0])):
            if c_map[row][column] == 0:
                if start_state.check_corner((row, column)):
                    result.append((row, column))
    second_result = set()

    # left
    for i in range(len(result)):
        for j in range(i + 1, len(result)):
            row_i, col_i = result[i]
            row_j, col_j = result[j]
            current_set = []

            not_deadlock = False

            if not row_i == row_j and not col_i == col_j:
                continue
            
            # left and right
            if row_i == row_j:
                for c in range(min(col_i, col_j) + 1, max(col_i, col_j)):
                    if c_map[row_i][c] == 0:
                        current_set.append((row_i, c))
                    if c_map[row_i][c] == BOX_SYMBOL or c_map[row_i][c] == OBSTACLE_SYMBOL:
                        break
                    if c_map[row_i][c] == TARGET_SYMBOL:
                        not_deadlock = True
                        break
            else:
                for r in range(min(row_i, row_j) + 1, max(row_i, row_j)):
                    if c_map[r][col_i] == 0:
                        current_set.append((r, col_i))
                    if c_map[r][col_i] == BOX_SYMBOL or c_map[r][col_i] == OBSTACLE_SYMBOL:
                        break
                    if c_map[r][col_i] == TARGET_SYMBOL:
                        not_deadlock = True
                        break

            if not not_deadlock:
                for c in current_set:
                    second_result.add(c)

    for s in result:
        second_result.add(s)
    return second_result


def check_deadlock(state : Map, deadlock_cells = None):
    if not deadlock_cells:
        deadlock_cells = get_deadlock_cells(state)
    for box in state.positions_of_boxes:
        if box in deadlock_cells:
            return True
    return False