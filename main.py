from sokoban import Box, DOWN, Map, Player


if __name__ == '__main__':
    map_from_yaml = Map.from_yaml('tests/easy_map1.yaml')

    plot_flag = True
    crt_map = map_from_yaml

    if plot_flag:
        crt_map.plot_map()
        print(crt_map)
        print(f"Is solved: {crt_map.is_solved()}")
        print("Neighbours:")
        for neighbour in crt_map.get_neighbours():
            next_state = neighbour
