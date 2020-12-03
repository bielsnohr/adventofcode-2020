#!/usr/bin/env python3

import math

with open('test_input.txt') as input:
    map = input.readlines()

downward_length = len(map)
rightward_length = len(map[0].rstrip('\n'))
rightward_step = 3
repeat_map = math.ceil(downward_length * rightward_step / rightward_length)

map = [x.rstrip('\n') * repeat_map for x in map]

x_pos = 0
tree_count = 0

for y_slice in map:
    if y_slice[x_pos] == '#':
        tree_count += 1
    x_pos += rightward_step

print(tree_count, x_pos)
