# Created by Tobias Bück at 2019-12-06 06:05:15.363116
# Solution of day 6 of advent of Code 2019
# 
# INPUTS 
import utility     # helper methods


def get_input_file():
    return open("../../../input/2019/input6.txt")


def get_clean_data():
    with get_input_file() as input_file:
        lines_input_file = utility.get_lines_of_file(input_file)
    return lines_input_file    


def get_indirect(adjacency_dict, name):
    orbits_used = set()
    orbits = adjacency_dict[name]
    orbits_copy = set(orbits)
    while len(orbits_copy) > 0:
        new_orbit = orbits_copy.pop()

        if new_orbit in orbits_used:
            continue

        if new_orbit == name:
            continue

        if new_orbit in adjacency_dict:
            for orbit in adjacency_dict[new_orbit]:
                orbits_copy.add(orbit)
        orbits_used.add(new_orbit)

    counter = len(orbits_used)
    return counter


def bfs(node, target, adjacency_dict, nodes_visited):
    queue = [(node, 0)]
    while len(queue) > 0:
        current, count = queue.pop()
        if current == target:
            return count
        nodes_visited.add(current)
        if current in adjacency_dict:
            for ad_node in adjacency_dict[current]:
                if ad_node not in nodes_visited:
                     queue.append((ad_node, count + 1))


def find_way_to_santa(adjacency_dict):
    nodes_visited = set()
    return bfs("YOU", "SAN", adjacency_dict, nodes_visited) - 2


def create_ad_dict(lines):
    adjacency_dict = {}
    for line in lines:
        orbit1, orbit2 = line.split(")")
        # orbit2 orbits orbit1
        if orbit2 not in adjacency_dict:
            adjacency_dict[orbit2] = set()
        adjacency_dict[orbit2].add(orbit1)
    return adjacency_dict


def create_ad_dict_part2(lines):
    adjacency_dict = {}
    for line in lines:
        orbit1, orbit2 = line.split(")")
        # orbit2 orbits orbit1
        if orbit2 not in adjacency_dict:
            adjacency_dict[orbit2] = set()
        if orbit1 not in adjacency_dict:
            adjacency_dict[orbit1] = set()
        adjacency_dict[orbit2].add(orbit1)
        adjacency_dict[orbit1].add(orbit2)
    return adjacency_dict


def part1():
    lines = get_clean_data()
    adjacency_dict = create_ad_dict(lines)
    direct_count = 0
    indirect_count = 0
    for key in adjacency_dict.keys():
        indirect_count += get_indirect(adjacency_dict, key)

    return direct_count + indirect_count


def part2():
    lines = get_clean_data()
    adjacency_dict = create_ad_dict_part2(lines)
    return find_way_to_santa(adjacency_dict)


def main():
    #print(f"part1: " + str(part1()))
    print(f"part2: " + str(part2()))


if __name__ == '__main__':
    main()    
