#!/usr/bin/env python3

import math


def count_trees_on_slope(rightward_step, downward_step, map):
    x_index = 0
    tree_count = 0

    for y_index in range(0, len(map), downward_step):
        if map[y_index][x_index] == '#':
            tree_count += 1
        x_index += rightward_step

    return tree_count


rightward_steps = [1, 3, 5, 7, 1]
downward_steps = [1, 1, 1, 1, 2]
steps = zip(rightward_steps, downward_steps)

with open('input1.txt') as input:
    map = input.readlines()

downward_length = len(map)
rightward_length = len(map[0].rstrip('\n'))
rightward_step = max(rightward_steps)
downward_step = min(downward_steps)
repeat_map = math.ceil(downward_length / downward_step * rightward_step /
                       rightward_length)

map = [x.rstrip('\n') * repeat_map for x in map]
multiplied_result = 1

for step in steps:
    multiplied_result *= count_trees_on_slope(*step, map)


print(multiplied_result)
